from flask import Flask
from flask_cors import CORS
from routes.movimiento_routes import movimiento_bp
from routes.obstaculo_routes import obstaculo_bp
from services.websocket_service import WebSocketServer


import threading


app = Flask(__name__)
CORS(app)

app.register_blueprint(movimiento_bp)
app.register_blueprint(obstaculo_bp)

if __name__ == '__main__':

    websocket_thread = threading.Thread(
        target=WebSocketServer.start
    )

    websocket_thread.daemon = True
    websocket_thread.start()

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )