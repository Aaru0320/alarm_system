**Streamlit-yolo-app**
The below content is for app_2.py
In this code, you are building a **Streamlit-based Object Detection Web App** using **YOLOv8** to detect objects in a video stream. The application allows users to input the name of a video file hosted on a simple local HTTP server, and the app will display the object detection results in real-time. Here's a breakdown of the purpose and functionality of the code:

1. **Local HTTP Video Server**
   - A simple **HTTP server** is created using Python's `http.server` module. This server serves video files from the local directory.
   - The server runs on a dynamically allocated free port to ensure it doesn't conflict with other services.
   - The server is started in a separate thread using Python's `threading` module, allowing it to serve video files while the Streamlit app runs.

2. **Streamlit Application**
   - **Title and Input Field:** The Streamlit app asks the user to input the name of the video file they wish to run object detection on. The video file should be located in the same directory as the script.
   - **Loading YOLO Model:** The app loads a **YOLOv8** (You Only Look Once) model using the `ultralytics` library. This model is used for real-time object detection in the video frames.
   - **Video Streaming and Object Detection:** 
     - When the user clicks the **"Start Object Detection"** button, the app attempts to stream the video from the local HTTP server.
     - If the video is found and successfully opened, the app reads the video frame-by-frame, runs object detection on each frame using the YOLO model, and displays the annotated frames (with bounding boxes and labels) on the Streamlit web interface.
   - **Error Handling:** If the video stream cannot be opened (e.g., the video file doesn't exist), the app displays an error message.

**Purpose of the Code**
- This application demonstrates how to build a **real-time object detection system** that allows users to load and analyze videos directly from a web interface. It combines the following components:
  - A **local video server** to serve video files over HTTP.
  - A **YOLOv8 object detection model** to process video frames and identify objects.
  - A **Streamlit web interface** to allow users to interact with the system and visualize results.

**How the App Works**
1. **Video File Server:** A simple HTTP server serves local video files, allowing the app to access them via a URL.
2. **User Input:** Users can specify the name of the video file they want to run object detection on.
3. **YOLOv8 Model:** The app uses YOLOv8 to detect objects in the video.
4. **Real-time Display:** Detected objects are highlighted and displayed on the web interface frame-by-frame.
5. **Error Messages:** If the video cannot be found or opened, the app informs the user to check the file path or server status.

**Why is this Useful?**
- The app provides a way to run object detection on videos from a local server, making it easier for developers and users to test videos without having to manually handle video files.
- It also shows how to integrate deep learning models, like YOLOv8, into a simple web-based interface for easy visualization of results.

**Potential Use Cases**
- **Security systems**: You can use this application to monitor security footage and detect objects of interest (e.g., people, vehicles).
- **Object tracking and analytics**: It can be expanded for real-time object tracking and analytics by processing video streams.
- **Custom deployments**: Useful in industries requiring real-time object detection, such as traffic monitoring, warehouse management, or retail analytics. 
