# ImportaciÃ³n de la clase Vehiculo desde el mÃ³dulo vehiculo
from vehiculo import Vehiculo

# CreaciÃ³n de una instancia de Vehiculo con patente 'KXPR84' y aÃ±o 2019
vehiculo1 = Vehiculo("KXPR84", 2019)

# 1. Prueba de los mÃ©todos getter pÃºblicos (obtener_patente, obtener_anio, esta_en_taller)
print("=== PRUEBA DE MÃ‰TODOS GETTER ===")
# Muestra la patente del vehÃ­culo obtenida con el mÃ©todo obtener_patente()
print(f"Patente obtenida: {vehiculo1.obtener_patente()}")
# Muestra el aÃ±o del vehÃ­culo obtenido con el mÃ©todo obtener_anio()
print(f"AÃ±o obtenido: {vehiculo1.obtener_anio()}")
# Muestra si el vehÃ­culo estÃ¡ en el taller mediante el mÃ©todo esta_en_taller()
print(f"Â¿EstÃ¡ en el taller reciÃ©n creado?: {vehiculo1.esta_en_taller()}")

# 2. Prueba del mÃ©todo ingresar()
print("\n=== PRUEBA DEL MÃ‰TODO INGRESAR() ===")
# Ejecuta el mÃ©todo ingresar() para simular el ingreso al taller
vehiculo1.ingresar()
# Verifica el nuevo estado del vehÃ­culo usando esta_en_taller()
print(f"Â¿EstÃ¡ en el taller tras ejecutar ingresar()?: {vehiculo1.esta_en_taller()}")

# 3. Prueba del mÃ©todo entregar()
print("\n=== PRUEBA DEL MÃ‰TODO ENTREGAR() ===")
# Ejecuta el mÃ©todo entregar() para simular la salida del taller
vehiculo1.entregar()
# Verifica el nuevo estado del vehÃ­culo usando esta_en_taller()
print(f"Â¿EstÃ¡ en el taller tras ejecutar entregar()?: {vehiculo1.esta_en_taller()}")
