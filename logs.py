from aiohttp import web
import jinja2
from aiohttp_jinja2 import render_template, setup
import os
import logging

TEMPLATE_DIR = os.path.join(os.getcwd(), 'templates')

route = web.RouteTableDef()

@route.get('/')
def index(request):
    x = 2/0
    return render_template('formulario_asincrono.html', request, {

    })

app = web.Application()
logging.basicConfig(level=logging.DEBUG, filename="registro.log")

app.add_routes(route)
setup(app, loader=jinja2.FileSystemLoader(str(TEMPLATE_DIR)))

if __name__ == '__main__':
    web.run_app(app, host='localhost')