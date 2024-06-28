"use client"

import React from 'react';

const SongSwipe = ({ imagePath, title, artist, nextSong}) => {
  console.log("title" + title);
  console.log("artist" +artist);
  return (
    <div style={{ textAlign: 'center'}}>
      <img src={imagePath} alt="Album Cover" style={{ width: '400px', height: '400px', borderRadius: '8px', marginBottom: 20}} />
      <h3 id="title">{title}</h3>
      <p id="artist">{artist}</p>
      <div>
        <button onClick={() => nextSong()} style={{ border: '2px solid black', borderRadius: '5px', marginRight: 40 }}>
          <img
            src={require("./icons8-end-50.png")}
            style={{ width: '25px', height: '25px', padding: 0, transform: 'scaleX(-1)' }}
            alt="End Reflected"
          />
        </button>
        <button onClick={() => nextSong()} style={{ border: '2px solid black', borderRadius: '5px', marginLeft: 40 }}>
          <img
            src={require("./icons8-end-50.png")}
            style={{ width: '25px', height: '25px', padding: 0 }}
            alt="End"
          />
        </button>
      </div>
    </div>
  );
};

export default SongSwipe;