**Streamlit-yolo-app**








THE BELOW CONTENT IS FOR **app_2.py**

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

The command to run app_2.py is:-  **streamlit run app_2.py**
This code is running on a port **localhost:8505**










THE BELOW CONTENT IS FOR **app_3.py**.

In this code, you are creating a **Streamlit-based Object Detection App** that allows users to upload a video, select an object detection model, and view the detected objects in real-time. The app uses **YOLOv8** (You Only Look Once) to perform object detection on each frame of the video and display the results directly in the Streamlit interface. 

Here's what this code aims to achieve, and how it works:

**Purpose of the Code**
- **Object Detection in Uploaded Videos:** This app provides a simple interface to upload a video file, select a detection model, and apply object detection algorithms to the video. It supports models like **YOLOv8** and can detect objects such as people, vehicles, animals, etc.
- **Real-time Visualization of Object Detection:** The video is processed frame-by-frame, and the detected objects are highlighted with bounding boxes and labels, which are displayed in the Streamlit app.
- **Video Processing Optimization:** The app also includes video transcoding to reduce file size for faster processing if the video file exceeds certain limits.

**How the App Works**
1. **File Upload:**
   - The app accepts video uploads in formats like **MP4**, **AVI**, or **MOV**. There's a limit of 20 MB to avoid large file processing delays.
   
2. **Model Selection:**
   - Users can choose between different object detection models:
     - **YOLOv8 Nano (Fast)**: A lightweight, fast model for quick processing.
     - **YOLOv8 Medium**: A more robust model for better detection accuracy.
     - **MobileNet (Lightweight)**: An alternative lightweight model, though in this example, it defaults to YOLOv8 Nano.

3. **Transcoding the Video (Optional):**
   - To avoid issues with large video sizes, the app uses **FFmpeg** to transcode the video. This reduces the video resolution and bitrate, making it more manageable for object detection and faster for processing.

4. **Object Detection Execution:**
   - Once the user selects a video and a model, the app processes the video:
     - It reads the video frame-by-frame.
     - It performs object detection using the chosen YOLOv8 model on each frame.
     - The results (bounding boxes and labels for detected objects) are overlaid on the frames.
     - The processed frames are then displayed in real-time in the Streamlit app, providing instant visual feedback of the detection process.

5. **Progress Bar and Real-time Feedback:**
   - A progress bar gives users a sense of how far the detection process has advanced.
   - Each processed frame is displayed as part of a continuous sequence, simulating a real-time object detection system.

6. **Error Handling:**
   - If the uploaded video exceeds the file size limit or cannot be processed, the app will display appropriate error messages.

**Why is this Useful?**
- **Real-time Object Detection:** It allows users to test object detection models on their own videos without requiring advanced coding or command-line expertise.
- **Interactive User Interface:** The Streamlit interface provides an easy way for users to interact with deep learning models and visualize the results.
- **Optimized for File Size:** By transcoding larger files, the app ensures that video processing remains fast and efficient.

**Use Cases**
- **Security Systems:** This app can be applied to detect intrusions, vehicles, or other objects of interest in security footage.
- **Surveillance:** Use the app for monitoring large areas for human presence, traffic, or wildlife.
- **Object Detection Research:** It serves as a tool for testing YOLO models on custom video data in real-time, making it useful for developers and researchers working on object detection problems.

**How to Use the Code**
1. **Upload a video file** by selecting it from your local system.
2. **Choose an object detection model** based on your performance needs (faster or more accurate).
3. **Start Object Detection**, and watch the real-time processing and display of detected objects in your video.



The command to run app_2.py is:-  **streamlit run app_3.py**
This code is running on a port **localhost:8505**


**Usage of configuration file**

This section of the configuration file is used to configure **Cloudflare Tunnel**, which securely exposes local services to the internet without needing to open ports or configure a firewall. Here’s a breakdown of the purpose of each part of the code:

**Tunnel:**
- **tunnel: <0c03c186-1ca2-441c-87c2-4718b33bd06a>**
  - This is the unique ID for the Cloudflare Tunnel. Each tunnel you create is identified by a unique identifier, and Cloudflare uses this ID to route traffic securely to the tunnel you created.

**Credentials File:**
- **credentials-file: /Users/aarushivishwakarma/.cloudflared/0c03c186-1ca2-441c-87c2-4718b33bd06a.json**
  - This is the path to the credentials file used to authenticate the tunnel with Cloudflare. This file contains necessary information to establish and maintain a secure connection between your local machine and Cloudflare’s servers.

**Ingress Rules:**
The `ingress` section defines how incoming traffic will be routed through the tunnel to your local services.

- **- hostname: myapp.ai4india.online**
  - This defines a **public hostname** that Cloudflare will associate with your tunnel. When users visit `myapp.ai4india.online`, Cloudflare will route traffic to this tunnel.
  
- **service: http://localhost:8505**
  - This specifies that the local service running on `http://localhost:8502` (on your machine) will be exposed to the public via the `myapp.ai4india.online` domain. For example, if you're running a **Streamlit app** on port `8505` locally, this will make it accessible through the internet under the given hostname.
  
- **- service: http_status:404**
  - This serves as a fallback route. If no specific hostname or service matches the incoming request, the tunnel will respond with an HTTP **404 status** (Not Found). This ensures that invalid requests that don't match the hostname (`myapp.ai4india.online`) get a 404 response rather than hitting your local services.

**Purpose of this Configuration:**
1. **Expose Local Service**: This configuration is exposing a service running on `http://localhost:8505` (like a web app or API) to the public via the hostname `myapp.ai4india.online`.
2. **Security**: Cloudflare Tunnel allows this exposure securely without the need to open ports in your firewall or configure your network manually.
3. **Fallback Handling**: The 404 rule ensures that any requests that don't match your intended routes (e.g., a mistyped domain) are properly handled by returning a **404 Not Found** response.

This setup is typically used when you want to securely make a local web application available to users over the internet.



**Usage of dockerfile**

This Dockerfile is used to containerize a **Streamlit application** that also relies on some additional dependencies, such as **ffmpeg** and a custom Python environment. Here's a detailed breakdown of each part of the Dockerfile and what you can explain in your README:

**1. Base Image**
```dockerfile
FROM python:3.9-slim
```
- This uses the lightweight `python:3.9-slim` image as the base. It’s a minimal Python environment (version 3.9) which provides all the essential Python features without unnecessary components. 
- **Purpose**: It ensures that the container has Python installed and is optimized for performance and size.

**2. Environment Variables**
```dockerfile
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
```
- **`PYTHONDONTWRITEBYTECODE`**: This prevents Python from generating `.pyc` files, which helps reduce unnecessary disk writes.
- **`PYTHONUNBUFFERED`**: This makes Python output to the console immediately, ensuring you get logs in real-time (especially useful in Dockerized environments).
- **Purpose**: These environment variables optimize the container for performance and debugging.

**3. System Dependencies Installation**
```dockerfile
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
    curl \
    && rm -rf /var/lib/apt/lists/*
```
- **System dependencies**: `build-essential` is needed for compiling packages, and `ffmpeg`, `libsm6`, and `libxext6` are necessary for video processing, especially with OpenCV.
- **Purpose**: These libraries ensure the container has the necessary system dependencies to process video files, making it suitable for an application like yours that handles object detection with video input.

**4. Install `ffmpeg`**
```dockerfile
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*
```
- **ffmpeg**: This command installs `ffmpeg`, which is a crucial tool for transcoding, processing, and streaming video and audio.
- **Purpose**: Since your application processes video files, `ffmpeg` is required to transcode and reduce file size for object detection tasks.

**5. Working Directory**
```dockerfile
WORKDIR /app
```
- **WORKDIR**: This sets the working directory inside the container to `/app`, where the application’s code will be located.
- **Purpose**: It ensures that all subsequent commands are executed inside the `/app` directory.

**6. Copy Project Files**
```dockerfile
COPY . /app
```
- **COPY**: This command copies all the files from your local project directory to the `/app` directory inside the container.
- **Purpose**: It transfers your application code, including the Python scripts, configuration files, and resources, into the container so it can be executed.

**7. Install Python Dependencies**
```dockerfile
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
```
- **Upgrade pip**: This ensures you’re using the latest version of `pip`.
- **Install requirements**: It installs all the Python dependencies listed in `requirements.txt`.
- **Purpose**: It sets up the Python environment with the necessary libraries for your app (e.g., `streamlit`, `ultralytics`, `opencv-python`, etc.).

**8. Expose the Streamlit Port**
```dockerfile
EXPOSE 8505
```
- **EXPOSE 8505**: This command tells Docker to expose port `8505`, which is the default port for Streamlit. 
- **Purpose**: It allows external access to the app on this port when the container is run.

**9. Run the Streamlit App**
```dockerfile
CMD ["streamlit", "run", "app_3.py", "--server.port=8505", "--server.address=0.0.0.0"]
```
- **CMD**: This sets the default command that will run when the container starts. It runs the `app_3.py` Streamlit app on port `8505` and binds it to all available network interfaces (`0.0.0.0`).
- **Purpose**: It starts the Streamlit application when the container is launched, making it accessible via the exposed port.

**Summary:**
This Dockerfile is used to create a lightweight, isolated environment for running a **Streamlit-based object detection application**. The container is based on Python 3.9 and includes necessary system libraries for video processing, such as **ffmpeg** and **OpenCV** dependencies.

The Dockerfile performs the following key actions:
1. Sets up a minimal Python 3.9 environment.
2. Installs necessary system and Python dependencies for video processing and object detection.
3. Copies the application files into the container.
4. Exposes port `8505`, which is used by Streamlit.
5. Runs the Streamlit app (`app_3.py`) when the container is started.

By containerizing the app, this Dockerfile ensures that the application can be deployed consistently across different environments without needing to manually install dependencies or deal with compatibility issues.





The command to run it on local server is :- **docker run -p 8505:8505 streamlit-yolo-app**

The command to run it across the internet server is :- **cloudflared tunnel --config /Users/aarushivishwakarma/theft_Detection/streamlit-yolo-app/configuration-file run my-tunnel** (this command has to run in another terminal and don't stop it otherwise it will not run the server across internet)

The website is **myapp.ai4india.online**