# tu_script_audio.py

import time
import threading
import wave
import pyaudio
import keyboard
from datetime import datetime

def run_audio_script():
    keyboard.unhook_all()
    key_note_map = {
        '0': 'DO_C',
        '1': 'RE_D',
        '2': 'MI_E',
        '3': 'FA_F',
        '4': 'SOL_G',
        '5': 'LA_A',
        '6': 'SI_B',
        '7': 'DOM_C',
        '8': 'REM_D',
        '9': 'MIM_E'
    }

    p = pyaudio.PyAudio()

    keys_pressed = {key: False for key in key_note_map.keys()}

    events_log = []
    start_time = datetime.now()
    events_log.append(f"Script iniciado a las {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def play_sound(key):
        note = key_note_map[key]
        filename = f"{note}.wav"
        wf = wave.open(filename, 'rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        start_time = time.time()
        print(f"{note} presionada")

        data = wf.readframes(1024)
        try:
            while keyboard.is_pressed(key):
                if not data:
                    wf.rewind()
                    data = wf.readframes(1024)

                stream.write(data)
                data = wf.readframes(1024)
        finally:
            keys_pressed[key] = False
            stream.stop_stream()
            stream.close()
            end_time = time.time()
            duration = end_time - start_time
            events_log.append(f"{note} presionada por {duration:.2f} segundos")
            print(f"{note} presionada por {duration:.2f} segundos")

    threads = []  # Lista para almacenar los objetos de hilos iniciados.
    def key_handler(e, k):
        # if k == 'esc':

            
             # Limpiar todos los manejadores de eventos de teclado
        #     p.terminate()  # Terminar PyAudio
        #     return events_log
        if k == 'esc':
            # Asegurarte de que todos los hilos han terminado antes de salir.
            for thread in threads:
                thread.join()
            threads.clear()  # Limpiar la lista de threads
            p.terminate()
             
            return events_log
        
        if not keys_pressed[k]:
            keys_pressed[k] = True
            thread = threading.Thread(target=play_sound, args=(k,))
            threads.append(thread)  # Añadir el hilo a la lista de hilos iniciados.
            thread.start()

    for key in key_note_map.keys():
        keyboard.on_press_key(key, lambda e, k=key: key_handler(e, k))

    keyboard.on_press_key('esc', lambda e: key_handler(e, 'esc'))

    print("Presiona las teclas del 0 al 9 para reproducir sonidos. Presiona 'esc' para salir.")

    keyboard.wait('esc')
    
    return events_log  # Devuelve el log al finalizar la función.

# Otro script Python que importa y ejecuta tu función

# import tu_script_audio
# events_log = tu_script_audio.run_audio_script()
# Ahora events_log contiene la información del log.
if __name__ == "__main__":
    events_log = run_audio_script()
    # Aquí puedes hacer algo con events_log si lo deseas, como imprimirlo o procesarlo de alguna manera.
    print(events_log)
