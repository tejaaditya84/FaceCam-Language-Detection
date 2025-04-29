Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 02:44:45) [MSC v.1941 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import cv2
import speech_recognition as sr
from langdetect import detect
import numpy as np
import threading

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000

current_text = "Speak now..."
current_language = ""
speaking_now = False

language_names = {
    'en': 'English'
}

def update_speech():
    global current_text, current_language, speaking_now
    speaking_now = True
    with sr.Microphone() as source:
        try:
            print("Listening for English...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            text = recognizer.recognize_google(audio, language='en-US')
            lang_code = detect(text)
...             language = language_names.get(lang_code, lang_code)
...             current_text = text
...             current_language = f"Language: {language}"
...         except Exception as e:
...             print("Audio Error:", e)
...             current_text = "Could not recognize."
...             current_language = ""
...     speaking_now = False
... 
... while True:
...     ret, frame = cap.read()
...     if not ret:
...         break
... 
...     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
...     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
... 
...     right_panel = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)
...     right_panel[:] = (240, 240, 240)
... 
...     cv2.putText(right_panel, current_text, (20, 50),
...                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
...     cv2.putText(right_panel, current_language, (20, 100),
...                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
... 
...     for (x, y, w, h) in faces:
...         color = (0, 255, 0) if speaking_now else (255, 0, 0)
...         cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
... 
...         if not speaking_now:
...             threading.Thread(target=update_speech, daemon=True).start()
... 
...     combined = np.hstack((frame, right_panel))
...     cv2.imshow('Dual Screen: Webcam + English Speech', combined)
... 
...     if cv2.waitKey(1) & 0xFF == ord('q'):
...         break
... 
... cap.release()
