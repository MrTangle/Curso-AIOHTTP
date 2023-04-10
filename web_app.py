from aiohttp import web
from aiohttp_jinja2 import render_template, template, setup
import jinja2
import os

TEMPLATE_DIR = os.path.join(os.getcwd(), 'templates') # Ubicamos el directorio donde guardaremos nuestras plantillas
route = web.RouteTableDef()

@route.get('/')
@template('index.html')
async def index(request):
    return {
        "titulo": "Mi app AIOHTTP",
        "contenido": "Ahora este es un contenido dinámico y es traído desde el back-end hacia el front-end"
    }

@route.get('/contacto')
async def contacto(request):
    return render_template('contacto.html', request, {
        "titulo": "Página Contacto",
        "contenido": "Esta es la página de contacto de mi aplicación"
    })

@route.get('/saludar/{nombre}') # Le decimos que esta url debe recibir un nombre
async def saludar(request):
    nombre = request.match_info.get('nombre', "Anónimo") # Acá le decimos que utilice lo que se encuentra en la variable nombre si existe, de lo contrario usara el string anonimo
    saludo = '<h2>Hola, {}, ¿cómo te encuentras hoy?</h2>'.format(nombre)
    return web.Response(text=saludo, content_type="text/html")

@route.get('/formulario')
@route.post('/formulario') # Con otro decorador del tipo post le decimos que queremos que esta vista acepte peticiones post
async def formulario(request):
    if request.method == 'POST':
        formulario = await request.post()
        nombre = formulario['nombre']
        password = formulario['password']
        print(nombre, password)

    return render_template('formulario.html', request, {

    })

import json

USUARIOS = []

@route.post('/usuarios')
async def formulario(request):
    if request.method == 'POST':
        formulario = await request.post()
        nombre = formulario['nombre']
        password = formulario['password']
        usuario = {
            "nombre": nombre,
            "password": password
        }
        USUARIOS.append(usuario)
        print(USUARIOS)
        return web.Response(text=json.dumps({"msg":"El usuario ha sido agregado correctamente"}), content_type="json")
    
@route.get('/formulario_asincrono')
async def formulario_async(request):
    formulario = await request.post()
    if formulario:
        nombre = formulario['nombre']
        password = formulario['password']

    return render_template('formulario_asincrono.html', request, {

    })

@route.post('/async_usuarios')
async def usuarios(request):
    if request.method == 'POST':
        formulario_asincrono = await request.json() # Obtenemos el objeto json que estamos enviando con fetch desde el front-end
        nombre = formulario_asincrono['nombre']
        password = formulario_asincrono['password']
        usuario = {
            "nombre": nombre,
            "password": password
        }
        USUARIOS.append(usuario)
        print(USUARIOS)
        return web.Response(text=json.dumps({"msg":"El usuario ha sido agregado correctamente"}), content_type="json")

app = web.Application()
setup(app, loader=jinja2.FileSystemLoader(str(TEMPLATE_DIR))) # Le pasamos nuestra app al motor de conexión y luego le decimos la ubicación de nuestras plantillas
app.add_routes(route)

if __name__ == '__main__':
    web.run_app(app, host='localhost')