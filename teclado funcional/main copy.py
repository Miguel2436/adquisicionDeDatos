from Teclado import run_audio_script
import os
import random
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt


def mostrar_info_paquete(numero):
    filename = f"info_paquete{numero}.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print(f"Información de {filename}:")
            content = file.readlines()
            print("".join(content))
            return content
    else:
        print(f"El archivo {filename} no existe")
        return []


def comparar_y_graficar(info_paquete, events_log):
    aciertos = 0
    diferencias_tiempos = []
    notas_erroneas = 0
    
    for i in range(6): # Siempre hay 6 notas para comparar
        info_linea = info_paquete[i].strip()
        events_linea = events_log[i + 1] # Ignoramos el primer elemento de events_log
        
        nota_info = info_linea.split(',')[0].split(':')[1].strip()
        tiempo_info = float(info_linea.split(',')[1].split(':')[1].strip().split(' ')[0])
        
        nota_events = events_linea.split(' ')[0]
        tiempo_events = float(events_linea.split(' ')[3])
        
        if nota_info == nota_events:
            aciertos += 1
            diferencias_tiempos.append(abs(tiempo_info - tiempo_events))
        else:
            notas_erroneas += 1
            diferencias_tiempos.append('n/a')

    # Graficar los resultados
    plt.figure(figsize=(10,6))
    
    plt.subplot(121)
    plt.bar(['Aciertos', 'Errores'], [aciertos, notas_erroneas], color=['green', 'red'])
    plt.title('Comparación de Notas')
    
    plt.subplot(122)
    plt.bar(range(1,7), [diff if diff != 'n/a' else 0 for diff in diferencias_tiempos], color='blue')
    plt.title('Diferencia de Tiempos en Notas Correctas')
    plt.xlabel('Número de Nota')
    plt.ylabel('Diferencia de Tiempo (s)')

    plt.tight_layout()
    plt.show()

    for i, diff in enumerate(diferencias_tiempos):
        if diff != 'n/a':
            print(f'Diferencia de tiempo en nota {i+1}: {diff} segundos')
        else:
            print(f'Nota {i+1} no coincide')


audio_files = [f"paquete{i}.wav" for i in range(1, 6)]  # Ajusta el rango si tienes más o menos archivos.
for _ in range(5):
    selected_files = random.sample(audio_files, 5)
    for file in selected_files:
        numero = file.replace("paquete", "").replace(".wav", "")
        info_paquete = mostrar_info_paquete(numero)
        if os.path.exists(file):
            sound = AudioSegment.from_file(file, format="wav")
            print(f"Reproduciendo {file}...")
            play(sound)
            events_log = run_audio_script()
            while len(events_log) < 7:
                print('Llamando de nuevo a la funcion por numero menor')
                events_log = run_audio_script()
            for u in events_log:
                print(u)
            print(info_paquete)
            comparar_y_graficar(info_paquete, events_log)
        else:
            print(f"El archivo de audio {file} no existe")



