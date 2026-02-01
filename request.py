import google.generativeai as genai
import speech_recognition as sr
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return None
    except sr.RequestError:
        print("Could not request results, check internet connection.")
        return None


def chat_with_gemini(prompt):
    response = model.generate_content(prompt)  # Jo input milega, wahi Gemini model ko diya jayega
    return response.text


if __name__ == "__main__":
    while True:
        user_input = listen()  # Listen se input milega
        if user_input:
            ai_response = chat_with_gemini(user_input)  # User input ko model ke pass bhejna
            print("Gemini:", ai_response)