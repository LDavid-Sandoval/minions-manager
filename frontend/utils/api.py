import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

class ApiClient:
    
    @staticmethod
    def get(endpoint: str):
        """Realiza una petición GET al backend"""
        try:
            response = requests.get(f"{API_URL}{endpoint}")
            response.raise_for_status() # Lanza error si no es 200 OK
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    @staticmethod
    def post(endpoint: str, data: dict):
        """Realiza una petición POST al backend"""
        try:
            response = requests.post(f"{API_URL}{endpoint}", json=data)
            # Si el backend devuelve error (ej: 400 Bad Request), retornamos el detalle
            if response.status_code >= 400:
                return {"error": response.json().get("detail", "Error desconocido")}
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}