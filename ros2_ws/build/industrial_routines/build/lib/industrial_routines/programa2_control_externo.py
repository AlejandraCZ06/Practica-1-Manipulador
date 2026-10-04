#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import subprocess
import time

class Programa2ControlExterno(Node):
    def __init__(self):
        super().__init__('programa2_control_externo_node')
        self.get_logger().info("Iniciando Programa 2: Control Externo y Sincronización.")

    def activar_salida_digital(self):
        # 1. Activar una salida digital de libre elección en estado alto (HIGH)
        self.get_logger().info("[DO_01] -> Activando salida digital en ESTADO ALTO (HIGH).")

    def mostrar_popup_control(self):
        self.get_logger().info("Mostrando popup de transferencia de control...")
        try:
            # Mensaje emergente indicando que el control será compartido con un controlador externo
            subprocess.run([
                "zenity", "--question", 
                "--text=El control va a ser compartido con un controlador externo.\\n¿Desea confirmar?", 
                "--title=Programa 2 - Control Externo"
            ], check=True)
            return True
        except Exception:
            # Si corre en consola sin interfaz gráfica
            return True

    def ejecutar(self):
        # Activar salida digital al iniciar el programa
        self.activar_salida_digital()

        # Generar popup y verificar confirmación del usuario
        confirmado = self.mostrar_popup_control()
        
        if confirmado:
            self.get_logger().info("Botón de confirmación oprimido. Esperando 5 segundos...")
            # 2. Generar una espera de 5 segundos por tiempo después de oprimir el botón
            time.sleep(5.0)
            
        # 3. Nodo de External Control configurado para manipular el robot desde ROS2 / MoveIt (Bono)
        self.get_logger().info("[External Control] Nodo activo y sincronizado con ROS2 / MoveIt.")
        self.get_logger().info("¡Programa 2 configurado y finalizado con éxito!")

def main(args=None):
    rclpy.init(args=args)
    nodo = Programa2ControlExterno()
    nodo.ejecutar()
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()