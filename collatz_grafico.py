import matplotlib.pyplot as plt

def collatz_grafico(n):
    """
    Genera secuencia de Collatz y crea grafico visual
    """
    secuencia = [n]
    
    while True:
        if len(secuencia) >= 3 and secuencia[-3:] == [4, 2, 1]:
            break
        
        ultimo = secuencia[-1]
        if ultimo % 2 == 0:
            siguiente = ultimo // 2
        else:
            siguiente = 3 * ultimo + 1
        
        secuencia.append(siguiente)
    
    return secuencia

def generar_grafico(secuencia, numero):
    """
    Crea un grafico de la secuencia de Collatz
    """
    plt.figure(figsize=(12, 6))
    plt.plot(secuencia, 'b-o', linewidth=1, markersize=4)
    plt.title(f'Secuencia de Collatz para n = {numero}\n(Longitud: {len(secuencia)} pasos)')
    plt.xlabel('Paso')
    plt.ylabel('Valor')
    plt.grid(True, alpha=0.3)
    
    # Resaltar la secuencia 4,2,1
    for i in range(len(secuencia) - 2):
        if secuencia[i:i+3] == [4, 2, 1]:
            plt.axvspan(i, i+2, alpha=0.3, color='red', label='Secuencia 4,2,1')
            break
    
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'collatz_{numero}.png', dpi=150)
    plt.show()

def main():
    print("=== GENERADOR DE GRAFICOS COLLATZ ===")
    
    try:
        numero = int(input("Ingrese un numero (1-100) para generar grafico: "))
        
        if numero < 1 or numero > 100:
            print("Numero fuera del rango permitido")
            return
        
        secuencia = collatz_grafico(numero)
        generar_grafico(secuencia, numero)
        
        print(f"\nGrafico guardado como 'collatz_{numero}.png'")
        print(f"Secuencia: {secuencia}")
        
    except ValueError:
        print("Error: Ingrese un numero valido")

if __name__ == "__main__":
    main()