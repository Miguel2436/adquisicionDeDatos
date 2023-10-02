import time
import random
from pydub import AudioSegment
from pydub.playback import play

# Lista de notas musicales
notas = [
    "DO_C.wav", "RE_D.wav", "MI_E.wav", "FA_F.wav",
    "SOL_G.wav", "LA_A.wav", "SI_B.wav", "DOM_C.wav",
    "REM_D.wav", "MIM_E.wav"
]

# Número de notas a reproducir
num_notas = 6

for _ in range(num_notas):
    # Selecciona aleatoriamente una nota musical y su duración
    nota = random.choice(notas)
    duracion = random.uniform(1, 5)  # Duración aleatoria entre 1 y 5 segundos
    
    # Carga la nota musical seleccionada
    sound = AudioSegment.from_file(nota, format="wav")
    
    # Corta la nota musical a la duración especificada
    sound = sound[:int(duracion * 1000)]  # pydub trabaja en milisegundos
    
    # Reproduce la nota musical cortada
    print(f'Reproduciendo {nota} por {duracion:.2f} segundos')
    play(sound)
