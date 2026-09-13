# Importación de la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Clase Moto: Subclase que representa una motocicleta e invalida/sobrescribe la tarifa por hora
class Moto(Vehiculo):

    # Sobrescribe el método tarifa_hora de la clase base para retornar la tarifa específica de una moto
    def tarifa_hora(self) -> int:
        # Retorna el valor entero 15000 correspondiente a la tarifa por hora de una motocicleta
        return 15000
