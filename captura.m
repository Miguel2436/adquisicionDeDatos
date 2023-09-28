function [t] = captura(puerto)
tic;
c=1;
t=0;
disp('Calculando frecuencia...');
while t <= 10
v(c)= puerto.analogRead(0);
c = c+1;
t=toc;
end
t=toc;
fs =round(length(v)/t);
disp('La frecuencia es: ');fs
end