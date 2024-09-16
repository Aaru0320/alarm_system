import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import os
import socket

# Set up a simple HTTP server to serve the video file
class VideoHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def run_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, VideoHandler)
    print(f"Serving video on port {port}")
    httpd.serve_forever()

# Start the server in a separate thread
server_port = find_free_port()
server_thread = threading.Thread(target=run_server, args=(server_port,))
server_thread.daemon = True
server_thread.start()

# Streamlit app
def main():
    st.title("Object Detection with YOLO")

    # Input for video file name
    video_file = st.text_input("Enter the name of the video file on the local server:", "store-aisle-detection.mp4")

    # Load the YOLOv8 model
    @st.cache_resource
    def load_model():
        return YOLO("yolov8n.pt")
    
    model = load_model()

    if st.button("Start Object Detection"):
        # Construct the URL for the video file
        video_url = f"http://localhost:{server_port}/{video_file}"
        
        st.text(f"Attempting to open video from: {video_url}")

        # Open the video stream
        cap = cv2.VideoCapture(video_url)

        # Check if the video stream is opened successfully
        if not cap.isOpened():
            st.error(f"Error opening video stream or file: {video_url}")
            st.error("Please make sure the video file exists in the same directory as this script.")
            return

        # Create a Streamlit image placeholder
        image_placeholder = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Perform object detection
            results = model(frame)

            # Draw bounding boxes and labels on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            image_placeholder.image(annotated_frame, channels="BGR")

        cap.release()

if __name__ == "__main__":
    main()