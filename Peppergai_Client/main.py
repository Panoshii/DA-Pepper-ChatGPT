import openai
import socket
import sounddevice
from scipy.io.wavfile import write

fs= 44100
print("Recording.....n")
record_voice = sounddevice.rec( int ( 6 * fs ) , samplerate = fs, channels = 2 )
sounddevice.wait()
write("out.wav", fs, record_voice)
print("Finished.....nPlease check your output file")


openai.api_key = "API KEY"
f = open("Pfad zu Server Projekt/out.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", f)
print(transcript['text'])
frage = transcript['text']


def frage_chatgpt(frage, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Auf deutsch bitte antworten:" + frage}
        ],
        max_tokens=50
    )
    return response.choices[0].message['content'].strip()



# Host und Port
HOST = 'localhost'
PORT = 12345

# Nachricht
message = frage_chatgpt(frage)
print(message.encode())

# Socket erstellen und Verbindung herstellen
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Nachricht senden
client_socket.sendall(message.encode())

# Verbindung schließen
client_socket.close()
