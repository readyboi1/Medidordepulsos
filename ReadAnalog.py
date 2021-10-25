#Serial nos permite traernos los datos del Arduino al Python, necesita instalarse con "pip install pyserial"
import serial 
import time

#Configuración del puerto serial
port = serial.Serial('COM4',9600)
while port.available():  #Se ejecutará mientras el puerto este disponible
  value = port.readline() #Lectura del valor del puerto
  print(value) 
  time.sleep(0.5) 