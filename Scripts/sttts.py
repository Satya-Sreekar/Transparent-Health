import speech_recognition as sr
import pyttsx3

# Create a recognizer instance
recognizer = sr.Recognizer()

# Use your microphone as the audio source
with sr.Microphone() as source:
    print("Please speak something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

text_speech = pyttsx3.init()

text_speech.say(text)
text_speech.runAndWait()