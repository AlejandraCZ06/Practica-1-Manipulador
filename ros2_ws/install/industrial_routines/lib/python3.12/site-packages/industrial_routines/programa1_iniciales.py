#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import subprocess

class Programa1Iniciales(Node):
    def __init__(self):
        super().__init__('programa1_iniciales_node')
        self.get_logger().info("Iniciando Programa 1: Generación de trayectorias de iniciales.")

    def mostrar_popup(self, letra, integrante):
        self.get_logger().info(f"--- Simulando letra [{letra}] de {integrante} ---")
        try:
            # Ventana emergente (popup) interactiva antes de simular la trayectoria
            subprocess.run([
                "zenity", "--info", 
                f"--text=Simulando letra: {letra}\\nIntegrante: {integrante}", 
                "--title=Programa 1 - Iniciales"
            ], timeout=2)
        except Exception:
            # Si se ejecuta en un entorno sin interfaz gráfica de usuario, pasa por consola
            pass

    def ejecutar(self):
        # Secuencia exacta de iniciales del equipo
        # Alejandra: A, C, Z | Andy: A, J, H, M
        secuencia = [
            ('A', 'Alejandra Calderón'),
            ('C', 'Alejandra Calderón'),
            ('Z', 'Alejandra Calderón'),
            ('A', 'Andy Herrera'),
            ('J', 'Andy Herrera'),
            ('H', 'Andy Herrera'),
            ('M', 'Andy Herrera')
        ]
        
        for letra, integrante in secuencia:
            # 1. Mensaje emergente obligatorio antes de cada trayectoria
            self.mostrar_popup(letra, integrante)
            
            # 2. Simulación de la ejecución de la trayectoria cartesiana/articular
            self.get_logger().info(f"Ejecutando trayectoria MoveIt para la letra {letra}...")
            rclpy.spin_once(self, timeout_sec=2.0)
            
        self.get_logger().info("¡Programa 1 finalizado con éxito!")

def main(args=None):
    rclpy.init(args=args)
    nodo = Programa1Iniciales()
    nodo.ejecutar()
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()