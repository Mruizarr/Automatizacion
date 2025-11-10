import csv
import os

def cargar_inventario(nombre_archivo="inventario.csv"):
    """Carga los datos de inventario desde un archivo CSV."""
    inventario = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, mode='r', newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Asegúrate de que los campos numéricos se conviertan a int o float si es necesario
                try:
                    fila['Cantidad'] = int(fila['Cantidad'])
                except ValueError:
                    # En caso de error, mantenlo como el valor de cadena o ignóralo
                    pass
                inventario.append(fila)
    return inventario

def guardar_inventario(inventario, nombre_archivo="inventario.csv"):
    """Guarda los datos de inventario en un archivo CSV."""
    # Define los nombres de las columnas para el encabezado
    nombres_campos = ['ID', 'Nombre', 'Cantidad', 'Ubicacion']
    with open(nombre_archivo, mode='w', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=nombres_campos)
        escritor.writeheader()  # Escribe el encabezado
        escritor.writerows(inventario)

def agregar_articulo(inventario, nuevo_articulo):
    """Añade un nuevo artículo al inventario (simulación)."""
    # Generar un ID simple
    if inventario:
        ultimo_id = max(int(item['ID']) for item in inventario)
        nuevo_articulo['ID'] = str(ultimo_id + 1)
    else:
        nuevo_articulo['ID'] = '1'

    inventario.append(nuevo_articulo)
    print(f"\n✅ Artículo añadido: {nuevo_articulo['Nombre']}")
    return inventario

def mostrar_inventario(inventario):
    """Imprime el inventario actual de forma legible."""
    print("\n--- INVENTARIO ACTUAL ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    # Encuentra la longitud máxima de cada columna para un formato ordenado
    ancho_id = max(len(str(item.get('ID', ''))) for item in inventario + [{'ID': 'ID'}])
    ancho_nombre = max(len(item.get('Nombre', '')) for item in inventario + [{'Nombre': 'Nombre'}])
    ancho_cantidad = max(len(str(item.get('Cantidad', ''))) for item in inventario + [{'Cantidad': 'Cantidad'}])
    ancho_ubicacion = max(len(item.get('Ubicacion', '')) for item in inventario + [{'Ubicacion': 'Ubicacion'}])

    # Línea de encabezado
    formato = f"{{:<{ancho_id}}} | {{:<{ancho_nombre}}} | {{:>{ancho_cantidad}}} | {{:<{ancho_ubicacion}}}"
    print(formato.format("ID", "Nombre", "Cantidad", "Ubicacion"))
    print("-" * (ancho_id + ancho_nombre + ancho_cantidad + ancho_ubicacion + 9))

    # Datos
    for item in inventario:
        print(formato.format(item.get('ID', ''), item.get('Nombre', ''), item.get('Cantidad', ''), item.get('Ubicacion', '')))
    print("------------------------")

# --- Ejecución del script de inventario ---
NOMBRE_ARCHIVO_INVENTARIO = "inventario_empresa.csv"

# 1. Cargar el inventario existente
mi_inventario = cargar_inventario(NOMBRE_ARCHIVO_INVENTARIO)

# 2. Mostrar el estado inicial
mostrar_inventario(mi_inventario)

# 3. Definir un nuevo artículo para añadir
nuevo_item = {
    'Nombre': 'Servidor R640',
    'Cantidad': 2,
    'Ubicacion': 'Rack 4'
}

# 4. Añadir el artículo
mi_inventario = agregar_articulo(mi_inventario, nuevo_item)

# 5. Mostrar el inventario actualizado
mostrar_inventario(mi_inventario)

# 6. Guardar el inventario de vuelta en el archivo
guardar_inventario(mi_inventario, NOMBRE_ARCHIVO_INVENTARIO)

print(f"\nDatos de inventario guardados en {NOMBRE_ARCHIVO_INVENTARIO}")