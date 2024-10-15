import streamlit as st
import cv2
import time
import numpy as np
from ultralytics import YOLO
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Move set_page_config to the very top before any Streamlit command
st.set_page_config(layout="wide")

# Title
st.title("Object Detection App")

# Set a maximum file size limit in bytes (e.g., 20 MB)
MAX_FILE_SIZE = 15 * 1024 * 1024  # 20 MB

# Step 1: Allow Users to Upload Video Files
st.header("Upload a video file for object detection")
uploaded_video = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

# Step 2: Select Object Detection Model
st.header("Select an Object Detection Model")
model_choice = st.selectbox(
    "Choose a model:",
    ["YOLOv8 Nano (Fast)", "YOLOv8 Medium", "MobileNet (Lightweight)"]
)

# Step 3: Load the YOLO or MobileNet model based on user selection
@st.cache_resource
def load_model(model_name):
    """Load the selected YOLO or MobileNet model."""
    if model_name == "YOLOv8 Nano (Fast)":
        return YOLO("yolov8n.pt")
    elif model_name == "YOLOv8 Medium":
        return YOLO("yolov8m.pt")
    else:
        return YOLO("yolov8n.pt")  # For demo purposes, we use YOLOv8 Nano

model = load_model(model_choice)

# Step 4: Efficient video transcoding function
def transcode_video(input_file, output_file):
    """Transcodes the video to a smaller size for faster processing."""
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'scale=640:-1',  # Reduce resolution (width = 640, height = auto)
        '-b:v', '500k',  # Set video bitrate to 500k
        '-y',  # Overwrite output file without asking
        output_file
    ]
    subprocess.run(command, check=True)

# Step 5: Function to process video with object detection
def process_video(video_file, model):
    """Process the video file with the selected object detection model."""
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        st.error("Error opening video file. Please try again.")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    st_frame = st.empty()  # Placeholder for displaying frames
    progress_bar = st.progress(0)

    # Using thread pool for parallel frame processing
    def process_frame(frame):
        """Helper function to process a single frame."""
        results = model(frame)
        annotated_frame = results[0].plot()
        return annotated_frame

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        frame_num = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Submit the frame to be processed in parallel
            future = executor.submit(process_frame, frame)
            futures.append(future)

            # Buffer control: Limit the number of concurrent futures to reduce lag
            if len(futures) >= 10:
                annotated_frame = futures.pop(0).result()  # Get the next completed frame
                st_frame.image(annotated_frame, channels="BGR", use_column_width=True)

            # Update progress bar every 10 frames
            frame_num += 1
            if frame_num % 10 == 0:
                progress_percentage = int((frame_num / frame_count) * 100)
                progress_bar.progress(progress_percentage / 100)

            time.sleep(0.01)  # Small delay for better UI responsiveness

        # Process any remaining frames
        while futures:
            annotated_frame = futures.pop(0).result()
            st_frame.image(annotated_frame, channels="BGR", use_column_width=True)

    # Cleanup
    cap.release()
    progress_bar.progress(100)
    st.success("Processing complete!")

# Step 6: Execute the video processing if a video is uploaded
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

        # Run the detection process
        process_video(transcoded_video_path, model)

# Step 7: Clean up temporary files after processing to avoid filling up storage
def cleanup_files():
    try:
        if os.path.exists("temp_video.mp4"):
            os.remove("temp_video.mp4")
        if os.path.exists("transcoded_video.mp4"):
            os.remove("transcoded_video.mp4")
    except Exception as e:
        st.error(f"Error cleaning up files: {e}")

cleanup_files()

