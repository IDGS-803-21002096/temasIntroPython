from io import open

class Diccionario:

    def __init__(self, palabraEspañol="", palabraIngles=""):
        self.palabraEspañol = palabraEspañol
        self.palabraIngles = palabraIngles

    def guardar(self):
        with open("palabras.txt", "a") as archivo:
            archivo.write("{}:{}\n".format(self.palabraEspañol, self.palabraIngles))
        print("Se guardó correctamente {} : {}".format(self.palabraEspañol, self.palabraIngles))

    def buscar(self, palabra):
            with open("palabras.txt", "r") as archivo:
                for linea in archivo:
                    palabraEsp, palabraIng = linea.strip().split(":") #Strip elimina espacios en blanco u otros caracteres y split divide una cadena en una lista
                    if palabra == palabraEsp or palabra == palabraIng:
                        print("Palabra encontrada: {} : {}".format(palabraEsp, palabraIng))
                        return
                print("Palabra no encontrada")

def funcion1():
    print("Ingresa las palabras a guardar: ")
    palabraEspañol = input("Palabra en español: ")
    palabraIngles = input("Palabra en inglés: ")
    obj = Diccionario(palabraEspañol, palabraIngles)
    obj.guardar()

def funcion2():
    while True:
        print("\nMenú de búsqueda:")
        print("1.- Buscar palabra en Español")
        print("2.- Buscar palabra en Inglés")
        print("3.- Regresar")
        opcion = int(input("Dame una opción: "))

        if opcion == 1:
            palabra = input("Escribe la palabra en español: ")
            obj = Diccionario()
            obj.buscar(palabra)
        elif opcion == 2:
            palabra = input("Escribe la palabra en inglés: ")
            obj = Diccionario()
            obj.buscar(palabra)
        elif opcion == 3:
            print("Regresando")
            break

def run():
    while True:
        print("\nMenú de opciones:")
        print("1.- Capturar palabras")
        print("2.- Buscar palabras")
        print("3.- Salir")
        opcion = int(input("Dame una opción: "))

        if opcion == 1:
            funcion1()
        elif opcion == 2:
            funcion2()
        elif opcion == 3:
            print("Saliendo...")
            break

if __name__ == "__main__":
    run()
