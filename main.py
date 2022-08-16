datos = {"codigo": ["001", "002", "003", "004", " 005"],
          "nombre": ["Juan", "David", "Smith", "Erick", "Fiorella"],
         "curso": ["Arte", "Algoritmos", "Diseño", "Matematicas","Comunicacion"]}
nota_ = []
resp = "s"
while resp == "s":
    codigo = input("Ingresar el codigo del alumno: ")
    curso = input("Ingresa el nombre del curso: ")
    nota_1 = int(input("Nota1: "))
    nota_2 = int(input("Nota2: "))
    nota_3 = int(input("Nota3: "))
    nota_4 = int(input("Nota4: "))
    x = 0
    for i in datos["codigo"]:
        if i == codigo:
            codigoTemp = i
            nombreTemp = datos["nombre"][x]
            promedio = (nota_1 + nota_2 + nota_3 + nota_4)/4
            registro = ["Codigo: " + str(codigoTemp) + " | " + "Nombre :" + str(nombreTemp) + " | " + "Curso :" + curso + " | " + "Promedio: " + str(promedio) + " | " +"Nota 1: " + str(nota_1) + "| " + "Nota 2: " + str(nota_2) + " | " + "Nota 3: " + str(nota_3) + " | " + "Nota 4: " + str(nota_4)]
            f = open("examen_final.txt", "a")
            cadena = "".join(registro)
            f.write("\n" + cadena)
        x += 1
    resp = input("¿Desea seguir ingresando datos? : s/n ")
    f = open("examen_final.txt")
    print(f.read())
    f.close()