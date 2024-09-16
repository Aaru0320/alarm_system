import sys
sys.path.append('/Users/aarushivishwakarma/theft_Detection/alarm_system/yolov5')  # Example: '/Users/aarushivishwakarma/theft_Detection/yolov5'

import streamlit as st
import cv2
import torch
import numpy as np 
from time import time 
from ultralytics import YOLO
from utils.plots import colors, Annotator

import supervision as sv  

# email send notification
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_settings import password, from_email, to_email

# Create server
server = smtplib.SMTP("smtp.gmail.com: 587")
server.starttls()

# Login credentials for sending notifications
server.login(from_email, password)

def send_email(to_email, from_email, object_detected=1):
    """Sends an email notification indicating the number of objects detected; defaults to 1 object."""
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = "Security Alert"
    # Add in the message body
    message_body = f"ALERT - {object_detected} objects have been detected!!"
    message.attach(MIMEText(message_body, "plain"))
    server.sendmail(from_email, to_email, message.as_string())

# Object detection and alert sender
class ObjectDetection:
    def __init__(self, capture_index):
        """Initializes an ObjectDetection instance with a given capture index or video path."""
        self.capture_index = capture_index
        self.email_sent = False

        # Model information
        self.model = YOLO("yolov8m.pt")

        # Visual information
        self.annotator = None
        self.start_time = 0
        self.end_time = 0

        # Device information
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def predict(self, im0):
        """Run prediction using a YOLO model for the input image `im0`."""
        results = self.model(im0)
        return results

    def display_fps(self, im0):
        """Displays the FPS on an image `im0` by calculating and overlaying as white text on a black rectangle."""
        self.end_time = time()
        fps = 1 / round(self.end_time - self.start_time, 2)
        text = f"FPS: {int(fps)}"
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
        gap = 10
        cv2.rectangle(
            im0,
            (20 - gap, 70 - text_size[1] - gap),
            (20 + text_size[0] + gap, 70 + gap),
            (255, 255, 255),
            -1,
        )
        cv2.putText(im0, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)

    def plot_bboxes(self, results, im0):
        """Plots bounding boxes on an image given detection results; returns annotated image and class IDs."""
        class_ids = []
        self.annotator = Annotator(im0, 3, results[0].names)
        boxes = results[0].boxes.xyxy.cpu()
        clss = results[0].boxes.cls.cpu().tolist()
        names = results[0].names
        for box, cls in zip(boxes, clss):
            class_ids.append(cls)
            self.annotator.box_label(box, label=names[int(cls)], color=colors(int(cls), True))
        return im0, class_ids
def run(self):
    """Run object detection on video frames from a video file, plotting and showing the results in Streamlit."""
    video_path = '/Users/aarushivishwakarma/theft_Detection/alarm_system/store-aisle-detection.mp4'
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), "Error: Unable to open video file."

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video_path = temp_video.name

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(temp_video_path, fourcc, 20.0, (640, 480))

        while True:
            self.start_time = time()
            ret, im0 = cap.read()
            if not ret:
                break

            results = self.predict(im0)
            im0, class_ids = self.plot_bboxes(results, im0)

            if len(class_ids) > 0 and not self.email_sent:
                send_email(to_email, from_email, len(class_ids))
                self.email_sent = True

            self.display_fps(im0)
            out.write(im0)

        cap.release()
        out.release()

        st.video(temp_video_path)
        # server.quit()

# Call the object detection class and run the inference
detector = ObjectDetection(capture_index=0)
detector.run()  # Explicitly call the method
