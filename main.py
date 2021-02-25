menu = True
datos = ""

while menu:
    print("Menu Principal")
    print("     1.- Cargar archivo")
    print("     2.- Procesar archivo")
    print("     3.- Escribir archivo salida")
    print("     4.- Mostrar datos del estudiante")
    print("     5.- Generar Gráfica")
    print("     6.- Salir")
    opcion = input("Ingrese su opción >_ ")
    if opcion == "1":
        ruta = input("Ingrese la ruta del archivo a cargar >_ ")
        print("Leyendo archivo...")
        try:
            f = open(ruta, 'r')
            datos = f.read()
            print("Datos de archivos cargados a memoria exitosamente")
            f.close()
        except FileNotFoundError:
            print("Algo salió mal, archivo no puedo ser cargado!")
            input("Ingrese una nueva ruta")

    elif opcion == "2":
        print("Procesando archivo...")
    elif opcion == "3":
        print("Escribiendo archivo de salida")
    elif opcion == "4":
        print("Datos del estudiante:")
        print("Nombre: René Leonel de León Velásquez")
        print("Carnet: 201801643")
        print("Curso: Introducción a la Programación y Computación E")
        print("Carrera: Ingenieria en Ciencias y Sistemas")
        print("Semestre actual: 4to Semestre")
        input("Presione ENTER para continuar...")
    elif opcion == "5":
        print("Generando gráfica...")
    elif opcion == "6":
        print("Gracias por usar el programa!")
        menu = False
    else:
        print("INGRESE UNA OPCION CORRECTA")