import React from "react";
import "./css/styles.css";
import axios from "axios";

const UploadPage = () => {


  const [video, setVideo] = React.useState([])
  const [title, setTitle] = React.useState([])
  const [submited, setsubmited] = React.useState([])
  const [checkboxval, setcheckboxval] = React.useState(false)

  function setVideoTofile(e) {
    setVideo(e.target.files[0])
  }

  function setTitleHandler(e) {
    setTitle(e.target.value)
  }

  // to add subtitle into formdata
  let subtitles = []
  let subtitleForm = new FormData();
  function addSubtitle(e) {
    if (e.target.files) {
      subtitleForm.append("subtitle", e.target.files[0])
    }
    else {
      subtitleForm.append("language", e.target.value)
    }
    subtitleForm.append("video", submited)

    if (subtitleForm.has("subtitle") && subtitleForm.has("language")) {
      subtitles.push(subtitleForm)
    }
  }

  // for submitting subtitles
  function submitSubtitles(e) {
    if (subtitles.length > 0) {
      subtitles.forEach((sub) => {
        axios.post('http://localhost:8000/video/subtitles/', sub)
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
      })
    }
  }

  // for submitting video without subtitle
  function submitHandler(e) {
    let vidFormOne = new FormData();
    vidFormOne.append('video_file', video)
    vidFormOne.append('title', title)
    axios.post('http://127.0.0.1:8000/video/videos/', vidFormOne)
      .then(function (response) {
        setsubmited(response.data.id)
        console.log(response);
        document.getElementById("check-box").style.display = "block"
      })
      .catch(function (error) {
        console.log(error);
      });
  }


  // toggle for subtitle options
  function toggleBox(e) {
    setcheckboxval(e.target.checked)
    let box1 = document.getElementById("hidden-box1")
    let box2 = document.getElementById("hidden-box2")
    let box3 = document.getElementById("hidden-box3")
    if (e.target.checked == true) {
      box1.style.display = "flex"
      box2.style.display = "flex"
      box3.style.display = "flex"
    }
    else {
      box1.style.display = "none"
      box2.style.display = "none"
      box3.style.display = "none"
    }
  }


  return (
    <>
      <div className="title">
        <h4>Add your video here</h4>
      </div>
      <div className="file-upload">
        <input class="form-control" type="text" placeholder="Video title" onChange={setTitleHandler} />
        <br />
        <div className="video-upload-wrap">

          <input className="file-upload-input" type='file'
            onChange={setVideoTofile}
            accept="video/*"
          />
          <div className="drag-text">
            <h3>Drag and drop video or select video</h3>
          </div>
        </div>
        <div className="file-upload-content">
          <img className="file-upload-video" src="#" alt="your video" />
          <div className="video-title-wrap">
            <button type="button" className="remove-video">Remove <span className="video-title">Uploaded Video</span></button>
          </div>
        </div>

        {/* <input type="file" accept="image/*" /> */}
      </div>
      <div className="submit-box" style={{ padding: "10px 20px" }}>
        <button type="button" class="submit-btn btn btn-outline-primary" onClick={submitHandler}>Submit</button>
      </div>
      <br />

      {/* checkbox for subtitle options */}
      <div class="form-check" style={{ display: "none" }} id="check-box">
        <div style={{ display: "flex", justifyContent: "center", marginBottom: "10px" }}>

          <input class="form-check-input" onChange={toggleBox} type="checkbox" value={checkboxval} id="flexCheckChecked" />
          <label class="form-check-label" for="flexCheckChecked">
            Add subtitles
          </label>
        </div>
      </div>


      {/* subtitle options */}
      <div
        className="file-upload"
        id="hidden-box1"
        style={{ padding: "10px 20px", display: "none", justifyContent: "space-between", }}
      >
        <input type="file" id="files" class="" onChange={addSubtitle} />

        <div style={{ display: "flex", justifyContent: "end" }}>
          <h5>Select subtitle</h5>
          &nbsp;&nbsp;
          <select className="" onChange={addSubtitle}>
            <option selected value="0">Select language</option>
            <option value="1">English</option>
            <option value="2">हिंदी</option>
          </select>
        </div>

      </div>

      <br />

      <div
        className="file-upload"
        id="hidden-box2"
        style={{ padding: "10px 20px", display: "none", justifyContent: "space-between", }}
      >
        <input type="file" id="files" class="" />

        <div style={{ display: "flex", justifyContent: "end" }}>
          <h5>Select subtitle</h5>
          &nbsp;&nbsp;
          <select className="">
            <option selected value="0">Select language</option>
            <option value="1">English</option>
            <option value="2">हिंदी</option>
          </select>
        </div>

      </div>
      {/* subtitle options */}

      <div
        id="hidden-box3"
        className="submit-box" style={{ padding: "10px 20px", display: "none" }}
      >
        <button type="button" class="submit-btn btn btn-outline-primary" onClick={submitSubtitles} >Submit Subtitles</button>
      </div>




    </>
  )
}

export default UploadPage;