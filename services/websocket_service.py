import socket
import threading
import base64
import hashlib
import json
import time

from models.movimiento_model import MovimientoModel
from decimal import Decimal


class WebSocketServer:

    GUID = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

    @staticmethod
    def start(host='0.0.0.0', port=8765):

        server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        # IMPORTANTE PARA WINDOWS
        server.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        server.bind((host, port))

        server.listen(5)

        print(f'WebSocket iniciado en {host}:{port}')

        while True:

            client, addr = server.accept()

            print(f'Cliente conectado: {addr}')

            threading.Thread(
                target=WebSocketServer.handle_client,
                args=(client,)
            ).start()

    @staticmethod
    def handle_client(client):

        try:

            request = client.recv(1024).decode()

            key = None

            for line in request.split('\r\n'):

                if 'Sec-WebSocket-Key' in line:

                    key = line.split(': ')[1]

            if not key:
                client.close()
                return

            accept_key = base64.b64encode(
                hashlib.sha1(
                    (key + WebSocketServer.GUID).encode()
                ).digest()
            ).decode()

            response = (
                'HTTP/1.1 101 Switching Protocols\r\n'
                'Upgrade: websocket\r\n'
                'Connection: Upgrade\r\n'
                f'Sec-WebSocket-Accept: {accept_key}\r\n\r\n'
            )

            client.send(response.encode())

            ultimo_id = -1

            while True:

                movimiento = MovimientoModel.obtener_ultimo_movimiento()

                if movimiento:

                    # Detecta nuevos registros
                    if movimiento['id_registro'] != ultimo_id:

                        ultimo_id = movimiento['id_registro']

                        for key, value in movimiento.items():

                            # Convertir datetime
                            if hasattr(value, 'isoformat'):

                                movimiento[key] = value.isoformat()

                            # Convertir Decimal
                            elif isinstance(value, Decimal):

                                movimiento[key] = float(value)

                        data = json.dumps({
                            "success": True,
                            "data": movimiento
                        })

                        WebSocketServer.send_message(
                            client,
                            data
                        )

                        print("Mensaje enviado")

                time.sleep(1)

        except Exception as e:

            print(f'Error WebSocket: {e}')

        finally:

            client.close()

    @staticmethod
    def send_message(client, message):

        encoded = message.encode()

        frame = bytearray()

        frame.append(129)

        length = len(encoded)

        if length <= 125:

            frame.append(length)

        elif length <= 65535:

            frame.append(126)

            frame.extend(
                length.to_bytes(2, 'big')
            )

        else:

            frame.append(127)

            frame.extend(
                length.to_bytes(8, 'big')
            )

        frame.extend(encoded)

        client.send(frame)

        if __name__ == '__main__':
            WebSocketServer.start()