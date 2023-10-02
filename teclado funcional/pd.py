import matplotlib.pyplot as plt

info_paquete = [
    'Nota 1: REM_D, duracion: 1.25 segundos\n',
    'Nota 2: LA_A, duracion: 1.07 segundos\n',
    'Nota 3: RE_D, duracion: 1.29 segundos\n',
    'Nota 4: FA_F, duracion: 1.09 segundos\n',
    'Nota 5: DOM_C, duracion: 1.34 segundos\n',
    'Nota 6: DOM_C, duracion: 1.35 segundos\n'
]

events_log = [
    'Script iniciado a las 2023-10-02 13:51:50',
    'RE_D presionada por 0.63 segundos',
    'MI_E presionada por 0.70 segundos',
    'FA_F presionada por 0.64 segundos',
    'SOL_G presionada por 0.67 segundos',
    'LA_A presionada por 0.84 segundos',
    'SI_B presionada por 0.74 segundos'
]

aciertos = 0
diferencias_tiempos = []

for i in range(6):
    info_linea = info_paquete[i].strip()
    events_linea = events_log[i + 1]  # i+1 porque ignoramos el primer elemento de events_log
    
    nota_info = info_linea.split(',')[0].split(':')[1].strip()
    tiempo_info = float(info_linea.split(',')[1].split(':')[1].strip().split(' ')[0])
    
    nota_events = events_linea.split(' ')[0]
    tiempo_events = float(events_linea.split(' ')[3])
    
    if nota_info == nota_events:
        aciertos += 1
        diferencias_tiempos.append(abs(tiempo_info - tiempo_events))
    else:
        diferencias_tiempos.append('n/a')

# Graficando los resultados
plt.figure(figsize=(10,6))
plt.bar(range(1, 7), [1 if diff != 'n/a' else 0 for diff in diferencias_tiempos], color='green', alpha=0.7, label='Aciertos')
plt.bar(range(1, 7), [0 if diff != 'n/a' else 1 for diff in diferencias_tiempos], bottom=[1 if diff != 'n/a' else 0 for diff in diferencias_tiempos], color='red', alpha=0.7, label='Errores')
plt.ylabel('Aciertos/Errores')
plt.xlabel('Número de nota')
plt.title('Comparación de Notas')
plt.xticks(range(1, 7))
plt.legend()
plt.show()

# Mostrando las diferencias en tiempos
for i, diff in enumerate(diferencias_tiempos):
    if diff != 'n/a':
        print(f'Diferencia de tiempo en nota {i+1}: {diff} segundos')
    else:
        print(f'Nota {i+1} no coincide')
