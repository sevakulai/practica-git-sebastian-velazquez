# ============================================================
# Actividad: Manejo de listas y tuplas en Python
# Estudiante: Velazquez Marcos
# Matrícula: 2630013
# Grupo: IM 1-1
# Archivo: 2630013_velazquez_marcos.py
# ============================================================

# RESUMEN DE LA INVESTIGACIÓN
# Una lista es una colección ordenada y modificable que puede almacenar varios valores.
# Una tupla es una colección ordenada e inmutable, útil para agrupar datos relacionados.
# Las listas permiten agregar, quitar, recorrer y buscar elementos.
# Las tuplas sirven para representar datos agrupados, como coordenadas o registros sencillos.
# Este programa contiene seis ejercicios prácticos que utilizan únicamente listas y tuplas.
# Cada ejercicio documenta sus entradas, salidas, validaciones y pruebas normales, límite y de error.
# La validación de entradas ayuda a evitar cálculos incorrectos y fallos por datos no válidos.

# BUENAS PRÁCTICAS
# Usa listas cuando necesites agregar o quitar elementos.
# Usa tuplas para agrupar datos relacionados que se manejan como una unidad.
# Valida los datos antes de procesarlos y comprueba que las listas no estén vacías.
# Utiliza nombres claros para las variables y mensajes de salida comprensibles.


def run_problem_1():
    """Crea una lista de compras, agrega un artículo y busca un elemento."""
    print("\n=== Problema 1: Lista de compras ===")
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
    """Calcula la distancia euclidiana y el punto medio entre dos puntos guardados en tuplas."""
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
    """Busca el precio de un producto en una lista de tuplas y calcula el total."""
    print("\n=== Problema 3: Catálogo de productos ===")
    product_prices = [("manzana", 10.0), ("pan", 25.5), ("leche", 32.0)]
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

    unit_price = None
    for item_name, item_price in product_prices:
        if item_name == product_name:
            unit_price = item_price
            break
    if unit_price is None:
        print("Error: producto no encontrado")
        return

    total_price = unit_price * quantity
    print("Precio unitario:", f"{unit_price:.2f}")
    print("Cantidad:", quantity)
    print("Total:", f"{total_price:.2f}")


def run_problem_4():
    """Calcula el promedio de un estudiante a partir de una lista de tuplas."""
    print("\n=== Problema 4: Calificaciones de estudiantes ===")
    student_grades = [
        ("ana", [90.0, 85.0, 88.0]),
        ("benito", [65.0, 70.0, 68.0]),
        ("chloe", [100.0, 95.0, 98.0]),
    ]
    student_name = input("Escribe el nombre del estudiante: ").strip().casefold()
    if not student_name:
        print("Error: entrada no válida")
        return

    grades_list = None
    for saved_name, saved_grades in student_grades:
        if saved_name == student_name:
            grades_list = saved_grades
            break
    if grades_list is None:
        print("Error: estudiante no encontrado")
        return
    if not grades_list:
        print("Error: no hay calificaciones disponibles")
        return

    average = sum(grades_list) / len(grades_list)
    is_passed = average >= 70.0
    print("Calificaciones:", grades_list)
    print("Promedio:", round(average, 2))
    print("Aprobó:", str(is_passed).lower())


def run_problem_5():
    """Cuenta las palabras de una oración utilizando una lista de tuplas."""
    print("\n=== Problema 5: Frecuencia de palabras ===")
    sentence = input("Escribe una oración: ").strip()
    if not sentence:
        print("Error: entrada no válida")
        return

    normalized_sentence = sentence.lower()
    for punctuation in ".,!?;:()[]{}\"":
        normalized_sentence = normalized_sentence.replace(punctuation, "")
    words_list = normalized_sentence.split()
    if not words_list:
        print("Error: no se encontraron palabras")
        return

    word_counts = []
    for word in words_list:
        found_word = False
        for index, (saved_word, count) in enumerate(word_counts):
            if saved_word == word:
                word_counts[index] = (saved_word, count + 1)
                found_word = True
                break
        if not found_word:
            word_counts.append((word, 1))

    most_common_word, highest_count = word_counts[0]
    for word, count in word_counts:
        if count > highest_count:
            most_common_word, highest_count = word, count

    print("Lista de palabras:", words_list)
    print("Frecuencias (palabra, cantidad):", word_counts)
    print("Palabra más frecuente:", most_common_word)
    print("Veces que aparece:", highest_count)


def run_problem_6():
    """Agrega, busca o elimina contactos almacenados en una lista de tuplas."""
    print("\n=== Problema 6: Agenda de contactos ===")
    contacts = [
        ("Ana", "5551234567"),
        ("Benito", "5557654321"),
        ("Carla", "5551112233"),
    ]
    action_text = input("Escribe la acción (AGREGAR, BUSCAR, ELIMINAR): ").strip().upper()
    if action_text not in ("AGREGAR", "BUSCAR", "ELIMINAR"):
        print("Error: acción no válida")
        return

    name = input("Escribe el nombre del contacto: ").strip()
    if not name:
        print("Error: entrada no válida")
        return

    contact_index = None
    for index, (contact_name, phone) in enumerate(contacts):
        if contact_name.casefold() == name.casefold():
            contact_index = index
            break

    if action_text == "AGREGAR":
        phone = input("Escribe el número telefónico: ").strip()
        if not phone:
            print("Error: entrada no válida")
            return
        if contact_index is not None:
            contacts[contact_index] = (contacts[contact_index][0], phone)
            saved_name = contacts[contact_index][0]
        else:
            contacts.append((name, phone))
            saved_name = name
        print("Contacto guardado:", saved_name)
        print("Teléfono:", phone)
    elif action_text == "BUSCAR":
        if contact_index is None:
            print("Error: contacto no encontrado")
        else:
            print("Teléfono:", contacts[contact_index][1])
    else:
        if contact_index is None:
            print("Error: contacto no encontrado")
        else:
            removed_contact = contacts.pop(contact_index)
            print("Contacto eliminado:", removed_contact[0])


# ============================================================
# DOCUMENTACIÓN DE LOS PROBLEMAS, ENTRADAS, SALIDAS, VALIDACIONES Y PRUEBAS
#
# Problema 1: Lista de compras
# Descripción: procesa una lista separada por comas, agrega un artículo y busca otro.
# Entradas: initial_items_text, new_item y search_item.
# Salidas: lista de artículos, cantidad y resultado de búsqueda.
# Validaciones: los textos no deben estar vacíos y la lista debe contener artículos.
# Pruebas: normal: "manzana, plátano", agregar "naranja", buscar "MANZANA" -> encontrado, 3 artículos.
# Límite: "manzana", agregar "pera", buscar "pera" -> encontrado, 2 artículos.
# Error: lista inicial vacía -> entrada no válida.
#
# Problema 2: Puntos y distancias con tuplas
# Descripción: guarda dos puntos como tuplas, calcula distancia y punto medio.
# Entradas: x1, y1, x2 y y2 como números.
# Salidas: puntos, distancia y punto medio.
# Validaciones: las cuatro entradas deben poder convertirse a float.
# Pruebas: normal: (0, 0) y (3, 4) -> distancia 5 y punto medio (1.5, 2.0).
# Límite: dos puntos iguales -> distancia 0. Error: x1="abc" -> entrada no válida.
#
# Problema 3: Catálogo de productos
# Descripción: busca el precio en una lista de tuplas (producto, precio) y calcula el costo.
# Entradas: product_name y quantity.
# Salidas: precio unitario, cantidad y total.
# Validaciones: nombre no vacío, cantidad entera mayor que cero y producto existente.
# Pruebas: normal: manzana, cantidad 3 -> total 30.00. Límite: leche, cantidad 1 -> 32.00.
# Error: cantidad 0 -> mensaje de cantidad no válida.
#
# Problema 4: Calificaciones de estudiantes
# Descripción: busca un estudiante en una lista de tuplas y calcula el promedio.
# Entradas: student_name. Salidas: calificaciones, promedio y resultado de aprobación.
# Validaciones: nombre no vacío, estudiante existente y lista de calificaciones no vacía.
# Pruebas: normal: "ana" -> promedio 87.67, aprobó. Límite: "benito" -> promedio 67.67, no aprobó.
# Error: "nadie" -> estudiante no encontrado.
#
# Problema 5: Frecuencia de palabras
# Descripción: limpia una oración, separa las palabras y cuenta las apariciones con una lista de tuplas.
# Entradas: sentence. Salidas: palabras, pares (palabra, cantidad) y palabra más frecuente.
# Validaciones: la oración debe contener al menos una palabra después de quitar puntuación común.
# Pruebas: normal: "Rojo azul rojo" -> rojo aparece dos veces. Límite: "¡Hola!" -> una palabra.
# Error: "!!!" -> no se encontraron palabras.
#
# Problema 6: Agenda de contactos
# Descripción: agrega, busca o elimina contactos almacenados como tuplas dentro de una lista.
# Entradas: action_text, name y phone al agregar.
# Salidas: confirmación, teléfono o mensaje de error.
# Validaciones: acción permitida, nombre no vacío, teléfono obligatorio al agregar y contacto existente al buscar/eliminar.
# Pruebas: normal: agregar Diana con teléfono 5550001111. Límite: buscar Ana -> 5551234567.
# Error: eliminar a Nadie -> contacto no encontrado.
#
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

def main():
    """Muestra un menú para ejecutar cada ejercicio."""
    problem_functions = [
        ("1", run_problem_1),
        ("2", run_problem_2),
        ("3", run_problem_3),
        ("4", run_problem_4),
        ("5", run_problem_5),
        ("6", run_problem_6),
    ]
    while True:
        print("\n=== Práctica de listas y tuplas en Python ===")
        print("1. Lista de compras")
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
        selected_problem = None
        for problem_number, problem_function in problem_functions:
            if problem_number == choice:
                selected_problem = problem_function
                break
        if selected_problem is None:
            print("Error: entrada no válida")
        else:
            selected_problem()


if __name__ == "__main__":
    main()

# ============================================================
# CONCLUSIONES
# Las listas son útiles para colecciones que necesitan agregarse, quitarse o recorrerse.
# Las tuplas agrupan datos relacionados, como coordenadas o registros de productos.
# Una lista de tuplas permite organizar catálogos, calificaciones y contactos sin usar estructuras adicionales.
# Recorrer listas permite buscar elementos y calcular estadísticas.
# Validar las entradas ayuda a evitar errores por datos vacíos o valores no válidos.
# Elegir estructuras simples y nombres claros facilita la lectura y el mantenimiento del programa.
#
# REFERENCIAS
# 1) Python Software Foundation. (s. f.). Tipos integrados. https://docs.python.org/3/library/stdtypes.html
# 2) Python Software Foundation. (s. f.). Estructuras de datos. https://docs.python.org/3/tutorial/datastructures.html
# 3) Python Software Foundation. (s. f.). Más información sobre listas. https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# 4) Python Software Foundation. (s. f.). Tuplas y secuencias. https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# 5) Python Software Foundation. (s. f.). Errores y excepciones. https://docs.python.org/3/tutorial/errors.html
# 6) Python Software Foundation. (s. f.). Entrada y salida. https://docs.python.org/3/tutorial/inputoutput.html
#
# REPOSITORIO DE GITHUB
# https://github.com/sevakulai/practica-git-sebastian-velazquez