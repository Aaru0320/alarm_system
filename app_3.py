import streamlit as st
import os
import cv2
import time
import numpy as np
from ultralytics import YOLO
import subprocess

# Set Streamlit page layout
st.set_page_config(layout="wide")

# Title
st.title("Object Detection App")

# Set a maximum file size limit in bytes (e.g., 20 MB)
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB

# Step 1: Allow Users to Upload Video Files
st.header("Upload a video file for object detection")
uploaded_video = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

# Check if the uploaded video exceeds the size limit
if uploaded_video is not None and uploaded_video.size > MAX_FILE_SIZE:
    st.error("File size exceeds 20 MB. Please upload a smaller video.")
else:
    # Step 2: Select Object Detection Model
    st.header("Select an Object Detection Model")
    model_choice = st.selectbox(
        "Choose a model:",
        ["YOLOv8 Nano (Fast)", "YOLOv8 Medium", "MobileNet (Lightweight)"]
    )

    # Step 3: Load the YOLO or MobileNet model based on user selection
    @st.cache_resource
    def load_model(model_name):
        if model_name == "YOLOv8 Nano (Fast)":
            return YOLO("yolov8n.pt")
        elif model_name == "YOLOv8 Medium":
            return YOLO("yolov8m.pt")
        else:
            return YOLO("yolov8n.pt")  # For demo purposes, we will use YOLOv8 Nano

    model = load_model(model_choice)

    # Function to transcode video to reduce its size
    def transcode_video(input_file, output_file):
        command = [
            'ffmpeg',
            '-i', input_file,
            '-vf', 'scale=640:-1',  # Reduce resolution (width = 640, height = auto)
            '-b:v', '500k',  # Set video bitrate to 500k
            '-y',  # Overwrite output file without asking
            output_file
        ]
        subprocess.run(command, check=True)

    # Step 4: Define function to process video
    def process_video(video_file, model):
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            st.error("Error opening video file. Please try again.")
            return
        
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        st_frame = st.empty()  # Placeholder for displaying frames
        progress_bar = st.progress(0)

        # Process video frame by frame
        frame_num = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Perform object detection on the current frame
            results = model(frame)
            annotated_frame = results[0].plot()

            # Display the annotated frame in Streamlit
            st_frame.image(annotated_frame, channels="BGR", use_column_width=True)

            # Update progress bar
            frame_num += 1
            progress_percentage = int((frame_num / frame_count) * 100)
            progress_bar.progress(progress_percentage)

            # Delay for better visualization
            time.sleep(0.03)

        cap.release()
        progress_bar.progress(100)

    # Step 5: Execute the video processing if a video is uploaded
    if uploaded_video and uploaded_video.size <= MAX_FILE_SIZE:
        # Write the video to a temporary location for OpenCV to process
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_video.getbuffer())

        # Transcode the video to reduce its size
        transcoded_video_path = "transcoded_video.mp4"
        transcode_video("temp_video.mp4", transcoded_video_path)

        st.success(f"Uploaded and transcoded: {uploaded_video.name}")

        # Start object detection when the user clicks the button
        if st.button("Start Object Detection"):
            st.info("Processing video, this may take some time depending on the video length and model selected.")
            process_video(transcoded_video_path, model)  # Run the process synchronously
            st.success("Object detection complete!")