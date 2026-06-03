import sys
import termios
import tty
import threading
import time

ultima_vez_presionada = 0
tecla_actual = None
corriendo = True

def leer_tecla_linux():
    config_original = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, config_original)

def watchdog_soltar_tecla():
    global ultima_vez_presionada, tecla_actual, corriendo
    
    while corriendo:
        # Si hay una tecla activa, revisamos cuánto tiempo ha pasado en silencio
        if tecla_actual is not None:
            tiempo_en_silencio = time.time() - ultima_vez_presionada
            
            # Si el silencio es mayor a 0.15 segundos, significa que soltó la tecla
            if tiempo_en_silencio > 0.15:
                print(f"\r[EVENTO]: TECLA SOLTADA ({tecla_actual.upper()}) -> <M1:0,M2:0>               ", end="", flush=True)
                tecla_actual = None # Reseteamos el estado a "ninguna tecla"
                
        time.sleep(0.02) # Pequeño descanso para no saturar el procesador de tu servidor

hilo_vigilante = threading.Thread(target=watchdog_soltar_tecla, daemon=True)
hilo_vigilante.start()

print("Mantén presionada una tecla (W,A,S,D). Suéltala para ver el freno.")
print("Presiona 'q' para salir.\n")

while True:
    tecla = leer_tecla_linux()
    
    if tecla.lower() == 'q':
        corriendo = False
        print("\r\nSaliendo...")
        break
        
    # Validamos que sea una tecla de control válida
    if tecla.lower() in ['w', 's', 'a', 'd']:
        # Actualizamos el reloj con el milisegundo exacto de la pulsación
        ultima_vez_presionada = time.time()
        
        # Si es una tecla nueva o continuación, imprimimos que se mantiene presionada
        if tecla_actual != tecla:
            tecla_actual = tecla
            print(f"\r[EVENTO]: TECLA PRESIONADA ({tecla.upper()}) -> Generando movimiento...", end="", flush=True)