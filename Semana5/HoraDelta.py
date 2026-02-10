import time

inicio = time.time()

try: 
    while True: 
        actual = time.time()
        tiempo = actual - inicio
        
        if (tiempo > 2):
            print("Hola!")
            inicio = time.time()

except KeyboardInterrupt:
    print("Codigo interrumpido por el usuario")