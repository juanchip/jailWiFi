# jailWiFi
Script de Python utilizado para reiniciar una Antena WiFi USB que se "colgaba" al pasar cierto tiempo de conexión.

### ¿ Como funciona ?
Por pura vagancia de no levantarme de la silla, hice este script que localiza el devID de la antena y luego realiza una prueba de conexión a internet ingresando a la dirección IP de **Google.com.ar** con un timeout de 1 segundo.

Si la conexión es exitosa, no hace nada ; caso contrario ejecuta un reset en la antena con el devID anteriormente hallado, espera 10 segundos para la reconexión por ///wpa_supplicant/// y nuevamente ejecuta una prueba de conexión.

La salida de esa condición determinará si la acción fue efectiva o no.


### Requisitos
- GCC
- Python 2.7 con urllib2 
- Conocer el driver del dipositivo con $ lsusb -t
```
$ lsusb -t
/:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=dwc_otg/1p, 480M
    |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/5p, 480M
        |__ Port 1: Dev 3, If 0, Class=Vendor Specific Class, Driver=smsc95xx, 480M
        |__ Port 2: Dev 4, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 2: Dev 4, If 3, Class=Audio, Driver=snd-usb-audio, 480M
        |__ Port 2: Dev 4, If 1, Class=Video, Driver=uvcvideo, 480M
        |__ Port 2: Dev 4, If 2, Class=Audio, Driver=snd-usb-audio, 480M
        |__ Port 3: Dev 10, If 0, Class=Vendor Specific Class, ***Driver=ath9k_htc****, 480M

```
### Instalación
Instalar urllib2

``` 
# pip install urllib2
```
Compilar
```
$ cd source

$ gcc resetusb.c -o resetusb

```
Permitirle ejecutarse al archivo de salida
```
chmod +x resetusb
```
Modificar el archivo run.py con el tipo de antena correspondiente

```
$ nano run.py
.
..
...
....
ant = "'ath'" #Reemplezar con el correspondiente driver detectado con lsusb -t
....
...
..
.
```
Ejecutar con privilegios de administrador

```
$sudo python run.py
```
