palabra = input("escribe una palabra: ")
palabra = palabra.lower()

al_reves = palabra[::-1]

if palabra == al_reves:
    print("si es palindromo")
else:
    print("no es palindromo")