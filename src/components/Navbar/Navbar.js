import React from 'react'
import "./Navbar.css"

function Navbar() {
  return (
    <div className="navbar">
      <h1>Logo</h1>
      <div className="links">
        <a className='link'>Home</a>
        <a className='link'>Github</a>
        <a className='link'>About Us</a>
        <a className='link'>Contact Us</a>
        <button className='signin'>Sign In</button>
      </div>
    </div>
  );
}

export default Navbar