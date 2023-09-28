% Parámetros de la señal
frecuencia = 5;  % Frecuencia de la señal en Hz
muestras_por_segundo = 1000;  % Tasa de muestreo en Hz
duracion_segundos = 2;  % Duración de la señal en segundos

% Generar una señal senoidal
tiempo = linspace(0, duracion_segundos, muestras_por_segundo * duracion_segundos);
senal = sin(2 * pi * frecuencia * tiempo);

% Calcular la Transformada de Fourier
transformada = fft(senal);

% Mostrar la Transformada de Fourier en un gráfico
figure;
subplot(2, 1, 1); % Crear un subplot para la señal en el dominio del tiempo
plot(tiempo, senal);
title('Señal en el Dominio del Tiempo');
xlabel('Tiempo (s)');
ylabel('Amplitud');
grid on;

subplot(2, 1, 2); % Crear un subplot para la Transformada de Fourier
frecuencias = linspace(0, muestras_por_segundo, length(transformada));
plot(frecuencias, abs(transformada));
title('Transformada de Fourier');
xlabel('Frecuencia (Hz)');
ylabel('Amplitud');
grid on;

% Ajustar el espacio entre subplots
spacing = 0.1;
set(subplot(2, 1, 1), 'Position', [0.1, 0.55, 0.8, 0.35]);
set(subplot(2, 1, 2), 'Position', [0.1, 0.1, 0.8, 0.35]);
