def es_palindromo_recursivo(palabra):
    # Caso base 1: Si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    
    # Caso base 2: Si la primera y la última letra son distintas, NO es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    
    # Llamada recursiva: Quitamos la primera y la última letra y repetimos
    return es_palindromo_recursivo(palabra[1:-1])

def main():
    palabra = input("Escribe una palabra: ").lower()
    
    if es_palindromo_recursivo(palabra):
        print("si es palindromo")
    else:
        print("no es palindromo")

if __name__ == "__main__":
    main()