#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket):
    direction = await websocket.recv()
    match direction:
        case "left":
            explorerhat.motor.one.forward()
            explorerhat.motor.two.backward()
        case "right":
            explorerhat.motor.one.backward()
            explorerhat.motor.two.forward()
        case "forwards":
            explorerhat.motor.forward()
        case "backwards":
            explorerhat.motor.backward()
        case "brake":
            explorerhat.motor.stop()
        case _:
            print("direction not valid")
async def main():
    async with websockets.serve(hello, "127.0.0.1", 6316):
        await asyncio.Future()  # run forever



if __name__ == "__main__":
    asyncio.run(main())