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
    grafi,basura=datos.split("\r\n")
    print(grafi)
    #print(basura)
    
    plt.scatter(datetime.now(),grafi)
    #plt.scatter(datetime.now(),float(data.decode()))
    plt.show()
    plt.pause(0.0001)


