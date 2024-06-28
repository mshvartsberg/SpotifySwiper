# make sure to have requests installed (pip3 install requests)
from fastapi import FastAPI
import base64
from requests import post, get
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import httpx
app = FastAPI()


# Set up CORS middleware
origins = [
    "http://localhost:3000",  # The origin of the frontend server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specifies the origins which can make requests to this server
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


CLIENT_ID = "cf8ca44262654fc486c4bc35bf51d594"
CLIENT_SECRET = "013b5238465e4f50bace319e36be1e1f"

# retrieves an access token using client credentials 
def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8" )
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
     
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

# returns the header needed for a get request
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


# returns a playlist
def search_for_playlist(token, playlist_name):
    url = "https://api.spotify.com/v1/search?"
    headers = get_auth_header(token)
    query = f"q={playlist_name}&type=playlist&markert=US&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers).json()
    return result["playlists"]["items"][0] 

def get_playlist_trackObject(token, playlist_id, num_tracks):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?market=US&limit={num_tracks}"
    headers = get_auth_header(token)
    result = get(url, headers=headers).json()
    return result["items"]

def get_track(id, token):
    url = f"https://api.spotify.com/v1/tracks/{id}"
    headers = get_auth_header(token)
    track = get(url, headers=headers).json()
    return track
    

@app.get("/get-top-tracks")
async def get_top_tracks():
    playlist_name = "Top 50 songs" 
    num_tracks = 10
        
    token = get_token()
    playlist = search_for_playlist(token, playlist_name)
    playlist_id = playlist["id"]
    trackObject = get_playlist_trackObject(token, playlist_id, num_tracks)
    track_ids = []
    tracks = []

    for object in trackObject:
        track_ids.append(object["track"]["id"])

    for id in track_ids:
        result = get_track(id, token)
        track = dict(
            name = result["name"],
            photo_url = result["album"]["images"][0]["url"],
            artist = result["artists"][0]["name"]
        )
        tracks.append(track)
    return tracks
