from abc import ABC, abstractmethod
# Importación de la excepción personalizada VehiculoNoIngresadoError desde el paquete Excepciones
from Excepciones.vehiculo_no_ingresado_error import VehiculoNoIngresadoError

# Clase Vehiculo: Representa la plantilla base abstracta para los vehículos del taller mecánico.
class Vehiculo(ABC):


    # Método constructor que inicializa un nuevo objeto de la clase Vehiculo
    def __init__(self, patente: str, anio: int):
        # Asigna la patente a través del setter para ejecutar la validación al crear el objeto
        self.patente = patente
        # Inicializa el atributo privado __anio con el valor del año recibido
        self.__anio = anio
        # Inicializa el atributo privado __en_taller en False (el vehículo parte fuera del taller)
        self.__en_taller = False

    # @property transforma el método en una propiedad de lectura para acceder a __patente
    @property
    def patente(self) -> str:
        # Retorna el valor del atributo privado __patente
        return self.__patente
    
    # @patente.setter define la lógica de validación e inserción al modificar la patente
    @patente.setter
    def patente(self, nueva_patente: str) -> None:
        # Valida que la patente tenga al menos 6 caracteres y no contenga espacios en blanco
        if len(nueva_patente) < 6 or " " in nueva_patente:
            # Lanza una excepción de tipo ValueError si la patente no cumple con las reglas de negocio
            raise ValueError("La patente debe tener al menos 6 caracteres y no contener espacios.")
        # Asigna el nuevo valor al atributo privado __patente una vez superada la validación
        self.__patente = nueva_patente

    # @property transforma el método en una propiedad para acceder a __anio
    @property
    def anio(self) -> int:
        # Retorna el valor del atributo privado __anio
        return self.__anio

    # @property transforma el método en una propiedad de solo lectura para acceder a __en_taller (sin setter)
    @property
    def en_taller(self) -> bool:
        # Retorna el valor booleano del atributo privado __en_taller
        return self.__en_taller

    # Método público para registrar el ingreso del vehículo al taller mecánico
    def ingresar(self) -> None:
        # Valida que el vehículo no esté ya en el taller antes de registrar su ingreso
        if self.__en_taller:
            raise ValueError("El vehículo ya se encuentra dentro del taller.")
        # Cambia el estado del atributo privado __en_taller a True
        self.__en_taller = True

    # Método público para registrar la entrega del vehículo sacándolo del taller
    def entregar(self) -> None:
        # Valida que el vehículo esté en el taller antes de proceder con su entrega
        if not self.__en_taller:
            # Lanza la excepción personalizada VehiculoNoIngresadoError pasando la patente
            raise VehiculoNoIngresadoError(self.patente)
        # Cambia el estado del atributo privado __en_taller a False
        self.__en_taller = False


    # Método abstracto que define el contrato tarifario por hora de reparación para las subclases
    @abstractmethod
    def tarifa_hora(self) -> int:
        pass

