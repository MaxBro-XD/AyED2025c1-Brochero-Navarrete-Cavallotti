class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def estavacia(self):
        return self.tamanio == 0

    def __len__(self):
        return self.tamanio

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.estavacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.estavacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def insertar(self, dato, posicion):
        if posicion < 0:
            posicion += self.tamanio
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            anterior = actual.anterior
            nuevo_nodo.anterior = anterior
            nuevo_nodo.siguiente = actual
            anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamanio += 1

    def extraer(self, posicion=None):
        if posicion < 0:
            posicion = self.tamanio + posicion
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango")

        if self.estavacia():
            raise IndexError("La lista está vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        if posicion < 0:
            posicion += self.tamanio
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1
        return dato

    def copiar(self):
        nueva = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            nueva.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva

    def invertir(self):
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otra):
        actual = otra.cabeza
        while actual:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return self

    def __add__(self, otra):
        nueva = self.copiar()
        nueva.concatenar(otra)
        return nueva





                    
                    
                    
                    
            
