def girar(palindromo):
    return palindromo[::-1]

def main():
    palabra = input("escribe una palabra: ")
    palabra = palabra.lower()

    girada = girar(palabra)

    if palabra == girada:
        print("si es palindromo")
    else:
        print("no es palindromo")

main()