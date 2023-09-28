function [v,ti] = Graficar(puerto)
tiempo=9999;
% while(1)
% tiempo=input('Ingresa el tiempo máximo de muestreo: ','s');
% tiempo=str2num(tiempo);
% if isscalar(tiempo)==0  || tiempo<=0 || tiempo>200 %El límite de medición será 30 segundos
%     disp('Valor no válido. Intente nuevamente');
%     pause(1.5);
%     clc;
%     continue;
% else
%     break;
% end
% end


v=[];
ti=[];
c=1;
EMG=figure('Name','Electromiograma');
ButtonHandle = uicontrol('Style', 'PushButton', ...
                         'String', 'ALTO', ...
                         'Callback', 'delete(gcbf)');
title('ELECTROMIOGRAMA','LineWidth',1,'FontName','Lucida Bright','FontSize',12);

xlabel('Segundos');
ylabel('Voltaje');
axis([0 tiempo 0 5]);
whitebg([0/255 0/255 0/255])
set(gca,'Color','k')
tic;

v(c)=puerto.analogRead(0)/1024*5
ti(c)=toc;
x=[0,ti(c)];
y=[0,v(c)];
%line(x,y,'Color','red');
drawnow
while ti(c)<=tiempo
    c=c+1;
    v(c)=puerto.analogRead(0)/1024*5;
    ti(c)=toc;
x=[ti(c-1),ti(c)];
y=[v(c-1),v(c)];
if ti(c)>=20
    axis([ti(c)-20 ti(c)+3 0 5]);
else
    axis([0 23 0 5]);
end

line(x,y,'Color','red');
drawnow
if ~ishandle(ButtonHandle)
    disp('Se ha detenido el ciclo');
    break;
  end
end
close all;
v= detrend(v);
EMGSAVE=[v;ti];
A=EMGSAVE.'
% Create a table with the data and variable names
writematrix(A, "EMGRead.txt");
plot(ti,v,'Color','red');
title('Electromiograma','LineWidth',1,'FontName','Arial','FontSize',12);
set(gca,'Color','k')
xlabel('Segundos');
ylabel('Voltaje');
axis([0 ti(end) -2.5 2.5]);
end
