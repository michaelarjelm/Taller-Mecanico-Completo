# Clase Vehiculo: Representa Ãºnicamente el molde o plantilla base para los vehÃ­culos del taller mecÃ¡nico.
class Vehiculo:
    # DeclaraciÃ³n de atributos con sus tipos de datos correspondientes
    patente: str  # Atributo para almacenar la patente del vehÃ­culo (cadena de texto)
    anio: int  # Atributo para almacenar el aÃ±o de fabricaciÃ³n (nÃºmero entero)
    _en_taller: bool  # Atributo para registrar si el vehÃ­culo estÃ¡ en el taller (booleano)

    # MÃ©todo constructor que inicializa un nuevo objeto de la clase Vehiculo
    def __init__(self, patente: str, anio: int):
        # Asigna la patente recibida como parÃ¡metro al atributo propio de la instancia
        self.patente = patente
        # Asigna el aÃ±o recibido como parÃ¡metro al atributo propio de la instancia
        self.anio = anio
        # Inicializa _en_taller en False de forma predeterminada (el vehÃ­culo reciÃ©n registrado no estÃ¡ en el taller)
        self._en_taller = False

    # MÃ©todo para registrar el ingreso del vehÃ­culo al taller mecÃ¡nico
    def ingresar(self) -> None:
        # Cambia el estado del atributo _en_taller a True indicando que el vehÃ­culo ingresÃ³ al taller
        self._en_taller = True

    # MÃ©todo para registrar la entrega del vehÃ­culo sacÃ¡ndolo del taller
    def entregar(self) -> None:
        # Cambia el estado del atributo _en_taller a False indicando que el vehÃ­culo fue entregado
        self._en_taller = False
