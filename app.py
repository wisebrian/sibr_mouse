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
        async with websockets.connect("ws://127.0.0.1:6316") as websocket:
          await websocket.send("left")
    asyncio.run(mcontrol())
    return "left"

@app.route('/Right')
def turnRight():
    async def mcontrol():
        async with websockets.connect("ws://127.0.0.1:6316") as websocket:
          await websocket.send("right")
    asyncio.run(mcontrol())
    return "right"

@app.route('/Forwards')
def forwards():
    async def mcontrol():
        async with websockets.connect("ws://127.0.0.1:6316") as websocket:
          await websocket.send("forwards")
    asyncio.run(mcontrol())
    return "forwards"

@app.route('/Backwards')
def backwards():
    async def mcontrol():
        async with websockets.connect("ws://127.0.0.1:6316") as websocket:
          await websocket.send("backwards")
    asyncio.run(mcontrol())
    return "backwards"

@app.route('/Brake')
def brake():
    async def mcontrol():
        async with websockets.connect("ws://127.0.0.1:6316") as websocket:
          await websocket.send("brake")
    asyncio.run(mcontrol())
    return "brake"

if __name__ == '__main__':
   app.run(host='0.0.0.0')