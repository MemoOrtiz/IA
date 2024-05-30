
print("Ocho puzzle")
print ("El espacio vacio debe ser representado por un _ (guión bajo)")
class Nodo:
    def __init__(self, datos, nivel, f_valor):
        #Inicializar el nodo con los siguientes atributos        
        self.datos = datos
        self.nivel = nivel
        self.f_valor = f_valor

    def generar_hijo(self):
        """ 
        Generar nodos hijos desde el nodo dado moviendo el espacio en blanco
        en cualquiera de las direcciones (arriba, abajo, izquierda, derecha) 
        """
        x, y = self.encontrar(self.datos, '_')
        
        """ 
        lista_posiciones_blanco contiene valores de posición para mover el espacio en blanco en cualquiera de
        las 4 direcciones [arriba, abajo, izquierda, derecha] respectivamente. 
        """
        lista_posiciones_blanco = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        hijos = []
        for i in lista_posiciones_blanco:
            hijo = self.mezclar(self.datos, x, y, i[0], i[1])
            if hijo is not None:
                nodo_hijo = Nodo(hijo, self.nivel + 1, 0)
                hijos.append(nodo_hijo)
        return hijos

    def mezclar(self, puz, x1, y1, x2, y2):

        """ 
        Mover el espacio en blanco en la dirección dada y si el valor de la posición está fuera
        de los límites, devolver None 
        """

        if x2 >= 0 and x2 < len(self.datos) and y2 >= 0 and y2 < len(self.datos):
            temp_puz = []
            temp_puz = self.copiar(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copiar(self, raiz):
        #Función de copia para crear una matriz similar al nodo dado 
        temp = []
        for i in raiz:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def encontrar(self, puz, x):
        #Metodo para encontrar la posición del espacio en blanco  
        for i in range(0, len(self.datos)):
            for j in range(0, len(self.datos)):
                if puz[i][j] == x:
                    return i, j

class Puzzle:

    def __init__(self, tamaño):
        #Inicia con el puzzle segun su tamaño
        self.n = tamaño
        self.abiertos = []
        self.cerrados = []

    def aceptar(self):
        #Acepta el puzzle 
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, inicio, objetivo):
        #Función heurística para calcular el valor heurístico f(x) = h(x) + g(x) 
        return self.h(inicio.datos, objetivo) + inicio.nivel

    def h(self, inicio, objetivo):
        #Calcula la diferencia entre los puzzles dados 
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if inicio[i][j] != objetivo[i][j] and inicio[i][j] != '_':
                    temp += 1
        return temp

    def procesar(self):
        #Acepta el estado inicial y el estado objetivo del puzzle 
        print("Ingrese la matriz del estado inicial\n")
        inicio = self.aceptar()
        print("Ingrese la matriz del estado objetivo\n")
        objetivo = self.aceptar()

        inicio = Nodo(inicio, 0, 0)
        inicio.f_valor = self.f(inicio, objetivo)

        #Poner el nodo inicial en la lista abierta 
        self.abiertos.append(inicio)
        #print("\n\n")
        movimiento = 0
        while True:
            actual = self.abiertos[0]
            print(f"\nMovimiento número: {movimiento}")
            print("Estado actual:")
            for i in actual.datos:
                for j in i:
                    print(j, end=" ")
                print("")

            #Si la diferencia entre el nodo actual y el nodo objetivo es 0, eureka!

            if self.h(actual.datos, objetivo) == 0:
                break

            hijos = actual.generar_hijo()
            for i in actual.generar_hijo():
                i.f_valor = self.f(i, objetivo)
                self.abiertos.append(i)
            self.cerrados.append(actual)
            del self.abiertos[0]

            print("\n")
            print("Hijos:")
            for hijo in hijos:
                for i in hijo.datos:
                    for j in i:
                        print(j, end=" ")
                    print("")
                print("---")


            """ Ordenar la lista abierta basada en el valor f """
            self.abiertos.sort(key=lambda x: x.f_valor, reverse=False)
            movimiento += 1

puz = Puzzle(3)
puz.procesar()
