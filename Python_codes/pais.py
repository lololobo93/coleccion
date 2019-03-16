class Pais(object):
    
    def __init__(self, name, ID, population_year = []):
        """ Inicializa la clase
        :param name: nombre del país, recibe un string
        :param ID: clave del país, recibe un string
        :param population_year: población por año, recibe un arreglo [(año, población)]
        """
        self.nombre = name
        self.codigo = ID
        self.poblacion_ano = dict(population_year)
    
    def __str__(self):
        """
        Redefine la función ``str`` para la clase.
        """
        year = max(self.poblacion_ano.keys())
        pob = self.poblacion_ano[year]
        return self.nombre + ' tiene una población de ' + str(pob) + ' habitantes'
    
    def asignapoblacion(self, year, poblacion):
        """
        Asigna la población al diccionario ``poblacion_ano``
        para el año ``year``
        :param year: año del conteo de población ``poblacion``
        :param poblacion: población del año ``year``
        :return: None o "Verificar año"
        """
        if (year >= 0) and (type(year) is int):
            self.poblacion_ano[year] = poblacion
            return None
        print("Año no válido")

    def poblacion(self, year = None):
        """
        Devuelve el conteo de población para el año 
        :param year: año del que se desea saber su población
        :return: conteo de población
        """
        if year == None:
            year = max(self.poblacion_ano.keys())
            return self.poblacion_ano[year]
        elif (year in self.poblacion_ano.keys()) and (type(year) is int):
            return self.poblacion_ano[year]
        print("Año no válido")

    def es_masgrande(self, other, year = None):
        """
        Compara la población para el año ``year`` con la de ``other``.
        :param year: año del que se desea comparar las poblaciones
        :return: True o False
        """
        if year == None:
            year = max(self.poblacion_ano.keys())
            
            if year in other.poblacion_ano.keys():
                pass
            else:
                print("No se pueden comparar")
                return None

            if self.poblacion_ano[year] > other.poblacion_ano[year]:
                return True
            else:
                return False
        elif (year in self.poblacion_ano.keys()) and (type(year) is int):
            
            if self.poblacion_ano[year] > other.poblacion_ano[year]:
                return True
            else:
                return False
                
        print("Año no válido")
