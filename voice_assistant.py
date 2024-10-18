import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the desired voice (choose an index based on available voices)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index to select different voice

def speak(text):
    """Convert text to speech using system voice."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen for a command from the microphone."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def play_song(song_name):
    """Play a song on YouTube."""
    url = f"https://www.youtube.com/results?search_query={'+'.join(song_name.split())}"
    webbrowser.open(url)
    speak(f"Playing {song_name} on YouTube.")

def main():
    speak("Hello! I am your voice assistant. How can I assist you today?")

    listening = True  # Flag to control listening state

    while True:
        if listening:
            command = listen_command()
            if command:
                if "hello slim" in command:
                    speak("Hello Master, what can I do for you?")
                    continue  # Skip to the next iteration of the loop

                elif "exit" in command:
                    speak("Goodbye!")
                    break

                elif "pause" in command:
                    listening = False
                    speak("I am now paused. Say 'resume' to start listening again.")

                elif "play song" in command or "play" in command:
                    song_name = command.replace("play song", "").replace("play", "").strip()
                    if song_name:
                        play_song(song_name)
                    else:
                        speak("Please specify which song you want me to play.")

                else:
                    speak("I'm sorry, I don't understand that command.")

        # Check for resume command while paused
        if not listening:
            resume_command = listen_command()
            if resume_command and "resume" in resume_command:
                listening = True
                speak("I am now listening again.")

if __name__ == "__main__":
    main()
