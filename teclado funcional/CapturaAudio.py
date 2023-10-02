from math import exp, log
 
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")
import sounddevice as sd

def frec(nota: int, octava: int) -> int:
    expo = octava * 12 + (nota - 58)
    return int(440 * ((2 ** (1 / 12)) ** expo))

# 1	DO	C
# 2	DO♯ / RE♭	C♯ / B♭
# 3	RE	D
# 4	RE♯ / MI♭	D♯ / E♭
# 5	MI	E
# 6	FA	F
# 7	FA♯ / SOL♭	F♯ / G♭
# 8	SOL	G
# 9	SOL♯ / LA♭	G♯ / A♭
# 10	LA	A
# 11	LA♯ / SI♭	A♯ / B♭
# 12	SI	B


# framerate = 44100
# duration = 1000
# t = np.linspace(0, duration / 1000, int(framerate * duration / 1000))
# frequency = frec(0, 0) # Do0
# data = np.sin(2 * np.pi * frequency * t)

# fig, ax = plt.subplots(figsize=(15, 5))
# ax.plot(t, data)
# ax.set_xlabel("tiempo")
# ax.set_ylabel("amplitud")
# fig.savefig("onda_16_pulsos.png")
# plt.show()

def beep(nota: int, octava: int, duracion: int) -> None:
    framerate = 44100
    t = np.linspace(0, duracion / 1000, int(framerate * duracion / 1000))
    frequency = frec(nota, octava)
    data = np.sin(2 * np.pi * frequency * t)
    sd.play(data, framerate)
    sd.wait()




imnote = [
    10, 10, 10, 6, 1,
    10, 6, 1, 10,
    5, 5, 5, 6, 1,
    9, 6, 1, 10,
    10, 10, 10, 10, 9, 8,
    7, 6, 8, 12, 4, 3, 2,
    1, 12, 1, 6, 9, 6, 9,
]
imoctave = [
    4, 4, 4, 4, 5,
    4, 4, 5, 4,
    5, 5, 5, 5, 5,
    4, 4, 5, 4,
    
    5, 4, 4, 5, 5, 5,
    5, 5, 5, 4, 5, 5, 5,
    5, 4, 5, 4, 4, 4, 4,
]
imlong = [
    500, 500, 500, 250, 250,
    500, 250, 250, 1000,
    500, 500, 500, 250, 250,
    500, 250, 250, 1000,
    500, 250, 250, 500, 250, 250,
    250, 250, 250, 250, 500, 250, 250,
    250, 250, 250, 250, 500, 250, 250,
]
 
for n, o, d in zip(imnote, imoctave, imlong):
    beep(n, o, d)

	
for i in range(1, 13):
    beep(i, 4, 250)

for i in range(1, 13):
    for v in range(4, 5):
        beep(i, v, 300)
        # print('La nota es: ',i)
        # print('La octava es: ',v)