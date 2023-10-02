import numpy as np
import wavio
import os
# Frecuencias de las notas musicales
frecuencias = {
    'DO': 261.63,
    'RE': 293.66,
    'MI': 329.63,
    'FA': 349.23,
    'SOL': 392.00,
    'LA': 440.00,
    'SI': 493.88
}

frecuencia_muestreo = 44100  # 44.1 kHz
duracion = 2  # segundos
def generar_onda_piano(frecuencia):
    t = np.linspace(0, duracion, int(frecuencia_muestreo * duracion), endpoint=False)
    onda = np.sin(2 * np.pi * frecuencia * t)
    
    # Añadir más armónicos con diferentes amplitudes y fases
    for i in range(2, 10):  # i representa el número de armónico
        onda += (1/i) * np.sin(2 * np.pi * i * frecuencia * t + (np.pi/4) * i)
    
    # Aplicar envolvente ADSR más detallada
    A = 0.01  # Attack
    D = 0.2   # Decay
    S = 0.7   # Sustain Level
    R = 0.2   # Release
    
    atk = np.linspace(0, 1, int(A * frecuencia_muestreo))
    dcy = np.linspace(1, S, int(D * frecuencia_muestreo))
    sus = np.ones(int((duracion - A - D - R) * frecuencia_muestreo)) * S
    rls = np.linspace(S, 0, int(R * frecuencia_muestreo))
    
    envolvente = np.concatenate([atk, dcy, sus, rls])
    
    return 0.5 * onda * envolvente

def guardar_onda_como_wav(onda, nombre_archivo):
    wavio.write(nombre_archivo, onda, frecuencia_muestreo, sampwidth=3)


for nota, frecuencia in frecuencias.items():
    onda = generar_onda_piano(frecuencia)
    nombre_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{nota}.wav")
    guardar_onda_como_wav(onda, nombre_archivo)

print("¡Archivos de audio creados exitosamente!")
