import cv2
import face_recognition
from datetime import datetime

# Load the known face image
known_image_path = "path/to/known_face.jpg"
known_image = face_recognition.load_image_file(known_image_path)
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize the face detector
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# IP camera URL (replace with your camera's URL)
camera_url = "http://your_camera_ip:your_camera_port/video"

# Open the video stream from the IP camera
video_capture = cv2.VideoCapture(camera_url)

# Load the image for face recognition in the video
search_image_path = "path/to/search_image.jpg"
search_image = face_recognition.load_image_file(search_image_path)
search_face_encoding = face_recognition.face_encodings(search_image)[0]

# Flag to indicate if a match has been found
match_found = False

# Get the start time of the video
start_time = datetime.now()

while True and not match_found:
    # Capture video frame-by-frame
    ret, frame = video_capture.read()

    # Check if the frame is empty (end of video)
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the video frame
    faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Crop the face region from the frame
        face_image = frame[y:y+h, x:x+w]

        # Encode the face for recognition
        face_encoding = face_recognition.face_encodings(face_image)

        # Check if the detected face matches the known face in the video
        if len(face_encoding) > 0 and face_recognition.compare_faces([search_face_encoding], face_encoding[0])[0]:
            # Get the current timestamp
            current_time = datetime.now()

            # Calculate the time elapsed since the start of the video
            elapsed_time = current_time - start_time

            # Format the elapsed time as HH-MM-SS
            elapsed_time_str = str(elapsed_time).split(".")[0]

            # Replace colons with dashes in the filename
            elapsed_time_str = elapsed_time_str.replace(":", "-")

            # Draw a green rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Print message to console
            print(f"Found the known face at {elapsed_time_str} in the video")

            # Save the frame as an image with elapsed time in the filename
            screenshot_filename = f"detected_face_{elapsed_time_str}.jpg"
            cv2.imwrite(screenshot_filename, frame)

            # Set the flag to indicate a match has been found
            match_found = True

            break  # Exit the loop after finding the first match

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video file and close all windows
video_capture.release()
cv2.destroyAllWindows()
