# Importación de la clase base abstracta Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Importación de la subclase Auto desde el módulo auto
from auto import Auto

# Importación de la subclase Moto desde el módulo moto
from moto import Moto

# Importación de la subclase Camion desde el módulo camion
from camion import Camion


# --- PRUEBA 1: Captura de excepciones con try/except al instanciar un objeto inválido ---

# Se inicia el bloque try para intentar ejecutar código propenso a errores (creación con patente inválida)
try:
    # Impresión informativa antes de ejecutar la instanciación propensa a error
    print("=== Intentando crear un Auto con patente inválida ('AB 12') ===")
    
    # Intento de crear un Auto con patente inválida (menos de 6 caracteres y con espacio)
    auto_invalido = Auto("AB 12", 2021)

# El bloque except captura la excepción ValueError lanzada por el setter de la clase Vehiculo
except ValueError as error:
    # Se imprime un mensaje controlado mostrando la descripción exacta de la excepción capturada
    print(f"[EXCEPCION CAPTURADA] Mensaje: {error}")
    # Se informa que gracias al try/except el programa no colapsó y continúa su flujo normal
    print("Manejo exitoso: El programa continúa su ejecución sin interrumpirse.\n")



# --- PRUEBA 2: Instanciación válida de subclases y flujo normal del programa ---

# Impresión informativa del inicio de la ejecución normal
print("=== Creando e ingresando objetos válidos ===")

# Creación de una instancia de Auto con patente válida de 7 caracteres sin espacios
auto1 = Auto("AB123CD", 2021)

# Creación de una instancia de Moto con patente válida de 6 caracteres sin espacios
moto1 = Moto("MOT123", 2022)

# Creación de una instancia de Camion con patente válida, año y capacidad de carga en kg
camion1 = Camion("CAM456", 2018, 5000)

# Registro del ingreso del automóvil al taller mediante el método ingresar()
auto1.ingresar()

# Impresión en consola de los datos del Auto demostrando herencia y método tarifa_hora()
print(f"Auto - Patente: {auto1.patente}, Año: {auto1.anio}, ¿En taller?: {auto1.en_taller}, Tarifa/Hora: ${auto1.tarifa_hora()}")

# Impresión en consola de los datos de la Moto demostrando herencia y su tarifa_hora() propia
print(f"Moto - Patente: {moto1.patente}, Año: {moto1.anio}, ¿En taller?: {moto1.en_taller}, Tarifa/Hora: ${moto1.tarifa_hora()}")

# Impresión en consola de los datos del Camión demostrando su atributo exclusivo capacidad_carga
print(f"Camión - Patente: {camion1.patente}, Año: {camion1.anio}, ¿En taller?: {camion1.en_taller}, Tarifa/Hora: ${camion1.tarifa_hora()}, Capacidad Carga: {camion1.capacidad_carga} kg")

