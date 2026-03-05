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

temperaturas = []
for d in datos:
    if "AmbientTemperature" in d:
        temperaturas.append(d["AmbientTemperature"])
plt.plot(temperaturas)
plt.title("temperatura del sensor")
plt.xlabel("tiempo")
plt.ylabel("temperatura")
plt.savefig("plots/temperatura.png")
print("graficaa guardada en plots/temperatura.png")
