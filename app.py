import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

port = int(os.getenv('PORT', 5687))
start_server = websockets.serve(hello, '', port, klass=HttpWSSProtocol)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
