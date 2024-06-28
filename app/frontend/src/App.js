import { useEffect, useState} from 'react';
import './App.css';
import SongSwipe from './SongSwipe';

function App() {

  const [tracks, setTracks] = useState([
    {
      "name": "i like the way you kiss me",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b273e67611dbbf69a90d0b6cb738",
      "artist": "Artemas"
    },
    {
      "name": "Too Sweet",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b2732e8b4358d044b75807e30bf0",
      "artist": "Hozier"
    },
    {
      "name": "Gata Only",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b2731d0777b3259d0bd618f4a1f6",
      "artist": "FloyyMenor"
    },
    {
      "name": "End of Beginning",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b273fddfffec51b4580acae727c1",
      "artist": "Djo"
    },
    {
      "name": "Beautiful Things",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b273cc04ff3e70e146ba9abacf40",
      "artist": "Benson Boone"
    },
    {
      "name": "we can't be friends (wait for your love)",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b2738b58d20f1b77295730db15b4",
      "artist": "Ariana Grande"
    },
    {
      "name": "Espresso",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b273659cd4673230913b3918e0d5",
      "artist": "Sabrina Carpenter"
    },
    {
      "name": "Like That",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b273a46b07c291e6dfdee13b3ee8",
      "artist": "Future"
    },
    {
      "name": "greedy",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b27322fd802bc61db666c7c81aa8",
      "artist": "Tate McRae"
    },
    {
      "name": "Lose Control",
      "photo_url": "https://i.scdn.co/image/ab67616d0000b2731a0323cc23419360a34a3ace",
      "artist": "Teddy Swims"
    }
  ]);
  const [count, setCount] = useState(0);

  // useEffect(() => {
  //   const url = `http://127.0.0.1:8000/get-top-tracks`;
  //   async function fetchTracks() {
  //     try {
  //       const response = await fetch(url);
  //       if (!response.ok) {
  //         throw new Error(`Error: ${response.status}`);
  //       }
  //       const data = await response.json();
  //       setTracks(data);
  //     } catch (error) {
  //       console.error("Failed to fetch item:", error);
  //       return "Error"
  //     }
  //   }
  //   fetchTracks();
  //   console.log(tracks)
  // }, []); 

  let nextSong = () => {
    setCount(count+1);
  }

  if(count < tracks.length) {
    console.log(tracks)  
  return (
      
      <div style={{ textAlign: 'center', paddingTop: 30, backgroundColor: '#f2d9e6', margin: '0', height: '100vh', width: '100%' }}>
        <h1 id="SpotifySwiper">SPOTIFY SWIPER</h1>
  
        <SongSwipe 
          imagePath={tracks[count].photo_url}
          title={tracks[count].name}
          artist={tracks[count].artist}
          nextSong = {nextSong}
        />
      </div>
    );

  } else {
    return (<h1>Thanks for playing!</h1>)
  }

  
}

export default App;
