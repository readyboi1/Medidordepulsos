import smtplib
from decouple import config
message='Hola esto es un mensaje de prueba'
server= smtplib.SMTP('smtp.live.com',587) #Servidor de correos a utilizar (outlook) y puerto por defecto
server.starttls()

#Autenticación del correo
server.login('CORREO DE QUIEN ENVÍA','CONTRASEÑA')

server.sendmail('Correo remitente','Correo destinatario',message)

server.quit()

print('Mensaje enviado con éxito!!!')

