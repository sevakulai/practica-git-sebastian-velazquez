# ============================================================
# Actividad: Manejo de Listas, Tuplas y Diccionarios en Python
# Estudiante: Velazquez Marcos
# Matrícula: 2630013
# Grupo: [ESCRIBE TU GRUPO]
# Archivo: 2630013_velazquez_marcos.py
# ============================================================

# RESUMEN DE LA INVESTIGACIÓN
# Una lista es una colección ordenada y modificable que puede almacenar varios valores.
# Una tupla es una colección ordenada e inmutable, útil para datos fijos como las coordenadas.
# Un diccionario almacena pares clave-valor y permite recuperar datos mediante claves descriptivas.
# Modificable significa que una colección puede cambiar después de crearse; inmutable significa que no puede cambiarse.
# Este programa contiene seis problemas prácticos que utilizan listas, tuplas y diccionarios.
# Cada problema documenta sus entradas, salidas, validaciones y pruebas normales, límite y de error.
# La validación de entradas evita cálculos incorrectos y fallos inesperados por datos no válidos.
# Los ejemplos abarcan artículos de compra, coordenadas, productos, calificaciones, frecuencia de palabras y contactos.

# BUENAS PRÁCTICAS
# Utiliza listas cuando sea necesario agregar o quitar elementos con frecuencia.
# Utiliza tuplas para datos que deben permanecer fijos, como las coordenadas.
# Utiliza diccionarios cuando necesites encontrar información mediante una clave, como un nombre o código de producto.
# Evita modificar una lista mientras la recorres, salvo que sea intencional.
# Utiliza claves descriptivas en los diccionarios, nombres claros para las variables y mensajes de salida comprensibles.
# Valida los datos antes de procesarlos y verifica que las colecciones no estén vacías antes de calcular estadísticas.

def run_problem_1():
    """Crea una lista de compras, agrega un artículo y busca un elemento."""
    print("\n=== Problema 1: Fundamentos de listas de compras ===")
    initial_items_text = input("Escribe los artículos separados por comas: ").strip()
    new_item = input("Escribe un artículo nuevo: ").strip()
    search_item = input("Escribe el artículo que deseas buscar: ").strip()

    if not initial_items_text or not new_item or not search_item:
        print("Error: entrada no válida")
        return

    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]
    if not items_list:
        print("Error: la lista inicial no puede estar vacía")
        return

    items_list.append(new_item)
    is_in_list = search_item.casefold() in [item.casefold() for item in items_list]
    print("Lista de artículos:", items_list)
    print("Cantidad de artículos:", len(items_list))
    print("Artículo encontrado:", str(is_in_list).lower())


def run_problem_2():
    """Calcula la distancia euclidiana y el punto medio entre dos puntos."""
    print("\n=== Problema 2: Puntos y distancias con tuplas ===")
    try:
        x1 = float(input("Escribe x1: ").strip())
        y1 = float(input("Escribe y1: ").strip())
        x2 = float(input("Escribe x2: ").strip())
        y2 = float(input("Escribe y2: ").strip())
    except ValueError:
        print("Error: entrada no válida")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    print("Punto A:", point_a)
    print("Punto B:", point_b)
    print("Distancia:", round(distance, 4))
    print("Punto medio:", midpoint)


def run_problem_3():
    """Busca el precio de un producto y calcula el costo total de la compra."""
    print("\n=== Problema 3: Catálogo de productos ===")
    product_prices = {"manzana": 10.0, "pan": 25.5, "leche": 32.0}
    product_name = input("Escribe el nombre del producto: ").strip().casefold()
    quantity_text = input("Escribe la cantidad: ").strip()

    if not product_name:
        print("Error: entrada no válida")
        return
    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Error: entrada no válida")
        return
    if quantity <= 0:
        print("Error: la cantidad debe ser mayor que cero")
        return
    if product_name not in product_prices:
        print("Error: producto no encontrado")
        return

    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print("Precio unitario:", f"{unit_price:.2f}")
    print("Cantidad:", quantity)
    print("Total:", f"{total_price:.2f}")


def run_problem_4():
    """Calcula el promedio de un estudiante y determina si aprobó."""
    print("\n=== Problema 4: Calificaciones de estudiantes ===")
    grades = {
        "ana": [90.0, 85.0, 88.0],
        "benito": [65.0, 70.0, 68.0],
        "chloe": [100.0, 95.0, 98.0],
    }
    student_name = input("Escribe el nombre del estudiante: ").strip().casefold()
    if not student_name:
        print("Error: entrada no válida")
        return
    if student_name not in grades:
        print("Error: estudiante no encontrado")
        return

    student_grades = grades[student_name]
    if not student_grades:
        print("Error: no hay calificaciones disponibles")
        return
    average = sum(student_grades) / len(student_grades)
    is_passed = average >= 70.0
    print("Calificaciones:", student_grades)
    print("Promedio:", round(average, 2))
    print("Aprobó:", str(is_passed).lower())


def run_problem_5():
    """Cuenta las palabras de una oración y muestra la más frecuente."""
    print("\n=== Problema 5: Contador de frecuencia de palabras ===")
    sentence = input("Escribe una oración: ").strip()
    if not sentence:
        print("Error: entrada no válida")
        return

    # Elimina los signos de puntuación más comunes antes de separar las palabras; conserva los apóstrofos dentro de ellas.
    normalized_sentence = sentence.lower()
    for punctuation in ".,!?;:()[]{}\"":
        normalized_sentence = normalized_sentence.replace(punctuation, "")
    words_list = normalized_sentence.split()
    if not words_list:
        print("Error: no se encontraron palabras")
        return

    freq_dict = {}
    for word in words_list:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    most_common_word = max(freq_dict, key=freq_dict.get)
    print("Lista de palabras:", words_list)
    print("Frecuencias:", freq_dict)
    print("Palabra más frecuente:", most_common_word)


def run_problem_6():
    """Agrega, busca o elimina un contacto en un diccionario."""
    print("\n=== Problema 6: Agenda de contactos ===")
    contacts = {"Ana": "5551234567", "Benito": "5557654321", "Carla": "5551112233"}
    action_text = input("Escribe la acción (AGREGAR, BUSCAR, ELIMINAR): ").strip().upper()
    if action_text not in {"AGREGAR", "BUSCAR", "ELIMINAR"}:
        print("Error: acción no válida")
        return

    name = input("Escribe el nombre del contacto: ").strip()
    if not name:
        print("Error: entrada no válida")
        return

    # Compara los nombres sin distinguir mayúsculas de minúsculas y conserva el formato guardado.
    existing_name = next((contact_name for contact_name in contacts
                          if contact_name.casefold() == name.casefold()), None)

    if action_text == "AGREGAR":
        phone = input("Escribe el número telefónico: ").strip()
        if not phone:
            print("Error: entrada no válida")
            return
        if existing_name is not None:
            contacts[existing_name] = phone
            saved_name = existing_name
        else:
            contacts[name] = phone
            saved_name = name
        print("Contacto guardado:", saved_name, contacts[saved_name])
    elif action_text == "BUSCAR":
        if existing_name is None:
            print("Error: contacto no encontrado")
        else:
            print("Teléfono:", contacts.get(existing_name))
    else:  # ELIMINAR
        if existing_name is None:
            print("Error: contacto no encontrado")
        else:
            contacts.pop(existing_name)
            print("Contacto eliminado:", existing_name)


# ============================================================
# DOCUMENTACIÓN DE LOS PROBLEMAS, ENTRADAS, SALIDAS, VALIDACIONES Y PRUEBAS
# Problema 1: Fundamentos de listas de compras
# Descripción: procesa una lista de compras separada por comas, agrega un artículo
# y comprueba si el artículo solicitado se encuentra en la lista.
# Entradas: initial_items_text (texto separado por comas), new_item y search_item.
# Salidas: lista de artículos, cantidad total y resultado de búsqueda (verdadero/falso).
# Validaciones: los textos no deben estar vacíos; se ignoran elementos vacíos y
# se rechaza una lista que quede sin artículos.
# Pruebas: normal: "manzana, plátano", agregar "naranja", buscar "MANZANA" -> encontrado, 3 artículos.
# Límite: "manzana", agregar "pera", buscar "pera" -> encontrado, 2 artículos.
# Error: lista inicial vacía -> entrada no válida.
#
# Problema 2: Puntos y distancias con tuplas
# Descripción: almacena dos puntos bidimensionales en tuplas, calcula la distancia
# euclidiana y encuentra el punto medio.
# Entradas: x1, y1, x2 y y2 como valores numéricos convertibles a float.
# Salidas: punto A, punto B, distancia y punto medio.
# Validaciones: las cuatro entradas deben poder convertirse a float.
# Pruebas: normal: (0, 0) y (3, 4) -> distancia 5 y punto medio (1.5, 2.0).
# Límite: dos puntos iguales -> distancia 0. Error: x1="abc" -> entrada no válida.
#
# Problema 3: Catálogo de productos
# Descripción: busca un producto en un diccionario y calcula el costo total.
# Entradas: product_name y quantity. Salidas: precio unitario, cantidad y total.
# Validaciones: el nombre no debe estar vacío, la cantidad debe ser un entero mayor que 0
# y el producto debe existir en el catálogo.
# Pruebas: normal: manzana, cantidad 3 -> total 30.00. Límite: leche, cantidad 1 -> 32.00.
# Error: cantidad 0 -> mensaje de cantidad no válida.
#
# Problema 4: Calificaciones de estudiantes
# Descripción: obtiene las calificaciones, calcula el promedio y verifica si alcanza 70.
# Entradas: student_name. Salidas: calificaciones, promedio y resultado de aprobación.
# Validaciones: el nombre no debe estar vacío, el estudiante debe existir y debe tener calificaciones.
# Pruebas: normal: "ana" -> promedio 87.67, aprobó. Límite: "benito" -> promedio 67.67, no aprobó.
# Error: "nadie" -> estudiante no encontrado.
#
# Problema 5: Contador de frecuencia de palabras
# Descripción: normaliza una oración, elimina signos de puntuación comunes y cuenta las palabras.
# Entradas: sentence. Salidas: lista de palabras, frecuencias y palabra más frecuente.
# Validaciones: la oración no debe estar vacía y debe producir al menos una palabra.
# Pruebas: normal: "Rojo azul rojo" -> rojo aparece dos veces. Límite: "¡Hola!" -> una palabra.
# Error: "!!!" -> no se encontraron palabras. Se eliminan signos comunes y se conservan apóstrofos.
#
# Problema 6: Agenda de contactos
# Descripción: agrega o actualiza contactos, busca teléfonos o elimina contactos mediante un diccionario.
# Entradas: action_text, name y phone únicamente al agregar.
# Salidas: confirmación de contacto guardado, teléfono, confirmación de eliminación o error.
# Validaciones: la acción debe ser AGREGAR, BUSCAR o ELIMINAR; el nombre no debe estar vacío;
# el teléfono es obligatorio al agregar y el contacto debe existir para buscar o eliminar.
# Pruebas: normal: agregar Diana con teléfono 5550001111. Límite: buscar Ana -> 5551234567.
# Error: eliminar a Nadie -> contacto no encontrado.

# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

def main():
    """Muestra un menú para ejecutar cada problema por separado."""
    problem_functions = {
        "1": run_problem_1,
        "2": run_problem_2,
        "3": run_problem_3,
        "4": run_problem_4,
        "5": run_problem_5,
        "6": run_problem_6,
    }
    while True:
        print("\n=== Práctica de colecciones en Python ===")
        print("1. Shopping list")
        print("2. Puntos y distancias")
        print("3. Catálogo de productos")
        print("4. Calificaciones")
        print("5. Frecuencia de palabras")
        print("6. Agenda de contactos")
        print("0. Salir")
        choice = input("Elige un problema (0-6): ").strip()
        if choice == "0":
            print("¡Hasta luego!")
            break
        selected_problem = problem_functions.get(choice)
        if selected_problem is None:
            print("Error: entrada no válida")
        else:
            selected_problem()


if __name__ == "__main__":
    main()

# ============================================================
# CONCLUSIONES
# Las listas son útiles cuando las colecciones necesitan crecer, reducirse o reordenarse.
# Las tuplas representan grupos fijos de valores y comunican que los datos no deberían cambiar.
# Los diccionarios permiten buscar información por clave y son útiles para catálogos y agendas.
# Combinar diccionarios con listas permite almacenar varias calificaciones por estudiante.
# Recorrer una lista permite crear resúmenes útiles, como diccionarios de frecuencia de palabras.
# Validar los datos de entrada ayuda a evitar errores por cantidades no válidas o nombres faltantes.
# Elegir la colección adecuada hace que el programa sea más claro y fácil de mantener.

# REFERENCIAS
# 1) Python Software Foundation. (s. f.). Tipos integrados. https://docs.python.org/3/library/stdtypes.html
# 2) Python Software Foundation. (s. f.). Estructuras de datos. https://docs.python.org/3/tutorial/datastructures.html
# 3) Python Software Foundation. (s. f.). Más información sobre listas. https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# 4) Python Software Foundation. (s. f.). Diccionarios. https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# 5) Python Software Foundation. (s. f.). Errores y excepciones. https://docs.python.org/3/tutorial/errors.html
# 6) Python Software Foundation. (s. f.). Entrada y salida. https://docs.python.org/3/tutorial/inputoutput.html
#
# REPOSITORIO DE GITHUB
# Agrega aquí la URL del repositorio después de subir este archivo a GitHub.
