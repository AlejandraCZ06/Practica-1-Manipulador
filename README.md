# Práctica 1: Programación y Control de un Manipulador UR5

Este repositorio contiene los archivos y scripts desarrollados para la programación de un robot colaborativo **UR5** utilizando el simulador **URSim CB3 (PolyScope)** y su integración con **ROS 2 Jazzy** para control externo.

## 👥 Integrantes
- Alejandra Calderón Zambrana
- Andy Joel Herrera Mejía

## 📋 Descripción de los Programas

El proyecto se divide en tres rutinas independientes que demuestran diferentes capacidades de programación y control:

### 1. Programa 1: Trazado de Iniciales
Genera trayectorias en URScript para simular el dibujo de las iniciales de los integrantes del grupo (A, H, A, C). 
- **Características:** Uso de movimientos articulares (`movej`) con orientación fija para evitar singularidades y límites de articulaciones. Incluye mensajes emergentes (`popup`) antes de cada letra.

### 2. Programa 2: Control Compartido con ROS 2
Cede el control del robot a un controlador externo (ROS 2) mediante el driver oficial.
- **Características:** Activación de salidas digitales, mensajes de advertencia al operador, temporizadores (`sleep`) y un bucle de espera para mantener la conexión RTDE activa.
- **Bono:** Incluye la configuración para planificar y ejecutar trayectorias usando **MoveIt 2** y **RViz 2**.

### 3. Programa 3: Rutina de Pick and Place
Simula una operación industrial de recogida y colocación de objetos.
- **Características:** Secuencia de movimientos con puntos de aproximación (intermedios), activación/desactivación del efector final (salidas digitales) y sincronización con el operador mediante una entrada digital (DI) para reiniciar el ciclo.
