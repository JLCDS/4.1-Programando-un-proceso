import time
import random
import matplotlib.pyplot as plt
from collections import deque

# Clase que representa un proceso en la simulación
class Proceso:
    def __init__(self, id, tiempo_ejecucion):
        self.id = id  # Identificador del proceso
        self.tiempo_ejecucion = tiempo_ejecucion  # Tiempo necesario para ejecutar el proceso

# Clase que simula un sistema operativo con diferentes estrategias de procesamiento
class SimuladorSO:
    def __init__(self, tipo):
        self.tipo = tipo  # Tipo de procesamiento (serie, lotes, tiempo compartido)
        self.cola_procesos = deque()  # Cola de procesos a ejecutar

    def agregar_proceso(self, proceso):
        """Agrega un proceso a la cola de procesos."""
        self.cola_procesos.append(proceso)

    def ejecutar(self):
        """Ejecuta los procesos según el esquema de procesamiento seleccionado."""
        tiempos_inicio = []  # Lista para almacenar los tiempos de inicio
        tiempos_fin = []  # Lista para almacenar los tiempos de finalización
        procesos_ids = []  # Lista de identificadores de los procesos ejecutados
        tiempo_actual = 0  # Tiempo acumulado de ejecución
        factor_aceleracion = 0.1  # Factor para acelerar la simulación visual

        if self.tipo == "serie":
            # Procesamiento en serie: un proceso a la vez, en orden de llegada
            while self.cola_procesos:
                proceso = self.cola_procesos.popleft()
                tiempos_inicio.append(tiempo_actual)  # Tiempo de inicio del proceso
                print(f"Ejecutando proceso {proceso.id} con tiempo de ejecución {proceso.tiempo_ejecucion} segundos")
                time.sleep(proceso.tiempo_ejecucion * factor_aceleracion)  # Simulación rápida
                tiempo_actual += proceso.tiempo_ejecucion
                tiempos_fin.append(tiempo_actual)  # Tiempo de finalización del proceso
                procesos_ids.append(proceso.id)

        elif self.tipo == "lotes":
            # Procesamiento por lotes: ejecuta grupos de dos procesos a la vez
            while self.cola_procesos:
                lote = [self.cola_procesos.popleft() for _ in range(min(2, len(self.cola_procesos)))]
                for proceso in lote:
                    tiempos_inicio.append(tiempo_actual)  # Tiempo de inicio del proceso
                    print(f"Ejecutando proceso {proceso.id} por {proceso.tiempo_ejecucion} segundos")
                    time.sleep(proceso.tiempo_ejecucion * factor_aceleracion)
                    tiempo_actual += proceso.tiempo_ejecucion
                    tiempos_fin.append(tiempo_actual)  # Tiempo de finalización del proceso
                    procesos_ids.append(proceso.id)

        elif self.tipo == "tiempo compartido":
            # Tiempo compartido: usa un quantum fijo para repartir el tiempo entre procesos
            quantum = 2
            while self.cola_procesos:
                proceso = self.cola_procesos.popleft()
                tiempo_ejecucion_actual = min(quantum, proceso.tiempo_ejecucion)
                tiempos_inicio.append(tiempo_actual)  # Tiempo de inicio del proceso
                print(f"Ejecutando proceso {proceso.id} por {tiempo_ejecucion_actual} segundos")
                time.sleep(tiempo_ejecucion_actual * factor_aceleracion)
                tiempo_actual += tiempo_ejecucion_actual
                proceso.tiempo_ejecucion -= tiempo_ejecucion_actual
                tiempos_fin.append(tiempo_actual)  # Tiempo de finalización del proceso
                procesos_ids.append(proceso.id)
                if proceso.tiempo_ejecucion > 0:
                    self.cola_procesos.append(proceso)  # Reagregar proceso si no ha terminado

        self.mostrar_grafico(procesos_ids, tiempos_inicio, tiempos_fin)

    def mostrar_grafico(self, procesos, tiempos_inicio, tiempos_fin):
        """Muestra un gráfico de los tiempos de inicio y finalización de los procesos."""
        plt.figure(figsize=(15, 5))
        bar_width = 0.35  # Ancho de las barras

        # Crear barras para tiempos de inicio y finalización
        plt.bar(procesos, tiempos_inicio, bar_width, label='Tiempo de Inicio', color='blue')
        plt.bar(procesos, [fin - inicio for inicio, fin in zip(tiempos_inicio, tiempos_fin)], 
                bar_width, bottom=tiempos_inicio, label='Duración del Proceso', color='red')

        plt.xlabel("ID Proceso")
        plt.ylabel("Tiempo (segundos)")
        plt.title(f"Simulación de Procesos - {self.tipo}")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Solicitar al usuario el tipo de procesamiento y la cantidad de procesos
    tipo = input("Ingrese el tipo de procesamiento (serie, lotes, tiempo compartido): ").strip().lower()
    n = int(input("Ingrese la cantidad de procesos a simular: "))
    simulador = SimuladorSO(tipo)

    # Generar procesos con tiempos de ejecución aleatorios
    for i in range(n):
        tiempo_ejecucion = random.randint(1, 5)
        simulador.agregar_proceso(Proceso(i + 1, tiempo_ejecucion))

    # Ejecutar la simulación
    simulador.ejecutar()