import random

arreglo_binario = []

# Generar 8 números binarios de 9 bits cada uno
for _ in range(8):
    numero_binario = ''.join(str(random.randint(0, 1)) for _ in range(9))
    arreglo_binario.append(numero_binario)


# Función para convertir un número binario con signo y ajuste a su equivalente decimal
def binario_con_signo_a_decimal(numero_binario):
    signo = int(numero_binario[0])  # Primer bit representa el signo
    valor_absoluto = int(numero_binario[1:-1], 2)  # Convertir los bits restantes a decimal

    if numero_binario[-1] == '1':
        valor_absoluto += 0.5  # Agregar 0.5 si el último bit es 1

    return (-1) ** signo * valor_absoluto  # Aplicar el signo al valor absoluto


def evaluar_expresion(decimal):
    resultado = 2 * (decimal ** 2) + 3 * decimal - 4
    return resultado

print("Arreglo Inicial:")
# Evaluar cada número binario generado en la función y mostrar los resultados
for numero_binario in arreglo_binario:
    decimal_correspondiente = binario_con_signo_a_decimal(numero_binario)
    resultado_evaluacion = evaluar_expresion(decimal_correspondiente)
    print(f"Número binario: {numero_binario} | Decimal: {decimal_correspondiente} | Resultado: {resultado_evaluacion}")
print("\n")


##############
# Función para realizar cruzamientos entre todos los elementos del arreglo
def cruzar_todos_numeros_binarios(arreglo_binario):
    cantidad_elementos = len(arreglo_binario)
    for i in range(cantidad_elementos // 2):
        indice_a = i
        indice_b = cantidad_elementos - 1 - i

        # Generar la cantidad de dígitos a cambiar (entre 1 y 8)
        cantidad_digitos_cambio = random.randint(1, 8)

        # Obtener los números binarios seleccionados para el cruzamiento
        numero_a = arreglo_binario[indice_a]
        numero_b = arreglo_binario[indice_b]

        # Realizar el cruzamiento intercambiando los últimos dígitos
        nuevo_numero_a = numero_a[:-cantidad_digitos_cambio] + numero_b[-cantidad_digitos_cambio:]
        nuevo_numero_b = numero_b[:-cantidad_digitos_cambio] + numero_a[-cantidad_digitos_cambio:]

        # Actualizar los números en el arreglo binario
        arreglo_binario[indice_a] = nuevo_numero_a
        arreglo_binario[indice_b] = nuevo_numero_b

    return arreglo_binario

##################### REPETIR 10 VECES ##################

# Función para repetir el proceso de encontrar números decimales, su signo y fracción
def repetir_proceso(arreglo_binario, repeticiones=10):
    i = 0
    for _ in range(repeticiones):
        # Realizar el cruzamiento entre todos los números binarios
        arreglo_binario = cruzar_todos_numeros_binarios(arreglo_binario)
        i += 1
        print("\n--- iteración ",i,"---\n")
        for numero_binario in arreglo_binario:
            decimal_correspondiente = binario_con_signo_a_decimal(numero_binario)
            resultado_evaluacion = evaluar_expresion(decimal_correspondiente)
            print(f"Número binario: {numero_binario} | Decimal: {decimal_correspondiente} | Resultado: {resultado_evaluacion}")
        



repetir_proceso(arreglo_binario, repeticiones=10)
