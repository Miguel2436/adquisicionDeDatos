clear all; close all

% Seleccionar el archivo de texto que contiene los datos de EMG
[FileName, PathName, FilterIndex] = uigetfile({'*.txt'}, 'Seleccione el archivo de EMG');
archivo_emg = fullfile(PathName, FileName);

% Cargar los datos del archivo de EMG
datos_emg = load(archivo_emg);

% Extraer el vector de voltaje y el vector de tiempo
voltaje_emg = datos_emg(:, 1); % Suponiendo que la columna 1 contiene el voltaje
tiempo = datos_emg(:, 2); % Suponiendo que la columna 2 contiene el tiempo

% Calcular la frecuencia de muestreo
fs = 1 / (tiempo(2) - tiempo(1)); % Frecuencia de muestreo (Hz)

% Filtrado utilizando Transformada de Fourier
senal_fft = fft(voltaje_emg); % Calcular la transformada de Fourier
filtro_fft = zeros(size(voltaje_emg)); % Crear un filtro en el dominio de la frecuencia
% Aplicar el filtro en el dominio de la frecuencia (puedes personalizarlo)
% Ejemplo: Suprimir frecuencias por debajo de 20 Hz y por encima de 500 Hz
filtro_fft(1:round(20 / fs)) = 0;
filtro_fft(round(500 / fs):end) = 0;
senal_filtrada_fft = ifft(senal_fft .* filtro_fft); % Aplicar la transformada inversa

% % Filtrado utilizando Wavelet
% wavelet_tipo = 'db4'; % Tipo de wavelet (puedes cambiarlo)
% nivel_wavelet = 5; % Nivel de descomposición (ajusta según tu señal)
% [coef_wavelet, estructura_descomposicion] = wavedec(voltaje_emg, nivel_wavelet, wavelet_tipo); % Descomposición wavelet
% umbral = 0.2; % Umbral para eliminar coeficientes de wavelet (ajusta según tu señal)
% coef_wavelet_filtrado = wthresh(coef_wavelet, 's', umbral); % Aplicar umbral
% senal_filtrada_wavelet = waverec(coef_wavelet_filtrado, estructura_descomposicion);

% Filtrado utilizando filtro pasa-bandas
frecuencia_corte_inf = .20; % Frecuencia de corte inferior en Hz
frecuencia_corte_sup = .500; % Frecuencia de corte superior en Hz
orden = 4; % Orden del filtro (ajusta según tu señal)
[b, a] = butter(orden, [frecuencia_corte_inf, frecuencia_corte_sup] / (fs/2), 'bandpass');
senal_filtrada_bandpass = filtfilt(b, a, voltaje_emg);

% Visualización de las señales originales y filtradas
figure;
subplot(4, 1, 1);
plot(tiempo, voltaje_emg);
title('Señal EMG Original');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(4, 1, 2);
plot(tiempo, senal_filtrada_fft);
title('Señal EMG Filtrada (Fourier)');
xlabel('Tiempo (s)');
ylabel('Amplitud');


subplot(4, 1, 4);
plot(tiempo, senal_filtrada_bandpass);
title('Señal EMG Filtrada (Pasa-bandas)');
xlabel('Tiempo (s)');
ylabel('Amplitud');

sgtitle('Filtrado de Señal EMG');

% Puedes ajustar y optimizar los parámetros de filtrado según tu señal y requisitos específicos.

% Puedes ajustar y optimizar los parámetros de
