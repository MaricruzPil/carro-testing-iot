# controllers/obstaculo_controller.py
from flask import request, jsonify
from models.obstaculo_model import ObstaculoModel
 
class ObstaculoController:
 
    @staticmethod
    def registrar_obstaculo():
        data = request.json
        ObstaculoModel.registrar_obstaculo(
            data['id_dispositivo'],
            data.get('id_telemetria', None),
            data['nombre_estatus'],
            data['distancia_cm'],
            data.get('observaciones', 'Lectura sensor ultrasónico')
        )
        return jsonify({"success": True, "message": "Obstáculo registrado"})
 
    @staticmethod
    def obtener_ultimo_obstaculo():
        result = ObstaculoModel.obtener_ultimo_obstaculo()
        return jsonify({"success": True, "data": result})