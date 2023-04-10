from aiohttp import web
import json
from aiohttp_jinja2 import render_template, setup
import os
import jinja2
from pymongo import MongoClient
from bson import ObjectId


TEMPLATE_DIR = os.path.join(os.getcwd(), 'templates')

route = web.RouteTableDef()

connect = MongoClient(host='localhost', port=27017,
                      connect=True)  # Nos conectamos a MongoDB
db = connect['registro_aiohttp']  # Creamos la base de datos
coleccion_usuarios = db['usuarios']  # Creamos la colección
@route.get('/')
async def index(request):
    return render_template('registrar_usuarios.html', request, {

    })
@route.post('/registrar')
@route.get('/registrar')
async def registrar(request):
    if request.method == 'POST':
        datos = await request.json()
        if not "" in datos.values():  # Si los datos no vienen vacios o no falta algún dato del input, entonces agregamos el usuario de lo contario se mostrará el error 400
            usuario = {
                "nombre": datos["nombre"],
                "apellido": datos["apellido"],
                "edad": datos["edad"],
                "email": datos["email"]
            }
            coleccion_usuarios.insert_one(usuario)
            return web.Response(text=json.dumps({"msg": "El usuario ha sido agregado satisfactoriamente"}), status=200)
    return web.Response(text=json.dumps({"msg": "Error, no se ha recibido ningun dato"}), status=400)

@route.get('/usuarios_json')
async def usuarios_json(request):
    usuarios = []
    for usuario in coleccion_usuarios.find():
        usuarios.append({
            '_id': str(ObjectId(usuario['_id'])),
            "nombre": usuario['nombre'],
            "apellido": usuario['apellido'],
            "edad": usuario['edad'],
            "email": usuario['email']
        })
    return web.Response(text=json.dumps({"usuarios": usuarios}), content_type="json")
app = web.Application()
setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
app.add_routes(route)

if __name__ == '__main__':
    web.run_app(app, host='localhost')