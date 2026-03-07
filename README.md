# Práctica 1 - Sistemas Operativos  
## Captura y visualización de datos con Bash y Python
##Estructura generada con IA
https://github.com/lukks775/practica1-so

### Descripcion

En esta practica hemos desarrollado un sistema para la captura, almacenamiento y visualizacion de datos de sensores.

Se utiliza un script Bash para capturar datos y gestionar procesos, y un script Python para analizar los datos almacenados y generar representaciones graficas.

El flujo de funcionamiento del sistema es el siguiente:

1. El usuario ejecuta el script Bash.
2. El script genera datos simulados de sensores en formato JSON.
3. Los datos se almacenan en un archivo de log.
4. Tras finalizar el tiempo de captura, el script ejecuta un programa Python.
5. Python procesa los datos y genera una grafica de temperatura.

---

## Estructura del proyecto (dibujada con chatgpt)

```
practica1-so/
│
├── capture_mqtt.sh      # Script Bash para capturar datos
├── plot_mqtt.py         # Script Python para analizar datos
├── mqtt_capture.log     # Archivo de log generado
├── README.md
├── informe.pdf
│
└── plots/
    └── temperatura.png  # Gráfica generada
```

---

## Ejecucion del programa

Dar permisos al script Bash:

```
chmod +x capture_mqtt.sh
```

Ejecutar el script:

```
./capture_mqtt.sh
```

El sistema solicita el tiempo de captura en segundos.

Al finalizar el proceso se genera:

- Archivo `mqtt_capture.log`
- Grafica `plots/temperatura.png`
- Visualizacion ASCII en la terminal

---

## Autores

- Lucia Castellanos Paz  
- Ander Zuazquita Pastor

