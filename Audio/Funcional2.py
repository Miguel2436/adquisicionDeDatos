import numpy as np
import sounddevice as sd
import keyboard
import time

# Frecuencias de las notas musicales
frecuencias = {
    'left': 440.0,  # LA
    'up': 587.33,  # RE
    'right': 659.26,  # MI
    'down': 698.46  # SOL
}

frecuencia_muestreo = 44100  # 44.1 kHz
stream = sd.OutputStream(samplerate=frecuencia_muestreo, channels=1)

def generar_onda_senoidal(frecuencia):
    t = np.arange(0, frecuencia_muestreo // frecuencia)
    onda = 0.5 * np.sin(2 * np.pi * frecuencia * t / frecuencia_muestreo).astype(np.float32)  # Cambiar a float32
    return onda


def reproducir_nota(tecla):
    if tecla in frecuencias:
        onda = generar_onda_senoidal(frecuencias[tecla])
        start_time = time.time()
        stream.start()
        while keyboard.is_pressed(tecla):
            stream.write(onda)
        stream.stop()
        elapsed_time = time.time() - start_time
        print(f'Tecla {tecla} presionada por {elapsed_time:.2f} segundos')


# Asigna funciones para ser llamadas cuando se presionen las teclas de flecha
keyboard.add_hotkey('left', lambda: reproducir_nota('left'))
keyboard.add_hotkey('up', lambda: reproducir_nota('up'))
keyboard.add_hotkey('right', lambda: reproducir_nota('right'))
keyboard.add_hotkey('down', lambda: reproducir_nota('down'))

print('Presiona las teclas de flechas...')
keyboard.wait('esc')
