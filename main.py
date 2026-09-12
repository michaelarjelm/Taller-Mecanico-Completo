# ImportaciÃ³n de la clase Vehiculo desde el mÃ³dulo vehiculo
from vehiculo import Vehiculo

# InstanciaciÃ³n de un objeto Vehiculo con patente 'KXPR84' y aÃ±o 2019
vehiculo1 = Vehiculo("KXPR84", 2019)

# ImpresiÃ³n del estado inicial accediendo a los mÃ©todos pÃºblicos getter
print(f"Estado inicial - Patente: {vehiculo1.obtener_patente()}, AÃ±o: {vehiculo1.obtener_anio()}, Â¿En taller?: {vehiculo1.esta_en_taller()}")

# InvocaciÃ³n del mÃ©todo ingresar() para simular la entrada del vehÃ­culo al taller
vehiculo1.ingresar()

# ImpresiÃ³n del estado tras llamar al mÃ©todo ingresar() usando esta_en_taller()
print(f"Tras ingresar() - Â¿En taller?: {vehiculo1.esta_en_taller()}")

# InvocaciÃ³n del mÃ©todo entregar() para simular la entrega del vehÃ­culo al cliente
vehiculo1.entregar()

# ImpresiÃ³n del estado tras llamar al mÃ©todo entregar() usando esta_en_taller()
print(f"Tras entregar() - Â¿En taller?: {vehiculo1.esta_en_taller()}")
