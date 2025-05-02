class Nodo:
    def __init__ (self, dato):
        self.dato=dato
        self.anterior=None
        self.siguiente=None
class ListaDobleEnlazada:
    def __init__ (self):
        self.cabeza=None
        self.cola=None
        self.tamanio=0
    def estavacia(self):
        if self.tamanio==0:
            return True
        else:
            return False
    def __len__(self):
        return self.tamanio
    def agregar_al_inicio(self, dato):
        nuevo_nodo=Nodo(dato)
        if self.estavacia():
            self.cabeza, self.cola =nuevo_nodo, nuevo_nodo
        else:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo_nodo
            self.cabeza=nuevo_nodo
        self.tamanio+=1
    def agregar_al_final(self, dato):
        nuevo_nodo=Nodo(dato)
        if self.estavacia():
            self.cabeza, self.cola =nuevo_nodo, nuevo_nodo
        else:
            nuevo_nodo.anterior=self.cola
            self.cola.siguiente=nuevo_nodo
            self.cola=nuevo_nodo
        self.tamanio+=1
    def __iter__(self): #este es para iterar NODOS, como iterabas listas con for x in range, pero con nodos
        posicion_actual=self.cabeza
        while posicion_actual:
            yield posicion_actual.dato
            posicion_actual=posicion_actual.siguiente
    def insertar(self, dato, posicion):
        if posicion< 0 or posicion>self.tamanio:
            raise IndexError("Posición fuera de rango")
        nuevo_nodo = Nodo(dato)
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
            nodo_anterior = nodo_actual.anterior
            nuevo_nodo.anterior = nodo_anterior
            nuevo_nodo.siguiente = nodo_actual
            nodo_anterior.siguiente = nuevo_nodo
            nodo_actual.anterior = nuevo_nodo
            self.tamanio += 1
    def extraer(self, posicion=None): #quedo largo porque tiene que ser O(1).Se puede hacer mas corto.
        if self.estavacia():
            raise IndexError("La lista está vacía")
        if posicion is None:
            posicion = self.tamanio - 1
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
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
            dato = nodo_actual.dato
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_actual.anterior
        self.tamanio -= 1
        return dato
    def copiar(self): #while recorre n nodos, o sea es O(n). agregar_Al_final ya es O(1). Total: O(n)
        nueva_lista = ListaDobleEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual:
            nueva_lista.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return nueva_lista
    def invertir(self):
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior  # antes era .siguiente, pero ahora está invertido
        self.cabeza, self.cola = self.cola, self.cabeza
    def concatenar(self, otra):
        nodo = otra.cabeza
        while nodo:
            self.agregar_al_final(nodo.dato)
            nodo = nodo.siguiente
        return self
    def __add__(self, otra):
        nueva = self.copiar()
        nueva.concatenar(otra)
        return nueva

                       
                    
                    
                    
                    
            