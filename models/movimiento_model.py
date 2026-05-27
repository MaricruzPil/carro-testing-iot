from database.connection import Database

class MovimientoModel:

    @staticmethod
    def actualizar_parametro(clave, valor):

        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:

                cursor.callproc(
                    'sp_actualizar_parametro',
                    (clave, valor)
                )

            connection.commit()

            return True

        finally:
            connection.close()

    @staticmethod
    def obtener_ultimo_movimiento():

        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:

                cursor.callproc(
                    'sp_obtener_ultimo_movimiento'
                )

                result = cursor.fetchone()

                return result

        finally:
            connection.close()

    @staticmethod
    def registrar_movimiento(
        id_movimiento,
        id_dispositivo,
        id_telemetria,
        origen
    ):

        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:

                cursor.callproc(
                    'sp_registrar_movimiento',
                    (
                        id_movimiento,
                        id_dispositivo,
                        id_telemetria,
                        origen
                    )
                )

            connection.commit()

            return True

        finally:
            connection.close()