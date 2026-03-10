import serial 
import time

PUERTO = '/dev/ttyACM0'
BAUD = 9600

try: 
    #arduino guarda el objeto serial serial.Serial(puerto, baudrate, cuanto tiempo de espera de contestación tiene el master)
    arduino = serial.Serial(PUERTO, BAUD, timeout = 0.3)
    time.sleep(2)
    print(f"Conectado a {PUERTO}")

    while True:
        comando = input("Escribe 1 (ON) o 0 (OFF): ")

        # Enviar comando
        # .encode() convierte texto a bytes (necesario para enviar)
        arduino.write(comando.encode()) 
        
        time.sleep(0.1)
        
        # Leer respuesta del Arduino (si la hay)
        #in_waiting revisa el buffer, en donde se guardan temporalmente el mensaje que biene de serial
        if arduino.in_waiting > 0:
            #readline(): lee lo que esta en el buffer, los bytes que llegaron del serial
            #decode(): decodifica con el sistema que tu quieras, en este caso utf-8
            #.strip(): lee el mensaje y checa si no hay espacios o backspaces en el inicio o final que sean invisibles, y los borra
            respuesta = arduino.readline().decode('utf-8').strip()
            print(f"Respuesta recibida: {respuesta}")
        
       
        
            
except serial.SerialException:
    print("ERROR: No se pudo conectar. Verifica el puerto o los permisos.")

except KeyboardInterrupt:
    print("\nCerrando conexión...")
    #locals() guarda todas las variables u objetos que se crearon en el codigo 
    
    if 'arduino' in locals():
        #deja de usar el puerto usb de arduino
        arduino.close()


