import aiohttp
import asyncio
from aiohttp import web

# Leer un sito web y extraer su HTML

async def fetch(session, url): # Creanis una función que se conoce como Fetching para leer el contenido HTML de una URL
    async with session.get(url) as response:
        return await response.text() # Hacemos uso de la función .text() para leer el contenido HTML

async def MyScript():
    print('Hola, ¿exactamente a que web deseas leer su HTML?')
    url = input('> ')
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        with open('data.html', 'w') as file:
            file.write(html)
            print("Se ha creado el archivo HTML")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(MyScript())