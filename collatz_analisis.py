def analizar_collatz(n):
    """
    Version de analisis que muestra el proceso paso a paso
    """
    print(f"\n--- ANALISIS DETALLADO PARA n = {n} ---")
    
    secuencia = [n]
    paso = 0
    
    while True:
        print(f"Paso {paso}: {secuencia[-1]}", end="")
        
        # Verificar condicion de parada
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
    Programa para analizar multiples casos de prueba
    """
    print("=== ANALISIS DE CASOS DE COLLATZ ===")
    
    # Casos de prueba interesantes
    casos_prueba = [1, 2, 3, 6, 27, 50, 97]
    
    for numero in casos_prueba:
        secuencia = analizar_collatz(numero)
        print(f"Secuencia completa: {secuencia}")
        print(f"Longitud: {len(secuencia)} pasos\n")
        print("-" * 50)

if __name__ == "__main__":
    main()