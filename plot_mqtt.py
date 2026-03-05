import json
import re
import matplotlib.pyplot as plt

archivo = "mqtt_capture.log"

with open(archivo, "r") as f:
    lineas = f.readlines()

print("Archivo cargado correctamente")
