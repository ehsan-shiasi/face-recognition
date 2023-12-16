import cv2
import face_recognition

# Load the known face image
known_image_path = "image.jpg"
known_image = face_recognition.load_image_file(known_image_path)
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize the face detector
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Path to the video file
video_file_path = "video.mp4"

# Load the video file
video_capture = cv2.VideoCapture(video_file_path)

# Load the image for face recognition in the video
search_image_path = "image.jpg"
search_image = face_recognition.load_image_file(search_image_path)
search_face_encoding = face_recognition.face_encodings(search_image)[0]

while True:
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
            # Print message to console
            print("Found the known face in the video")

            # Save the frame as an image
            cv2.imwrite("detected_face_in_video.jpg", frame)

    # Draw rectangles around the detected faces (optional)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video file and close all windows
video_capture.release()
cv2.destroyAllWindows()