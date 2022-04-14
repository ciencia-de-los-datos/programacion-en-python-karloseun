"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""
import pprint
from operator import itemgetter
import re

pp = pprint.PrettyPrinter() 
path = 'data.csv'

# load and clean file
def preparedFile(path):

    dataFile = []

    # print('\nstep 1: reading file !')
    with open(path, 'r') as file:
        dataFile = file.readlines()

    # print('\nstep 2: cleaning file !')
    dataFile = [line.strip().split('\t') for line in dataFile]
    
    # print('\nstep 3: summary !')
    # print('\tlines:',len(dataFile))
    # pp.pprint(dataFile)
    
    return dataFile


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # print('\nstep 0: obtain data')    
    data = preparedFile(path)
    
    suma = 0
    [ suma:= suma + int(row[1]) for row in data ]
    
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    # print('\nstep 0: obtain data')
    data = preparedFile(path)

    # print('\nstep 1: verify row zero (0)')
    data = [row[0] for row in data]
    # print(data)

    # print('\nstep 2: creating dictionary > Key (column A), Value: how many times the letter of column A appears')
    result = dict()
    for letra in data:
        if letra in result.keys(): # si la letra esta en la lista de claves del diccionario
            result[letra] = result[letra] + 1
        else:
            result[letra] = 1

    # print('\nstep 3: put the result in a tuple')
    tuplas = [(key, valor) for key, valor in result.items()]
    # print(tuplas)
    # print(*tuplas,sep="\n")

    # print('\nstep 4: sort tuples by first column, ASC')
    tuplas = sorted(tuplas, key=itemgetter(0), reverse=False)
    # pp.pprint(tuplas)

    # print('\nstep 5: display result vertically')
    # print(*tuplas,sep="\n")
    
    return tuplas

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    # print('\nstep 0: obtain data')
    data = preparedFile(path)
    
    # print('\nstep 1: extracting the first two items for each list')
    data = [row[:2] for row in data]
    # print(data)

    # print('\nstep 2: creating dictionary key (column A), value (column B)')
    dictQ3 = {}
    for key, value in data:

        value = int(value)        
        if key in dictQ3.keys():
            dictQ3[key].append(value)
        else:
            dictQ3[key] = [value]
    # pp.pprint(dictQ3)

    # print('\nstep 3: creating a list that contains summation of list for each dictionary key')
    resultQ3 = [] 
    for key in dictQ3.keys():
        resultQ3.append( [key,sum(dictQ3[key])] )

    # print('\nstep 4: sorted list for firts element of tuple')
    resultQ3 = sorted(resultQ3,key=itemgetter(0), reverse=False)

    # print('\nstep 5: display result!')
    # print(resultQ3)

    return resultQ3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    # print('\nstep 0: obtain data')
    data = preparedFile(path)

    # print('\nstep 1: extracting the first three items for each list')
    data = [row[:3] for row in data]
    # pp.pprint(data)

    # print('\nstep 2: attach new item> month for each list in data')
    for i in data:
        # print(i[2])
        # print( (i[2].split("-"))[1] )
        i.append( (i[2].split("-"))[1] )
    # print(data)

    # print('\nstep 3: creating dictionary key > month, value > times for month')
    dictQ4 = {}
    for i in data:
        month = str(i[3])
        if month in dictQ4.keys():
            dictQ4[month] = dictQ4[month] + 1
        else:
            dictQ4[month] = 1
    # print(dictQ4)

    # sort dictionary
    dictQ4 = dict(sorted(dictQ4.items()))

    #convert dict to list
    listQ4 = sorted(list(dictQ4.items()), key=itemgetter(0), reverse=False)
    
    
    return listQ4


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    # print('\nstep 0: obtain data')
    data = preparedFile(path)

    # print('\nstep 1: verify data set !')
    data = [row[:2]for row in data]
    # pp.pprint(data)

    # print('\nstep 2: create dictionary > key (column A), value (list of elements column B)')
    dictQ5 = {}
    for key, value in data:
        value = int(value)
        if key in dictQ5.keys():
            dictQ5[key].append(value)
        else:
            dictQ5[key] = [value]
    # pp.pprint(dictQ5)

    # print('\nstep 3: extract values MIN and MAX from dataset for each dictionary value')
    resuktQ5 = []
    for k in dictQ5.keys():
        resuktQ5.append( (k,max(dictQ5[k]),min(dictQ5[k])) )
    # print(resuktQ5)

    # print('\nstep 4: sorted list for first element of tuple ')
    resuktQ5 = sorted(resuktQ5, key=itemgetter(0), reverse=False)
    # print(resuktQ5)

    # print('\nstep 5: display result ')
    # print(*resuktQ5,sep="\n")
        
    return resuktQ5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    # print('\nstep 0: obtain data')
    data = preparedFile(path)

    # print('\nstep 1: verify data set !')
    data = [row[:5]for row in data]
    # pp.pprint(data)

    # print('\nstep 2: comprenhension for create a list of items (key:value) of dictionary !')
    listQ6 = []
    [ listQ6 := listQ6 + ((i[4]).split(",")) for i in data ]
    # print(listQ6)
    
    # print('\nstep 3: comprenhension for create a list of lists for codificacion: key:value !')
    llistQ6 = []
    # [ llistQ6.append(i.split(":")) for i in listQ6 ]
    llistQ6 = [ i.split(":") for i in listQ6 ]
    # print(llistQ6)
    
    # print('\nstep 4: creating dictionary from list of lists !')
    dictQ6 = {}
    for key, value in llistQ6:
        if key in dictQ6.keys():
            dictQ6[key].append(int(value))
        else:
            dictQ6[key] = [int(value)]
    
    # pp.pprint(dictQ6)

    # print('\nstep 5: list comprenhension for extratc MIN, MAX values of dictionary !')
    resultQ6 = []    
    # [ resultQ6.append( (key, min(dictQ6[key]), max(dictQ6[key])) ) for key in dictQ6.keys() ]
    resultQ6 = [ (key, min(dictQ6[key]), max(dictQ6[key])) for key in dictQ6.keys() ]
    
    # print('\nstep 6: sorted list !')
    # pp.pprint( sorted(resultQ6,key=itemgetter(0),reverse=False) )
    resultQ6 = sorted(resultQ6,key=itemgetter(0),reverse=False)

    return resultQ6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    # print('\nstep 0: obtain data')
    data = preparedFile(path)

    # print('\nstep 1: verify data set !')
    data = [row[:2]for row in data]
    # pp.pprint(data)

    # print('\nstep 2: creating dictionary !')
    dictQ7 = {}
    for v,k in data:
        k = int(k) 
        if k in dictQ7.keys():
            dictQ7[k].append(v)
        else:
            dictQ7[k] = [v]

    # print('\nstep 3: convert dict to list and then, sorted and return')

    return sorted(list(dictQ7.items()), key=itemgetter(0), reverse=False)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    # print('\nstep 0: obtain data')
    data = preparedFile(path)

    # print('\nstep 1: verify data set !')
    data = [row[:2]for row in data]
    # pp.pprint(data)

    # print('\nstep 2: creating dictionary !')
    dictQ8 = {}
    for v,k in data:
        k = int(k) 
        if k in dictQ8.keys():
            dictQ8[k].append(v)
        else:
            dictQ8[k] = [v]
    
    listQ8 = []
    listQ8 = [ (key, sorted(set(dictQ8[key]))) for key in dictQ8 ]
    listQ8 = sorted(listQ8,key=itemgetter(0),reverse=False)

    return listQ8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    # print('\nstep 0: obtain data')
    data = preparedFile(path)

    # print('\nstep 1: verify data set !')
    data = [row[:5]for row in data]
    # pp.pprint(data)

    # print('\nstep 2: comprenhension for create a list of items (key:value) of dictionary !')
    listQ9 = []
    [ listQ9 := listQ9 + ((i[4]).split(",")) for i in data ]
    # print(listQ9)
    
    # print('\nstep 3: comprenhension for create a list of lists for codificacion: key:value !')
    llistQ9 = []
    llistQ9 = [ i.split(":") for i in listQ9 ]
    # print(llistQ9[:11])
    
    # print('\nstep 4: creating dictionary from list of lists !')
    dictQ9 = {}
    for key, value in llistQ9:
        if key in dictQ9.keys():
            dictQ9[key].append(int(value))
        else:
            dictQ9[key] = [int(value)]
    # pp.pprint(dictQ9)

    # print('\nstep 5: len of values of dictionary !')
    resultQ9 = []
    resultQ9 = [ (key, len(dictQ9[key]) ) for key in dictQ9.keys() ]
    # print(resultQ9)

    # print('\nstep 6: sorted list !')
    resultQ9 = sorted(resultQ9,key=itemgetter(0),reverse=False)

    # print('\nstep 7: dict comprenhension for convert list to dictionary !')
    dictRQ9 = { i[0] : i[1] for i in resultQ9 }
    # pp.pprint(dictRQ9)

    return dictRQ9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    # print('\nstep 0: obtain data')
    data = preparedFile(path)
    # pp.pprint(data)

    # print('\nstep 1: list comprenhension por LEN list !')
    data = [  ( row[0], len(row[3].split(",")), len(row[4].split(",")) ) for row in data ]
    # pp.pprint(data)

    return data


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """
    # print('\nstep 0: obtain data')
    data = preparedFile(path)
    # pp.pprint(data)
    # print( (data[0])[3], (data[0])[1] )

    dictQ11 = {}
    cont = 0
    
    for _ in data:
        key = (data[cont])[3]
        value = int((data[cont])[1])
        cont += 1

        for i in key.split(","):
            if ( i in dictQ11.keys() ):
                dictQ11[i] += value
            else:
                dictQ11[i] = value

    # print(dictQ11)
    dictQ11 = dict(sorted(dictQ11.items()))

    return dictQ11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    # print('\nstep 0: obtain data')
    data = preparedFile(path)

    dictQ12 = {}
    cont = 0
    
    for _ in data:
        key = (data[cont])[0]
        value = str((data[cont])[4])
        cont += 1
        # print (key,":",value)
        value = sum( [ int(i) for i in (re.findall(r"\d[0-9]*",value)) ] )

        if key in dictQ12.keys():
            dictQ12[key] = dictQ12[key] + value
        else:
            dictQ12[key] = value

    dictQ12 = dict(sorted(dictQ12.items()))

    return dictQ12

"""
# display responses
print("* * * * * * * * * * * * * * * S O L U T I O N S   L A B 1 * * * * * * * * * * * * * * * * * *")
print("\nResult_Question_01\n")
print(pregunta_01()) # probando la respuesta
print("\nResult_Question_02\n")
pp.pprint(pregunta_02()) # probando la respuesta
print("\nResult_Question_03\n")
pp.pprint(pregunta_03()) # probando la respuesta
print("\nResult_Question_04\n")
pp.pprint(pregunta_04()) # probando la respuesta
print("\nResult_Question_05\n")
pp.pprint(pregunta_05()) # probando la respuesta
print("\nResult_Question_06\n")
pp.pprint(pregunta_06()) # probando la respuesta
print("\nResult_Question_07\n")
pp.pprint(pregunta_07()) # probando la respuesta
print("\nResult_Question_08\n")
pp.pprint(pregunta_08()) # probando la respuesta
print("\nResult_Question_09\n")
pp.pprint(pregunta_09()) # probando la respuesta
print("\nResult_Question_10\n")
pp.pprint(pregunta_10()) # probando la respuesta
print("\nResult_Question_11\n")
pp.pprint(pregunta_11()) # probando la respuesta
print("\nResult_Question_12\n")
pp.pprint(pregunta_12()) # probando la respuesta
print("\n\n\n\n")
"""