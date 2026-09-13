# Importación de la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Clase Auto: Subclase que representa un automóvil e invalida/sobrescribe la tarifa por hora
class Auto(Vehiculo):

    # Sobrescribe el método tarifa_hora de la clase base para retornar la tarifa específica de un auto
    def tarifa_hora(self) -> int:
        # Retorna el valor entero 25000 correspondiente a la tarifa por hora de un automóvil
        return 25000
