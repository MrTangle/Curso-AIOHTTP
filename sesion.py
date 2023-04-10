import asyncio
import aiohttp

async def holaMundo():

    async with aiohttp.ClientSession() as session:

        while True:
            websocket = await session.ws_connect("wss://echo.websocket.org") # Nos conectamos al socket de websocket.org

            await websocket.send_str("¡Hola Mundo :D!") # Enviamos nuestro mensaje al socket
            
            respuesta = await websocket.receive() # Con .receive() recibimos la respuesta del socket la cual es un objeto

            respuesta_data = respuesta.data # Con el método .data accedemos solamente al mensaje que nos está enviando el socket

            print("Recibido: ", respuesta_data)

            await websocket.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(holaMundo())