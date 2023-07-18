import React from "react";
import "./css/styles.css";
import { Outlet, Link } from "react-router-dom";


const HomePage = () => {

  return (

    <>
      <div className="top-box">

      </div>
      <center>
        <div className="main-box">
          <Link to="upload-video" style={{ textDecoration: 'none' }}>
            <h1 className="cont-box">Upload video</h1>
          </Link>
          <Link to="video-list" style={{ textDecoration: 'none' }}>
            <h1 className="cont-box">Video list</h1>
          </Link>
        </div>
      </center>
    </>

  )

}

export default HomePage