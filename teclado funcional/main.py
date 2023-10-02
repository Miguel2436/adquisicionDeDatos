from Teclado import run_audio_script
from Sonidos import notas
import os
import random
from pydub import AudioSegment
from pydub.playback import play

# NotasAleatorias = []
# for i in range(1, 6, 1):
#     NotasAleatorias.append(notas(i))
#     print(i)
#     # events_log = run_audio_script()
# print(NotasAleatorias)
# print('Tocado')
# print(events_log)
events_log = run_audio_script()
print(events_log)
def mostrar_info_paquete(numero):
    filename = f"info_paquete{numero}.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print(f"Información de {filename}:")
            print(file.read())  # Lee y muestra el contenido del archivo
    else:
        print(f"El archivo {filename} no existe")


# Suponiendo que tienes audios nombrados como paquete1.wav, paquete2.wav, paquete3.wav, etc.
audio_files = [f"paquete{i}.wav" for i in range(1, 6)]  # Ajusta el rango si tienes más o menos archivos.
for i in range(2):  # Repite el proceso 5 veces
    print('Primera seccion/n/n/n/n')
    selected_files = random.sample(audio_files, 5)  # Selecciona 5 archivos de audio de forma aleatoria
    for file in selected_files:
        numero = file.replace("paquete", "").replace(".wav", "")  # Extrae el número del nombre del archivo de audio
        mostrar_info_paquete(numero)  # Muestra la información del paquete
        if os.path.exists(file):  # Comprueba si el archivo de audio existe
            sound = AudioSegment.from_file(file, format="wav")  # Carga el archivo de audio
            print(f"Reproduciendo {file}...")
            play(sound)  # Reproduce el audio
            events_log = run_audio_script()
        else:
            print(f"El archivo de audio {file} no existe")


