# ImportaciÃ³n de la clase Vehiculo desde el mÃ³dulo vehiculo
from vehiculo import Vehiculo

# CreaciÃ³n de la primera instancia v1 con patente 'KXPR84' y aÃ±o 2019
v1 = Vehiculo("KXPR84", 2019)

# CreaciÃ³n de la segunda instancia v2 con patente 'JKLM12' y aÃ±o 2016
v2 = Vehiculo("JKLM12", 2016)

# Se registra el ingreso al taller Ãºnicamente para el vehÃ­culo v1
v1.ingresar()

# ImpresiÃ³n de los datos del vehÃ­culo v1 usando las propiedades patente y en_taller
print(f"VehÃ­culo 1 - Patente: {v1.patente}, Â¿En taller?: {v1.en_taller}")

# ImpresiÃ³n de los datos del vehÃ­culo v2 usando las propiedades patente y en_taller
print(f"VehÃ­culo 2 - Patente: {v2.patente}, Â¿En taller?: {v2.en_taller}")
