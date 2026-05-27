from flask import request, jsonify
from models.movimiento_model import MovimientoModel

class MovimientoController:

    @staticmethod
    def actualizar_parametro():

        data = request.json

        clave = data['clave']
        valor = data['valor']

        MovimientoModel.actualizar_parametro(
            clave,
            valor
        )

        return jsonify({
            "success": True,
            "message": "Parámetro actualizado"
        })

    @staticmethod
    def obtener_ultimo_movimiento():

        result = MovimientoModel.obtener_ultimo_movimiento()

        return jsonify({
            "success": True,
            "data": result
        })

    @staticmethod
    def registrar_movimiento():

        data = request.json

        MovimientoModel.registrar_movimiento(
            data['id_movimiento'],
            data['id_dispositivo'],
            data['id_telemetria'],
            data['origen']
        )

        return jsonify({
            "success": True,
            "message": "Movimiento registrado"
        })