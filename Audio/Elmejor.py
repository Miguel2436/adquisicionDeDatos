import numpy as np
import sounddevice as sd
import keyboard
import time
import threading

# Frecuencias de las notas musicales
frecuencias = {
    'left': 440.0,  # LA
    'up': 587.33,  # RE
    'right': 659.26,  # MI
    'down': 698.46,  # SOL
    '1': 261.63,  # DO
    '2': 293.66,  # RE
    '3': 329.63,  # MI
    '4': 349.23,  # FA
    '5': 392.00,  # SOL
    '6': 440.00,  # LA
    '7': 493.88,  # SI
    '8': 523.25,  # DO (octava superior)
    '9': 587.33   # RE (octava superior)
}

frecuencia_muestreo = 44100  # 44.1 kHz

teclas_presionadas = {}  # Diccionario para rastrear teclas presionadas


def generar_onda_senoidal(frecuencia):
    t = np.arange(0, 10 * frecuencia_muestreo / frecuencia)
    onda = 0.5 * np.sin(2 * np.pi * frecuencia * t / frecuencia_muestreo).astype(np.float32)
    return onda


def reproducir_nota(tecla):
    onda = generar_onda_senoidal(frecuencias[tecla])
    with sd.OutputStream(samplerate=frecuencia_muestreo, channels=1) as stream:
        start_time = time.time()
        indice = 0
        chunk_size = frecuencia_muestreo // 10  # 1/10 de segundo
        while keyboard.is_pressed(tecla):
            # Envía el siguiente fragmento (chunk) de la onda al stream de audio
            fin = indice + chunk_size
            stream.write(onda[indice:fin])
            indice += chunk_size
            # Si se alcanza el final de la onda, reinicia el índice
            if fin >= len(onda):
                indice = 0
        elapsed_time = time.time() - start_time
        print(f'Tecla {tecla} presionada por {elapsed_time:.2f} segundos')
    teclas_presionadas[tecla] = False  # Marcar la tecla como no presionada


def iniciar_reproduccion(tecla):
    # Si la tecla presionada es una de las teclas de flecha y no está siendo presionada, inicia un nuevo hilo para reproducir la nota
    if tecla in frecuencias and not teclas_presionadas.get(tecla, False):
        teclas_presionadas[tecla] = True  # Marcar la tecla como presionada
        t = threading.Thread(target=reproducir_nota, args=(tecla,))
        t.start()


print('Presiona las teclas de flechas o números...')
keyboard.on_press(lambda event: iniciar_reproduccion(event.name))
keyboard.wait('esc')



