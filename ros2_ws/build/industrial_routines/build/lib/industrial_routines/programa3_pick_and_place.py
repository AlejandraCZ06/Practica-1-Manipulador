#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time

class Programa3PickAndPlace(Node):
    def __init__(self):
        super().__init__('programa3_pick_and_place_node')
        self.get_logger().info("Iniciando Programa 3: Rutina automatizada de Pick and Place.")

    def simular_movimiento(self, descripcion):
        self.get_logger().info(f"-> [Movimiento] {descripcion}")
        time.sleep(1.0)

    def ejecutar_ciclo(self):
        # 2 puntos de recogida de libre elección
        puntos_recogida = [
            "Punto de Recogida 1 (Zona A)", 
            "Punto de Recogida 2 (Zona B)"
        ]
        punto_llegada = "Punto de Destino / Ensamblaje"

        for idx, recogida in enumerate(puntos_recogida, start=1):
            self.get_logger().info(f"\n--- Iniciando Ciclo {idx}: {recogida} ---")
            
            # 1. Trayectoria hasta el punto intermedio (arriba del punto de recogida)
            self.simular_movimiento(f"Moviendo a punto intermedio superior sobre {recogida}")
            
            # 2. Descenso hasta el punto de recogida
            self.simular_movimiento(f"Descendiendo y alcanzando {recogida}")
            
            # 3. Activar el efector final (Pinza / Gripper)
            self.get_logger().info("[Efector Final] -> Activado (Carga útil sujeta).")
            time.sleep(1.0)
            
            # 4. Trayectoria de retorno al punto intermedio (arriba de recogida)
            self.simular_movimiento("Elevando carga al punto intermedio superior de recogida")
            
            # 5. Trayectoria hacia el punto intermedio (arriba del punto de llegada)
            self.simular_movimiento(f"Transfiriendo carga hacia el punto intermedio superior de {punto_llegada}")
            
            # 6. Descenso al punto de llegada
            self.simular_movimiento(f"Descendiendo y alcanzando {punto_llegada}")
            
            # 7. Liberar la carga útil (Payload)
            self.get_logger().info("[Payload] -> Carga útil liberada en destino.")
            time.sleep(1.0)
            
            # 8. Retirada del efector final
            self.simular_movimiento("Retrayendo efector final vacío a posición segura")

    def esperar_entrada_digital(self):
        self.get_logger().info("\n[DI_Wait] Esperando confirmación por ENTRADA DIGITAL en ESTADO ALTO (HIGH)...")
        # Simulación de espera de la señal de entrada digital del usuario
        time.sleep(3.0)
        self.get_logger().info("[DI_Wait] ¡Entrada digital detectada en HIGH! Reiniciando programa de Pick and Place.")

    def ejecutar(self):
        # Ejecutar todas las rutinas de pick and place
        self.ejecutar_ciclo()
        
        # Esperar la confirmación mediante entrada digital en alto para volver a ejecutar
        self.esperar_entrada_digital()
        
        self.get_logger().info("¡Programa 3 finalizado correctamente!")

def main(args=None):
    rclpy.init(args=args)
    nodo = Programa3PickAndPlace()
    nodo.ejecutar()
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()