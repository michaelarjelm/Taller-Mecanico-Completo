# Clase Vehiculo: Representa la plantilla base para los vehÃ­culos del taller mecÃ¡nico.
class Vehiculo:

    # MÃ©todo constructor que inicializa un nuevo objeto de la clase Vehiculo
    def __init__(self, patente: str, anio: int):
        # Inicializa el atributo privado __patente con el valor de la patente recibida
        self.__patente = patente
        # Inicializa el atributo privado __anio con el valor del aÃ±o recibido
        self.__anio = anio
        # Inicializa el atributo privado __en_taller en False (el vehÃ­culo parte fuera del taller)
        self.__en_taller = False

    # @property transforma el mÃ©todo en una propiedad de solo lectura para acceder a __patente como si fuera un atributo sintÃ¡cticamente (sin parÃ©ntesis)
    @property
    def patente(self) -> str:
        # Retorna el valor del atributo privado __patente
        return self.__patente

    # @property transforma el mÃ©todo en una propiedad de solo lectura para acceder a __anio como si fuera un atributo sintÃ¡cticamente (sin parÃ©ntesis)
    @property
    def anio(self) -> int:
        # Retorna el valor del atributo privado __anio
        return self.__anio

    # @property transforma el mÃ©todo en una propiedad de solo lectura para acceder a __en_taller como si fuera un atributo sintÃ¡cticamente (sin parÃ©ntesis)
    @property
    def en_taller(self) -> bool:
        # Retorna el valor booleano del atributo privado __en_taller
        return self.__en_taller

    # MÃ©todo pÃºblico para registrar el ingreso del vehÃ­culo al taller mecÃ¡nico
    def ingresar(self) -> None:
        # Cambia el estado del atributo privado __en_taller a True
        self.__en_taller = True

    # MÃ©todo pÃºblico para registrar la entrega del vehÃ­culo sacÃ¡ndolo del taller
    def entregar(self) -> None:
        # Cambia el estado del atributo privado __en_taller a False
        self.__en_taller = False
