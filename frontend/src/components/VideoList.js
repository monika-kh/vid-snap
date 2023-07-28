import React from "react";
import $ from "jquery";
// import "./css/styles.css";
import "./css/list.css";
import kang from "../images/kang.jpg"
import PlayCircleIcon from '@mui/icons-material/PlayCircle';
import FileDownloadIcon from '@mui/icons-material/FileDownload';
import axios from "axios";
import ReactPlayer from 'react-player'
import Swal from 'sweetalert2'


const VideoList = () => {

  function callVideo(e) {
    setVideoFilePath(e)
  }

  const [videoList, setVideoList] = React.useState([])
  const [merged, setmerged] = React.useState(false)

  React.useEffect(() => {
    axios.get('http://127.0.0.1:8000/video/videos/')
      .then(function (response) {
        setVideoList(response.data)
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }, [merged])

  function mergeSubtitle(e) {
    let subtitle_id = e.target.previousElementSibling.innerHTML
    let video_id = e.target.previousElementSibling.previousElementSibling.innerHTML
    axios.get(`http://localhost:8000/video/videos/${video_id}/?lang=${subtitle_id}`)
      .then(function (response) {
        setVideoList(response.data)
        console.log(response);
        setmerged(true)
        Swal.fire(
          'Now you can play this video with subtitle!',
        )
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  const [videoFilePath, setVideoFilePath] = React.useState(null);


  return (
    <>
      <h1>UI Card</h1>
      <div className="container">
        <div className="row">

          {
            videoList.length > 0 ?
              videoList.map((el) => {
                return (
                  <div className="col-md-4">
                    <div className="blog-card blog-card-blog">
                      <div className="blog-card-image">
                        <img className="img" src={el.thumbnail} />
                        <div className="ripple-cont"></div>
                      </div>

                      <div className="blog-table" style={{ marginBottom: "10px" }}>
                        <h4 className="blog-card-caption">
                          <h4 className="blog-card-caption">
                            {el.title ? el.title : "Video"}
                          </h4>
                        </h4>

                        <div>
                          <span>{el.subtitles.length > 0 ? "Select subtitles" : " Video has not subtitles"}</span>
                          &nbsp;&nbsp;
                          {
                            el.subtitles ?
                              el.subtitles.map((subtitle) => {
                                return (
                                  <>
                                    <span style={{ display: "none" }}>{el.id}</span>
                                    <span style={{ display: "none" }}>{subtitle.language}</span>
                                    <span style={{ fontWeight: "800", fontSize: "18px", cursor: "pointer" }} onClick={mergeSubtitle}>
                                      {subtitle.language_name}
                                      <span><br />Click on subtitle to play video</span>
                                    </span>
                                  </>
                                )
                              })
                              : null
                          }
                        </div>
                        <div style={{ display: "flex", justifyContent: "space-between", paddingBottom: "5px" }}>
                          <a href="#myModal" data-toggle="modal" onClick={(e) => callVideo(el.processed_video ? el.processed_video : el.video_file)}>
                            {el.processed_video ?
                              <>
                                <PlayCircleIcon style={{ width: "40px", height: "40px", cursor: "pointer" }} />
                              </>
                              : null}
                          </a>
                        </div>

                      </div>
                    </div>
                  </div>
                )
              })
              : null
          }

        </div>
      </div>

      <div class="bs-example">

        <div id="myModal" class="modal fade">
          <div class="modal-dialog">
            <div class="modal-content">
              <button type="button" class="close" data-dismiss="modal">&times;</button>
              <div class="modal-body">
                <div class="embed-responsive embed-responsive-16by9">
                  {
                    videoFilePath ? <ReactPlayer url={videoFilePath} width="100%" height="100%" controls={true} /> : null
                  }

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </>
  )

}

export default VideoList