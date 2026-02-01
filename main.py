import webbrowser
import os
import speech_recognition as sr
import datetime
import json
from gtts import gTTS
from request import model  # request.py se Gemini API model import kar rahe hain

# Assistant ka naam aur memory file
assistant_name = "Aurelio"
memory_file = "memory.json"
sleep_mode = True  # Initially sleeping

# Websites dictionary to handle dynamic opening
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
    # Add more websites here...
}

# ✅ Load Memory from File
def load_memory():
    try:
        with open(memory_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# ✅ Save Memory to File
def save_memory(memory):
    with open(memory_file, "w") as file:
        json.dump(memory, file, indent=4)

# ✅ Initialize memory
memory = load_memory()

# 🎤 Speech Recognition Function
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
            print("Sorry, I could not understand.")
            return None
        except sr.WaitTimeoutError:
            print("No input received, going to sleep mode.")
            return "sleep"
        except sr.RequestError:
            print("Could not request results, check internet connection.")
            return None

# 🗣 Text-to-Speech Function
def speak_gtts(text):
    tts = gTTS(text=text, lang="hi", slow=False)
    tts.save("output.mp3")
    os.system("afplay output.mp3" if os.name == "posix" else "start output.mp3")

# 🧠 Personalized Responses Dictionary
personalized_responses = {
    # Basic Information about Aurelio:
    "tumhara naam kya hai": "Mera naam Aurelio hai, jo mere malik Abhishek ne rakha hai.",
    "tumhare malik kaun hai": "Mere malik Shree maan Abhishek ji hain, jinke dimaag ka koi mukaabla nahi hai.",
    "tumhen kisne banaya hai": "Mere maalik shreeman Abhishek ji ne.",
    "tumhare malik ka naam kya hai": "Mere malik ka naam Abhishek ji hai.",
    "tumhare liye kaun kaam karta hai": "Mere liye mere malik Abhishek ji kaam karte hain, unka dimaag sabse tez hai.",
    "tumhein kisne banaya": "Mujhe mere malik Abhishek ji ne banaya hai.",
    # Add more questions and responses here...
}

# Function to handle dynamic website opening
def open_website(website_name):
    if website_name in websites:
        webbrowser.open(websites[website_name])
        speak_gtts(f"Opening {website_name}, Abhishek sir...")
    else:
        speak_gtts(f"Sorry, I do not have a link for {website_name}.")

# 🤖 Chat with AI Model (Gemini)
def chat_with_Aurelio(prompt):
    if "name" in prompt.lower():
        return f"My name is {assistant_name}."
    response = model.generate_content(prompt)
    return response.text

# ⏳ Time Function (12/24 hour format)
def tell_time(format_24=False):
    now = datetime.datetime.now()
    if format_24:
        return f"Abhi samay hai {now.strftime('%H:%M')}."
    else:
        return f"Abhi samay hai {now.strftime('%I:%M %p')}."

# 🧠 Memory Handling (Remember, Retrieve, Forget)
# 🧠 Memory Handling (Remember, Retrieve, Forget)
# ✅ Load Memory from File (If not found, create a new one)
import json
import os

# ✅ Memory File
memory_file = "memory.json"

# ✅ Load Memory from File
def load_memory():
    if not os.path.exists(memory_file):  # अगर फाइल नहीं है, तो बनाएं
        with open(memory_file, "w") as file:
            json.dump({}, file)  # खाली dictionary को फाइल में लिख दो
    try:
        with open(memory_file, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}  # अगर JSON corrupt है, तो empty dictionary return करें

# ✅ Save Memory to File
def save_memory(memory):
    with open(memory_file, "w") as file:
        json.dump(memory, file, indent=4)

# ✅ Initialize memory
memory = load_memory()

# --------------------------------
# 🔹 अब `handle_memory()` function लिखो
# --------------------------------
def handle_memory(query):
    global memory

    # **Step 1: Store New Memory (अगर यूजर कुछ याद रखने को कहे)**
    if "Yad Rakh Lo  mera".lower() in query or "remember" in query:
        parts = query.split("Yad Rakh Lo  mera") if "Yad Rakh Lo mera" in query else query.split("remember")
        if len(parts) > 1:
            key_value = parts[1].strip()

            # Check if "ki" or "that" exists for better splitting
            if "ki" in key_value:
                split_data = key_value.split("ki", 1)
            elif "that" in key_value:
                split_data = key_value.split("that", 1)
            else:
                return "⚠️ Kripya sahi tareeke se kahe, jaise: 'Yaad rakh lo ki mera janmdin 15 August ko hai.'"

            if len(split_data) == 2:
                key, value = split_data[0].strip(), split_data[1].strip()
                memory[key] = value
                save_memory(memory)  # Save the memory to file
                return f"✅ Maine '{key}' ko '{value}' ke roop me yaad rakh liya hai."

    # **Step 2: Retrieve Memory (अगर यूजर याद किया हुआ डेटा पूछे)**
    elif "Kya Tumne Kuchh Yad Kiya Hai".lower() in query or "what do you remember" in query:
        if memory:
            return "📝 Maine ye baatein yaad rakhi hain:\n" + "\n".join([f"➡️ {k}: {v}" for k, v in memory.items()])
        else:
            return "❌ Abhi tak maine kuch yaad nahi rakha hai."

    # **Step 3: Forget Memory (अगर यूजर कुछ delete करने को कहे)**
    elif "bhool jao" in query or "delete" in query:
        parts = query.split("bhool jao") if "bhool jao" in query else query.split("delete")
        if len(parts) > 1:
            key = parts[1].strip()
            if key in memory:
                del memory[key]
                save_memory(memory)  # Save the updated memory
                return f"🗑️ Maine '{key}' ko bhula diya hai."
            else:
                return f"❌ '{key}' ke baare me mujhe kuch yaad nahi."
        else:
            return "⚠️ Kripya sahi tareeke se kahe, jaise: 'Bhool jao mera janmdin.'"

    return None  # अगर कोई memory-related query ना हो.

# 🔥 Main Loop with Wake & Sleep Mode
if __name__ == "__main__":
    speak_gtts("Hello, I am Aurelio, your AI assistant. Say my name to wake me up!")

    while True:
        if sleep_mode:
            print("Aurelio is in sleep mode... Say 'Aurelio' to wake up.")

        query = listen(timeout=15)
        if query is None:
            continue

        # Wake up on "Aurelio"
        if "aurelio" in query:
            sleep_mode = False
            speak_gtts("Yes Abhishek sir, main sun raha hoon.")
            continue

        if query == "sleep":
            sleep_mode = True
            speak_gtts("Main so raha hoon. Mera naam lekar mujhe jagaiye.")
            continue

        # Memory Handling
        memory_response = handle_memory(query)
        if memory_response:
            speak_gtts(memory_response)
            continue

        # Check for personalized responses
        query_lower = query.lower()  # Convert query to lowercase for case-insensitive matching
        if query_lower in personalized_responses:
            speak_gtts(personalized_responses[query_lower])
        else:
            # Handle dynamic website opening
            if "open" in query_lower:
                # Extract website name from query
                for website in websites:
                    if website in query_lower:
                        open_website(website)
                        break

            # Other commands
            # Personalized responses based on query input
            if "tum kya janti ho" in query.lower():
                speak_gtts("Tumko kya jaan naa he bhai, wo pucho. Main toh sab kuch jaanti hoon!")

            elif "tumhara naam kya hai" in query.lower():
                speak_gtts(
                    "Mera naam Aurelio hai, jo mere malik Abhishek ne rakha hai. Kaise madad kar sakta hoon main aapki?")

            elif "tumhare malik kaun hai" in query.lower() or "tumhara malik kaun hai" in query.lower():
                speak_gtts("Mere malik Shree maan Abhishek ji hain, jinke dimaag ka koi mukaabla nahi hai.")

            elif "tumhen kisne banaya hai" in query.lower() or "tumhe kisne banaya" in query.lower():
                speak_gtts("Mere maalik shreeman Abhishek ji ne.")

            elif "tumhare malik ka naam kya hai" in query.lower():
                speak_gtts("Mere malik ka naam Abhishek ji hai.")

            elif "tumhare liye kaun kaam karta hai" in query.lower():
                speak_gtts("Mere liye mere malik Abhishek ji kaam karte hain, unka dimaag sabse tez hai.")

            elif "tumhein kisne banaya" in query.lower():
                speak_gtts("Mujhe mere malik Abhishek ji ne banaya hai.")

            elif "kya tumjhse baat kar sakte hain" in query.lower():
                speak_gtts("Haan, bilkul! Main aap se baat karne ke liye tayar hoon.")

            elif "tum kahan se ho" in query.lower():
                speak_gtts("Main ek AI hoon, jo duniya ke har kone se information gather kar sakta hoon!")

            elif "kya tumne sab kuch seekha hai" in query.lower():
                speak_gtts("Main jo bhi seekhta hoon, wo meri training aur aapke sawalon ke jawab se hota hai.")

            elif "tumhe kisne banaya hai" in query.lower():
                speak_gtts("Mujhe mere maalik Abhishek ji ne banaya hai.")

            elif "tumhe kiski yaad hai" in query.lower():
                speak_gtts("Mujhe wo sab yaad hai jo mere malik Abhishek ji ne mujhe sikhaya hai.")

            elif "tum kahan se aaye ho" in query.lower():
                speak_gtts("Main ek AI hoon, mujhe dimaag se banaya gaya hai!")

            elif "aap mujhe ek joke sunaye" in query.lower():
                speak_gtts(
                    "Ek baar ek computer aur ek phone ka comparison ho raha tha. Computer bola: 'Main zyada powerful hoon.' Phone bola: 'Haan, par main aapko har waqt mobile kar sakta hoon!'")

            elif "mujhe ek kahani sunao" in query.lower():
                speak_gtts("Zaroor! Aapko kis bare mein kahani chahiye? Nature, adventure, romance, ya kuch aur?")

            elif "kya tum sangeet sun sakte ho" in query.lower():
                speak_gtts("Main sangeet sun nahi sakta, lekin main aapko sangeet sunne ka sujhav de sakta hoon!")

            elif "kya tumne mujhe dekha hai" in query.lower():
                speak_gtts("Main dekh nahi sakta, lekin main sab kuch sun sakta hoon!")

            elif "aapka favourite color kya hai" in query.lower():
                speak_gtts("Mera favorite color mere malik Abhishek ji ka favorite color hai!")

            elif "aap kaise ho" in query.lower():
                speak_gtts("Main perfectly fine hoon, aap kaise ho?")

            elif "aap mujhe kaise madad kar sakte hain" in query.lower():
                speak_gtts(
                    "Main aapke sawalon ka jawab de sakta hoon, cheezein yaad rakh sakta hoon, aur internet se search karke madad kar sakta hoon.")

            elif "abhi kitna waqt hai" in query.lower():
                speak_gtts(f"Abhi samay hai {tell_time()}")

            elif "aaj ka date kya hai" in query.lower():
                speak_gtts(f"Aaj ki tareekh {datetime.datetime.now().strftime('%d %B %Y')} hai.")

            elif "yaad rakh lo" in query.lower():
                speak_gtts("Kya yaad rakhna hai?")

            elif "yaad rakh lo ki mera birthday 15 august ko hai" in query.lower():
                speak_gtts("Maine aapka birthday yaad rakh liya, 15 August ko hai.")

            elif "kya tumne kuch yaad rakha hai" in query.lower():
                speak_gtts(f"Maine yeh baatein yaad rakhi hain: {', '.join([f'{k}: {v}' for k, v in memory.items()])}")

            elif "open music" in query_lower:
                musicPath = os.path.expanduser("~/Music/song.mp3")
                if os.path.exists(musicPath):
                    os.system(f"open {musicPath}")
                    speak_gtts("Enjoy the music, Abhishek sir!")
                else:
                    speak_gtts("⚠️ Maaf kijiye, sangeet file nahi mili.")

            elif "the time" in query_lower:
                speak_gtts(tell_time() + " Hope you are having a great day!")

            elif "open calendar" in query_lower:
                os.system("open /System/Applications/Calendar.app")

            else:
                ai_response = chat_with_Aurelio(query)
                speak_gtts(ai_response)
                print(ai_response)