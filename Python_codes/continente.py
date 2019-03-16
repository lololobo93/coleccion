class Continente(object):
    
    def __init__(self, name, ID, paises = None):
        """ Inicializa la clase
        :param name: nombre del continente, recibe un string
        :param ID: clave del continente, recibe un string
        :param piases: recibe un arreglo de clases ``Pais``
        """
        self.nombre = name
        self.codigo = ID
        self.paises = sorted(paises, key=lambda x:x.nombre)

    def __str__(self):
        """
        Redefine la función ``str`` para la clase.
        """
        names = '('
        for country in self.paises:
            names += country.nombre + ', '
        names = names[:-2] + ')'
        return self.nombre + ' ' + names

    def poblacion(self, year = None):
        """
        Devuelve el conteo de población para el año 
        :param year: año del que se desea saber su población
        :return: conteo de población
        """
        if year == None:
            year = max(self.paises[0].poblacion_ano.keys())
            sum = 0
            for country in self.paises:
                sum += country.poblacion_ano[year]
            return sum
        elif type(year) is int:
            sum = 0
            for country in self.paises:
                sum += country.poblacion_ano[year]
            return sum
        print("Año no válido")