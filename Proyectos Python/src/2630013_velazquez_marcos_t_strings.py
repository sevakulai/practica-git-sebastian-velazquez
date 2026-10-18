# Actividad: Manejo de strings en Python
# Estudiante: Velazquez Marcos | Matrícula: 2630013 | Grupo: [ESCRIBE TU GRUPO]
# Archivo: 2630013_velazquez_marcos_t_strings.py
#
# RESUMEN DE LA INVESTIGACIÓN
# Una cadena de texto es una secuencia inmutable de caracteres que representa texto.
# Las cadenas permiten acceder a posiciones, extraer fragmentos, concatenar, buscar, reemplazar y dar formato.
# Los métodos strip(), lower(), upper(), split() y join() ayudan a normalizar el texto.
# La normalización hace que las comparaciones sean más consistentes y reduce errores evitables.
# Este programa practica el manejo de nombres, correos electrónicos, palíndromos y estadísticas de oraciones,
# así como la evaluación de contraseñas y etiquetas de productos de ancho fijo.
# Cada problema documenta entradas, salidas, validaciones y tres casos de prueba.
# Las operaciones con cadenas devuelven nuevas cadenas en lugar de modificar la original.
#
# BUENAS PRÁCTICAS
# Normaliza la entrada con strip() y lower() cuando sea apropiado.
# Comprueba que el texto no esté vacío antes de revisar su formato.
# Utiliza nombres descriptivos para las variables, mensajes de error claros y límites de fragmentos bien definidos.
# Recuerda que las cadenas son inmutables y sus métodos devuelven nuevos valores.


def run_problem_1():
    print("\n=== Problema 1: Formateador de nombres completos ===")
    full_name = input("Escribe el nombre completo: ").strip()
    name_parts = full_name.split()
    if len(name_parts) < 2:
        print("Error: escribe al menos dos palabras")
        return
    formatted_name = " ".join(name_parts).title()
    initials = ".".join(part[0].upper() for part in name_parts) + "."
    print("Nombre con formato:", formatted_name)
    print("Iniciales:", initials)


def run_problem_2():
    print("\n=== Problema 2: Validador básico de correo electrónico ===")
    email_text = input("Escribe el correo electrónico: ").strip()
    valid_email = False
    if email_text and email_text.count("@") == 1 and not any(ch.isspace() for ch in email_text):
        local_part, domain_part = email_text.split("@")
        valid_email = bool(local_part and "." in domain_part and
                           not domain_part.startswith(".") and not domain_part.endswith("."))
    print("Correo válido:", str(valid_email).lower())
    if valid_email:
        print("Dominio:", email_text.split("@", 1)[1])


def run_problem_3():
    print("\n=== Problema 3: Comprobador de palíndromos ===")
    phrase = input("Escribe una frase: ").strip()
    normalized_phrase = "".join(phrase.lower().split())
    if len(normalized_phrase) < 3:
        print("Error: la frase debe contener al menos tres caracteres que no sean espacios")
        return
    print("Frase normalizada:", normalized_phrase)
    print("¿Es palíndromo?:", str(normalized_phrase == normalized_phrase[::-1]).lower())


def run_problem_4():
    print("\n=== Problema 4: Estadísticas de palabras en una oración ===")
    sentence = input("Escribe una oración: ").strip()
    words_list = sentence.split()
    if not words_list:
        print("Error: entrada no válida")
        return
    print("Cantidad de palabras:", len(words_list))
    print("Primera palabra:", words_list[0])
    print("Última palabra:", words_list[-1])
    print("Palabra más corta:", min(words_list, key=len))
    print("Palabra más larga:", max(words_list, key=len))


def run_problem_5():
    print("\n=== Problema 5: Clasificador de seguridad de contraseñas ===")
    password_input = input("Escribe la contraseña: ")
    if not password_input:
        print("Error: entrada no válida")
        return
    has_upper = any(ch.isupper() for ch in password_input)
    has_lower = any(ch.islower() for ch in password_input)
    has_digit = any(ch.isdigit() for ch in password_input)
    has_symbol = any(not ch.isalnum() and not ch.isspace() for ch in password_input)
    if len(password_input) >= 8 and has_upper and has_lower and has_digit and has_symbol:
        password_strength = "fuerte"
    elif len(password_input) >= 8 and ((has_upper and has_lower) or
                                       (has_digit and (has_upper or has_lower))):
        password_strength = "media"
    else:
        password_strength = "débil"
    print("Seguridad de la contraseña:", password_strength)


def run_problem_6():
    print("\n=== Problema 6: Formateador de etiquetas de productos ===")
    product_name = input("Escribe el nombre del producto: ").strip()
    price_text = input("Escribe el precio del producto: ").strip()
    if not product_name:
        print("Error: entrada no válida")
        return
    try:
        price_value = float(price_text)
    except ValueError:
        print("Error: entrada no válida")
        return
    if price_value <= 0:
        print("Error: el precio debe ser positivo")
        return
    label_text = f"Product: {product_name} | Price: $\{price_value:.2f}"
    label_text = label_text[:30].ljust(30)
    print("Etiqueta:", repr(label_text))
    print("Longitud de la etiqueta:", len(label_text))

# DOCUMENTACIÓN DE LOS PROBLEMAS
# Problema 1: Formateador de nombres completos
# Descripción: elimina espacios sobrantes, aplica formato de título al nombre y obtiene las iniciales.
# Entradas: full_name, una cadena de texto. Salidas: nombre formateado e iniciales.
# Validaciones: se requieren al menos dos palabras.
# Pruebas: normal: "juan carlos tovar" -> Juan Carlos Tovar / J.C.T.; límite: "ana lopez" -> Ana Lopez / A.L.; error: "Marcos" -> mensaje de error.
#
# Problema 2: Validador básico de correo electrónico
# Descripción: comprueba la estructura básica de un correo y muestra el dominio si parece válido.
# Entradas: email_text. Salidas: resultado verdadero/falso y dominio cuando corresponde.
# Validaciones: exactamente un símbolo @, sin espacios, parte local no vacía y dominio con punto.
# Pruebas: normal: "student@example.com" -> verdadero; límite: "a@b.co" -> verdadero; error: "student example.com" -> falso.
# Esta comprobación es básica y no sustituye una validación completa del estándar de correo.
#
# Problema 3: Comprobador de palíndromos
# Descripción: compara una frase con su versión invertida, ignorando espacios y diferencias entre mayúsculas y minúsculas.
# Entradas: phrase. Salidas: frase normalizada y resultado booleano.
# Validaciones: al menos tres caracteres que no sean espacios.
# Pruebas: normal: "Anita lava la tina" -> verdadero; límite: "abc" -> falso; error: texto con solo espacios -> mensaje de error.
# Los signos de puntuación no se eliminan.
#
# Problema 4: Estadísticas de palabras en una oración
# Descripción: muestra el número de palabras, la primera y última, y las palabras más corta y más larga.
# Entradas: sentence. Salidas: cantidad y cuatro estadísticas de palabras.
# Validaciones: split() debe producir al menos una palabra.
# Pruebas: normal: "Python is very useful" -> 4 palabras; límite: "Hola" -> una palabra para todas las posiciones; error: texto vacío -> entrada no válida.
#
# Problema 5: Clasificador de seguridad de contraseñas
# Descripción: clasifica la contraseña como débil, media o fuerte según su longitud y tipos de caracteres.
# Entradas: password_input. Salidas: nivel de seguridad.
# Validaciones: la contraseña no debe estar vacía; para ser fuerte requiere 8 caracteres, mayúsculas, minúsculas, dígito y símbolo.
# Para ser media requiere al menos 8 caracteres y una combinación de tipos de caracteres.
# Pruebas: normal: "Hello123!" -> fuerte; límite: "hello" -> débil; error: texto vacío -> entrada no válida.
#
# Problema 6: Formateador de etiquetas de productos
# Descripción: crea una etiqueta y la ajusta a exactamente 30 caracteres, recortando o agregando espacios.
# Entradas: product_name y un precio numérico positivo. Salidas: etiqueta y longitud.
# Validaciones: nombre no vacío y precio numérico mayor que 0.
# Pruebas: normal: "Pen", "12.5" -> longitud 30; límite: nombre muy largo -> recorte a 30 caracteres; error: precio "-2" -> mensaje de error.


def main():
    functions = {"1": run_problem_1, "2": run_problem_2, "3": run_problem_3,
                 "4": run_problem_4, "5": run_problem_5, "6": run_problem_6}
    while True:
        print("\n=== Práctica de cadenas de texto en Python ===")
        print("1. Formateador de nombres\n2. Validador de correo\n3. Comprobador de palíndromos")
        print("4. Estadísticas de oración\n5. Seguridad de contraseña\n6. Etiqueta de producto\n0. Salir")
        choice = input("Elige un problema (0-6): ").strip()
        if choice == "0":
            print("¡Hasta luego!")
            break
        function = functions.get(choice)
        if function is None:
            print("Error: entrada no válida")
        else:
            function()


if __name__ == "__main__":
    main()

# CONCLUSIONES
# Las cadenas son esenciales para recibir, procesar y mostrar texto.
# strip() y split() limpian la entrada y la separan en partes útiles.
# lower() y upper() permiten comparar texto de forma consistente cuando no importan las mayúsculas.
# La validación reduce errores causados por entradas vacías o con formato incorrecto.
# El uso de segmentos permite extraer partes del texto y revertir cadenas para comprobar palíndromos.
# Como las cadenas son inmutables, las transformaciones producen nuevos valores de texto.
#
# REFERENCIAS
# 1) Python Software Foundation. (s. f.). Tipo de secuencia de texto: str. https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python Software Foundation. (s. f.). Métodos de cadenas. https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python Software Foundation. (s. f.). Operaciones comunes con cadenas. https://docs.python.org/3/library/string.html
# 4) Python Software Foundation. (s. f.). Entrada y salida. https://docs.python.org/3/tutorial/inputoutput.html
# 5) Python Software Foundation. (s. f.). Errores y excepciones. https://docs.python.org/3/tutorial/errors.html
# REPOSITORIO DE GITHUB: agrega la URL después de subir este archivo a GitHub.
