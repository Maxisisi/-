import xml.etree.ElementTree as ET

ruta_xml = "inventario.xml"

# Parsear archivo XML
xml = ET.parse(ruta_xml)
raiz = xml.getroot()

# Listar todas las categorías
print("Categorías disponibles:")
for categoria in raiz.findall('categoria'):
    nombre_categoria = categoria.get('nombre')
    print(f"- {nombre_categoria}")

    # Mostrar productos de esta categoría
    print("  Productos:")
    for producto in categoria.findall('producto'):
        id_producto = producto.get('id')
        nombre = producto.find('nombre').text
        precio = producto.find('precio').text
        stock = producto.find('stock').text
        
        print(f"  - ID: {id_producto}, Nombre: {nombre}, Precio: ${precio}, Stock: {stock}")
    print()
