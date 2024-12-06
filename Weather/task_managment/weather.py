import requests
from task_managment.decorators import log_function_call

@log_function_call
def obtener_clima(latitud, longitud):
    """
    Obtiene el clima actual de una ubicación específica usando la API de Open-Meteo.
    :param latitud: Latitud de la ubicación.
    :param longitud: Longitud de la ubicación.
    :return: Diccionario con la información del clima.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperatura": data["current_weather"]["temperature"],
            "viento": data["current_weather"]["windspeed"],
            "descripcion": data["current_weather"]["weathercode"]
        }
    else:
        raise Exception(f"Error al obtener el clima: {response.status_code}")
