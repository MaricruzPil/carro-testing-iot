# routes/obstaculo_routes.py
from flask import Blueprint
from controllers.obstaculo_controller import ObstaculoController
 
obstaculo_bp = Blueprint('obstaculo_bp', __name__)
 
obstaculo_bp.route(
    '/api/obstaculo',
    methods=['POST']
)(ObstaculoController.registrar_obstaculo)
 
obstaculo_bp.route(
    '/api/obstaculo/ultimo',
    methods=['GET']
)(ObstaculoController.obtener_ultimo_obstaculo)