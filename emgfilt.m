clear all; close all

% Seleccionar el archivo de texto que contiene los datos de EMG
[FileName, PathName, FilterIndex] = uigetfile({'*.txt'}, 'Seleccione el archivo de EMG');
archivo_emg = fullfile(PathName, FileName);

% Cargar los datos del archivo de EMG
datos_emg = load(archivo_emg);



% Extraer el vector de voltaje y el vector de tiempo
voltaje_emg = datos_emg(:, 1); % Suponiendo que la columna 1 contiene el voltaje
tiempo = datos_emg(:, 2); % Suponiendo que la columna 2 contiene el tiempo
% Especifica la frecuencia de corte del filtro en Hz. Ajusta este valor según tus necesidades.
frecuencia_de_corte = 10; % Por ejemplo, 20 Hz
fs= length(voltaje_emg)/tiempo(end);

% Calcula la frecuencia normalizada
frecuencia_normalizada = frecuencia_de_corte / (0.5 * fs);

% Diseña el filtro Butterworth
orden_del_filtro = 4; % Puedes ajustar este valor según tus necesidades
[b, a] = butter(orden_del_filtro, frecuencia_normalizada, 'high');

% Aplica el filtro a la señal EMG
senal_filtrada = filtfilt(b, a, voltaje_emg);


frecuencias = linspace(0, fs, length(voltaje_emg));
transformada = abs(fft(voltaje_emg));



% Grafica la señal original y la señal filtrada para comparar
t = (0:length(voltaje_emg) - 1) / fs;
figure;
subplot(2,1,1);
plot(t, voltaje_emg);
title('Señal EMG Original');
xlabel('Tiempo (s)');
ylabel('Amplitud');
subplot(2,1,2);
plot(t, senal_filtrada);
title('Señal EMG Filtrada');
xlabel('Tiempo (s)');
ylabel('Amplitud');
% subplot(3,1,3)
% plot(frecuencias, transformada);
% title('Transformada de Fourier');
% xlabel('Frecuencia (Hz)');
% ylabel('Amplitud');
% Puedes ajustar los parámetros del filtro (frecuencia de corte, orden, etc.) según tus necesidades específicas.




