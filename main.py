# Importación de las subclases Auto, Moto y Camion desde sus respectivos módulos
from auto import Auto
from moto import Moto
from camion import Camion

# Instanciación de vehículos válidos
auto1 = Auto("AB123CD", 2021)
moto1 = Moto("MOT123", 2022)
camion1 = Camion("CAM456", 2018, 5000)

# --- PRUEBA DE CICLO NORMAL ---
auto1.ingresar()
print(f"Auto ingresado con éxito - ¿En taller?: {auto1.en_taller}")

# --- PRUEBAS DE VALIDACIÓN DE ESTADO EN TALLER ---
# Descomenta una de las siguientes líneas para verificar que se lanza el ValueError correspondiente:

# Intento de re-ingresar un vehículo que ya está en el taller:
#auto1.ingresar()  # Lanzará: ValueError: El vehículo ya se encuentra dentro del taller.

# Intento de entregar una moto que nunca ingresó al taller:
moto1.entregar()  # Lanzará: ValueError: El vehículo no se encuentra en el taller, no se puede entregar.
