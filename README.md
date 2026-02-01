# Aurelio Voice Assistant 🎙️🤖

Aurelio is a smart voice assistant powered by **Google's Gemini 1.5 Flash** model. It listens to your voice commands, processes them using advanced AI, and responds back with synthesized speech. It features memory capabilities, website navigation, and system interactions.

## 🚀 Features

*   **Voice Interaction**: Uses `SpeechRecognition` to listen and `gTTS` to speak.
*   **AI Intelligence**: Powered by `google-generativeai` (Gemini 1.5 Flash) for natural conversations.
*   **Wake/Sleep Mode**: Can be put to sleep and woken up with voice commands ("wake up", "sleep").
*   **Persistent Memory**: Remembers context and user details across sessions via `memory.json`.
*   **Web & System Control**: Can open websites (Youtube, Google, Instagram, etc.) and launch system applications.
*   **Conversation History**: Maintains a chat history for context-aware responses.

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/CodeWithHarry123/Aurelio-Voice-Assistant.git
    cd Aurelio-Voice-Assistant
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: You may need to install `PyAudio` separately if `pip` fails. On macOS: `brew install portaudio` then `pip install pyaudio`.*

4.  **Set up Environment Variables**:
    *   Create a `.env` file in the root directory.
    *   Add your Google Gemini API key:
        ```env
        GEMINI_API_KEY=your_actual_api_key_here
        ```

## ▶️ Usage

Run the main script to start the assistant:

```bash
python main.py
```

*   **Wake Word**: "Wake up"
*   **Sleep Word**: "Sleep", "Stop"
*   **Exit**: "Exit", "Bye"

## 📂 Project Structure

*   `main.py`: The core orchestration script handling the event loop, voice input/output, and command routing.
*   `request.py`: Handles interactions with the Google Gemini API.
*   `memory.json`: JSON file storing the assistant's long-term memory.
*   `testing.py`: Contains experimental code (legacy).

## 🛡️ Security

This project uses a `.env` file to manage sensitive API keys. **Never commit your `.env` file to version control.**

## 🤝 Contributing

Feel free to fork this repository and submit pull requests.

## 📄 License

[MIT License](LICENSE)
