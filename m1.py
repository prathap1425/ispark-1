import speech_recognition as sr
import pyttsx3
from gpiozero import AngularServo
from time import sleep

# Initialize the servo
servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',170)
engine.setProperty('voice','english_rp+f4')


def listen_for_hello():
    with sr.Microphone() as source:
        print("\aListening for 'prompt'...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("\a")
        try:
            # Recognize the speech using Google's speech recognition
            command = recognizer.recognize_google(audio)
            print(f"Command heard: {command}")
            if "hello" in command.lower():
                return True
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return False

def name_checker():
    with sr.Microphone() as source:
        print("\aListening for 'prompt'...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("\a")
        try:
            # Recognize the speech using Google's speech recognition
            command = recognizer.recognize_google(audio)
            temp = 'my name is'
            print(f"Command heard: {command}")
            if temp in command:
                global name
                name = command[10:]
                return True
        except sr.UnknownValueError:
            print("Sorry i couldn't hear that....")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return False


def respond_with_name():
    engine.say('hello ')
    engine.say(name)
    engine.runAndWait()
    engine.say("Nice to meet you")
    servo.angle = 90
    engine.runAndWait()
    engine.say("i  am")
    engine.say("AURA Version 1.0")
    engine.say("From i__spaark")
    engine.runAndWait()
    print('hello i am AURA Version 1.0 from iSpark')
    engine.runAndWait()
    sleep(2)
    servo.angle=0


def respond_and_move_servo():
    # Respond with audio output
    engine.say("Hello")
    engine.runAndWait()
    engine.say("i  am")
    engine.say("AURA Version 1.0")
    engine.say("From i__spaark")
    engine.runAndWait()
    print('hello', name,' i am aura version 1.0 from iSpark')
    engine.runAndWait()

    # Move the servo to 45 degrees
    servo.angle = 90
    sleep(2)
    servo.angle=0

while True:
    if name_checker():
        respond_with_name()
    elif listen_for_hello():
        respond_and_move_servo()

