import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
recognizer = sr.Recognizer()


def get_audio():
    with sr.Microphone() as source:
        print("Clearing the background noises... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Ask me anything...")
        audio = recognizer.listen(source)
    return audio


def recognize_command(audio):
    try:
        command = recognizer.recognize_google(audio)
        print("Your message:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


def execute_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Current time:", current_time)
        engine.say("The current time is " + current_time)
        engine.runAndWait()
    else:
        print("Command not recognized.")


def main():
    audio = get_audio()
    command = recognize_command(audio)

    if command:
        execute_command(command)


if __name__ == "__main__":
    main()
