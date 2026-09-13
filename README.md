# Taller Mecánico Completo

Repositorio para el desarrollo del modelo completo de un taller mecánico, correspondiente al módulo **Programación Orientada a Objetos Seguro** del **segundo semestre del año 2026**.

**Profesor:** Michael Arjel  
**Institución:** INACAP  
**Periodo Académico:** Primavera 2026 (Segundo Semestre)  

---

## 📌 Descripción del Proyecto

Este repositorio tiene como propósito construir paso a paso la arquitectura y el modelo completo para la gestión integral de un taller mecánico. Se aplican principios fundamentales de la Programación Orientada a Objetos (POO) con un enfoque en diseño seguro y buenas prácticas de software:

- **Encapsulamiento y Validación:** Protección del estado interno de los objetos y validación rigurosa de entradas mediante atributos privados, `@property` y setters.
- **Herencia y Polimorfismo:** Modelado de jerarquías de vehículos con sobrescritura de métodos (`override`).
- **Modularidad:** Separación limpia de responsabilidades, cada clase en su propio archivo.
- **Manejo de Errores:** Validación activa en setters lanzando `ValueError` cuando los datos no cumplen las reglas de negocio.

---

## 🗂️ Estructura de Archivos

```
Taller-Mecanico-Completo/
├── vehiculo.py    # Clase base Vehiculo
├── auto.py        # Subclase Auto (hereda de Vehiculo)
├── moto.py        # Subclase Moto (hereda de Vehiculo)
├── camion.py      # Subclase Camion (hereda de Vehiculo)
└── main.py        # Script de pruebas
```

---

## 📋 Bitácora de Desarrollo

### ✅ Commit 1 — `feat: creación de la clase vacía Vehiculo`
**Archivo:** `vehiculo.py`

Se crea el archivo `vehiculo.py` con la clase `Vehiculo` completamente vacía usando `pass`. Esta es la estructura mínima en Python para declarar una clase que aún no tiene cuerpo. Representa el "molde" o plantilla base sobre la que se construirá toda la jerarquía de vehículos del taller.

```python
class Vehiculo:
    pass
```

---

### ✅ Commit 2 — `feat: declaración de atributos patente, anio y _en_taller`
**Archivo:** `vehiculo.py`

Se incorporan las tres declaraciones de atributos de clase con **anotación de tipos** (`type hints`): `patente` como `str`, `anio` como `int` y `_en_taller` como `bool`. En esta etapa son solo declaraciones en el cuerpo de la clase, sin constructor aún. El prefijo `_` en `_en_taller` indica convencionalmente que es un atributo protegido.

```python
class Vehiculo:
    patente: str
    anio: int
    _en_taller: bool
```

---

### ✅ Commit 3 — `feat: implementación del constructor __init__`
**Archivo:** `vehiculo.py`

Se define el método especial `__init__()`, el constructor de la clase. Recibe `patente` y `anio` como parámetros y los asigna directamente a atributos de instancia. El atributo `_en_taller` se fija en `False` de forma predeterminada, ya que un vehículo recién registrado nunca parte dentro del taller. Cada línea está comentada con propósito pedagógico.

```python
def __init__(self, patente: str, anio: int):
    self.patente = patente
    self.anio = anio
    self._en_taller = False
```

---

### ✅ Commit 4 — `test: creación de main.py e instanciación inicial de Vehiculo`
**Archivo:** `main.py`

Se crea el script de pruebas `main.py`. Se importa la clase `Vehiculo`, se instancia un objeto con patente `'KXPR84'` y año `2019`, y se imprimen sus tres atributos usando `print()`. Permite verificar que el constructor funciona correctamente.

```python
from vehiculo import Vehiculo
vehiculo1 = Vehiculo("KXPR84", 2019)
print(f"Patente: {vehiculo1.patente}")
print(f"Año: {vehiculo1.anio}")
print(f"¿En taller?: {vehiculo1._en_taller}")
```

---

### ✅ Commit 5 — `feat: agregado de métodos ingresar() y entregar()`
**Archivos:** `vehiculo.py`, `main.py`

Se implementan los dos métodos de comportamiento de la clase: `ingresar()` cambia `_en_taller` a `True` y `entregar()` lo cambia a `False`. Ninguno recibe parámetros adicionales ni retorna valor (`-> None`). Se actualiza `main.py` para probar el ciclo de ingreso y entrega sobre el mismo vehículo.

```python
def ingresar(self) -> None:
    self._en_taller = True

def entregar(self) -> None:
    self._en_taller = False
```

---

### ✅ Commit 6 — `refactor: encapsulamiento con atributos privados y métodos getter`
**Archivos:** `vehiculo.py`, `main.py`

Se aplica **encapsulamiento estricto**: los atributos pasan a ser privados con doble guion bajo (`__patente`, `__anio`, `__en_taller`), eliminando las declaraciones de clase que quedaban fuera del constructor. Se crean métodos getter públicos (`obtener_patente()`, `obtener_anio()`, `esta_en_taller()`) para exponer los valores de forma controlada. Se actualiza `main.py` para usar los nuevos getters.

```python
def obtener_patente(self) -> str:
    return self.__patente

def obtener_anio(self) -> int:
    return self.__anio

def esta_en_taller(self) -> bool:
    return self.__en_taller
```

---

### ✅ Commit 7 — `test: prueba detallada de getters e ingreso/entrega`
**Archivo:** `main.py`

Se reestructura `main.py` dividiéndolo en tres bloques de prueba explícitos y bien comentados: uno para verificar los getters (`obtener_patente`, `obtener_anio`, `esta_en_taller`), otro para probar `ingresar()` y otro para `entregar()`. Cada sección imprime el estado del objeto con `print()`.

---

### ✅ Commit 8 — `refactor: uso del decorador @property para atributos de solo lectura`
**Archivos:** `vehiculo.py`, `main.py`

Se reemplazan los tres métodos getter por el decorador `@property`, que convierte los métodos en **propiedades de solo lectura** accesibles sin paréntesis (`vehiculo1.patente` en lugar de `vehiculo1.obtener_patente()`). Esto mejora la legibilidad y sigue el estilo idiomático de Python.

```python
@property
def patente(self) -> str:
    return self.__patente

@property
def anio(self) -> int:
    return self.__anio

@property
def en_taller(self) -> bool:
    return self.__en_taller
```

---

### ✅ Commit 9 — `test: prueba de estado independiente con múltiples instancias v1 y v2`
**Archivo:** `main.py`

Se instancian dos objetos distintos (`v1` con patente `'KXPR84'` y `v2` con patente `'JKLM12'`). Se llama a `ingresar()` solo en `v1` y se imprime el estado de ambos. Este test demuestra que cada instancia mantiene su propio estado independiente, validando el correcto funcionamiento del encapsulamiento.

```
Vehículo 1 - Patente: KXPR84, ¿En taller?: True
Vehículo 2 - Patente: JKLM12, ¿En taller?: False
```

---

### ✅ Commit 10 — `docs: incorporación de la bitácora de commits al README`
**Archivo:** `README.md`

Se documenta formalmente en el `README.md` la bitácora evolutiva de los primeros 9 commits, describiendo qué se hizo en cada etapa, el propósito pedagógico y fragmentos de código representativos. Este documento sirve como guía de lectura para los alumnos que recorran el historial del repositorio.

---

### ✅ Commit 11 — `feat: agregado del método tarifa_hora() en Vehiculo`
**Archivo:** `vehiculo.py`

Se agrega el método `tarifa_hora()` a la clase base `Vehiculo`, que retorna el valor entero `5000` representando la tarifa base de reparación por hora. Este método está pensado para ser sobrescrito en las subclases.

```python
def tarifa_hora(self) -> int:
    return 5000
```

---

### ✅ Commit 12 — `feat: creación de subclases Auto, Moto y Camion`
**Archivos:** `auto.py`, `moto.py`, `camion.py`, `main.py`

Se crean tres nuevas subclases en archivos separados, cada una heredando de `Vehiculo` usando `class NombreClase(Vehiculo):`. En esta etapa, las tres clases se dejan vacías con `pass`: heredan automáticamente el constructor, todas las propiedades y todos los métodos de `Vehiculo`. Se actualiza `main.py` para importar y probar las tres.

```python
class Auto(Vehiculo):
    pass

class Moto(Vehiculo):
    pass

class Camion(Vehiculo):
    pass
```

---

### ✅ Commit 13 — `feat: constructor propio y propiedad capacidad_carga en Camion`
**Archivo:** `camion.py`

Se implementa un constructor propio en `Camion`, que recibe `patente`, `anio` y `capacidad_carga`. Primero invoca a `super().__init__(patente, anio)` para inicializar los atributos heredados, luego guarda `capacidad_carga` como atributo privado `__capacidad_carga`. Se agrega su `@property` de solo lectura.

```python
def __init__(self, patente: str, anio: int, capacidad_carga: int):
    super().__init__(patente, anio)
    self.__capacidad_carga = capacidad_carga

@property
def capacidad_carga(self) -> int:
    return self.__capacidad_carga
```

---

### ✅ Commit 14 — `feat: polimorfismo - sobrescritura de tarifa_hora() en Auto, Moto y Camion`
**Archivos:** `auto.py`, `moto.py`, `camion.py`

Se aplica **polimorfismo mediante sobrescritura** (`method overriding`): cada subclase redefine `tarifa_hora()` retornando su propia tarifa diferenciada, sin modificar `vehiculo.py`. Python resuelve en tiempo de ejecución qué versión del método invocar según el tipo real del objeto.

| Clase | Tarifa/Hora |
|-------|------------|
| `Vehiculo` (base) | $5.000 |
| `Auto` | $25.000 |
| `Moto` | $15.000 |
| `Camion` | $40.000 |

---

### ✅ Commit 15 — `feat: setter con validación para patente en Vehiculo`
**Archivo:** `vehiculo.py`

Se agrega un **setter** para la propiedad `patente` usando el decorador `@patente.setter`. El setter valida que el valor ingresado tenga al menos 6 caracteres y no contenga espacios; si no cumple, lanza un `ValueError` con un mensaje descriptivo. El constructor se actualiza para asignar a través del setter (`self.patente = patente`) en lugar de directo al atributo privado, asegurando que la validación corra también al crear el objeto.

```python
@patente.setter
def patente(self, nueva_patente: str) -> None:
    if len(nueva_patente) < 6 or " " in nueva_patente:
        raise ValueError("La patente debe tener al menos 6 caracteres y no contener espacios.")
    self.__patente = nueva_patente
```

---

### ✅ Commit 16 — `feat: validación de estado preexistente en métodos ingresar() y entregar()`
**Archivos:** `vehiculo.py`, `main.py`

Se incorporan **validaciones de precondición** en los métodos de comportamiento de `Vehiculo`. El método `ingresar()` valida que el vehículo no se encuentre previamente dentro del taller (`self.__en_taller == False`), de lo contrario lanza un `ValueError`. De forma análoga, `entregar()` verifica que el vehículo esté en el taller (`self.__en_taller == True`) antes de proceder con su entrega. Se actualizan las pruebas en `main.py` para demostrar ambas reglas de negocio.

```python
def ingresar(self) -> None:
    if self.__en_taller:
        raise ValueError("El vehículo ya se encuentra dentro del taller.")
    self.__en_taller = True

def entregar(self) -> None:
    if not self.__en_taller:
        raise ValueError("El vehículo no se encuentra en el taller, no se puede entregar.")
    self.__en_taller = False
```

---

### ✅ Commit 17 — `refactor: conversión de Vehiculo en clase base abstracta con ABC`
**Archivos:** `vehiculo.py`, `main.py`

Se transforma la clase base `Vehiculo` en una **Clase Base Abstracta** mediante la herencia de `ABC` del módulo `abc` y la aplicación del decorador `@abstractmethod` sobre el método `tarifa_hora()`. Esto impide la instanciación directa de `Vehiculo` (lanzando `TypeError`) y establece el contrato tarifario que deben implementar obligatoriamente las subclases concretas. Se actualiza `main.py` comentando minuciosamente cada línea para verificar tanto la ejecución de las subclases como el bloqueo de instanciación directa de `Vehiculo`.

```python
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    ...
    @abstractmethod
    def tarifa_hora(self) -> int:
        pass
```

---

### ✅ Commit 18 — `test: captura de excepciones con try/except en main.py`
**Archivo:** `main.py`

Se implementa la **captura de excepciones** en `main.py` envolviendo la instanciación de un objeto con datos inválidos dentro de un bloque `try...except ValueError as error`. Esto demuestra la interacción entre la validación interna de la clase (`raise ValueError`) y el manejo controlado de errores en la capa de ejecución, evitando el colapso del programa. Se comentaron minuciosamente todas las líneas de código con propósito pedagógico.

```python
try:
    auto_invalido = Auto("AB 12", 2021)
except ValueError as error:
    print(f"[EXCEPCION CAPTURADA] Mensaje: {error}")
```

---

## 🛠️ Estructura y Plan de Desarrollo Futuro

1. **Gestión de Clientes y Personal:** Registro de propietarios, mecánicos y roles del taller.
2. **Órdenes de Trabajo y Servicios:** Ciclo de vida del mantenimiento, asignación de tareas y cálculo de tarifas.
3. **Inventario y Repuestos:** Control de insumos utilizados en las reparaciones.

---

## 🚀 Historial de Versiones

- **v0.1.0 (Inicial):** Estructura base del repositorio y documentación inicial del proyecto.
- **v0.2.0:** Clase `Vehiculo` completa con encapsulamiento, `@property`, setter con validación y método `tarifa_hora()`.
- **v0.3.0:** Jerarquía de herencia con `Auto`, `Moto` y `Camion`. Polimorfismo aplicado en `tarifa_hora()`.
- **v0.3.1:** Validación de precondiciones de estado para `ingresar()` y `entregar()` en la clase base `Vehiculo`.
- **v0.4.0:** Transformación de `Vehiculo` en clase base abstracta (`ABC`) con `@abstractmethod` en `tarifa_hora()`.
- **v0.4.1:** Demostración pedagógica del manejo de excepciones con `try...except` en `main.py`.

