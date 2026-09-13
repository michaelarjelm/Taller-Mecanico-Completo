# Importación de la clase base abstracta Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Importación de la subclase Auto desde el módulo auto
from auto import Auto

# Importación de la subclase Moto desde el módulo moto
from moto import Moto

# Importación de la subclase Camion desde el módulo camion
from camion import Camion

# Importación de la excepción personalizada VehiculoNoIngresadoError desde el paquete Excepciones
from Excepciones.vehiculo_no_ingresado_error import VehiculoNoIngresadoError


# --- PRUEBA 1: Captura de ValueError al crear un Auto con patente inválida ---

# Se inicia el bloque try para evaluar la instanciación con datos inválidos
try:
    # Mensaje en consola indicando el inicio de la prueba de patente inválida
    print("=== CASO 1: Intentando crear un Auto con patente inválida ('AB 12') ===")
    
    # Intento de crear un Auto con patente corta y con espacio
    auto_invalido = Auto("AB 12", 2021)

# Captura la excepción ValueError lanzada por la validación de la patente
except ValueError as error:
    # Imprime el mensaje específico de error de valor recibido
    print(f"[ERROR DE VALOR CAPTURADO] {error}")

# Captura la excepción TypeError en caso de tipo de dato inadecuado
except TypeError as error:
    # Imprime el mensaje de error de tipo
    print(f"[ERROR DE TIPO CAPTURADO] {error}")

# Bloque finally garantizado al terminar la prueba
finally:
    # Muestra mensaje indicando el fin del intento de creación
    print("El intento de creación del valor ha finalizado.\n")


# --- PRUEBA 2: Captura de la excepción personalizada VehiculoNoIngresadoError ---

# Se inicia el bloque try para evaluar el intento de entregar un vehículo que no está en el taller
try:
    # Mensaje en consola indicando la prueba de entrega sin haber ingresado previamente
    print("=== CASO 2: Intentando entregar una Moto que NO se encuentra en el taller ===")
    
    # Creación de una instancia válida de Moto
    moto1 = Moto("MOT123", 2022)
    
    # Intento de entregar la moto directamente (lanzará VehiculoNoIngresadoError)
    moto1.entregar()

# Captura específica de la excepción personalizada VehiculoNoIngresadoError
except VehiculoNoIngresadoError as error:
    # Imprime el mensaje personalizado generado por VehiculoNoIngresadoError
    print(f"[EXCEPCION PERSONALIZADA CAPTURADA] {error}")

# Captura de resguardo para ValueError
except ValueError as error:
    # Imprime mensaje en caso de error de valor
    print(f"[ERROR DE VALOR CAPTURADO] {error}")

# Bloque finally garantizado al terminar la prueba
finally:
    # Muestra mensaje indicando el fin del intento de entrega
    print("El intento de entrega del vehículo ha finalizado.\n")


# --- PRUEBA 3: Flujo normal con operaciones válidas ---

# Mensaje en consola indicando inicio de operaciones válidas
print("=== CASO 3: Flujo normal de ingreso y consulta de vehículos válidos ===")

# Creación de instancia válida de Auto
auto1 = Auto("AB123CD", 2021)

# Creación de instancia válida de Camión
camion1 = Camion("CAM456", 2018, 5000)

# Registro de ingreso exitoso del auto al taller
auto1.ingresar()

# Muestra información del Auto
print(f"Auto - Patente: {auto1.patente}, Año: {auto1.anio}, ¿En taller?: {auto1.en_taller}, Tarifa/Hora: ${auto1.tarifa_hora()}")

# Muestra información del Camión
print(f"Camión - Patente: {camion1.patente}, Año: {camion1.anio}, ¿En taller?: {camion1.en_taller}, Tarifa/Hora: ${camion1.tarifa_hora()}, Capacidad Carga: {camion1.capacidad_carga} kg")



