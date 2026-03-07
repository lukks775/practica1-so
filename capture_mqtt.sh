#!/bin/bash
echo "script de captura MQTT"
echo "iintroduce el tiempo de captura en segundos:"
read tiempo #solicita el tiempo  y lo guarda  en la variable tiempo
echo "iniciando captura de datos..."
while true; do #bucle infinito con la recepcion de datos
echo "Payload: {\"AmbientTemperature\":$((RANDOM % 40))}"; sleep 1; done > mqtt_capture.log &
#Random genera un numero aleatorio y %40 limita el numero entre 0 y 39
#done> mqtt_capture.log &: guarda la salida en mqtt_capture.log y ejecuta el proceso en segundo plano
PID=$! #guarda el PID del proceso en segundo plano para controlarlo
echo "Proceso iniciado con PID: $PID" #muestra el identificador del proceso
contador=0 #controla el tiempo de captura
while kill -0 $PID 2>/dev/null #comprueba si el proceso sigue activo usando kill
do
    sleep 1 #espera 1 segundo antes de generar el siguientr dato
    contador=$((contador+1)) #incrementa el contador

    if [ $contador -ge $tiempo ]; then #comprueba si el tiempo de captura ha terminado
        echo "Tiempo alcanzado. Finalizando proceso..."
        kill -SIGTERM $PID #envia la señal SIGTERM para finalizar el proceso
        break #sale del bucle
    fi
done
echo "Ejecutando analisis en Python..."
python3 plot_mqtt.py #ejecuta el script de pythom que analiza los datos y genera la grafica

