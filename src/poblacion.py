from collections import namedtuple
import csv

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta):
    res = []

    with open(ruta, encoding='UTF-8') as f:
        lista = csv.reader(f)
        for pais, codigo, año, censo in lista :
            año = int(año)
            censo = int(censo)
            tupla = RegistroPoblacion(pais, codigo, año, censo)
            res.append(tupla)
        return res
    

def calcula_paises(poblaciones):
    res = set()
    
    for tupla in poblaciones:
        res.add(tupla.pais)

    res=list(res)
    res.sort()
    return res

def filtra_por_pais(poblaciones, nombre_o_codigo):
    res = []

    for linea in poblaciones:
        if nombre_o_codigo == linea.pais or nombre_o_codigo == linea.codigo:
            tupla = ( linea.año, linea.censo)
            res.append(tupla)
    return res

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    res = []

    for linea in poblaciones:
        if anyo == linea.año and linea.pais in paises:
            tupla = (linea.pais, linea.censo)
            res.append(tupla)
    return res

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    lista_años = []
    lista_habitantes = []

    for linea in poblaciones:
        if nombre_o_codigo == linea.pais or nombre_o_codigo == linea.codigo:
            lista_años.append(linea.año)
            lista_habitantes.append(linea.censo)

    return lista_años, lista_habitantes

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    lista_habitantes = []
    lista_paises = []

    for linea in poblaciones:
        if anyo == linea.año and linea.pais in paises:
            lista_paises.append(linea.pais)
            lista_habitantes.append(linea.censo)

    return lista_paises, lista_habitantes