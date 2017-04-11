SaldoBIP-ApiREST
=============================================================
**Api REST** para consultar el saldo de la tarjeta BIP.
Aplicación hecha bajo el Framework Python **Flask**.

## Descripción

Esta aplicación se conecta con el AFT de transantiago para verificar el saldo de una tarjeta BIP.

## Funcionamiento General

Esta **API REST** tiene la finalidad de entregar el saldo de una tarjeta BIP, esta aplicación para obtener el saldo utiliza **Scraping**.

Esta API manda una solicitud POST a http://pocae.tstgo.cl/PortalCAE-WAR-MODULE/SesionPortalServlet con los siguientes datos de formulario:

```
accion=6
NumDistribuidor=99
NomUsuario=usuInternet
NomHost=AFT
NomDominio=aft.cl
RutUsuario=0
NumTarjeta=numero_tarjeta (este parametro depende del número de tarjeta).
bloqueable=0
```

Luego de realizar la solicitud POST se recibe una página en HTML, esta es parseada buscando los siguientes tag HTML:
```
<td bgcolor="#B9D2EC" class="verdanabold-ckc"></td>
```
Esta página contiene dos tag exactamente iguales, en uno de ellos se encuentra el saldo de la tarjeta BIP y en el otro se encuentra la fecha del saldo.

Finalmente, se devuelve un **JSON** con la fecha y el saldo de la tarjeta.


## Documentación API

La documentación de la API se encuentra disponible en: http://saldobip.yasserisa.com/

En la carpeta **/Documentacion/apidoc** se encuentran todas las fuentes HTML de la documentación de la API, esta documentación es generada automáticamente con la herramienta **apidoc**. En la carpeta **/Documentacion** se encuentran los archivos de configuración para generar la documentación en HTML. 

### apidoc
=============================================================

#### Instalación
```
# npm install apidoc -g
```

#### Ejecución
```
$ apidoc -i SaldoBIP-ApiREST/Documentacion/ -o SaldoBIP-ApiREST/Documentacion/apidoc/

```

Instalar Dependencias de API REST
---------------------
```
# pip install -r requirements.txt
```
Ejecucion de la API
------------------------------------
```
# python bip.py
```
Comentarios Generales
------------------------------------

## Deploy en Heroku

```
http://saldobip-apirest.herokuapp.com/
```


### Ejemplo de consulta de saldo

 ```
 curl http://saldobip.yasser.pro/v1/tarjetas/54545454/saldo
 ```
 o
 
```
curl http://saldobip-apirest.herokuapp.com/v1/tarjetas/54545454/saldo
```

Resultado:

```
{
  "error": "Corrobore si el numero de su tarjeta existe, si esta correcto, consulte con un centro BIP!"
}
```
Header HTTP
```
HTTP/1.1 404 NOT FOUND
```
