import threading
import time 

try:
    def funcionA():
        while True:
            print("Radar escaneando...")
            time.sleep(1)

    def funcionB():
        while True:
            print("Calculando IA")
            time.sleep(3)
        
    t1 = threading.Thread(target = funcionA)
    t2 = threading.Thread(target = funcionB)

    t1.start()
    t2.start()
    

except KeyboardInterrupt:
    print("el usuario ha interrumpido la operacion")