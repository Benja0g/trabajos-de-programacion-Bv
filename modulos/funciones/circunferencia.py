import math
#Definir tres funciones.... calculo perimetro, area y volumen....
pi = math.pi
def perimetro_circ(radio):
    return radio * pi * 2

def area_circ(radio):   
    return radio ** 2 * pi
    

def volumen_circ(radio):
    return 4/3 * pi * radio **3