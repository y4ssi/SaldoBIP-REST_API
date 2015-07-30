# -*- coding: utf-8 -*-

# Importamos librerías necesarias
import requests
import re
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.errorhandler(405)
def page_not_found(e):
    '''
    Function: page_not_found
    Summary: En caso de usar un método diferente al GET, mostramos error
    Attributes:
        @param (e):exceptions
    Returns: json response
    '''
    response = jsonify({'error': 'Metodo HTTP no permitido'})
    response.status_code = 405
    return response


@app.route('/v1/tarjetas/<numero_tarjeta>/saldo', methods=['GET'])
def consulta_saldo(numero_tarjeta):
    '''
    Function: consulta_saldo
    Summary: Se recibe el número de BIP via URL y consulta el saldo con AFT
    Examples: GET HTTP/1.1 /tarjetas/30303030/saldo
    Attributes:
        @param (numero_tarjeta):unicode
    Returns: json response
    '''
    # Verificamos si el número de tarjetas es un entero, en caso
    # contrario devolvemos error
    try:
        int(numero_tarjeta)
    except:
        response = jsonify({'error': ('Ingrese un numero correcto de '
                                      'tarjeta BIP!')})
        response.status_code = 400
        return response

    # Preparamos los datos para realizar la consulta de saldo, con el sistema
    # oficial de la tarjeta BIP
    url_consulta = ('http://pocae.tstgo.cl/PortalCAE-WAR-MODULE'
                    '/SesionPortalServlet')
    data_form = {'accion': '6',
                 'NumDistribuidor': '99',
                 'NomUsuario': 'usuInternet',
                 'NomHost': 'AFT',
                 'NomDominio': 'aft.cl',
                 'RutUsuario': '0',
                 'NumTarjeta': numero_tarjeta,
                 'bloqueable': '0'
                 }
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    # Mandamos una solicitud POST a la pagina de consulta de
    # saldo de la tarjeta BIP
    r = requests.post(url_consulta, data=data_form, headers=headers)

    '''
    Recibimos la respuesta del servidor (Pagina HTML) y verificamos si existe
    saldo, en caso contrario devolvemos un mensaje de error. Si la consulta es
    efectiva parseamos el texto HTML para buscar el saldo de la tarjeta y la
    fecha del saldo
    '''

    if '<td bgcolor="#B9D2EC" class="verdanabold-ckc">$' in r.text:
        saldo_check = re.findall(('<td bgcolor="#B9D2EC"'
                                  ' class="verdanabold-ckc">(.*?)</td>'),
                                 r.text, re.DOTALL
                                 )
        if saldo_check:

            # Devolvemos el saldo de la tarjeta y su fecha
            return jsonify({'Saldo': saldo_check[0],
                            'Fecha': saldo_check[1]})

    # En caso de no obtener el saldo devolvemos error
    else:
        response = jsonify({'error': ('Corrobore si el numero de su tarjeta'
                                      ' existe, '
                                      'si esta correcto, '
                                      'consulte con un centro BIP!')})
        response.status_code = 404
        return response

# Inicializamos un servidor web en el puerto 80 (puerto por defecto 5000)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=True)
