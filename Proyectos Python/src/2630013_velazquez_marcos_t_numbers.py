# Actividad: Manejo de números y booleanos en Python
# Estudiante: Velazquez Marcos | Matrícula: 2630013 | Grupo: IM 1-1
# Archivo: 2630013_velazquez_marcos_t_numbers.py
#
# RESUMEN DE LA INVESTIGACIÓN
# Los enteros (int) representan números sin parte decimal; los flotantes (float) representan valores decimales.
# Los valores booleanos (True y False) representan los resultados de condiciones lógicas.
# Los operadores aritméticos realizan cálculos y los operadores relacionales comparan valores.
# Los operadores lógicos, como and y or, combinan condiciones para tomar decisiones.
# La validación evita rangos no permitidos, errores de conversión y divisiones entre cero.
# Este programa aborda temperatura, salarios, descuentos, estadísticas, préstamos e índice de masa corporal.
# Cada problema incluye entradas, salidas, validaciones y tres casos de prueba documentados.
#
# BUENAS PRÁCTICAS
# Utiliza int para cantidades enteras y float para valores decimales.
# Guarda los cálculos intermedios en variables con nombres descriptivos.
# Valida los rangos antes de calcular y evita la división entre cero.
# Utiliza nombres descriptivos para los valores booleanos y mensajes de error claros.


def run_problem_1():
    print("\n=== Problema 1: Conversor de temperatura ===")
    try:
        temp_c = float(input("Escribe la temperatura en Celsius: ").strip())
    except ValueError:
        print("Error: entrada no válida"); return
    temp_k = temp_c + 273.15
    if temp_k < 0:
        print("Error: la temperatura está por debajo del cero absoluto"); return
    temp_f = temp_c * 9 / 5 + 32
    is_high_temperature = temp_c >= 30.0
    print("Fahrenheit:", round(temp_f, 2))
    print("Kelvin:", round(temp_k, 2))
    print("Temperatura alta:", str(is_high_temperature).lower())


def run_problem_2():
    print("\n=== Problema 2: Horas trabajadas y tiempo extra ===")
    try:
        hours_worked = float(input("Escribe las horas trabajadas: ").strip())
        hourly_rate = float(input("Escribe el pago por hora: ").strip())
    except ValueError:
        print("Error: entrada no válida"); return
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: entrada no válida"); return
    regular_hours = min(hours_worked, 40.0)
    overtime_hours = max(hours_worked - 40.0, 0.0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    print("Pago regular:", round(regular_pay, 2))
    print("Pago por horas extra:", round(overtime_pay, 2))
    print("Pago total:", round(regular_pay + overtime_pay, 2))
    print("¿Tiene horas extra?:", str(hours_worked > 40).lower())


def run_problem_3():
    print("\n=== Problema 3: Elegibilidad para descuentos ===")
    try:
        purchase_total = float(input("Escribe el total de la compra: ").strip())
    except ValueError:
        print("Error: entrada no válida"); return
    is_student_text = input("¿El cliente es estudiante? (SI/NO): ").strip().upper()
    is_senior_text = input("¿El cliente es adulto mayor? (SI/NO): ").strip().upper()
    if purchase_total < 0 or is_student_text not in {"SI", "NO"} or is_senior_text not in {"SI", "NO"}:
        print("Error: entrada no válida"); return
    is_student = is_student_text == "SI"
    is_senior = is_senior_text == "SI"
    discount_eligible = is_student or is_senior or purchase_total >= 1000.0
    final_total = purchase_total * 0.9 if discount_eligible else purchase_total
    print("Tiene derecho al descuento:", str(discount_eligible).lower())
    print("Total final:", round(final_total, 2))


def run_problem_4():
    print("\n=== Problema 4: Estadísticas de tres números enteros ===")
    try:
        numbers_list = [int(input(f"Escribe el número entero {index}: ").strip()) for index in range(1, 4)]
    except ValueError:
        print("Error: entrada no válida"); return
    sum_value = sum(numbers_list)
    print("Suma:", sum_value)
    print("Promedio:", round(sum_value / len(numbers_list), 2))
    print("Máximo:", max(numbers_list))
    print("Mínimo:", min(numbers_list))
    print("¿Todos son pares?:", str(all(number % 2 == 0 for number in numbers_list)).lower())


def run_problem_5():
    print("\n=== Problema 5: Elegibilidad para un préstamo ===")
    try:
        monthly_income = float(input("Escribe el ingreso mensual: ").strip())
        monthly_debt = float(input("Escribe los pagos mensuales de deudas: ").strip())
        credit_score = int(input("Escribe la puntuación crediticia: ").strip())
    except ValueError:
        print("Error: entrada no válida"); return
    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: entrada no válida"); return
    debt_ratio = monthly_debt / monthly_income
    eligible = monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650
    print("Proporción de deuda:", round(debt_ratio, 3))
    print("Cumple los requisitos:", str(eligible).lower())


def run_problem_6():
    print("\n=== Problema 6: Índice de masa corporal (IMC) ===")
    try:
        weight_kg = float(input("Escribe el peso en kilogramos: ").strip())
        height_m = float(input("Escribe la estatura en metros: ").strip())
    except ValueError:
        print("Error: entrada no válida"); return
    if weight_kg <= 0 or height_m <= 0:
        print("Error: entrada no válida"); return
    bmi = weight_kg / (height_m ** 2)
    print("IMC:", round(bmi, 2))
    print("Bajo peso:", str(bmi < 18.5).lower())
    print("Peso normal:", str(18.5 <= bmi < 25.0).lower())
    print("Sobrepeso:", str(bmi >= 25.0).lower())

# DOCUMENTACIÓN DE LOS PROBLEMAS
# Problema 1: Conversión de temperatura y evaluación de rango
# Descripción: convierte Celsius a Fahrenheit y Kelvin, y verifica si Celsius es al menos 30 grados.
# Entradas: temp_c como número decimal. Salidas: Fahrenheit, Kelvin y valor booleano de temperatura alta.
# Validaciones: entrada numérica y temperatura Kelvin no menor que cero.
# Pruebas: normal: 25 -> 77 °F / 298.15 K / falso; límite: 30 -> 86 °F / 303.15 K / verdadero; error: "caliente" o -300 -> error.
#
# Problema 2: Horas trabajadas y pago por tiempo extra
# Descripción: paga normalmente hasta 40 horas y las horas adicionales al 150 % de la tarifa por hora.
# Entradas: hours_worked y hourly_rate. Salidas: pago regular, pago extra, pago total y valor booleano.
# Validaciones: horas mayores o iguales a cero y tarifa mayor que cero.
# Pruebas: normal: 45 horas y tarifa 100 -> 4000 / 750 / 4750; límite: 40 y 100 -> total 4000 sin tiempo extra; error: horas -1 o tarifa 0.
#
# Problema 3: Elegibilidad para descuentos con valores booleanos
# Descripción: aplica un descuento del 10 % a estudiantes, adultos mayores o compras de al menos 1000.
# Entradas: purchase_total y respuestas SI/NO para estudiante y adulto mayor. Salidas: elegibilidad y total final.
# Validaciones: total mayor o igual a cero y respuestas limitadas a SI o NO.
# Pruebas: normal: 500, SI, NO -> 450; límite: 1000, NO, NO -> 900; error: respuesta MAYBE -> entrada no válida.
#
# Problema 4: Estadísticas de tres números enteros
# Descripción: calcula suma, promedio, máximo, mínimo y si todos los números son pares.
# Entradas: tres números enteros. Salidas: suma, promedio, máximo, mínimo y valor booleano.
# Validaciones: cada entrada debe convertirse a int; se permiten números negativos.
# Pruebas: normal: 2, 4, 6 -> suma 12, promedio 4, verdadero; límite: 0, 0, 0 -> todos pares; error: 2, abc, 6 -> entrada no válida.
#
# Problema 5: Elegibilidad para un préstamo
# Descripción: verifica ingreso mínimo, proporción de deuda menor o igual a 0.4 y puntuación crediticia de al menos 650.
# Entradas: ingreso mensual, deuda mensual y puntuación crediticia. Salidas: proporción de deuda y elegibilidad.
# Validaciones: ingreso mayor que cero, deuda y puntuación mayores o iguales a cero.
# Pruebas: normal: 10000, 3000, 700 -> cumple; límite: 8000, 3200, 650 -> cumple; error: ingreso 0 -> entrada no válida y evita división entre cero.
#
# Problema 6: Índice de masa corporal y categorías
# Descripción: calcula el IMC y determina si corresponde a bajo peso, peso normal o sobrepeso.
# Entradas: weight_kg y height_m. Salidas: IMC y tres valores booleanos.
# Validaciones: peso y estatura deben ser mayores que cero.
# Pruebas: normal: 70 kg y 1.75 m -> IMC 22.86, peso normal; límite: 50 kg y 1.6 m -> IMC 19.53, peso normal; error: peso o estatura 0.


def main():
    functions = {"1": run_problem_1, "2": run_problem_2, "3": run_problem_3,
                 "4": run_problem_4, "5": run_problem_5, "6": run_problem_6}
    while True:
        print("\n=== Práctica de números y valores booleanos en Python ===")
        print("1. Conversor de temperatura\n2. Horas extra\n3. Descuentos")
        print("4. Estadísticas de enteros\n5. Préstamos\n6. Índice de masa corporal\n0. Salir")
        choice = input("Elige un problema (0-6): ").strip()
        if choice == "0":
            print("¡Hasta luego!"); break
        function = functions.get(choice)
        if function is None:
            print("Error: entrada no válida")
        else:
            function()


if __name__ == "__main__":
    main()

# CONCLUSIONES
# Los enteros y los flotantes se utilizan en conjunto para conteos, mediciones y cálculos financieros.
# Las comparaciones producen valores booleanos que permiten al programa tomar decisiones.
# La validación de rangos rechaza datos inadecuados antes de realizar los cálculos.
# Verificar los divisores antes de dividir evita errores por división entre cero.
# Los operadores and/or combinan condiciones para evaluar requisitos y categorías.
# Estos recursos son útiles para nóminas, descuentos, evaluación de préstamos y mediciones.
#
# REFERENCIAS
# 1) Python Software Foundation. (s. f.). Tipos integrados. https://docs.python.org/3/library/stdtypes.html
# 2) Python Software Foundation. (s. f.). Tipos numéricos: int, float y complex. https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 3) Python Software Foundation. (s. f.). Tipo booleano: bool. https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 4) Python Software Foundation. (s. f.). Expresiones. https://docs.python.org/3/reference/expressions.html
# 5) Python Software Foundation. (s. f.). Errores y excepciones. https://docs.python.org/3/tutorial/errors.html
# REPOSITORIO DE GITHUB: agrega la URL después de subir este archivo a GitHub.