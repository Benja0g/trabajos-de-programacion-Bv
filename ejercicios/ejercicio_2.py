

# lista_peliculas = ["Destino Final", "eternauta", "Lilo y Stich", "Los Piratas del Caribe", "El bueno, el malo y el feo"]

# contador = 1
# for pelicula in lista_peliculas:
#     print(f"{contador}.-{pelicula}")
#     contador = contador + 1
#print()
# for i in range(len(lista_peliculas)):
#     print(f"{i}.-{lista_peliculas[i]}")
    
# print()
# print(f"3.-:{lista_peliculas[2]} ")

# print(len("DOTA"))
# print(len(range(10)))

lista_estudiantes = [
    ['Aquiles Baeza', [6.5,5.7,6.3]],
    ["Wendy sulca", [5.0,4.7,5.8]],
    ["Peter Parker", [7.0,6.8,7.0]],
    ["Delfin Quispe", [4.3,3.8,2.9]]
]
# for i in range(len(lista_estudiantes)):
#     print(f"{i}.-{lista_estudiantes[i]}")

# print()
# contador = 1
# for estudiante in lista_estudiantes:
#     print(f"{contador}.-{estudiante}")
#     contador = contador + 1

# print()
# for estudiante in lista_estudiantes:
#     for i in range (len(estudiante)):
#         print(estudiante)

# for x in range(len(lista_estudiantes)):
#     for estudiante in (lista_estudiantes[x]):
#         print(estudiante[0])

rango = [0,1,2]
for estudiante in lista_estudiantes:
    print(estudiante[0])
    suma = 0
    for i in range(len(estudiante[1])):
        suma = suma + estudiante[1][i]
        promedio = suma / len(estudiante[1])
    print(f"{estudiante[0]}, Notas:{estudiante[1]}, Promedio : {round(promedio,1)}")
    print()
