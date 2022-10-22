import React from 'react';
import Hero from './components/Hero/Hero';
import "./index.css";
import Navbar from './components/Navbar/Navbar';
import bg from "./bg.mp4"
function App() {
  return (
    <>
      <video src={bg} autoPlay loop muted></video>
      <div className="content">
        <Navbar />
        <Hero />
      </div>
    </>
  );
}

export default App;
