import serial
import time

PUERTO = '/dev/ttyACM0'
BAUD = 9600

try: 
    arduino = serial.Serial(PUERTO, BAUD, timeout = 1)
    time.sleep(2)
    print(f"Conectado a {PUERTO}")
    
    while True:
        opc = input("F) Forward\nB) Backward\nS) Stop\n").upper()
        
        arduino.reset_input_buffer()
        
        arduino.write(opc.encode())
        
        time.sleep(0.1)
        
        if arduino.in_waiting > 0:
            respuesta = arduino.readline().decode('utf-8', errors='ignore').strip()
            print(f"respuesta recibida: {respuesta}")

except serial.SerialException:
    print("Error en el serial, no se puede conectar")

except KeyboardInterrupt:
    print("Cancelado por usuario, cerrando...")
    
    if 'arduino' in locals():
        arduino.close() 
