function main
clear all
clc;

while(1)
    clear all
clc;
disp('                        ----ELECTROMIOGRAMA----');
delete(instrfind({'Port'},{'COM5'}));
puerto = arduino('COM3');
[t] = captura(puerto);
[v,ti] = Graficar(puerto);

disp('�Desea repetir el EMG?  Presiona 1,');
ww=input(' sino presiona cualquier tecla -->  ','s');

if strcmpi(ww,'1')==1
    clc;
else
     clc  
     disp('  ----OPERACI�N TERMINADA----');
     break;
end
end
end