import random
from pydub import AudioSegment
from pydub.playback import play

def notas(numero_paquete):
    # Lista de notas musicales
    notas = [
        "DO_C.wav", "RE_D.wav", "MI_E.wav", "FA_F.wav",
        "SOL_G.wav", "LA_A.wav", "SI_B.wav", "DOM_C.wav",
        "REM_D.wav", "MIM_E.wav"
    ]

    # Número de notas a reproducir
    num_notas = 6
    
    # Inicializar un objeto AudioSegment silencioso para concatenar las notas
    paquete = AudioSegment.silent(duration=0)
    
    Notasale = []

    for i in range(num_notas):
        # Selecciona aleatoriamente una nota musical
        nota = random.choice(notas)
        
        # Carga la nota musical seleccionada
        sound = AudioSegment.from_file(nota, format="wav")
        
        # Determina una duración aleatoria para la reproducción de la nota musical
        duracion_reproduccion = random.uniform(1, 1.50)  # Duración aleatoria entre 1 y 1.50 segundos
        
        # Si la duración de la reproducción es menor que la duración total de la nota musical,
        # corta la nota musical a la duración de la reproducción
        if duracion_reproduccion < sound.duration_seconds:
            sound = sound[:int(duracion_reproduccion * 1000)]  # pydub trabaja en milisegundos
        
        # Añade la nota y su duración de reproducción a la lista de salida
        Notasale.append(f'Nota {i + 1}: {nota[:-4]}, duracion: {duracion_reproduccion:.2f} segundos')
        
        # Reproduce la nota musical seleccionada
        print(f'Reproduciendo {nota[:-4]} por {duracion_reproduccion:.2f} segundos')
        play(sound)
        
        # Concatena la nota musical al paquete
        paquete += sound
    
    # Guarda el paquete de notas en un nuevo archivo
    nombre_archivo = f"Paquete{numero_paquete}.wav"
    paquete.export(nombre_archivo, format="wav")
    
    # Guarda la información de Notasale en un archivo de texto
    with open(f"Info_Paquete{numero_paquete}.txt", "w") as file:
        for item in Notasale:
            file.write("%s\n" % item)
    
    return Notasale# nombre_archivo  # También se devuelve el nombre del archivo guardado
