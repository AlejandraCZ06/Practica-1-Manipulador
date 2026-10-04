# Practica 1: Manipulador (ROS2 y MoveIt)

Repositorio oficial para la entrega de las rutinas de robótica industrial desarrolladas en ROS2, MoveIt y contenedores Docker.

## 👥 Integrantes del Equipo
* **Alejandra Calderón Zambrana** (Escuela Colombiana de Ingeniería Julio Garavito)
* **Andy Joel Herrera Mejía**

---

## 📋 Descripción de los Programas

1. **Programa 1 (`programa1_iniciales.py`):** 
   * Genera trayectorias cartesianas para simular el trazo de las iniciales del equipo completo (**A, C, Z** para Alejandra y **A, J, H, M** para Andy).
   * Muestra un mensaje emergente (`popup`) interactivo indicando qué letra se va a simular antes de ejecutar cada trayectoria.

2. **Programa 2 (`programa2_control_externo.py`):** 
   * Activa una salida digital de libre elección en estado alto (`HIGH`) al iniciar.
   * Despliega un mensaje emergente indicando la transferencia del control a un controlador externo, esperando 5 segundos estrictos tras la confirmación del usuario.
   * Configura el nodo de *External Control* para la manipulación del robot desde ROS2.

3. **Programa 3 (`programa3_pick_and_place.py`):** 
   * Ejecuta una rutina de *Pick and Place* simulando operaciones en al menos dos puntos de recogida.
   * Incluye puntos intermedios de aproximación en altura (tanto al recoger como al dejar), control del efector final, liberación de carga útil (*payload*) y un bucle de espera mediante una entrada digital en alto para reanudar el ciclo.

---

## 🚀 Instrucciones de Ejecución

1. Clonar el repositorio en tu espacio de trabajo de ROS2:
   ```bash
   git clone [https://github.com/AlejandraCZ06/Practica-1-Manipulador.git](https://github.com/AlejandraCZ06/Practica-1-Manipulador.git)