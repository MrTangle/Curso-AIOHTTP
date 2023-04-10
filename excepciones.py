from aiohttp import web
import jinja2
from aiohttp_jinja2 import render_template, setup
import os
import json

TEMPLATE_DIR = os.path.join(os.getcwd(), 'templates')

route = web.RouteTableDef()


@route.get('/')
async def index(request):
    return render_template('login.html', request, {

    })


@route.post('/login')
@route.get('/login')
async def login(request):
    usuario_registrado = {
        "nombre": "Jose Ramirez",
        "password": "12345"
    }

    error401 = render_template('error401.html', request, {
        "contenido": "Acceso no autorizado, debes estar logueado."
    }).text

    if request.method == 'POST':
        usuario = await request.post()
        nombre = usuario['nombre']
        password = usuario['password']

        if usuario_registrado['nombre'] == nombre and usuario_registrado['password'] == password:
            return web.Response(text=json.dumps({"msg": "Te has logueado correctamente"}), content_type="json")
        else:
            return web.HTTPUnauthorized(text=error401, content_type="text/html")

    return web.HTTPUnauthorized(text=error401, content_type="text/html")


app = web.Application()
app.add_routes(route)
setup(app, loader=jinja2.FileSystemLoader(str(TEMPLATE_DIR)))

if __name__ == '__main__':
    web.run_app(app, host='localhost')