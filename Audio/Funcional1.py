import keyboard
import time
import numpy as np
import sounddevice as sd
import threading

def frec(nota: int, octava: int) -> int:
    expo = octava * 12 + (nota - 58)
    return int(440 * ((2 ** (1 / 12)) ** expo))

def beep(nota: int, octava: int, duracion: int) -> None:
    framerate = 44100
    t = np.linspace(0, duracion / 1000, int(framerate * duracion / 1000))
    frequency = frec(nota, octava)
    data = np.sin(2 * np.pi * frequency * t)
    # wave = np.zeros((len(t), 2), dtype=np.int16)asdqq
    # sd.play(data, framerate)
    threading.Thread(target=sd.play, args=(data, framerate)).start()
    # sd.play(data, framerate)
    # sd.wait()



def main():
    pressed_keys = {}  # Un diccionario para realizar un seguimiento del tiempo de presión de cada tecla
    
  
    while True:
        event = keyboard.read_event()
        key = event.name
        
        if key == "mayusculas":
            print("Programa detenido.")
            break
        
        if event.event_type == keyboard.KEY_DOWN:
            if key not in pressed_keys:
                pressed_keys[key] = time.time()
                print(f"Tecla {key} presionada")
                if key == 'flecha abajo':
                    beep(5, 4, 5000)
                if key == 'flecha arriba':
                    beep(8, 4, 5000)
                if key == 'flecha izquierda':
                    beep(10, 4, 5000)
                if key == 'flecha derecha':
                    beep(13, 4, 5000)
                
        elif event.event_type == keyboard.KEY_UP:
            if key in pressed_keys:
                release_time = time.time()
                press_time = pressed_keys.pop(key)
                duration = release_time - press_time
                print(f"Tecla {key} liberada después de {duration:.2f} segundos")
                sd.stop()
                

if __name__ == "__main__":
    main()


