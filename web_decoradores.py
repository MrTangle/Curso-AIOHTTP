from aiohttp import web

route = web.RouteTableDef()  # Creamos una instancia para la ruta

@route.get('/') # decoramos la función con la ruta para indicarle a python que la función de abajo pertenece a esta ruta
async def index(request):
    return web.Response(
        text="""\
<h1>Mensaje en texto HTML de varias lineas desde el backend</h1>
<h2>Esto es una linea de texto</h2>
<h3>Esto es otra linea de texto</h3>
""",  # Colocamos \ para indicarle a python que debe ignorar esa linea y comenzar a leer desde la siguiente
        content_type="text/html"
    )

app = web.Application()  # Instanciamos la app
app.add_routes(route) # Agregamos las rutas


if __name__ == '__main__':
    web.run_app(app, host='localhost')