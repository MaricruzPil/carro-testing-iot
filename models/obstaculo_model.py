# models/obstaculo_model.py
from database.connection import Database
 
class ObstaculoModel:
 
    @staticmethod
    def registrar_obstaculo(
        id_dispositivo,
        id_telemetria,
        nombre_estatus,
        distancia_cm,
        observaciones
    ):
        connection = Database.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.callproc(
                    'sp_registrar_obstaculo',
                    (id_dispositivo, id_telemetria,
                     nombre_estatus, distancia_cm, observaciones)
                )
                connection.commit()
                return True
        finally:
            connection.close()
 
    @staticmethod
    def obtener_ultimo_obstaculo():
        connection = Database.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT o.*, e.nombre_estatus
                    FROM obstaculos_registrados o
                    JOIN cat_estatus_obstaculo e
                      ON o.id_estatus = e.id_estatus
                    ORDER BY o.fecha_registro DESC
                    LIMIT 1
                """)
                return cursor.fetchone()
        finally:
            connection.close()