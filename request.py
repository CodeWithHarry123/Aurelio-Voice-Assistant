import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # Note: If running for the first time, ensure .env exists with GEMINI_API_KEY
    print("Warning: GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=api_key if api_key else "DUMMY_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

def chat_with_gemini(prompt):
    """
    Direct interface to Gemini AI
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error connecting to Gemini: {e}"

if __name__ == "__main__":
    # Test connection
    print("Testing Gemini Connection...")
    print(chat_with_gemini("Say hello in Hindi"))
