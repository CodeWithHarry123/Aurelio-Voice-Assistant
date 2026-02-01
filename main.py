import webbrowser
import os
import speech_recognition as sr
import datetime
import json
from gtts import gTTS
from dotenv import load_dotenv
from request import model  # Import model from request.py

# Load environment variables
load_dotenv()

# Assistant configuration
assistant_name = "Aurelio"
memory_file = "memory.json"
sleep_mode = True  # Initially sleeping

# Websites dictionary
websites = {
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.com",
    "google": "https://www.google.com",
    "twitter": "https://www.twitter.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
    "physics wala": "https://www.pw.live",
}

# Personalized responses
personalized_responses = {
    "tumhara naam kya hai": "Mera naam Aurelio hai, jo mere malik Abhishek ne rakha hai.",
    "tumhare malik kaun hai": "Mere malik Shree maan Abhishek ji hain, jinke dimaag ka koi mukaabla nahi hai.",
    "tumhen kisne banaya hai": "Mere maalik shreeman Abhishek ji ne.",
    "tumhe kisne banaya": "Mujhe mere malik Abhishek ji ne banaya hai.",
    "tumhare malik ka naam kya hai": "Mere malik ka naam Abhishek ji hai.",
    "tumhare liye kaun kaam karta hai": "Mere liye mere malik Abhishek ji kaam karte hain, unka dimaag sabse tez hai.",
    "kya tumjhse baat kar sakte hain": "Haan, bilkul! Main aap se baat karne ke liye tayar hoon.",
    "tum kahan se ho": "Main ek AI hoon, jo duniya ke har kone se information gather kar sakta hoon!",
    "kya tumne sab kuch seekha hai": "Main jo bhi seekhta hoon, wo meri training aur aapke sawalon ke jawab se hota hai.",
    "tumhe kiski yaad hai": "Mujhe wo sab yaad hai jo mere malik Abhishek ji ne mujhe sikhaya hai.",
    "tum kahan se aaye ho": "Main ek AI hoon, mujhe dimaag se banaya gaya hai!",
    "aap mujhe ek joke sunaye": "Ek baar ek computer aur ek phone ka comparison ho raha tha. Computer bola: 'Main zyada powerful hoon.' Phone bola: ' Haan, par main aapko har waqt mobile kar sakta hoon!'",
    "mujhe ek kahani sunao": "Zaroor! Aapko kis bare mein kahani chahiye? Nature, adventure, romance, ya kuch aur?",
    "kya tum sangeet sun sakte ho": "Main sangeet sun nahi sakta, lekin main aapko sangeet sunne ka sujhav de sakta hoon!",
    "kya tumne mujhe dekha hai": "Main dekh nahi sakta, lekin main sab kuch sun sakta hoon!",
    "aapka favourite color kya hai": "Mera favorite color mere malik Abhishek ji ka favorite color hai!",
    "aap kaise ho": "Main perfectly fine hoon, aap kaise ho?",
    "aap mujhe kaise madad kar sakte hain": "Main aapke sawalon ka jawab de sakta hoon, cheezein yaad rakh sakta hoon, aur internet se search karke madad kar sakta hoon.",
    "tum kya janti ho": "Tumko kya jaan naa he bhai, wo pucho. Main toh sab kuch jaanti hoon!",
}

# --- Utility Functions ---

def load_memory():
    if not os.path.exists(memory_file):
        with open(memory_file, "w") as file:
            json.dump({}, file)
    try:
        with open(memory_file, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_memory(memory_data):
    with open(memory_file, "w") as file:
        json.dump(memory_data, file, indent=4)

def speak_gtts(text):
    print(f"Aurelio: {text}")
    try:
        tts = gTTS(text=text, lang="hi", slow=False)
        tts.save("output.mp3")
        os.system("afplay output.mp3" if os.name == "posix" else "start output.mp3")
    except Exception as e:
        print(f"Error in TTS: {e}")

def listen(timeout=10):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            command = recognizer.recognize_google(audio, language="en")
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return None
        except sr.WaitTimeoutError:
            return "sleep"
        except Exception as e:
            print(f"Error in Recognition: {e}")
            return None

def open_website(website_name):
    if website_name in websites:
        webbrowser.open(websites[website_name])
        speak_gtts(f"Opening {website_name}, Abhishek sir...")
    else:
        speak_gtts(f"Sorry, I do not have a link for {website_name}.")

def chat_with_Aurelio(prompt):
    if "name" in prompt.lower():
        return f"My name is {assistant_name}."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

def tell_time(format_24=False):
    now = datetime.datetime.now()
    if format_24:
        return f"Abhi samay hai {now.strftime('%H:%M')}."
    else:
        return f"Abhi samay hai {now.strftime('%I:%M %p')}."

def handle_memory(query, memory):
    query_lower = query.lower()
    
    # Store memory
    if "yad rakh lo" in query_lower or "remember" in query_lower:
        # Improved splitting logic
        trigger = "yad rakh lo" if "yad rakh lo" in query_lower else "remember"
        content = query_lower.split(trigger)[-1].strip()
        
        for sep in [" ki ", " that ", " "]:
            if sep in content:
                parts = content.split(sep, 1)
                if len(parts) == 2:
                    key, value = parts[0].strip(), parts[1].strip()
                    memory[key] = value
                    save_memory(memory)
                    return f"✅ Maine '{key}' ko '{value}' ke roop me yaad rakh liya hai."
        return "⚠️ Kripya sahi tareeke se kahe, jaise: 'Yaad rakh lo ki mera janmdin 15 August ko hai.'"

    # Retrieve memory
    elif "kya tumne kuchh yad kiya hai" in query_lower or "what do you remember" in query_lower:
        if memory:
            return "📝 Maine ye baatein yaad rakhi hain:\n" + "\n".join([f"➡️ {k}: {v}" for k, v in memory.items()])
        else:
            return "❌ Abhi tak maine kuch yaad nahi rakha hai."

    # Forget memory
    elif "bhool jao" in query_lower or "delete" in query_lower:
        trigger = "bhool jao" if "bhool jao" in query_lower else "delete"
        key = query_lower.split(trigger)[-1].strip()
        if key in memory:
            del memory[key]
            save_memory(memory)
            return f"🗑️ Maine '{key}' ko bhula diya hai."
        else:
            return f"❌ '{key}' ke baare me mujhe kuch yaad nahi."

    return None

# --- Main Application ---

def main():
    global sleep_mode
    memory = load_memory()
    speak_gtts("Hello, I am Aurelio, your AI assistant. Say my name to wake me up!")

    while True:
        if sleep_mode:
            print("Aurelio is in sleep mode... Say 'Aurelio' to wake up.")

        query = listen(timeout=15)
        if not query:
            continue

        # Wake up logic
        if "aurelio" in query:
            sleep_mode = False
            speak_gtts("Yes Abhishek sir, main sun raha hoon.")
            continue

        if sleep_mode:
            continue

        # Sleep logic
        if query in ["sleep", "go to sleep", "stop"]:
            sleep_mode = True
            speak_gtts("Main so raha hoon. Mera naam lekar mujhe jagaiye.")
            continue

        # Exit logic
        if query in ["exit", "bye", "quit"]:
            speak_gtts("Goodbye Abhishek sir!")
            break

        # Memory Handling
        memory_response = handle_memory(query, memory)
        if memory_response:
            speak_gtts(memory_response)
            continue

        # Personalized Responses
        query_clean = query.strip().lower()
        if query_clean in personalized_responses:
            speak_gtts(personalized_responses[query_clean])
            continue

        # Time/Date
        if "samay" in query_clean or "time" in query_clean:
            speak_gtts(tell_time())
            continue
        if "tareekh" in query_clean or "date" in query_clean:
            speak_gtts(f"Aaj ki tareekh {datetime.datetime.now().strftime('%d %B %Y')}")
            continue

        # Website Opening
        if "open" in query_clean:
            found = False
            for site in websites:
                if site in query_clean:
                    open_website(site)
                    found = True
                    break
            if found: continue

        # System apps
        if "open music" in query_clean:
            musicPath = os.path.expanduser("~/Music/song.mp3")
            if os.path.exists(musicPath):
                os.system(f"open {musicPath}")
                speak_gtts("Enjoy the music, Abhishek sir!")
            else:
                speak_gtts("⚠️ Maaf kijiye, sangeet file nahi mili.")
            continue
            
        if "open calendar" in query_clean:
            os.system("open /System/Applications/Calendar.app")
            continue

        # Default AI Response
        ai_response = chat_with_Aurelio(query)
        speak_gtts(ai_response)

if __name__ == "__main__":
    main()
