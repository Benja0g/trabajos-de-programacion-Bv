import funciones.cuadrilatero

def menu_principal():
    print()
    print("Cálculo de funciones geométricas.")
    print("1: Perimetro")
    print("2: Área")
    print("3: Volumen")
    print("0: Salir")
    print()

menu_principal()

while True:
    opcion = input("Seleccione su Opción (0-3): ")
    if opcion == "1":
      ancho = int(input("ingrese el ancho: "))
      largo = int(input("ingrese el largo: "))
      print(funciones.cuadrilatero.perimetro(ancho,largo))

    elif opcion == "2":
        ancho = int(input("ingrese el ancho: "))
        largo = int(input("ingrese el largo: "))
        print(funciones.cuadrilatero.area(ancho,largo))
    elif opcion == "3":
        ancho = int(input("ingrese el ancho: "))
        largo = int(input("ingrese el largo: "))
        alto = int(input("ingrese el alto: "))
    elif opcion == "0":
        print("saliendo del sistema...")
        break
    else:
        print("opcion invalida")

