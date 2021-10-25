import serial
import matplotlib.pyplot as plt
import numpy as np
from datetime import date, datetime

plt.ion()
fig=plt.figure()

i=0
x=list()
y=list()
i=0

port= serial.Serial('COM4',9600)
port.close()
port.open()

while True:
    data=port.readline()
    print(data.decode())
    x.append(datetime.now())
    y.append(data.decode())
    datos=data.decode()
    #grafi almacena los datos que necesitas,solo enteros, mientras que basura, es como dice
    #Solo almacena la parte "\r\n" del string generado por linea
    grafi,basura=datos.split("\r\n")
      
    plt.scatter(datetime.now(),grafi)
    #plt.scatter(datetime.now(),float(data.decode()))
    plt.show()
    plt.pause(0.0001)


