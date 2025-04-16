from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero(loop=True):
    while True:
        try:
            entrada = input("Ingresa un número positivo: ")
            numero = int(entrada)
            if numero < 0:
                raise NumeroDebeSerPositivo("El número debe ser mayor o igual a cero.")
            print(f"Número ingresado: {numero}")
            return numero
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
            if not loop:
                raise  
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            if not loop:
                raise  

        if not loop:
            break

if __name__ == "__main__":
    numero = ingrese_numero()
    print(f"El número ingresado es: {numero}")