import csv

def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    
    return newlist

def get_element (my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element):
    
    if my_list["size"] == 0:
        return -1
    
    for i in range(0, my_list["size"]):
        if my_list['elements'][i] == element:
            return i
        
    return -1
        
    
    
    

    
def add_first(lista, elemento):
    #Agrega un elemento de primeras a la lista
    lista["elements"].insert(0, elemento)  # Metemos el elemento en la posición 0
    lista["size"] += 1  # Por utlimo aumento el contador. 

def add_last(lista, elemento):
    #Agrego un elemento al final de la lista.
    lista["elements"].append(elemento)  # Agregamos el elemento al final
    lista["size"] += 1  # Aumentamos el contador de tamaño

def size(lista):
    #Retorna el tamaño de la lista.
    return lista["size"]  #Y entra al tamaño ya establecido.

def first_element(lista):
    # Retorna el primer elemento de la lista o None si está vacía.
    if lista["size"] == 0:  # Si la lista está vacía, retorna None
        return None
    return lista["elements"][0]  # Retorna el primer elemento.

def is_empty(lista):
    #Verifica si la lista esta vacia.
    return lista["size"] == 0

def remove_first(lista):
    #Elimino y retorno el primer elemento de la lista.
    if lista["size"] == 0:
        return None
    lista["size"] -= 1
    return lista["elements"].pop(0)

def remove_last(lista):
    #Elimina y retorna el último elemento de la lista.
    if lista["size"] == 0:
        return None
    lista["size"] -= 1
    return lista["elements"].pop()

def insert_element(lista, index, elemento):
   #Inserta un elemento en una posición específica de la lista.
    if 0 <= index <= lista["size"]:
        lista["elements"].insert(index, elemento)
        lista["size"] += 1
        return lista 
    return None


def delete_element(lista, index):
    #Elimina un elemento en una posición específica y retorna la lista.
    if 0 <= index < lista["size"]:
        lista["elements"].pop(index)
        lista["size"] -= 1
        return lista 
    return None


def change_info(lista, index, elemento):
    #Cambio el valor de un elemento en la posición index.
    if 0 <= index < lista["size"]:
        lista["elements"][index] = elemento
        return lista 
    return None

def exchange(lista, index1, index2):
    #Intercambia dos elementos en la lista.
    if 0 <= index1 < lista["size"] and 0 <= index2 < lista["size"]:
        lista["elements"][index1], lista["elements"][index2] = lista["elements"][index2], lista["elements"][index1]
        return lista  # Se retorna la lista después del intercambio
    return None

def sub_list(lista, start, end):
    #Retorna una sublista desde start hasta end.
    if 0 <= start < lista["size"] and 0 <= end <= lista["size"] and start < end:
        return {
            "elements": lista["elements"][start:end],
            "size": end - start
        }
    return None

def last_element(my_list):
    
    if my_list["size"] == 0:
        
        raise Exception('IndexError: list index out of range')
    
    return my_list["elements"][my_list["size"] - 1]

def cmp_function(element1, element2):
    
    if element1 > element2: #caso_1 (mayor que)
        return 1
    
    elif element1 < element2: #caso_2 (menor que)
        
        return -1
    
    else: #caso_3 (iguales)
        
        return 0





