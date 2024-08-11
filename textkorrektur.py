import keyboard
import pyperclip
from playsound import playsound
import openai
import time


#######################################################################################
# Set up the OpenAI client with your API key
api_key = '' #hier kannst du dir einen erstellen https://platform.openai.com/api-keys

#######################################################################################


if not api_key:
    raise ValueError("API key not set. Please set the OPENAI_API_KEY environment variable.")
client = openai.OpenAI(api_key=api_key)


def correct_text(text):

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", #Schnellere Antworten -> Update von GPT 3.5 -> GPT-4o-mini
            #model="gpt-4o", #bessere Antworten 
            messages=[
                {"role": "system", "content": "Du korrigierst alle Texte auf Rechtschreibfehler und Grammatikfehler, mehr nicht. Die Antworten sind direkt, ohne Erklärungen oder Ausschmückungen, und konzentrieren sich ausschließlich auf die Wiedergabe des korrigierten Textes."},
                {"role": "user", "content": text}
            ]
        )
        # Correctly accessing the message content
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None




def on_activate():
    print("start")
    time.sleep(0.1)
    text = pyperclip.paste()
    print(text)
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
    

# Register the hotkey with the `keyboard` library
keyboard.add_hotkey('ctrl+e', on_activate)


# Run the event loop to keep the script running
while True:
    keyboard.wait()
