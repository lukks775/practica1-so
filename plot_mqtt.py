import json    #importa la libreria json para poder leer datos JSON
import matplotlib.pyplot as plt #importa matplitlib para generar graficas
archivo="mqtt_capture.log" #nombre del archivo log generado por el Bash
with open(archivo, "r") as f: #abre el archivo log en modo lectura
    lineas=f.readlines() #lee todas las lineas del archivo y las guarda en listas
datos=[] #lista para guardar los datos JSON del log
for linea in lineas: #recorre todas las lineas
    if "Payload:" in linea: #comprueba si la linea contiene datos del sensor
        json_str=linea.split("Payload:")[1] #extrae la parte JSON del mensaje

        try: #para evitar errores
            data=json.loads(json_str) #convierte el JSON en un dic de python
            datos.append(data) #añade el dato extraido a la lista de datos
        except: #ignora errores
            pass

print("nmero de mensajes encontrados:",len(datos)) #muestra cuantos mensajes se encontraron el log
if len(datos)==0: #comprueba si no se encontraron datos 
    print("no se encontraron datos en el log.")
    print("asegurate de ejectar primero el script Bash para capturar datos MQTT.")
    exit() #termina el programa si no hay datos

temperaturas = [] #lista para almacenar las temperaturas
for d in datos: 
    if "AmbientTemperature" in d: #comprueba si el dato contiene temperatura
        temperaturas.append(d["AmbientTemperature"]) #guarda el valor de temperatura en la lista
plt.plot(temperaturas) #genera una grafica con los valores temperatura
plt.title("temperatura del sensor")
plt.xlabel("tiempo") #etiqueta eje X
plt.ylabel("temperatura") #etiqueta eje Y
plt.savefig("plots/temperatura.png") #guarda la grafica en la carpeta plots
print("graficaa guardada en plots/temperatura.png")

print("\ngrafica ASCII:\n") #muestra una representacion ASCII de la grafica en la terminal

for t in temperaturas:
    barras=int(t) #convierte la temperatura en numero de caracteres 
    print("|" + "#" * barras) #genera barras con ASCII
