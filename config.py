import os

DB_HOST     = os.environ.get("DB_HOST", "instancia-iot.caz0nbt6kzyw.us-east-1.rds.amazonaws.com")
DB_USER     = os.environ.get("DB_USER", "admin")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "Admin12345#!")
DB_NAME     = os.environ.get("DB_NAME", "carrito_iot")

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 5000))