#import speech_recognition as sr
#import os
#import webbrowser
#import datetime
#import json
#from gtts import gTTS
#from request import model  # request.py से Gemini API मॉडल इंपोर्ट कर रहे हैं
#
## Assistant ka naam
#assistant_name = "Aurelio"
#memory_file = "memory.json"
#
## Load memory from file
#def load_memory():
#    try:
#        with open(memory_file, "r") as file:
#            return json.load(file)
#    except (FileNotFoundError, json.JSONDecodeError):
#        return {}  # Return empty dictionary if file not found or empty
#
## Save memory to file
#def save_memory(memory):
#    with open(memory_file, "w") as file:
#        json.dump(memory, file, indent=4)
#
## Initialize memory
#memory = load_memory()
#
## Say function to speak text using system's speech synthesis
#def say(text):
#    os.system(f'say "{text}"')
#
## Listen function to capture audio input from microphone
#def listen():
#    recognizer = sr.Recognizer()
#    with sr.Microphone() as source:
#        print("Listening...")
#        recognizer.adjust_for_ambient_noise(source)
#        audio = recognizer.listen(source)
#
#    try:
#        command = recognizer.recognize_google(audio, language="en-in")
#        print(f"You said: {command}")
#        return command.lower()
#    except sr.UnknownValueError:
#        print("Sorry, I could not understand.")
#        return None
#    except sr.RequestError:
#        print("Could not request results, check internet connection.")
#        return None
#
## Text-to-Speech function using gTTS
#def speak_gtts(text, lang="hi"):
#    tts = gTTS(text=text, lang=lang, slow=False)
#    tts.save("output.mp3")
#    os.system("afplay output.mp3")  # macOS (Windows में 'start' और Linux में 'mpg321' यूज़ करो)
#
## Chat with AI model (Gemini)
#def chat_with_Aurelio(prompt):
#    # Check if the user asked for the assistant's name
#    if "name" in prompt:
#        return f"My name is {assistant_name}."
#
#    # If not, proceed with the Gemini response
#    response = model.generate_content(prompt)
#    return response.text
#
## Time telling function
#def tell_time():
#    hour = datetime.datetime.now().strftime("%H")
#    minute = datetime.datetime.now().strftime("%M")
#    return f"Sir, time is {hour} hours and {minute} minutes."
#
## Function to handle memory (Remember & Retrieve)
#def handle_memory(query):
#    global memory
#    if "Yad Rakh Lo" in query or "remember" in query:
#        parts = query.split("Yad Rakh Lo") if "Yad Rakh Lo" in query else query.split("remember")
#        if len(parts) > 1:
#            key_value = parts[1].strip()
#
#            # Check if "कि" or "that" exists and split safely
#            if "कि" in key_value:
#                split_data = key_value.split("कि", 1)  # Only split once
#            elif "that" in key_value:
#                split_data = key_value.split("that", 1)
#            else:
#                return "मुझे समझ नहीं आया, कृपया सही तरीके से कहें।"
#
#            # Ensure we have exactly two parts
#            if len(split_data) == 2:
#                key, value = split_data[0].strip(), split_data[1].strip()
#                memory[key] = value
#                save_memory(memory)
#                return f"ठीक है, मैंने याद रख लिया कि {key} {value}."
#            else:
#                return "मुझे समझ नहीं आया, कृपया सही तरीके से कहें।"
#
#    elif "क्या तुमने कुछ याद रखा" in query or "what do you remember" in query:
#        if memory:
#            return "मैंने ये बातें याद रखी हैं: " + ", ".join([f"{k} {v}" for k, v in memory.items()])
#        else:
#            return "अभी तक मैंने कुछ याद नहीं रखा है।"
#
#    else:
#        for key in memory:
#            if key in query:
#                return f"आपने कहा था कि {key} {memory[key]}."
#
#    return None  # If no memory-related query is found
#
## Main loop to listen and execute commands
#if __name__ == "__main__":
#    say("Hello, I am Aurelio, your AI assistant.")
#    while True:
#        query = listen()  # Listen for user command
#        if query:
#            # Check if query is related to memory
#            memory_response = handle_memory(query)
#            if memory_response:
#                say(memory_response)
#                continue
#
#            # Handle specific queries
#            if "open youtube" in query:
#                say("Opening YouTube abhishek sir...")
#                webbrowser.open("https://www.youtube.com")
#            elif "open wikipedia" in query:
#                say("Opening Wikipedia abhishek sir...")
#                webbrowser.open("https://www.wikipedia.com")
#            elif "open google" in query:
#                say("Opening Google abhishek sir...")
#                webbrowser.open("https://www.google.com")
#            elif "open physics wala" in query:
#                say("Opening Physics Wala abhishek sir...")
#                webbrowser.open("https://www.pw.live")
#            elif "open music" in query:
#                musicPath = "Users/abhishekabhishek/Music/Music/Media/Music/Unknown Artist/Unknown Album/Kal_Ho_Naa_Ho_Full_Video_-_Title_Track_Shah_Rukh_Khan,Saif_Ali,Preity_Sonu_Nigam_Karan_J(128k).mp3"
#                os.system(f"open {musicPath}")
#            elif "the time" in query:
#                time_info = tell_time()
#                speak_gtts(time_info)
#            elif "open calendar" in query:
#                os.system("open /System/Applications/Calendar.app")
#            else:
#                ai_response = chat_with_Aurelio(query)  # If no specific match, chat with Aurelio
#                print("Aurelio:", ai_response)
#                speak_gtts(ai_response)


Hello,  dost  me  Aurelio, aaapka  A.I assistant mujse jo man me aaye wo bindaas hoke puche