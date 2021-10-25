import matplotlib.pyplot as plt
from datetime import date, datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange

plt.style.use('ggplot') #Estilo de la gráfica

x_data=[] #Arreglo de datos 
y_data=[]

figure=pyplot.figure()
line,=pyplot.plot_date(x_data,y_data,'-') #Linea para los gráficos

#Función para meter los datos en la gráfica
def grafica(frame):
    x_data.append(datetime.now()) #En el eje x va a ir el momento en el que leemos el dato
    y_data.append(randrange(0,100)) #Un número aleatorio entre 0 y 100, para el proyecto leeremos los datos del arduino
    #y_data.append(port.readline())
    line.set_data(x_data,y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line, #Devuelve la información de la posición del gráfico

animacion= FuncAnimation(figure, grafica, interval=1000)
pyplot.show()
