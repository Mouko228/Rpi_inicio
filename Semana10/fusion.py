import threading 
import queue
import time 

buzon = queue.Queue()

try: 
    def cerebro():
        comando = f"<M1:80>"
        while True:
            buzon.put(comando)
            time.sleep(2)
            
    def arduino():
        while True:
            try:
                mensaje = buzon.get(timeout = 1)
                print(mensaje)
            except queue.Empty:
                pass

    t1 = threading.Thread(target = cerebro)
    t2 = threading.Thread(target = arduino)
    
    t1.start()
    t2.start()
    
            
except KeyboardInterrupt:
    print("el usuario ha detenido esta sesion")
    