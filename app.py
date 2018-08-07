import asyncio
import websockets

async def hello(websocket, path):
    await websocket.send("Hello World!!")

port = int(os.getenv('PORT', 5687))
start_server = websockets.serve(hello, '', port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
