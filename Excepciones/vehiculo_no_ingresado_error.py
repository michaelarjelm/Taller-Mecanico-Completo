# Clase de excepción personalizada VehiculoNoIngresadoError que hereda de la clase base Exception
class VehiculoNoIngresadoError(Exception):

    # Método constructor que recibe la patente del vehículo que generó el error
    def __init__(self, patente: str):
        # Construye un mensaje de error descriptivo incorporando la patente recibida
        mensaje = f"El vehículo con patente '{patente}' no se encuentra en el taller, no se puede entregar."
        # Llama al constructor de la clase base Exception para registrar el mensaje
        super().__init__(mensaje)
