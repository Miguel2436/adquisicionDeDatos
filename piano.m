function piano()
    % Configuración de frecuencias para las notas do, re, mi y sol
    freqs.C4 = 261.63;
    freqs.D4 = 293.66;
    freqs.E4 = 329.63;
    freqs.G4 = 392.00;

    % Diccionario para mantener un seguimiento de las notas que están sonando actualmente
    playingNotes = containers.Map();

    % Crear una figura y configurar una función de interrupción para detener el sonido
    fig = figure;
    set(fig, 'KeyPressFcn', @keyDown, 'KeyReleaseFcn', @keyUp);
    set(fig, 'NumberTitle', 'off', 'Name', 'Piano con MATLAB');

    % Función para generar una onda sinusoidal para una nota dada
    function wave = generateSineWave(note, duration_ms)
        sample_rate = 44100; % Tasa de muestreo en Hz
        t = 0:1/sample_rate:duration_ms/1000;
        wave = sin(2 * pi * freqs(note) * t);
    end

    % Función para tocar una nota
    function keyDown(~, event)
        key = event.Key;
        if isfield(freqs, key) && ~isKey(playingNotes, key)
            note = freqs.(key);
            wave = generateSineWave(key, 0.5); % Duración de 0.5 segundos
            scaled_wave = wave / max(abs(wave)); % Escalar al rango [-1, 1]
            sound(scaled_wave, sample_rate);
            playingNotes(key) = scaled_wave;
        end
    end

    % Función para detener una nota al soltar la tecla
    function keyUp(~, event)
        key = event.Key;
        if isKey(playingNotes, key)
            stopSound(playingNotes(key));
            remove(playingNotes, key);
        end
    end

    % Esperar hasta que se cierre la figura
    uiwait(fig);

    % Detener todas las notas antes de salir
    keys = keys(playingNotes);
    for i = 1:length(keys)
        stopSound(playingNotes(keys{i}));
    end
end

% Función para detener el sonido
function stopSound(sound)
    try
        clear sound; % Detener el sonido
    catch
    end
end
