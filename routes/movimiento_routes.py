from flask import Blueprint
from controllers.movimiento_controller import MovimientoController

movimiento_bp = Blueprint(
    'movimiento_bp',
    __name__
)

movimiento_bp.route(
    '/api/parametro',
    methods=['PUT']
)(
    MovimientoController.actualizar_parametro
)

movimiento_bp.route(
    '/api/movimiento/ultimo',
    methods=['GET']
)(
    MovimientoController.obtener_ultimo_movimiento
)

movimiento_bp.route(
    '/api/movimiento',
    methods=['POST']
)(
    MovimientoController.registrar_movimiento
)