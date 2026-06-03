import sys
import termios
import tty

def leer_tecla_linux():
    # 1. Guarda la configuración actual de tu terminal shuji@star
    config_original = termios.tcgetattr(sys.stdin)
    try:
        # 2. Cambia la terminal a modo "raw" (captura en bruto)
        tty.setraw(sys.stdin.fileno())
        # 3. Lee un solo carácter del flujo del teclado
        tecla = sys.stdin.read(1)
        return tecla
    finally:
        # 4. Pase lo que pase, devuelve la terminal a la normalidad al terminar
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, config_original)

def traducir_comando(tecla):
    if tecla.lower() == 'w':
        return "<M1:100,M2:100>"  # Avanzar
    elif tecla.lower() == 's':
        return "<M1:-100,M2:-100>" # Retroceder
    return "<M1:0,M2:0>"

print("SISTEMA LISTO. Presiona letras para probar (Presiona 'q' para salir):")
while True:
    tecla_activa = leer_tecla_linux()
    
    # Salida de emergencia si presionas 'q'
    if tecla_activa.lower() == 'q':
        print("\r\nSaliendo del simulador...")
        break
        
    # Fase 2 en acción
    trama_serial = traducir_comando(tecla_activa)
    print(f"\rTecla: {tecla_activa} -> Trama generada: {trama_serial}            ", end="")