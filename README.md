# 🔐 Voice Unlock AI – Terminal Style

Welcome to **Voice Unlock AI**, a terminal-based voice authentication system that unlocks access with your **secret spoken phrase**.

Inspired by high-tech security systems. This project allows you to unlock access using your voice in a **smooth, hacker-style terminal interface**, powered by real-time speech recognition and fuzzy phrase matching.

---

## 🧠 Features

- 🎙️ Real-time voice recognition
- 🔎 Smart fuzzy matching with similarity scores
- ✅ Access granted only if secret phrase is matched
- 🧠 Female voice feedback (Indian accent)
- ⚙️ Mic calibration with dynamic instruction
- 📟 Terminal-only interface for maximum style
- 🧪 Works offline (after dependencies installed)

---


## 🚀 How It Works

1. Microphone is calibrated
2. User is prompted to speak the **secret phrase**
3. Voice is recognized and compared using fuzzy matching
4. If similarity ≥ 0.85 → Access Granted ✅  
   Else → Access Denied ❌

Example secret phrase:
> `power to the code kishore`

---

## 🛠️ Tech Stack

- Python 3
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
- [pyttsx3](https://pypi.org/project/pyttsx3/) (TTS with Indian-accent female voice)
- Terminal / Command Prompt

---

## 📂 Project Structure

voice-unlock-ai-terminal/
├── unlock_ai.py # Main voice unlock logic
├── requirements.txt # Project dependencies
├── README.md 
└── demo/
├── screenshot.jpeg
└── demo_video.mp4