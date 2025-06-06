class NodoAVL:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha
        self.temperatura = temperatura
        self.izquierda = None
        self.derecha = None
        self.altura = 1  #Todos los nodos empiezan con altura 1

#Funciones auxiliares internas

def altura(nodo):
    return nodo.altura if nodo else 0

def balance(nodo):
    return altura(nodo.izquierda) - altura(nodo.derecha) if nodo else 0

def actualizar_altura(nodo):
    nodo.altura = 1 + max(altura(nodo.izquierda), altura(nodo.derecha))

def rotar_derecha(y):
    x = y.izquierda
    T2 = x.derecha
    x.derecha = y
    y.izquierda = T2
    actualizar_altura(y)
    actualizar_altura(x)
    return x

def rotar_izquierda(x):
    y = x.derecha
    T2 = y.izquierda
    y.izquierda = x
    x.derecha = T2
    actualizar_altura(x)
    actualizar_altura(y)
    return y

# Funciones públicas 

def insertar_avl(nodo, fecha, temperatura):
    if not nodo:
        return NodoAVL(fecha, temperatura)

    if fecha < nodo.fecha:
        nodo.izquierda = insertar_avl(nodo.izquierda, fecha, temperatura)
    elif fecha > nodo.fecha:
        nodo.derecha = insertar_avl(nodo.derecha, fecha, temperatura)
    else:
        nodo.temperatura = temperatura  #Si la fecha ya existe  , solo actualizo la temperatura
        return nodo

    actualizar_altura(nodo)
    b = balance(nodo)

    if b > 1:
        if fecha < nodo.izquierda.fecha:
            return rotar_derecha(nodo)
        else:
            nodo.izquierda = rotar_izquierda(nodo.izquierda)
            return rotar_derecha(nodo)

    if b < -1:
        if fecha > nodo.derecha.fecha:
            return rotar_izquierda(nodo)
        else:
            nodo.derecha = rotar_derecha(nodo.derecha)
            return rotar_izquierda(nodo)

    return nodo

def buscar_avl(nodo, fecha):
    if not nodo:
        return None
    if fecha == nodo.fecha:
        return nodo.temperatura
    elif fecha < nodo.fecha:
        return buscar_avl(nodo.izquierda, fecha)
    else:
        return buscar_avl(nodo.derecha, fecha)

def en_rango_avl(nodo, f1, f2):
    res = []
    def recorrer(n):
        if not n:
            return
        if f1 <= n.fecha <= f2:
            recorrer(n.izquierda)
            res.append((n.fecha, n.temperatura))
            recorrer(n.derecha)
        elif n.fecha < f1:
            recorrer(n.derecha)
        else:
            recorrer(n.izquierda)
    recorrer(nodo)
    return res

def min_value_node(nodo):
    while nodo.izquierda:
        nodo = nodo.izquierda
    return nodo

def borrar_avl(nodo, fecha):
    if not nodo:
        return nodo

    if fecha < nodo.fecha:
        nodo.izquierda = borrar_avl(nodo.izquierda, fecha)
    elif fecha > nodo.fecha:
        nodo.derecha = borrar_avl(nodo.derecha, fecha)
    else:
        if not nodo.izquierda:
            return nodo.derecha
        elif not nodo.derecha:
            return nodo.izquierda
        temp = min_value_node(nodo.derecha)
        nodo.fecha = temp.fecha
        nodo.temperatura = temp.temperatura
        nodo.derecha = borrar_avl(nodo.derecha, temp.fecha)

    actualizar_altura(nodo)
    b = balance(nodo)

    if b > 1:
        if balance(nodo.izquierda) >= 0:
            return rotar_derecha(nodo)
        else:
            nodo.izquierda = rotar_izquierda(nodo.izquierda)
            return rotar_derecha(nodo)

    if b < -1:
        if balance(nodo.derecha) <= 0:
            return rotar_izquierda(nodo)
        else:
            nodo.derecha = rotar_derecha(nodo.derecha)
            return rotar_izquierda(nodo)

    return nodo

def cantidad_nodos(nodo):
    if not nodo:
        return 0
    return 1 + cantidad_nodos(nodo.izquierda) + cantidad_nodos(nodo.derecha)
