import logo from './logo.svg';
import './App.css';
import UploadPage from './components/UploadPage';
import HomePage from './components/HomePage';
import VideoList from './components/VideoList';
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route, } from "react-router-dom";



function App() {
  return (

    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/upload-video" element={<UploadPage />} />
        <Route path="/video-list" element={<VideoList />} />
      </Routes>
    </BrowserRouter>

  );
}

export default App;
