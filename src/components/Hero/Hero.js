import React, { useEffect, useState } from "react";
import "./Hero.css";

function Hero() {
  const [images, setImages] = useState([]);
  const [imageUrls, setImageUrls] = useState([]);
  useEffect(() => {
    if (images.length < 1) return;
    const newImageUrls = [];
    images.forEach((image) => newImageUrls.push(URL.createObjectURL(image)));
    setImageUrls(newImageUrls);
  }, [images]);
  function onImageChange(e) {
    setImages([...e.target.files]);
  }
  return (
    <div className="hero">
      <div className="des">
        <h1 className="title">Welcome to Logo</h1>
        <form>
          <div className="for">
            <div className="col-10 col-md-10">
              <input
                type="file"
                className="form-control"
                accept="image/*"
                onChange={onImageChange}
              />
            </div>
            <div className="col-2 col-md-2">
              <button
                className="btn btn-primary"
                style={{
                  "background": "#0088CC",
                  "borderRadius": "8px",
                  "fontWeight": "600",
                  "marginLeft": "20px",
                }}
                type="submit"
              >
                Upload
              </button>
            </div>
          </div>
          {/* {imageUrls.map((ima) => (
        <img src={ima} />
      ))} */}
          {/* <input type="file" accept="image/*" onChange={onImageChange} /> */}
        </form>
      </div>
    </div>
  );
}

export default Hero;
