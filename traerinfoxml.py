import xml.etree.ElementTree as ET
import re

ruta_xml = r"C:\Users\ricar\Desktop\estudiuo\myfile.xml"

# Parsear archivo XML
xml = ET.parse(ruta_xml)
raiz = xml.getroot()

# Obtener espacio ...
ns = re.match(r'{.*}', raiz.tag).group(0)
editconf = raiz.find(f"{ns}editar-config")
defop = editconf.find(f"{ns}operacion-por-defecto")
testop = editconf.find(f"{ns}opcion-prueba")

# Imprimir info obtenida
operacion_por_defecto = defop.text if defop is not None else "No encontrado"
opcion_prueba = testop.text if testop is not None else "No encontrado"

print(f"La operación por defecto contiene: {operacion_por_defecto}")
print(f"La opción de prueba contiene: {opcion_prueba}")
