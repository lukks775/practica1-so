#!/bin/bash
echo "Script de captura MQTT"
echo "Introduce el tiempo de captura en segundos:"
read tiempo
echo "Iniciando captura de datos..."
./mqtt_program > mqtt_capture.log 2>&1 &
PID=$!
echo "Proceso iniciado con PID: $PID"
contador=0
while kill -0 $PID 2>/dev/null
do
sleep 1
contador=$((contador+1))
if [ $contador -ge $tiempo];then
echo "Tiempo alcanzado. Finalizando proceso..."
kill -SIGTERM $PID
break
fi
done
echo "ejecutendo analisis en Python..."

python3 plot_mqtt.py

