def collatz(n):
    """
    Implementa el algoritmo de la Conjetura de Collatz para un número dado.
    
    Args:
        n (int): Número entero positivo inicial
    
    Returns:
        list: Secuencia de números generada por el algoritmo
    """
    secuencia = [n]
    
    while n != 1:
        if n % 2 == 0:  # Si es par
            n = n // 2
        else:  # Si es impar
            n = 3 * n + 1
        secuencia.append(n)
        
        # Detener si encontramos la secuencia 4,2,1
        if len(secuencia) >= 3 and secuencia[-3:] == [4, 2, 1]:
            break
    
    return secuencia

def main():
    print("=== ALGORITMO DE LA CONJETURA DE COLLATZ ===")
    print("Reglas:")
    print("- Si el número es par, se divide entre 2")
    print("- Si el número es impar, se multiplica por 3 y se suma 1")
    print("- La secuencia termina al encontrar 4,2,1")
    print()
    
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        
        if numero <= 0:
            print("Error: Debe ingresar un número positivo.")
            return
        
        secuencia = collatz(numero)
        
        print(f"\nSecuencia para el número {numero}:")
        print(" → ".join(map(str, secuencia)))
        print(f"\nLongitud de la secuencia: {len(secuencia)} pasos")
        
        # Mostrar estadísticas
        pares = sum(1 for n in secuencia if n % 2 == 0)
        impares = len(secuencia) - pares
        print(f"Números pares en la secuencia: {pares}")
        print(f"Números impares en la secuencia: {impares}")
        print(f"Valor máximo alcanzado: {max(secuencia)}")
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()