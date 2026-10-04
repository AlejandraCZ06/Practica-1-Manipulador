import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alejandra/Practica 1 Manipulador/ros2_ws/install/industrial_routines'
