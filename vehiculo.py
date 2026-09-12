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

    # MÃ©todo pÃºblico para obtener la patente del vehÃ­culo
    def obtener_patente(self) -> str:
        # Retorna el valor almacenado en el atributo privado __patente
        return self.__patente

    # MÃ©todo pÃºblico para obtener el aÃ±o del vehÃ­culo
    def obtener_anio(self) -> int:
        # Retorna el valor almacenado en el atributo privado __anio
        return self.__anio

    # MÃ©todo pÃºblico para consultar si el vehÃ­culo se encuentra en el taller
    def esta_en_taller(self) -> bool:
        # Retorna el valor booleano almacenado en el atributo privado __en_taller
        return self.__en_taller

    # MÃ©todo pÃºblico para registrar el ingreso del vehÃ­culo al taller mecÃ¡nico
    def ingresar(self) -> None:
        # Cambia el estado del atributo privado __en_taller a True
        self.__en_taller = True

    # MÃ©todo pÃºblico para registrar la entrega del vehÃ­culo sacÃ¡ndolo del taller
    def entregar(self) -> None:
        # Cambia el estado del atributo privado __en_taller a False
        self.__en_taller = False
