import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import Tk, Button
import time

# Configuración del puerto serie
puerto_serie = 'COM3'  # Cambiado a COM3
baud_rate = 9600

# Inicialización del puerto serie
ser = serial.Serial(puerto_serie, baud_rate)

# Configuración del gráfico
plt.ion()  # Activa el modo interactivo
fig, ax = plt.subplots()
x, y = [], []
line, = plt.plot(x, y)
plt.ylim(0, 5)  # Configura los límites del eje Y

# Registro del tiempo inicial
start_time = time.time()

def stop_graficar():
    """Detiene la animación y cierra la ventana"""
    anim.event_source.stop()
    plt.close(fig)
    
def update(frame):
    """Actualiza el gráfico con nuevos datos"""
    current_time = time.time() - start_time  # Calcula el tiempo transcurrido
    data = ser.readline().strip()  # Lee una línea del puerto serie
    if data:
        try:
            valor = int(data)  # Convierte el valor leído a entero
            voltaje = (valor * 5.0) / 1024.0  # Conversión a voltaje
            x.append(current_time)
            y.append(voltaje)
            line.set_data(x, y)
            
            # Si han pasado más de 30 segundos, actualiza los límites del eje X
            if current_time > 15:
                plt.xlim(current_time - 15, current_time)
                
            ax.relim()
            ax.autoscale_view()
        except ValueError:
            pass  # Ignora el error si no se puede convertir el valor a un entero

# Crear un botón para detener el gráfico
root = Tk()
root.title("Control")
button = Button(root, text="Detener", command=stop_graficar)
button.pack()

# Inicia la animación
anim = FuncAnimation(fig, update, frames=None, interval=100)
plt.show(block=False)
root.mainloop()

# Cierra el puerto serie cuando se termina el programa
ser.close()
