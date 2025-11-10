import requests
import json
import os
from datetime import datetime

# --- Configuración ---
API_URL = "https://jsonplaceholder.typicode.com/posts/1" # API pública de prueba
OUTPUT_FILENAME = "datos_procesados.txt"

def consumir_api_y_procesar():
    """
    Consume la API REST, obtiene un post, procesa los datos y guarda el resultado.
    """
    print(f"✅ Iniciando consumo de API: {API_URL}")

    try:
        # 1. Consumo de la API REST
        response = requests.get(API_URL)
        response.raise_for_status() # Lanza una excepción para códigos de estado de error (4xx o 5xx)

        data = response.json()
        print("📥 Datos obtenidos con exito.")

        # 2. Tarea de automatización: Procesamiento de datos
        post_id = data.get('id')
        post_title = data.get('title')
        post_body = data.get('body')
        
        # Simulación de una tarea: Crear un resumen y añadir metadatos
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resumen = f"""
        --- Informe de Datos Procesados ---
        
        Fecha de Ejecucion: {timestamp}
        API Consumida: {API_URL}
        
        Detalles del Post (ID: {post_id}):
        ------------------------------------
        Titulo: {post_title.upper()}
        Longitud del Cuerpo: {len(post_body)} caracteres
        Primeras 50 palabras del Cuerpo: {" ".join(post_body.split()[:50])}...

        ------------------------------------
        """

        # 3. Guardar el resultado
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
            f.write(resumen.strip())
        
        print(f"✨ Tarea completada. Resultado guardado en **{OUTPUT_FILENAME}**.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error al consumir la API: {e}")
    except Exception as e:
        print(f"❌ Ocurrio un error inesperado durante el procesamiento: {e}")

if __name__ == "__main__":
    consumir_api_y_procesar()