import pygame
import numpy as np

# Inicializar pygame
pygame.init()

# Configuración de la ventana (no la usamos, pero es necesaria para pygame)
window = pygame.display.set_mode((200, 200))

# Frecuencias para las notas do, re, mi y sol
freqs = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'G4': 392.00,
}

# Diccionario para mantener un seguimiento de las notas que están sonando actualmente
playing_notes = {}

# Función para generar una onda sinusoidal bidimensional para una nota dada
def generate_sine_wave(note):
    sample_rate = 54800  # Tasa de muestreo en Hz
    duration_ms = 100  # Duración de la nota en milisegundos
    t = np.linspace(0, duration_ms / 1000, int(sample_rate * (duration_ms / 1000)), endpoint=False)
    wave = np.zeros((len(t), 2), dtype=np.int16)
    amplitude = 0.5 * 32767  # Amplitud máxima para formato de 16 bits
    wave[:, 0] = (amplitude * np.sin(2 * np.pi * freqs[note] * t)).astype(np.int16)
    wave[:, 1] = wave[:, 0]
    return wave

# Función para tocar una nota
def play_note(note):
    if note not in playing_notes:
        wave = generate_sine_wave(note)
        sound = pygame.sndarray.make_sound(wave)
        sound.play(loops=-1)  # -1 significa reproducir continuamente
        playing_notes[note] = sound

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                play_note('C4')
            elif event.key == pygame.K_s:
                play_note('D4')
            elif event.key == pygame.K_d:
                play_note('E4')
            elif event.key == pygame.K_f:
                play_note('G4')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a and 'C4' in playing_notes:
                playing_notes['C4'].stop()
                del playing_notes['C4']
            elif event.key == pygame.K_s and 'D4' in playing_notes:
                playing_notes['D4'].stop()
                del playing_notes['D4']
            elif event.key == pygame.K_d and 'E4' in playing_notes:
                playing_notes['E4'].stop()
                del playing_notes['E4']
            elif event.key == pygame.K_f and 'G4' in playing_notes:
                playing_notes['G4'].stop()
                del playing_notes['G4']

    # Pausa para reducir el uso de CPU
    pygame.time.delay(10)

# Detener todos los sonidos antes de salir
for sound in playing_notes.values():
    sound.stop()

# Salir de pygame
pygame.quit()
