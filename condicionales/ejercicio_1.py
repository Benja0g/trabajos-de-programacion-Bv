#Crear un programa que convierta unidades de temperatura
#1._ el usuario deberá ingresar el valor de T°.
#2._ el usuario deberá ingresar escala de T° original.
#3._ el usuario deberá ingresar escala de T° final.
#4._ el sistema deberá entregar resultados de conversion

# de °C a °K => °C + 273.15
# de °K a °C => °K + 273.15

# de °C a °F => (°C * 9/5) + 32
# de °F a °C => (°F -32) * 5/9

# de °F a °K => (°F -32) * 5/9 + 273.15
# de °K a °F => ((°K - 273.15)* 9/5) + 32


#DEFINIR FUNCION
def convertidor_temp(temperatura, inicio, fin):
    #DEFINIR RESULTADO
    resultado = 0.0
    #CREAR CONDICIONAL DE DISTINTAS ESCALAS
    if inicio == "K":
        if fin == "C":
            resultado = temperatura - 273.15
        elif fin == "F":
            resultado = ((temperatura - 273.15)* 9/5) + 32
        else:
            print("escala final erronea")
    elif inicio == "C":
        if fin == "K":
            resultado = temperatura + 273.15
        elif fin == "F":
            resultado = (temperatura * 9/5) + 32
        else:
            print("Escala final erronea")
    elif inicio == "F":
        if fin == "K":
            resultado = (temperatura - 32) * 5/9 + 273.15
        elif fin == "C":
            resultado = (temperatura - 32) * 5/9
        else:
            print("escala final erronea")
    else:
        print("escala inicial erronea")
    
    print(resultado)
        
temp = float(input("ingrese su temperatura a convertir: "))
escala_inicial = input("Indique escala inicial: C, F o K: ").upper().strip()
escala_final = input("Ingrese escala final: C, F o K: ").upper().strip()
#EJECUTAR FUNCION
convertidor_temp(temp,escala_inicial,escala_final)