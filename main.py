# Importación de la clase base abstracta Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Importación de la subclase Auto desde el módulo auto
from auto import Auto

# Importación de la subclase Moto desde el módulo moto
from moto import Moto

# Importación de la subclase Camion desde el módulo camion
from camion import Camion

# --- PRUEBA 1: Instanciación y funcionamiento de subclases concretas ---

# Creación de una instancia de Auto especificando patente y año
auto1 = Auto("AB123CD", 2021)

# Creación de una instancia de Moto especificando patente y año
moto1 = Moto("MOT123", 2022)

# Creación de una instancia de Camion especificando patente, año y capacidad de carga en kg
camion1 = Camion("CAM456", 2018, 5000)

# Invocación del método ingresar() en el auto para cambiar su estado en taller
auto1.ingresar()

# Muestra en consola los datos del Auto demostrando herencia y el método tarifa_hora()
print(f"Auto - Patente: {auto1.patente}, Año: {auto1.anio}, ¿En taller?: {auto1.en_taller}, Tarifa/Hora: ${auto1.tarifa_hora()}")

# Muestra en consola los datos de la Moto demostrando herencia y su propia tarifa_hora()
print(f"Moto - Patente: {moto1.patente}, Año: {moto1.anio}, ¿En taller?: {moto1.en_taller}, Tarifa/Hora: ${moto1.tarifa_hora()}")

# Muestra en consola los datos del Camión demostrando atributo propio y su tarifa_hora()
print(f"Camión - Patente: {camion1.patente}, Año: {camion1.anio}, ¿En taller?: {camion1.en_taller}, Tarifa/Hora: ${camion1.tarifa_hora()}, Capacidad Carga: {camion1.capacidad_carga} kg")

# --- PRUEBA 2: Comprobación de abstracción (intento de instanciar Vehiculo directamente) ---
# Intentar instanciar la clase Vehiculo producirá un TypeError porque hereda de ABC y tiene un método abstracto.
# No se utiliza try/except ya que el manejo de excepciones no ha sido abordado aún con los estudiantes.

vehiculo_invalido = Vehiculo("VEH123", 2020)  # Lanzará: TypeError: Can't instantiate abstract class Vehiculo
