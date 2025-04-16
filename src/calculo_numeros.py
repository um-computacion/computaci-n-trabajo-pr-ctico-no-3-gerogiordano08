def ingrese_numero():
    while True:
        try:
            entrada = input("Ingresa un número positivo: ")
            numero = int(entrada)
            print(f"Número ingresado: {numero}")
        except ValueError:
            print("Error: Debes ingresar un número válido.")
if __name__ == "__main__":
    numero = ingrese_numero()
    print(f"El número ingresado es: {numero}")