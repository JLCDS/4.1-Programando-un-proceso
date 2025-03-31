# Simulador de Procesamiento de Sistemas Operativos

Este proyecto es un simulador de ejecución de procesos en un sistema operativo, implementado en Python. Soporta tres tipos de procesamiento:

- **Procesamiento en Serie**: Los procesos se ejecutan uno tras otro.
- **Procesamiento por Lotes**: Los procesos se agrupan en lotes y se ejecutan en orden.
- **Procesamiento por Tiempo Compartido**: Cada proceso recibe un tiempo de ejecución fijo antes de ceder la CPU al siguiente.

## 📌 Características
- Simulación visual de la ejecución de procesos mediante gráficos.
- Muestra el orden de ejecución de los procesos en consola.
- Permite elegir el tipo de procesamiento antes de iniciar la simulación.

## 📂 Instalación
1. Clona este repositorio:
   ```sh
   git clone https://github.com/tuusuario/simulador-procesos.git
   ```
2. Ingresa al directorio del proyecto:
   ```sh
   cd simulador-procesos
   ```
3. Instala las dependencias necesarias:
   ```sh
   pip install matplotlib numpy
   ```

## ▶️ Uso
Ejecuta el script principal:
```sh
ProgramandoUnProceso.py
```
Luego, ingresa el tipo de procesamiento que deseas simular (**serie, lotes o tiempo compartido**) y la cantidad de procesos.

## 📊 Ejemplo de Ejecución
### 1️⃣ Procesamiento en Serie
```
Ingrese el tipo de procesamiento (serie, lotes, tiempo compartido): serie
Ingrese la cantidad de procesos a simular: 5
Ejecutando proceso 1 con tiempo de ejecución 3 segundos
Ejecutando proceso 2 con tiempo de ejecución 2 segundos
...
```
_Generará una gráfica mostrando el tiempo de inicio y duración de cada proceso._

### 2️⃣ Procesamiento por Lotes
```
Ingrese el tipo de procesamiento (serie, lotes, tiempo compartido): lotes
Ingrese la cantidad de procesos a simular: 5
Ejecutando proceso 1 por 4 segundos
Ejecutando proceso 2 por 3 segundos
...
```

### 3️⃣ Procesamiento por Tiempo Compartido
```
Ingrese el tipo de procesamiento (serie, lotes, tiempo compartido): tiempo compartido
Ingrese la cantidad de procesos a simular: 5
Ejecutando proceso 1 por 2 segundos
Ejecutando proceso 2 por 2 segundos
Ejecutando proceso 3 por 2 segundos
...
```

## 📜 Licencia
Este proyecto está bajo la licencia MIT.

## ✨ Autor
Desarrollado por JLC

