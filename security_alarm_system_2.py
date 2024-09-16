import sys
sys.path.append('/Users/aarushivishwakarma/theft_Detection/alarm_system/yolov5')  # Example: '/Users/aarushivishwakarma/theft_Detection/yolov5'

import streamlit as st
import cv2
import torch
import numpy as np 
from time import time 
from ultralytics import YOLO
from utilis.plots.py import colors, Annotator


import supervision as sv  


#the below code is for streamlit application running on local server
# x = st.slider("select a value")
# st.write(x, "squaredis", x*x)

#email send notification
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_settings import password, from_email, to_email


#create server
server = smtplib.SMTP("smtp.gmail.com: 587")
server.starttls()

#login credentials for send notification
server.login(from_email, password)

def send_email(to_email, from_email, object_detected=1):
    """Sends an email notification indicating the number of objects detected; defaults to 1 object."""
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = "Security Alert"
    # Add in the message body
    message_body = f"ALERT - {object_detected} objects has been detected!!"

    message.attach(MIMEText(message_body, "plain"))
    server.sendmail(from_email, to_email, message.as_string())

#object detection and alert sender
class ObjectDetection:
    def __init__(self, capture_index=0, video_path=None):
        """Initializes an ObjectDetection instance with a camera index or video file path."""
        self.capture_index = capture_index
        self.video_path = video_path
        self.email_sent = False

        # Model information
        self.model = YOLO("yolov8m.pt")

        # Device information
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def predict(self, im0):
        """Run prediction using a YOLO model for the input image `im0`."""
        results = self.model(im0)
        return results

    def display_fps(self, im0):
        """Displays FPS on an image by calculating and overlaying it."""
        self.end_time = time()
        fps = 1 / round(self.end_time - self.start_time, 2)
        text = f"FPS: {int(fps)}"
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
        gap = 10
        cv2.rectangle(im0, (20 - gap, 70 - text_size[1] - gap), 
                      (20 + text_size[0] + gap, 70 + gap), (255, 255, 255), -1)
        cv2.putText(im0, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)

    def plot_bboxes(self, results, im0):
        """Plots bounding boxes on an image."""
        class_ids = []
        self.annotator = Annotator(im0, 3, results[0].names)
        boxes = results[0].boxes.xyxy.cpu()
        clss = results[0].boxes.cls.cpu().tolist()
        names = results[0].names
        for box, cls in zip(boxes, clss):
            class_ids.append(cls)
            self.annotator.box_label(box, label=names[int(cls)], color=colors(int(cls), True))
        return im0, class_ids

    def __call__(self):
        """Run object detection on video frames from a video file or camera stream."""
        # If video path is provided, read from the video file; otherwise, use live capture
        cap = cv2.VideoCapture(self.video_path if self.video_path else self.capture_index)
        if not cap.isOpened():
            st.error("Error: Cannot open video source")
            return
        
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while True:
            self.start_time = time()
            ret, im0 = cap.read()
            if not ret:
                st.warning("Warning: Unable to retrieve frame. Exiting...")
                break
            results = self.predict(im0)
            im0, class_ids = self.plot_bboxes(results, im0)

            if len(class_ids) > 0 and not self.email_sent:
                send_email(to_email, from_email, len(class_ids))
                self.email_sent = True
            else:
                self.email_sent = False

            self.display_fps(im0)
            cv2.imshow("YOLOv8 Detection", im0)

            if cv2.waitKey(5) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
        server.quit()

#call the object detection class and run the inference
detector = ObjectDetection(capture_index=0)
detector()