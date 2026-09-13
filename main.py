# Importación de la clase base abstracta Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Importación de la subclase Auto desde el módulo auto
from auto import Auto

# Importación de la subclase Moto desde el módulo moto
from moto import Moto

# Importación de la subclase Camion desde el módulo camion
from camion import Camion


# --- PRUEBA 1: Estructura try / except (múltiples bloques) / finally para patente inválida ---

# Se inicia el bloque try para evaluar la creación de un objeto susceptible a errores
try:
    # Mensaje en consola indicando el inicio del primer intento de instanciación
    print("=== CASO 1: Intentando crear un Auto con patente inválida ('AB 12') ===")
    
    # Intento de crear un Auto con patente con menos de 6 caracteres y con un espacio en blanco
    auto_invalido = Auto("AB 12", 2021)

# Primer bloque except: captura errores de datos o formato (ValueError lanzado por el setter)
except ValueError as error:
    # Muestra el mensaje específico del ValueError recibido desde la clase Vehiculo
    print(f"[ERROR DE VALOR CAPTURADO] {error}")

# Segundo bloque except: captura errores de tipo (TypeError en caso de tipos de datos o instanciación)
except TypeError as error:
    # Muestra el mensaje específico de un error de tipo
    print(f"[ERROR DE TIPO CAPTURADO] {error}")

# Bloque except genérico: captura cualquier otra excepción no contemplada previamente
except Exception as error:
    # Muestra el mensaje de cualquier otro error inesperado
    print(f"[ERROR INESPERADO CAPTURADO] {error}")

# Bloque finally: se ejecuta SIEMPRE al terminar el bloque try/except, sin importar si hubo error o no
finally:
    # Informa al usuario que el proceso e intento de creación ha finalizado
    print("El intento de creación del valor ha finalizado.\n")


# --- PRUEBA 2: Estructura try / except (múltiples bloques) / finally para clase abstracta ---

# Se inicia un segundo bloque try para evaluar el intento de instanciar la clase base abstracta
try:
    # Mensaje en consola indicando el inicio del segundo intento de instanciación
    print("=== CASO 2: Intentando instanciar la clase base abstracta Vehiculo directamente ===")
    
    # Intento de instanciar Vehiculo directamente (provocará un TypeError al ser una clase ABC)
    vehiculo_base = Vehiculo("VEH123", 2020)

# Primer bloque except: captura errores de valor (ValueError)
except ValueError as error:
    # Muestra el mensaje de un ValueError
    print(f"[ERROR DE VALOR CAPTURADO] {error}")

# Segundo bloque except: captura el TypeError generado por intentar instanciar la clase abstracta
except TypeError as error:
    # Muestra el mensaje del TypeError lanzado por Python al intentar instanciar una clase ABC
    print(f"[ERROR DE TIPO CAPTURADO] {error}")

# Bloque except genérico: captura cualquier otro error no especificado
except Exception as error:
    # Muestra el mensaje de cualquier otro error
    print(f"[ERROR INESPERADO CAPTURADO] {error}")

# Bloque finally: se ejecuta de forma garantizada al finalizar el bloque de control
finally:
    # Informa al usuario que el proceso e intento de creación ha finalizado
    print("El intento de creación del valor ha finalizado.\n")


# --- PRUEBA 3: Flujo normal con creación exitosa de objetos válidos ---

# Mensaje en consola indicando el inicio del flujo normal
print("=== CASO 3: Creación e ingreso exitoso de objetos válidos ===")

# Creación de una instancia de Auto con patente válida de 7 caracteres sin espacios
auto1 = Auto("AB123CD", 2021)

# Creación de una instancia de Moto con patente válida de 6 caracteres sin espacios
moto1 = Moto("MOT123", 2022)

# Creación de una instancia de Camion con patente válida, año y capacidad de carga en kg
camion1 = Camion("CAM456", 2018, 5000)

# Registro del ingreso del automóvil al taller mediante el método ingresar()
auto1.ingresar()

# Muestra en consola los datos del Auto demostrando herencia y el método tarifa_hora()
print(f"Auto - Patente: {auto1.patente}, Año: {auto1.anio}, ¿En taller?: {auto1.en_taller}, Tarifa/Hora: ${auto1.tarifa_hora()}")

# Muestra en consola los datos de la Moto demostrando herencia y su tarifa_hora() propia
print(f"Moto - Patente: {moto1.patente}, Año: {moto1.anio}, ¿En taller?: {moto1.en_taller}, Tarifa/Hora: ${moto1.tarifa_hora()}")

# Muestra en consola los datos del Camión demostrando su atributo exclusivo capacidad_carga
print(f"Camión - Patente: {camion1.patente}, Año: {camion1.anio}, ¿En taller?: {camion1.en_taller}, Tarifa/Hora: ${camion1.tarifa_hora()}, Capacidad Carga: {camion1.capacidad_carga} kg")


