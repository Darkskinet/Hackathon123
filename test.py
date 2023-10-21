import websockets
import threading
import asyncio


async def hello(websocket, path):
    async for data in websocket:
        print(f"Received: '{data}'")
        await websocket.send(data)


def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    ws_server = websockets.serve(hello, 'localhost', 8899)

    loop.run_until_complete(ws_server)
    loop.run_forever()  # this is missing
    loop.close()


async def send_receive_message(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send('This is some text.')
        reply = await websocket.recv()
        print(f"The reply is: '{reply}'")


def client():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_receive_message('ws://localhost:8899'))
    loop.close()


if __name__ == "__main__":
    # daemon server thread:
    server = threading.Thread(target=between_callback, daemon=True)
    server.start()
    client = threading.Thread(target=client)
    client.start()
    client.join()
