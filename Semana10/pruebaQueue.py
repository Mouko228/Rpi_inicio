import queue

# 1. Instanciamos el buzón
mi_buzon = queue.Queue()

# 2. Metemos 3 misiones (El orden de entrada importa)
mi_buzon.put("Misión 1: Encender motores")
mi_buzon.put("Misión 2: Avanzar")
mi_buzon.put("Misión 3: Frenar")

print(f"Tamaño de la fila: {mi_buzon.qsize()} misiones pendientes\n")

# 3. Las sacamos (Saldrán exactamente en el orden en que entraron)
print("Ejecutando:", mi_buzon.get())
print("Ejecutando:", mi_buzon.get())

print(f"\nTamaño restante: {mi_buzon.qsize()} misión pendiente")

print("Ejecutando:", mi_buzon.get())
