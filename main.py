# ImportaciÃ³n de la clase Vehiculo desde el archivo vehiculo.py
from vehiculo import Vehiculo

# CreaciÃ³n de una instancia de Vehiculo con patente 'KXPR84' y aÃ±o 2019
vehiculo1 = Vehiculo("KXPR84", 2019)

# ImpresiÃ³n de los datos del vehÃ­culo por consola
print(f"Patente: {vehiculo1.patente}")
print(f"AÃ±o: {vehiculo1.anio}")
print(f"Â¿En taller?: {vehiculo1._en_taller}")
