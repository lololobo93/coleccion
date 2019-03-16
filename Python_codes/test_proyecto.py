from pais import Pais
from continente import Continente


def test_pais():
    canada = Pais('Canada', 'CAN', [(2016, 31995000),(2015, 31676000)])
    assert canada.nombre == 'Canada'
    assert canada.codigo == 'CAN'

test_pais()

def test_pais_poblacion():
    canada = Pais('Canada', 'CAN', [(2016, 31995000),(2015, 31676000)])
    assert canada.poblacion(2016) == 31995000
    assert canada.poblacion(2015) == 31676000
    assert canada.poblacion() == 31995000

test_pais_poblacion()

def test_pais_asignaploblacion():
    canada = Pais('Canada', 'CAN', [(2016, 31995000),(2015, 31676000)])
    canada.asignapoblacion(2017, 32312000)
    assert canada.poblacion(2017) == 32312000
    assert canada.poblacion(2016) == 31995000
    assert canada.poblacion() == 32312000

test_pais_asignaploblacion()

def test_pais_es_maspoblado():
    canada = Pais('Canada', 'CAN', [(2016, 31995000), (2015, 31676000)])
    usa = Pais('United States', 'USA', [(2016, 31995001), (2015, 31675000)])
    assert canada.es_masgrande(usa, 2015) is True
    assert canada.es_masgrande(usa) is False

test_pais_es_maspoblado()

def test_pais_str():
    canada = Pais('Canada', 'CAN', [(2016, 31995000), (2015, 31676000)])
    assert str(canada) == 'Canada tiene una población de 31995000 habitantes'

test_pais_str()

def test_continente():
    canada = Pais('Canada', 'CAN', [(2016, 31995000), (2015, 31676000)])
    usa = Pais('United States', 'USA', [(2016, 31995001), (2015, 31675000)])
    mexico = Pais('Mexico', 'MEX', [(2016, 127540423), (2015, 112336538)])
    paises = [canada, usa, mexico]
    america_norte = Continente('América del Norte', 'AN', paises)
    assert america_norte.nombre == 'América del Norte'
    assert america_norte.codigo == 'AN'

test_continente()

def test_continente_poblacion():
    canada = Pais('Canada', 'CAN', [(2016, 31995000), (2015, 31676000)])
    usa = Pais('United States', 'USA', [(2016, 31995001), (2015, 31675000)])
    mexico = Pais('Mexico', 'MEX', [(2016, 127540423), (2015, 112336538)])
    paises = [canada, usa, mexico]
    america_norte = Continente('América del Norte', 'AN', paises)
    assert america_norte.poblacion() == 191530424
    assert america_norte.poblacion(2015) == 175687538

test_continente_poblacion()

def test_continente_str():
    canada = Pais('Canada', 'CAN', [(2016, 31995000), (2015, 31676000)])
    usa = Pais('United States', 'USA', [(2016, 31995001), (2015, 31675000)])
    mexico = Pais('Mexico', 'MEX', [(2016, 127540423), (2015, 112336538)])
    paises = [canada, usa, mexico]
    america_norte = Continente('América del Norte', 'AN', paises)
    assert str(america_norte) == 'América del Norte (Canada, Mexico, United States)'

test_continente_str()