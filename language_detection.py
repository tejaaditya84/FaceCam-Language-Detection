import speech_recognition as sr
from langdetect import detect

def detect_language():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source, timeout=3)  # Listen for 3 seconds
    
    try:
        text = recognizer.recognize_google(audio)  # Recognize speech using Google API
        print("You said:", text)  # Print the recognized text
        language = detect(text)  # Detect the language of the text
        print("Detected language:", language)  # Print the detected language
        return language, text
    except Exception as e:
        print("Error:", e)
        return None, None

# Call the function to test
detect_language()
