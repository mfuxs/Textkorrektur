from pynput import keyboard
import pyperclip
from playsound import playsound
import openai
import os
import time 
import subprocess 


#######################################################################################
# Set up the OpenAI client with your API key
api_key = '' #hier kannst du dir einen erstellen https://platform.openai.com/api-keys

#######################################################################################


if not api_key:
    raise ValueError("API key not set. Please set the OPENAI_API_KEY environment variable.")
client = openai.OpenAI(api_key=api_key )


def correct_text(text):
 
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", #Schnellere Antworten 
            #model="gpt-4o", #bessere Antworten 
            messages=[
                {"role": "system", "content": "Du korrigiert alle deutschen Texte, wobei die Erhaltung des ursprünglichen Stils und Tons im Vordergrund steht. Es wird Wert darauf gelegt, den natürlichen Fluss und die ursprüngliche Formulierung beizubehalten und nur die für die grammatikalische Korrektheit notwendigen Änderungen vorzunehmen.  Du vermeidest umfangreiche Änderungen, die die ursprüngliche Absicht oder den Ton des Textes verändern könnten. Die Antworten sind direkt, ohne Erklärungen oder Ausschmückungen, und konzentrieren sich ausschließlich auf die Wiedergabe des korrigierten Textes."},
                {"role": "user", "content": text}
            ]
        )
        # Correctly accessing the message content
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    

    

def on_activate():

    print ("start")


    
    time.sleep(0.1)
    text = pyperclip.paste()
    print (text)
    if text:
        corrected_text = correct_text(text)
        if corrected_text:
            pyperclip.copy(corrected_text)
            playsound('signal.mp3')
            print("Text korrigiert und in Zwischenablage kopiert.")
        else:
            print("Keine Korrektur durchgeführt.")
    else:
        print("Kein Text in der Zwischenablage gefunden.")

def for_canonical(f):
    return lambda k: f(listener.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+e'),
    on_activate
)

listener = keyboard.Listener(
    on_press=for_canonical(hotkey.press),
    on_release=for_canonical(hotkey.release)
)

with listener:
    listener.join()
