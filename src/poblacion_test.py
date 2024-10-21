from poblacion import *
import matplotlib.pyplot as plt

def test_lee_poblaciones(datos):
    print(' ---- Lista de registro de poblacion ----')
    print('Los primeros tres elementos')
    for elementos in datos[:3]:
        print(elementos)
    
    print('Los ultimos tres elementos')
    for elementos in datos[-3:]:
        print(elementos)

def test_calcula_paises(lista):
    print('Lista de paises para los que hay datos')
    print(f'Hay un total de {len(lista)} paises registrados')
    print(lista)


def test_filtra_por_pais(lista, nombre):
    print(f'Cuando se manda {nombre} se recoge esto:')
    print('Los primeros tres elementos')
    for elementos in lista[:3]:
        print(elementos)
    
    print('Los ultimos tres elementos')
    for elementos in lista[-3:]:
        print(elementos)

def test_filtra_por_paises_y_anyo(lista, año, listanombres):
    print('En estos paises',listanombres,'en el año',año,'su censo era:')

    for elementos in lista:
        print(elementos)

def test_muestra_evolucion_poblacion(lista_años, lista_habitantes, nombre):
    titulo = f'Evolucion de poblacion de {nombre}'

    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()


def test_muestra_comparativa_paises_anyo(lista_paises, lista_habitantes,año):
    titulo = f'Comparacion de poblacion en el año {año}'

    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
    




if __name__=="__main__":
    datos = lee_poblaciones('data/population.csv')
    #test_lee_poblaciones(datos) 
    #calculo = calcula_paises(datos)   
    #test_calcula_paises(calculo)
    #nombrepais = 'ESP'
    #filtrado = filtra_por_pais(datos, nombrepais)
    #test_filtra_por_pais(filtrado, nombrepais)
    #listanombres = ['Tanzania','Micronesia','Mexico']
    #año = 2000
    #listanyo = filtra_por_paises_y_anyo(datos, año, listanombres)
    #test_filtra_por_paises_y_anyo(listanyo, año, listanombres)
    #lista_años, lista_habitantes = muestra_evolucion_poblacion(datos, nombrepais)
    #test_muestra_evolucion_poblacion(lista_años, lista_habitantes, nombrepais)
    #lista_paises2, lista_habitantes2 = muestra_comparativa_paises_anyo(datos, año, listanombres)
    #test_muestra_comparativa_paises_anyo(lista_paises2, lista_habitantes2,año)
