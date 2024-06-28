from fastapi import FastAPI
import base64
from requests import post, get
import json
import httpx
app = FastAPI()

CLIENT_ID = "cf8ca44262654fc486c4bc35bf51d594"
CLIENT_SECRET = "013b5238465e4f50bace319e36be1e1f"


@app.get("/token")
async def get_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=data)
    token = response.json()["access_token"]
    return token

# returns the header needed for a get request
def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}


# returns a playlist
@app.get("/search")
async def search_for_playlist(token, playlist_name):
    url = "https://api.spotify.com/v1/search?"
    headers = get_auth_header(token)
    query = f"q={playlist_name}&type=playlist&markert=US&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers).json()
    return result["playlists"]["items"][0] 


@app.get("/playlist/{token}/{playlist_id}/{num_tracks}")
async def get_playlist_trackObject(token, playlist_id, num_tracks):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?market=US&limit={num_tracks}"
    headers = get_auth_header(token)
    result = get(url, headers=headers).json()
    return result["items"]


@app.get("/track/{id}")
async def get_track(id: str, token: str):
    url = f"https://api.spotify.com/v1/tracks/{id}"
    headers = get_auth_header(token)
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
    track = response.json()
    return track
    
token = get_token() 
