import speech_recognition as sr
import pyttsx3
import time
import difflib  # Added for fuzzy matching

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Force-select a female voice if available
female_voice_found = False
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        female_voice_found = True
        break

# Fallback to manually selecting the second voice (often female on Windows)
if not female_voice_found and len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

SECRET_PHRASE = "hello world"  # Your preferred phrase

def speak(text):
    print(f"🤖 {text}")
    engine.say(text)
    engine.runAndWait()

def microphone_chooser():
    print("🔍 Available Microphones:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{index}: {name}")
    
    while True:
        try:
            device_index = int(input("Enter the microphone index to use (default is 0): ") or 0)
            if device_index < 0 or device_index >= len(sr.Microphone.list_microphone_names()):
                raise ValueError("Invalid index")
            return device_index
        except ValueError as e:
            print(f"⚠️ Error: {e}. Please enter a valid microphone index.")

def listen_for_phrase():
    with sr.Microphone(device_index=microphone_chooser()) as source:
        print("\n🎙️ Listening for your secret phrase...")
        speak("Calibrating microphone. Please stay silent.")    
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("✅ Calibration complete.")
        speak("Calibration complete. You can now speak your passphrase Boss.")

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("🔍 Recognizing...")

            phrase = recognizer.recognize_google(audio).strip().casefold()
            print(f"🗣️ You said: '{phrase}'")

            # Fuzzy match to allow close matches
            similarity = difflib.SequenceMatcher(None, phrase, SECRET_PHRASE.casefold()).ratio()
            print(f"🔎 Similarity: {similarity:.2f}")

            if similarity > 0.8:
                print("✅ Access Granted.")
                speak("Access granted. Welcome Boss.")
            else:
                print("❌ Access Denied.")
                speak("Incorrect phrase. You are not my boss.")

        except sr.WaitTimeoutError:
            print("⏱️ Listening timed out.")
            speak("You took too long to speak, Boss.")
        except sr.UnknownValueError:
            print("⚠️ Could not understand audio.")
            speak("I didn't catch that, Boss.")
        except sr.RequestError:
            print("❌ Could not connect to recognition service.")
            speak("There was a problem with the voice service.")

# Run the system
if __name__ == "__main__":
    print("🔐 Voice Unlock AI - Terminal Style")
    time.sleep(1)
    listen_for_phrase()
