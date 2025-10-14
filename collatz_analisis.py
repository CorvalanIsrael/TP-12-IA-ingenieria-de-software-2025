def analizar_collatz(n):
    """
    Versión de análisis que muestra el proceso paso a paso
    """
    print(f"\n--- ANÁLISIS DETALLADO PARA n = {n} ---")
    
    secuencia = [n]
    paso = 0
    
    while True:
        print(f"Paso {paso}: {secuencia[-1]}", end="")
        
        # Verificar condición de parada
        if len(secuencia) >= 3 and secuencia[-3:] == [4, 2, 1]:
            print(" -> [SECUENCIA 4,2,1 DETECTADA - FIN]")
            break
        
        # Aplicar reglas
        actual = secuencia[-1]
        if actual % 2 == 0:
            siguiente = actual // 2
            print(f" (par) -> {siguiente}")
        else:
            siguiente = 3 * actual + 1
            print(f" (impar) -> {siguiente}")
        
        secuencia.append(siguiente)
        paso += 1
    
    return secuencia

def main():
    """
    Programa para analizar casos de prueba con opción de entrada personalizada
    """
    print("=== ANALISIS DE CASOS DE COLLATZ ===")
    
    opcion = input("¿Desea usar (P) casos predefinidos o (I) ingresar un numero? ").upper()
    
    if opcion == 'I':
        try:
            numero = int(input("Ingrese un numero (1-100) para analizar: "))
            if numero < 1 or numero > 100:
                print("Numero fuera del rango permitido")
                return
            casos_prueba = [numero]
        except ValueError:
            print("Error: Ingrese un numero valido")
            return
    else:
        # Casos de prueba predefinidos
        casos_prueba = [1, 2, 3, 6, 27, 50, 97]
        print("Usando casos predefinidos:", casos_prueba)
    
    for numero in casos_prueba:
        secuencia = analizar_collatz(numero)
        print(f"Secuencia completa: {secuencia}")
        print(f"Longitud: {len(secuencia)} pasos")
        
        # Estadísticas adicionales
        max_valor = max(secuencia)
        pos_max = secuencia.index(max_valor)
        print(f"Valor maximo: {max_valor} (en paso {pos_max})")
        print("-" * 50)

if __name__ == "__main__":
    main()