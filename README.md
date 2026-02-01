# 🎙️ Aurelio Voice Assistant (The AI Companion)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Gemini AI](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange?style=for-the-badge&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Aurelio** is a next-generation, hyper-intelligent voice assistant designed to be your personalized digital companion. Powered by **Google's Gemini 1.5 Flash**, Aurelio bridges the gap between static voice commands and dynamic, conversational AI.

It doesn't just "search" things—it **remembers**, **learns**, and **interacts** with your system contextually.

---

## 🌟 Supreme Features

### 🧠 Cognitive AI Core
- **Powered by Gemini 1.5 Flash:** Experience lightning-fast, context-aware conversations.
- **Long-Term Memory (LTM):** Aurelio remembers details about you (birthday, preferences, facts) across sessions using a local JSON database (`memory.json`).
- **Dynamic Context:** Remembers previous turns of conversation for a fluid chat experience.

### ⚡ System Automation
- **Website Navigation:** Instantly opens YouTube, Google, Wikipedia, Instagram, Twitter, and more.
- **App Launching:** Can launch system applications like Music and Calendar directly from voice commands.
- **Smart Wake/Sleep Protocols:**
  - **Wake Word:** "Aurelio" (activates the assistant).
  - **Sleep Mode:** "Sleep" or "Stop" (conserves resources and stops listening for active queries).

### 🛡️ Robust Architecture
- **Secure Environment:** Uses `.env` for API key security (never hardcoded).
- **Graceful Error Handling:** Self-healing logic for internet disconnection or unrecognized speech.
- **Modular Design:** Clean separation of concerns between `main.py` (Orchestrator) and `request.py` (AI Interface).

---

## 📂 Project Structure

```text
Aurelio-Voice-Assistant/
├── main.py              # 🧠 The Brain: Handles voice loops, commands, and memory.
├── request.py           # 🔌 The Interface: Manages secure connections to Gemini AI.
├── memory.json          # 💾 The Hippocampus: Stores long-term user data (Auto-generated).
├── requirements.txt     # 📦 Dependency Manifest: All required libraries.
├── .env                 # 🔐 Key Vault: Stores your GEMINI_API_KEY (Not committed).
└── README.md            # 📘 The Manual: This supreme documentation.
```

---

## 🚀 Installation & Setup

Follow these steps to get Aurelio running perfectly on your local machine.

### Prerequisites
- **Python 3.10+** installed.
- **Microphone** connected.
- **PortAudio** (Required for `PyAudio`):
  - **macOS:** `brew install portaudio`
  - **Linux:** `sudo apt-get install python3-pyaudio portaudio19-dev`
  - **Windows:** Usually pre-installed or handled by pip.

### 1. Clone the Repository
```bash
git clone https://github.com/CodeWithHarry123/Aurelio-Voice-Assistant.git
cd Aurelio-Voice-Assistant
```

### 2. Create a Virtual Environment (Crucial)
To avoid `ModuleNotFoundError`, always run inside a virtual environment.

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Security
Create a file named `.env` in the root folder and add your API key:
```env
GEMINI_API_KEY=AIzaSyD...YourActualKeyHere...
```

---

## 🎮 How to Run

Once setup is complete, launch the assistant:

```bash
python main.py
```

### 🗣️ Voice Command Examples

| Category | Command Example | Action |
| :--- | :--- | :--- |
| **Wake Up** | "Wake up Aurelio", "Aurelio" | Activates listening mode. |
| **Memory** | "Remember that my birthday is August 15th" | Saves to `memory.json`. |
| **Recall** | "What do you remember about me?" | Reads from memory. |
| **Forget** | "Forget my birthday" | Deletes specific memory. |
| **General** | "Tell me a joke", "Who made you?" | AI Conversation. |
| **System** | "Open Google", "Open Calendar" | System Automation. |
| **Sleep** | "Go to sleep", "Stop" | Enters standby mode. |

---

## 🔧 Troubleshooting

**Error: `ModuleNotFoundError: No module named 'speech_recognition'`**
- **Fix:** You are likely running the global Python instead of the virtual environment. Ensure you see `(.venv)` in your terminal, or use `.venv/bin/python main.py`.

**Error: `PyAudio` fails to install**
- **Fix:** Install the system-level header files.
  - Mac: `brew install portaudio`
  - Linux: `sudo apt install portaudio19-dev`

**Error: `GoogleGenerativeAI Error`**
- **Fix:** Check your `.env` file. Ensure `GEMINI_API_KEY` is correct and has no extra spaces.

---

## 👨‍💻 Contributing
Contributions are welcome! Fork the repo, make your changes, and submit a PR.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.