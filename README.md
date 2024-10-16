This is a python based program that detects objects in a video streaming application. The goal is to create a dockerized application that be spun in any enviroment and Xynocast can cater the images over cloud.



The below content is for **new_security_system.py**

In this code, you're building a **real-time object detection system** using Streamlit and the YOLOv8 model, with the added functionality of sending **email alerts** when objects are detected. Here's a breakdown of what the code does and how you can describe it in the README:

### **Purpose of the Code:**
This application is designed to detect objects from a video stream or live webcam feed using the **YOLOv8** object detection model. It displays the video frames with bounding boxes around detected objects and sends an email alert when objects are detected. The application can work with either pre-recorded video files (uploaded by the user) or a live webcam feed.

### **How the Code Works:**

1. **Object Detection with YOLOv8:**
   - The system uses the **YOLOv8 medium model (`yolov8m.pt`)** to detect objects in video frames. YOLO is a real-time object detection model that identifies and localizes objects in an image.
   - The model is loaded and used to make predictions on each frame of the video or live webcam feed.

2. **Video Input:**
   - The code supports both **video file uploads** and **live webcam feeds**. If a video file is uploaded, it processes the video frame by frame; otherwise, it defaults to using the computer's webcam.

3. **Bounding Boxes:**
   - Detected objects are **highlighted with bounding boxes**. The `plot_bboxes()` method draws these bounding boxes on the frame, labeling them with the corresponding object classes (e.g., person, car).

4. **Displaying FPS:**
   - The system calculates and displays the **frames per second (FPS)** on each frame. This gives users an idea of how fast the object detection is being performed in real-time.

5. **Email Alerts:**
   - When objects are detected in the video feed, an **email alert** is sent to a specified recipient. The `send_email()` function sends an email notifying the recipient that one or more objects have been detected. The email includes the number of detected objects.
   - The email is sent only once for the first detection, and the system resets the email flag after that to avoid spamming.

6. **Streamlit Integration:**
   - The code integrates with **Streamlit** to provide a **web-based interface** where users can upload videos, view the real-time video processing, and receive feedback (such as detection results and email notifications).
   - The application includes an intuitive file uploader for video files, and it displays real-time object detection output directly in the Streamlit interface.

7. **Video Capture and Display:**
   - The `__call__()` method captures frames from the video or webcam stream and passes them to the YOLO model for prediction.
   - It uses OpenCV (`cv2.imshow`) to display the processed video with bounding boxes overlaid on the detected objects.

**Real-Time Object Detection System**

This application is a **real-time object detection system** built using **YOLOv8** and **Streamlit**. It allows users to either upload a video file or use their live webcam feed to detect objects in the video stream. The system can detect multiple objects in each frame and highlights them with bounding boxes, along with displaying the frames per second (FPS) for real-time performance.

**Key Features:**
1. **Object Detection with YOLOv8:**
   - Uses the YOLOv8 medium model to detect objects in each frame of the video.
   - Bounding boxes and labels are drawn on the video to indicate detected objects.
   
2. **Video Input:**
   - Supports both **pre-recorded video files** (e.g., MP4, AVI, MOV) and **live webcam feed**.
   - Users can upload a video file through the Streamlit interface.

3. **Email Notifications:**
   - Sends an **email alert** whenever one or more objects are detected in the video stream.
   - The email contains the number of detected objects and is sent only once during each detection event.

4. **Real-Time Display:**
   - Displays the video frames with **bounding boxes** over detected objects.
   - Shows the **frames per second (FPS)**, providing feedback on the speed of the detection process.

**How It Works:**
- The system captures video frames either from an uploaded video file or a live webcam feed.
- Each frame is passed through the YOLOv8 model, which detects objects and returns the bounding boxes and class labels.
- If objects are detected, the system sends an email notification to the specified email address, alerting the user to the detection event.
- The processed video (with bounding boxes) is displayed in real-time via the Streamlit web interface.
  
**Dependencies:**
- **YOLOv8** for object detection.
- **OpenCV** for video capture and processing.
- **Streamlit** for the web interface.
- **SMTP** for sending email alerts.




**Why we have another file as **email_settings.py**

In the `email_settings.py` file, the purpose of the code is to store **email credentials** that are used to send automated email notifications in the application.

### Purpose:
- **`password`**: This is the app-specific password generated for the sender's Gmail account (in this case, `aarushivishwakarma65@gmail.com`). It allows the application to authenticate and log into the Gmail SMTP server to send emails.
- **`from_email`**: This is the email address from which the notification emails will be sent. The email must match the one used to generate the app password for security reasons.
- **`to_email`**: This is the recipient's email address, where the alerts or notifications will be sent (in this case, `kunal@xynocast.com`).

### Why This Code Is Used:
1. **Automated Email Alerts**: The application (e.g., an object detection system) sends notifications via email when certain events (like detection of objects) occur. This is useful in security systems or surveillance setups.
   
2. **Security**: By storing the email credentials separately in a file, the application can securely access the necessary details without hardcoding sensitive information directly into the main logic.

3. **Modular Setup**: Keeping the email settings in a separate file makes the code more modular and easier to manage. If the email credentials or recipient changes, you can update them in the `email_settings.py` file without modifying the main codebase.

### Example for README:
```markdown
### Email Settings

The `email_settings.py` file stores the email credentials required for sending notifications from the application. These credentials include:
- `password`: An app-specific password for the Gmail account used to send the email.
- `from_email`: The sender's email address.
- `to_email`: The recipient's email address for receiving notifications.

The email functionality is used to notify users when specific events (e.g., object detection) occur in the system.





**The files app.py, security_alarm_system.py, security_alarm_system_2.py are the working drafts .**



The command to run new_security_system.py :- **python new_security_system.py**