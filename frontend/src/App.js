import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';

const socket = io('http://localhost:8000');

function App() {
  const [pictureStatus, setPictureStatus] = useState("");

  useEffect(() => {
    socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });
    return () => {
      socket.off('picture_taken');
    };
  }, []);

  return (
    <div className="app">
      <h1>HACK 2025</h1>
    </div>
  );
}

export default App;
