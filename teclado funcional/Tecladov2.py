import time
import threading
import wave
import pyaudio
import keyboard
from datetime import datetime

def run_audio_script():
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
    keys_counter = [0]

    events_log = []
    start_time = datetime.now()
    events_log.append(f"Script iniciado a las {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def save_events_log():
        with open("events_log.txt", "w") as f:
            for event in events_log:
                f.write(event + '\n')
        p.terminate()

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
            
            keys_counter[0] += 1
            if keys_counter[0] >= 6:
                save_events_log()
                exit(0)  # Finalizar el script después de la sexta tecla.
                return events_log 
                

    def key_handler(e, k):
        if not keys_pressed[k]:
            keys_pressed[k] = True
            threading.Thread(target=play_sound, args=(k,)).start()

    for key in key_note_map.keys():
        keyboard.on_press_key(key, lambda e, k=key: key_handler(e, k))

    print("Presiona las teclas del 0 al 9 para reproducir sonidos. El script se terminará después de la sexta tecla.")

    keyboard.wait('esc')  # No necesitarás esperar por 'esc', pero debes mantener esto para mantener el script en ejecución.

if __name__ == "__main__":
    run_audio_script()
