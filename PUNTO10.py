import sys

def collatz_secuencia(n):
    """
    Implementa el algoritmo de Collatz según el requerimiento mejorado.
    Retorna la cantidad de iteraciones y la secuencia generada.
    """
    if not isinstance(n, int):
        return "Error: Debe ingresar un número entero."
    if n < 1 or n > 100:
        return "Error: El número debe estar entre 1 y 100."

    secuencia = [n]
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        secuencia.append(n)

        # Verificar si los tres últimos elementos son 4,2,1 consecutivos
        if len(secuencia) >= 3 and secuencia[-3:] == [4, 2, 1]:
            break

    iteraciones = len(secuencia) - 1
    return iteraciones, secuencia


# Programa principal con argumento por línea de comandos
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python collatz.py <número entero entre 1 y 100>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        resultado = collatz_secuencia(n)

        if isinstance(resultado, tuple):
            iteraciones, secuencia = resultado
            print(f"\nNúmero de entrada: {n}")
            print(f"Número de iteraciones: {iteraciones}")
            print(f"Secuencia generada: {secuencia}")
        else:
            print(f"\n{resultado}")

    except ValueError:
        print("Error: El argumento debe ser un número entero válido.")
