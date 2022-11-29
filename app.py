from flask import Flask, jsonify, render_template, request
import websockets
import asyncio
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Left')
def turnLeft():
    async def mcontrol():
        async with websockets.connect("ws://localhost:6316") as websocket:
          await websocket.send("left")
    asyncio.run(mcontrol())
    return "left"

@app.route('/Right')
def turnRight():
    async def mcontrol():
        async with websockets.connect("ws://localhost:6316") as websocket:
          await websocket.send("right")
    asyncio.run(mcontrol())
    return "right"

@app.route('/Forwards')
def forwards():
    async def mcontrol():
        async with websockets.connect("ws://localhost:6316") as websocket:
          await websocket.send("forwards")
    asyncio.run(mcontrol())
    return "forwards"

@app.route('/Backwards')
def backwards():
    async def mcontrol():
        async with websockets.connect("ws://localhost:6316") as websocket:
          await websocket.send("backwards")
    asyncio.run(mcontrol())
    return "backwards"

@app.route('/STOP')
def stop():
    async def mcontrol():
        async with websockets.connect("ws://localhost:6316") as websocket:
          await websocket.send("STOP")
    asyncio.run(mcontrol())
    return "STOP"

if __name__ == '__main__':
   app.run()