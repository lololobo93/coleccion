# Liberías
import json
# Las librerías inferiores son para graficar
import matplotlib.pyplot as plt
from matplotlib import cm
import mpl_toolkits.mplot3d.axes3d as axes3d
from matplotlib import rc, ticker
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
rc('font',**{'family':'serif'})
rc('text', usetex=True)

# Importamos las clases
from pais import Pais
from continente import Continente

# Cargamos el archivo paises_prueba.txt.
with open('paises_prueba.txt') as f1:
    paises = f1.readlines()
paises = [x.strip() for x in paises] 

def make_dict(paises_prueba):
    """ Crea un diccionaro de los continentes en los que
    se encuentran los paises de la lista ``paises prueba``.
    :param paises_prueba: lista con los nombres de los 
    paises a buscar en los archivos .json
    :return dict_cont: diccionario con los contientes y
    las respectivas clases ``Continente``
    """

    # Cargamos los archivos json donde se obtendrán la población y códigos
    with open('population_json.json') as f2:    
        population_json = json.load(f2)
    with open('country-and-continent-codes-list_json.json') as f3:    
        country_continent_json = json.load(f3)

    dict_cont = {} # Diccionario

    # Obtenemos la información para cada país
    for pd in country_continent_json:
        name = pd['Country_Name']
        cont = pd['Continent_Name']
        if name in paises_prueba:
            actual = (Pais(name, pd['Three_Letter_Country_Code'], []))
            for pj in population_json:
                if pj['Country Code'] == actual.codigo:
                    actual.asignapoblacion(pj['Year'], int(pj['Value']))
            if cont in dict_cont.keys():
                dict_cont[cont].paises.append(actual)
            else:
                dict_cont[cont] = Continente(cont, pd['Continent_Code'],
                    [actual])

    return dict_cont

def print_poblacion(list_cont, year):
    """ Imprime en pantalla la población total de los continentes en
    ``list_cont`` para el año ``year``
    :param list_cont: lista de continentes a imprimir
    :param year: año para el que se desea saber la poblacion
    """
    dict_cont = make_dict(paises)
    
    for cont in list_cont:
        if cont in dict_cont.keys():
            print('La población de ' + str(dict_cont[cont]) + ' es:')
            print(dict_cont[cont].poblacion(year)) 
        else:
            print('No existen datos para ' + cont)

# Obtenemos las poblaciones deseadas
list_cont = ['North America', 'South America', 'Europe']
print_poblacion(list_cont, 2016)

#-------------------------------------------------------#

# Punto extra.

def finder(pais):
    """ Encuentra la clase dentro del diccionario producido por
    ``make_dict`` para ``pais``
    :param pais: nombre del pais a buscar
    :return 
    """
    dict_cont = make_dict(paises)
    for key in dict_cont.keys():
        for country in dict_cont[key].paises:
            if pais == country.nombre:
                return country
    
    print('No se encontró ' + pais)
    return None

def plotter(pais, year0, year1):
    """ Grafica el conteo de población del pais ``pais`` en el 
    periodo [``year0``, ``year1``].
    :param pais: (string) país que se desea graficar su población
    :param year0: (int) límite inferior del intervalo a graficar
    :param year1: (int) límite inferior del intervalo a graficar
    """
    pais_class = finder(pais)
    if pais_class == None:
        print('Verificar entrada ' + pais)
    years = []
    pobl = []
    for year in range(year0, year1+1):
        years.append(year)
        pobl.append(pais_class.poblacion(year))
    plt.plot(years, pobl)
    ax = plt.gca()
    ax.tick_params(which='major', direction = 'in', right = True, top = True)
    ax.set_xlabel('Año', fontsize = 12)
    ax.set_ylabel('Población', fontsize = 12)
    ax.set_title('Población de ' + pais)
    ax.grid(True, linestyle='--', alpha = 0.3)
    plt.show()

# Graficamos la población de México de 2000 a 2016.
plotter('Mexico', 2000, 2016)
