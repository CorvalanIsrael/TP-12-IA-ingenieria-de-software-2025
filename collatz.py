def collatz(n):
    """
    Implementa el algoritmo de la Conjetura de Collatz según los requerimientos:
    - Si es par: dividir entre 2
    - Si es impar: multiplicar por 3 y sumar 1
    - Se detiene solo cuando encuentra la secuencia 4,2,1 de manera consecutiva
    - Si llega a 1 sin la secuencia, continúa
    
    Args:
        n (int): Número entero positivo entre 1 y 100
    
    Returns:
        list: Secuencia completa hasta encontrar 4,2,1 consecutivos
    """
    if not isinstance(n, int) or n < 1 or n > 100:
        raise ValueError("El número debe ser un entero positivo entre 1 y 100")
    
    secuencia = [n]
    
    # Continuar hasta encontrar la secuencia 4,2,1 consecutiva
    while True:
        # Verificar si los últimos 3 elementos son 4,2,1
        if len(secuencia) >= 3:
            ultimos_tres = secuencia[-3:]
            if ultimos_tres == [4, 2, 1]:
                break
        
        # Aplicar reglas de Collatz al último elemento
        ultimo = secuencia[-1]
        if ultimo % 2 == 0:  # Par
            siguiente = ultimo // 2
        else:  # Impar
            siguiente = 3 * ultimo + 1
        
        secuencia.append(siguiente)
    
    return secuencia

def mostrar_secuencia_detallada(secuencia):
    """Muestra la secuencia con formato detallado"""
    print(" → ".join(map(str, secuencia)))
    
    # Resaltar la secuencia 4,2,1
    for i in range(len(secuencia) - 2):
        if secuencia[i:i+3] == [4, 2, 1]:
            print(f"\n¡Secuencia 4,2,1 encontrada en las posiciones {i+1}-{i+3}!")
            break

def main():
    print("=== ALGORITMO DE COLLATZ - IMPLEMENTACIÓN ESPECÍFICA ===")
    print("Requerimientos implementados:")
    print("- Rango: números del 1 al 100")
    print("- Si es par → dividir entre 2")
    print("- Si es impar → multiplicar por 3 y sumar 1")
    print("- Se detiene SOLO al encontrar 4,2,1 consecutivos")
    print("- Si llega a 1 sin la secuencia, continúa ejecutándose")
    print()
    
    try:
        numero = int(input("Ingrese un número entero (1-100): "))
        
        if numero < 1 or numero > 100:
            print("Error: El número debe estar entre 1 y 100")
            return
        
        print(f"\nCalculando secuencia para el número {numero}...")
        secuencia = collatz(numero)
        
        print(f"\nSECUENCIA COMPLETA:")
        mostrar_secuencia_detallada(secuencia)
        
        print(f"\nESTADÍSTICAS:")
        print(f"- Longitud total: {len(secuencia)} pasos")
        print(f"- Valor máximo: {max(secuencia)}")
        print(f"- Posición donde comienza 4,2,1: {len(secuencia)-2}")
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()