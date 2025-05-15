from funciones.cuadrilatero import perimetro_cuad,area_cuad,volumen_cuad
from funciones.circunferencia import perimetro_circ,area_circ,volumen_circ
import math

def menu():
    print()
    print("Cálculo de funciones geométricas.")
    print("1: Perimetro")
    print("2: Área")
    print("3: Volumen")
    print("0: Salir")
    print()


def sub_menu():
    print()
    print("Cálculo de funciones geométricas.")
    print("1: cuadrilatero")
    print("2: circunferencia")
    print("0: salir")
    print()
    

def programa_principal():
    while True:
        menu()
        opcion = input("Seleccione su Opción (0-3): ")
        
        if opcion == "1":
            sub_menu()
            opcion_sub_menu = input("seleccione su opción (0-3): ")
           
            if opcion_sub_menu == "1":
                ancho = float(input("ingrese el ancho: "))
                largo = float(input("ingrese el largo: "))
                print(f"perimetro: {perimetro_cuad(ancho,largo)}")
            
            
            elif opcion_sub_menu == "2":
                radio = float(input("Ingrese el radio: "))
                print(f"perimetro: {perimetro_circ(radio)}")
        
            elif opcion_sub_menu == "0":
                print("volviendo al menu..")
                menu()
                
            else:
                print("opcion invalida")
                return
            
        elif opcion == "2":
            sub_menu()
            opcion_sub_menu = input("seleccione su opción (0-3): ")
            if opcion_sub_menu == "1":
                ancho = float(input("ingrese el ancho: "))
                largo = float(input("ingrese el largo: "))
                print(f"area: {area_cuad(ancho,largo)}")
            
            elif opcion_sub_menu == "2":
                radio = float(input("ingrese el radio: "))
                print(f"area: {area_circ(radio)}")
            
            elif opcion_sub_menu == "0":
                print("volviendo al menu..")
                menu()
            else:
                print("opcion invalida")
                return
        
        elif opcion == "3":
            sub_menu()
            opcion_sub_menu = input("seleccione su opción (0-3): ")
            if opcion_sub_menu == "1":
               ancho = float(input("ingrese el ancho: ")) 
               largo = float(input("ingrese el largo: "))
               alto = float(input("ingrese el alto;: "))
               print(f"volumen: {volumen_cuad(ancho,largo,alto)}")
            
            elif opcion_sub_menu == "2":
                radio = float(input("ingrese el radio: "))
                print(f"volumen: {volumen_circ(radio)}")
            elif opcion_sub_menu == "0":
                print("volviendo al menu..")
                menu()
            else:
                print("opcion invalida")
                return

        elif opcion == "0":
            print("saliendo del sistema....")
            break
        
        else:
            print("opción invalida...")

programa_principal()
                
        

    

            
    

    
