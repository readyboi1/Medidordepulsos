#Imports para la graficadora en tiempo real
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

#Import para obtener la hora actual
from datetime import date, datetime

#Import para utilizar el puerto serial del ARDUINO
import serial

plt.style.use('ggplot') #Estilo de la gráfica

x_data=[] #Arreglo de la hora
y_data=[] #Arreglo de los pulsos
port = serial.Serial('COM4',9600) #Puerto serial del Arduino

figure=pyplot.figure()
line,=pyplot.plot_date(x_data,y_data,'-') #Linea para los gráficos

#Función para meter los datos en la gráfica
def grafica(frame):
    x_data.append(datetime.now()) #En el eje x va a ir el momento en el que leemos el dato
    #Leemos la variable del puerto serial y lo decodificamos en código ascii
    pulsoStr=port.readline().decode('ascii')
    #Hacemos un casteo de un string a int
    pulso=int(pulsoStr)
    #Agregamos el pulso que es un entero al array de los datos del eje 'y'
    y_data.append(pulso) 
    line.set_data(x_data,y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line, #Devuelve la información de la posición del gráfico

#Vamos a estar llamando la función para graficar datos cada 1 segundo
animacion= FuncAnimation(figure, grafica, interval=1000)
pyplot.show()