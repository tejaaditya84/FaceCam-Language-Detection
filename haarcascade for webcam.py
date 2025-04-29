Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 02:44:45) [MSC v.1941 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
... 
... # Load Haar Cascade for face detection
... face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
... 
... # Initialize webcam
... cap = cv2.VideoCapture(0)
... 
... while True:
...     ret, frame = cap.read()
...     if not ret:
...         break
...     
...     # Convert to grayscale (better for face detection)
...     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
...     
...     # Detect faces
...     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
...     
...     # Draw rectangles around faces
...     for (x, y, w, h) in faces:
...         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
...     
...     # Display the output
...     cv2.imshow('Face + Language Detection', frame)
...     
...     if cv2.waitKey(1) & 0xFF == ord('q'):
...         break
... 
... cap.release()
