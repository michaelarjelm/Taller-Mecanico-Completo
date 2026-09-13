# Importación de la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Clase Camion: Subclase especializada que hereda de Vehiculo e incorpora capacidad de carga y tarifa propia
class Camion(Vehiculo):

    # Método constructor que recibe la patente, año y la capacidad de carga propia del camión
    def __init__(self, patente: str, anio: int, capacidad_carga: int):
        # Llama al constructor de la clase base (Vehiculo) para inicializar los atributos heredados
        super().__init__(patente, anio)
        # Inicializa el atributo privado propio __capacidad_carga con el valor recibido (en kilos)
        self.__capacidad_carga = capacidad_carga

    # @property transforma el método en una propiedad de solo lectura para consultar la capacidad de carga
    @property
    def capacidad_carga(self) -> int:
        # Retorna el valor almacenado en el atributo privado __capacidad_carga
        return self.__capacidad_carga

    # Sobrescribe el método tarifa_hora de la clase base para retornar la tarifa específica de un camión
    def tarifa_hora(self) -> int:
        # Retorna el valor entero 40000 correspondiente a la tarifa por hora de un camión
        return 40000
