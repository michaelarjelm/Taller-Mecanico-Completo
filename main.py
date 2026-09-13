# Importación de las subclases Auto, Moto y Camion desde sus respectivos módulos
from auto import Auto
from moto import Moto
from camion import Camion

# Creación de una instancia de Auto heredando el constructor de Vehiculo
auto1 = Auto("AB123CD", 2021)

# Creación de una instancia de Moto heredando el constructor de Vehiculo
moto1 = Moto("MOT123", 2022)

# Creación de una instancia de Camion especificando patente, año y su capacidad de carga (5000 kg)
camion1 = Camion("CAM456", 2018, 5000)

# Invocación del método heredado ingresar() en la instancia de Auto
auto1.ingresar()

# Impresión de datos demostrando la herencia y el atributo propio capacidad_carga de Camion
print(f"Auto - Patente: {auto1.patente}, Año: {auto1.anio}, ¿En taller?: {auto1.en_taller}, Tarifa/Hora: ${auto1.tarifa_hora()}")
print(f"Moto - Patente: {moto1.patente}, Año: {moto1.anio}, ¿En taller?: {moto1.en_taller}, Tarifa/Hora: ${moto1.tarifa_hora()}")
print(f"Camión - Patente: {camion1.patente}, Año: {camion1.anio}, ¿En taller?: {camion1.en_taller}, Tarifa/Hora: ${camion1.tarifa_hora()}, Capacidad Carga: {camion1.capacidad_carga} kg")
