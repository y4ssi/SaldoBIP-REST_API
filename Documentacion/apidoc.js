/**
* @api {get} /tarjetas/{numero_tarjeta}/saldo
* @apiGroup Consulta Saldo
* @apiDescription Por medio de los servidores del AFT se obtiene el saldo y la fecha del saldo de la tarjeta BIP ingresada por el usuario
*
*
*
* @apiParam {Int} numero_tarjeta Número de tarjeta BIP.
*
* @apiSuccess (200) {json} Fecha DD/MM/YYYY HH:MM.
* @apiSuccess (200) {json} Saldo $.
* @apiSuccessExample {json} Respuesta Exitosa:
* HTTP/1.1 200 OK
* {
*	"Fecha": "04/05/2015 09:27", 
*	"Saldo": "$-220"
* }
* 
* @apiError 404 <code>numero_tarjeta</code> no encontrado o con problemas.
* @apiErrorExample {json} No encontrado:
* HTTP/1.1 404 Not found
* { 
*	"error": "Corrobore si el numero de su tarjeta existe, si esta correcto, consulte con un centro BIP!"
* }
* @apiError 405 Método HTTP no permitido.
* @apiErrorExample {json} No Permitido:
* HTTP/1.1 405 Method Not Allowed
* { 
*	"error": "Metodo HTTP no permitido"
* }
* @apiError 400 URL Mal formada.
* @apiErrorExample {json} Tarjeta mal Ingresada:
* HTTP/1.1 400 Bad Request
* { 
*	"error": "Ingrese un numero correcto de tarjeta BIP!"
* }
*/
