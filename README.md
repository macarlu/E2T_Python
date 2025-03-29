# E2T_Python

# Manejo de JSON en Python ()

Guia sacada de Aqui

1. Introducción a JSON
Definición: Formato ligero de intercambio de datos, independiente del lenguaje.

Usos Comunes:

Transferencia de datos en aplicaciones web (cliente-servidor).

Archivos de configuración (ej: manifest.json en extensiones de Chrome).

Características Clave:

Sintaxis basada en pares clave: valor.

Soporta múltiples tipos de datos: strings, números, booleanos, arrays, objetos, null.

2. Estructura de JSON
Ejemplo:

json
Copy
{
  "tamano": "mediana",
  "precio": 15.67,
  "toppings": ["champinones", "pepperoni"],
  "cliente": {
    "nombre": "Jane Doe",
    "telefono": null
  }
}
Reglas Básicas:

Claves deben ser strings (entre comillas dobles).

Valores pueden ser: string, number, boolean, array, object, null.

Pares clave-valor separados por comas.

No se permiten comentarios.

3. JSON vs Diccionarios de Python
JSON	Diccionario Python
Formato de texto para almacenar datos.	Estructura de datos en memoria.
Claves siempre son strings.	Claves pueden ser cualquier tipo hashable.
Valores: tipos JSON específicos.	Valores: cualquier objeto Python.
Relación:

JSON → Cadena de texto.

Diccionario → Objeto Python manipulable.

Conversión necesaria para trabajar en Python:

python
Copy
import json
datos_dict = json.loads(json_str)  # JSON → Diccionario
json_str = json.dumps(datos_dict)  # Diccionario → JSON
4. Funciones Clave del Módulo json
Conversiones Básicas
json.loads(): Convierte cadena JSON → diccionario Python.

python
Copy
datos_dict = json.loads('{"nombre": "Juan", "edad": 30}')
json.dumps(): Convierte diccionario Python → cadena JSON.

python
Copy
json_str = json.dumps(datos_dict, indent=4, sort_keys=True)
Trabajar con Archivos
json.load(): Lee archivo JSON → diccionario Python.

python
Copy
with open('datos.json', 'r') as archivo:
    datos = json.load(archivo)
json.dump(): Escribe diccionario Python → archivo JSON.

python
Copy
with open('nuevos_datos.json', 'w') as archivo:
    json.dump(datos_dict, archivo, indent=4)
5. Procesamiento Avanzado
Indentación y Orden
Indentación Automática:

python
Copy
json_str = json.dumps(datos_dict, indent=4)  # 4 espacios por nivel.
Ordenar Claves Alfabéticamente:

python
Copy
json_str = json.dumps(datos_dict, sort_keys=True)
Manejo de Tipos de Datos
Tipo JSON	Tipo Python
string	str
number	int/float
array	list
object	dict
true/false	True/False
null	None
6. Lectura/Escritura de Archivos
Lectura (JSON → Python)
python
Copy
with open('ordenes.json', 'r') as archivo:
    datos = json.load(archivo)
# Acceso a datos:
print(datos["ordenes"][0]["cliente"]["nombre"])
Escritura (Python → JSON)
python
Copy
nuevos_datos = {"producto": "laptop", "precio": 999.99}
with open('productos.json', 'w') as archivo:
    json.dump(nuevos_datos, archivo, indent=4)
7. Diferencias Clave: Funciones
Función	Entrada	Salida	Uso Típico
loads()	Cadena JSON	Diccionario Python	Procesar datos de API.
dumps()	Diccionario Python	Cadena JSON	Enviar datos a API.
load()	Archivo JSON	Diccionario Python	Leer archivos locales.
dump()	Diccionario Python	Archivo JSON	Guardar configuraciones.
8. Terminología Esencial
Serialización: Convertir un objeto → cadena JSON (dumps/dump).

Deserialización: Convertir cadena JSON → objeto (loads/load).

Tips Visuales:
✅ Usa indent=4 para archivos JSON legibles.
✅ sort_keys=True ordena claves alfabéticamente.
⚠️ Las claves en JSON siempre son strings.

Ejemplo de Flujo de Trabajo:

python
Copy
# 1. Leer archivo JSON
with open('datos.json', 'r') as f:
    datos = json.load(f)

# 2. Modificar datos
datos['nueva_clave'] = 'valor'

# 3. Guardar cambios
with open('datos_actualizados.json', 'w') as f:
    json.dump(datos, f, indent=4)
