شناسایی و تشخیص چهره با دو کتابخانه بسیار معروف 
# face-recognition

This Python script performs face recognition in a video using the face_recognition and OpenCV libraries. The script detects a known face in the video and saves the frames where the face is recognized.

این اسکریپت پایتون با استفاده از کتابخانه های face_recognition و OpenCV، تشخیص چهره را در یک ویدیو انجام می دهد. این اسکریپت یک چهره شناخته شده را در ویدیو تشخیص می دهد و فریم هایی را که در آن صورت شناسایی می شود ذخیره می کند.

Requirements:
Python 3.x (last version 3.8)
OpenCV (pip install opencv-python)
face_recognition (pip install face_recognition)

Usage:
Install the required libraries using the following commands:

pip install opencv-python

pip install face_recognition


Replace the placeholder images and video file paths with your own in the script:
known_image_path: Path to the known face image.
video_file_path: Path to the video file.
search_image_path: Path to the image used for face recognition in the video.

Run the script:
python face_recognition_video.py

Press 'q' to exit the video playback.

Script Overview
Loads a known face image for recognition.
Uses a Haar cascade classifier for face detection.
Reads frames from a video file.
Compares each detected face with the known face using face recognition.
If a match is found, it draws a green rectangle around the detected face, prints the timestamp to the console, and saves the frame as an image.

Notes
Ensure that the video file and image paths are correctly set.
The script exits when the 'q' key is pressed.
Feel free to modify the script according to your specific requirements.
