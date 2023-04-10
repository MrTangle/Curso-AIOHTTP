from aiohttp import web

app = web.Application()
async def index(request):
    return web.Response(
        text="<h1>Mensaje en texto HTML desde el backend</h1>", # Enviamos el texto en HTML
        content_type="text/html" # Le decimos que el tipo de contenido es en HTML
    )

app.add_routes([web.get('/', index)])

if __name__ == '__main__':
    web.run_app(app, host='localhost')