#!/bin/bash

echo "script de captura MQTT"

echo "iintroduce el tiempo de captura en segundos:"
read tiempo

echo "Iniciando captura de datos..."

while true; do
echo 'Payload: {"AmbientTemperature":20}'; sleep 1; done > mqtt_capture.log &

PID=$!

echo "Proceso iniciado con PID: $PID"

contador=0

while kill -0 $PID 2>/dev/null
do
    sleep 1
    contador=$((contador+1))

    if [ $contador -ge $tiempo ]; then
        echo "Tiempo alcanzado. Finalizando proceso..."
        kill -SIGTERM $PID
        break
    fi
done

echo "Ejecutando analisis en Python..."

python3 plot_mqtt.py

