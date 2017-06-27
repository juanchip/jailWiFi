# -*- coding: utf-8 -*-
import os  #librería que vamos a usar para controlar comandos de sistema.
import checkInternet #Clase externa para chequear internet con la Web de Google
import time  #Librería para controlar el sleep.

# Aquí escribimos el tipo de antena, como la mía está basada en un chip Atheros
# le escribo 'ath' como filtro para obtener el Device ID, que mas adelante se 
# usará para establecer el dispositivo que vamos a reiniciar

ant = "'ath'"

# Lee el listado de dispositivos y los almacena en archivos temporales
os.system("lsusb -t | grep " + ant + "  | cut -d ',' -f 1 | cut -d 'v' -f 2 > tmp")
os.system("lsusb -t | grep " + ant + " | cut -d ':' -f 1 | cut -d 't' -f 2 > tnp")

devID = open('tmp','r').read().split(' ')
portID= open('tnp','r').read().split(' ')

# Un filtrado del \n que quedó dando vueltas

dev = devID[1].split()
port = portID[1].split()

print 'ID Antenna '+str(dev[0])
print 'Port Antenna ' +str(port[0])

print 'Verificando Conexión a internet' 


if checkInternet.internet_on() == True:
	print 'Hay internet, no se aplica Reset'
else:
	print 'No hay internet, se aplica Reset'
	os.system('sudo ./usbreset /dev/bus/usb/001/0'+str(dev[0]))
	print 'espere 10 segundos para reconexión automática de internet'
	time.sleep(10)
	if checkInternet.internet_on() == True:
		print 'Internet recuperado'
	else:
		print 'Internet NO recuperado, reintente el script'

#Eliminando los archivos temporales creados	
os.system('rm -r tmp')
os.system('rm -r tnp')
