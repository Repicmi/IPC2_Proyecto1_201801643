import os
import xml.etree.ElementTree as ET
menu = True
datos = ""
matrices = []


class DatosMatriz:
    def __init__(self, datosArbol, nombre, n, m, grupo):
        self.datosArbol = datosArbol
        self.nombre = nombre
        self.n = n
        self.m = m
        self.grupo = grupo


class Nodo:
    def __init__(self, objeto):
        self.objeto = objeto
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregarNodo(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
        else:
            self.ultimo.siguiente = nuevo
            nuevo.siguiente = self.primero
            self.primero = nuevo

    def agregarNodoFinal(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero

    def quitarNodoInicio(self):
        if self.primero is None:
            print("Imposible eliminar elemento, lista vacía")
        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            temp = self.primero
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero
            temp = None

    def quitarNodoFinal(self):
        if self.primero is None:
            print("Imposible eliminar elemento, lista vacía")
        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            correcto = True
            temp = self.primero
            while correcto:
                if temp.siguiente == self.ultimo:
                    temp2 = self.ultimo
                    self.ultimo = temp
                    self.ultimo.siguiente = self.primero
                    temp2 = None
                    correcto = False
                else:
                    temp = temp.siguiente


def crearGrafica(datos):
    repeticion = 1
    columna = 0
    fila = 0
    contenido = [[0 for x in range(int(datos.m))] for y in range(int(datos.n))]

    for x in range(int(datos.n)):
        for y in range(int(datos.m)):
            if datos.grupo > 1:
                fila = datos.grupo-1

            contenido[x][y] = datos.datosArbol[fila][columna].text
            columna += 1


    datos_grafo = 'digraph G{ \n' \
                  'A[label="' + datos.nombre + '" shape="box", style=filled, fillcolor="burlywood"]\n' \
                  'B[label="Dimensiones n = ' + datos.n + ' m = ' + datos.m + ' " shape="box", style=filled, fillcolor="burlywood"]\n' \
                  'A -> B\n' \

    for i in range(datos.grupo):
        if repeticion == datos.grupo:
            numLabel = 0
            contador = 0
            primero = 0
            ene = int(datos.n)
            eme = int(datos.m)
            #print("AHUEVO, grupo de datos: " + str(repeticion))
            for a in range(ene):
                for b in range(eme):
                    contador += 1
                    datos_grafo += str(numLabel) + '[label="' + str(contenido[a][b]) + '" shape="egg", style=filled, fillcolor="burlywood1"]\n'
                    if primero == 0:
                        datos_grafo += "B -> " + str(numLabel) + " \n"
                        primero += 1
                    if contador == 2:
                        datos_grafo += str(numLabel-1) + ' -> ' + str(numLabel) + "\n"
                        contador = 0
                        if b < eme-1:
                            datos_grafo += str(numLabel) + ' -> ' + str(numLabel+1) + "\n"
                    numLabel += 1
                primero = 0
        else:
            print("No se pudo banda, grupo: " + str(repeticion))
        repeticion += 1
    datos_grafo += "}"
    file = open("grafo.dot", "w")
    file.write(datos_grafo)
    file.close()
    os.system("dot -Tpng grafo.dot -Gcharset=latin1 -o grafo.png ")
    os.startfile("grafo.png")


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
        arbol = ET.fromstring(datos)
        childNum = 1
        for child in arbol:
            print("Nombre = " + child.get("nombre") + " n = " + child.get("n") + " m = " + child.get("m")) #AQUI SALE LA N LET'S FUCKING GOOOO
            print("Imprimiendo grupo de datos: " + str(childNum))
            print(child.tag, child.attrib) #Nos da el elemento nombre, n y m :D
            nuevoDato = DatosMatriz(arbol, child.get("nombre"), child.get("n"), child.get("m"), childNum)
            matrices.append(nuevoDato)
            childNum += 1

        print(arbol[0][3].text) #Nos muestra el contenido en ese espacio x,y

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
        print("Generando gráfica(s)...")
        for elemento in matrices:
            crearGrafica(elemento)
    elif opcion == "6":
        print("Gracias por usar el programa!")
        menu = False
    else:
        print("INGRESE UNA OPCION CORRECTA")