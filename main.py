# ImportaciÃ³n de la clase Vehiculo desde el mÃ³dulo vehiculo
from vehiculo import Vehiculo

# CreaciÃ³n de una instancia de Vehiculo con patente 'KXPR84' y aÃ±o 2019
vehiculo1 = Vehiculo("KXPR84", 2019)

# 1. Prueba de las propiedades de solo lectura (@property)
print("=== PRUEBA DE PROPIEDADES (@property) ===")
# Acceso a la propiedad de solo lectura patente (sin parÃ©ntesis)
print(f"Patente obtenida: {vehiculo1.patente}")
# Acceso a la propiedad de solo lectura anio (sin parÃ©ntesis)
print(f"AÃ±o obtenido: {vehiculo1.anio}")
# Acceso a la propiedad de solo lectura en_taller (sin parÃ©ntesis)
print(f"Â¿EstÃ¡ en el taller reciÃ©n creado?: {vehiculo1.en_taller}")

# 2. Prueba del mÃ©todo ingresar()
print("\n=== PRUEBA DEL MÃ‰TODO INGRESAR() ===")
# Ejecuta el mÃ©todo ingresar() para simular el ingreso al taller
vehiculo1.ingresar()
# Consulta la propiedad en_taller tras llamar a ingresar()
print(f"Â¿EstÃ¡ en el taller tras ejecutar ingresar()?: {vehiculo1.en_taller}")

# 3. Prueba del mÃ©todo entregar()
print("\n=== PRUEBA DEL MÃ‰TODO ENTREGAR() ===")
# Ejecuta el mÃ©todo entregar() para simular la salida del taller
vehiculo1.entregar()
# Consulta la propiedad en_taller tras llamar a entregar()
print(f"Â¿EstÃ¡ en el taller tras ejecutar entregar()?: {vehiculo1.en_taller}")
