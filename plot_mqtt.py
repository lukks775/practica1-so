import json
import matplotlib.pyplot as plt

archivo="mqtt_capture.log"

with open(archivo, "r") as f:
    lineas=f.readlines()
datos=[]
for linea in lineas:
    if "Payload:" in linea:
        json_str=linea.split("Payload:")[1]

        try:
            data=json.loads(json_str)
            datos.append(data)
        except:
            pass

print("nmero de mensajes encontrados:",len(datos))
