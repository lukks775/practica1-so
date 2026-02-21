# practica1-so
# Práctica 1 - Sistemas Operativos

Automatización con Bash y Python para captura y visualización de datos MQTT.

## Autor
Nombre Apellidos

## Descripción
Este proyecto automatiza la captura de datos desde un broker MQTT,
almacena la salida en un archivo log y posteriormente genera gráficas
mediante un script Python.

## Estructura del proyecto

- capture_mqtt.sh → Script Bash principal
- plot_mqtt.py → Script Python para análisis y gráficas
- mqtt_capture.log → Archivo de captura
- plots/ → Carpeta de gráficas generadas

## Requisitos

- Bash
- Python 3
- Librerías Python:
  - matplotlib
  - json
  - re

Instalación:

```bash
pip install matplotlib
