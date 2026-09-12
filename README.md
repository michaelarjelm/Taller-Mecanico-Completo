# Taller Mecánico Completo

Repositorio para el desarrollo del modelo completo de un taller mecánico, correspondiente al módulo **Programación Orientada a Objetos Seguro** del **segundo semestre del año 2026**.

**Profesor:** Michael Arjel  
**Institución:** INACAP  
**Periodo Académico:** Primavera 2026 (Segundo Semestre)  

---

## 📌 Descripción del Proyecto

Este repositorio tiene como propósito construir paso a paso la arquitectura y el modelo completo para la gestión integral de un taller mecánico. Se aplicarán principios fundamentales de la Programación Orientada a Objetos (POO) con un enfoque en diseño seguro y buenas prácticas de software:

- **Encapsulamiento y Validación:** Protección del estado interno de los objetos y validación rigurosa de entradas y transiciones de estado.
- **Herencia y Polimorfismo:** Modelado de jerarquías de vehículos, personal y servicios.
- **Modularidad:** Separación limpia de responsabilidades (modelos de datos, lógica de negocio y persistencia).
- **Manejo de Errores y Excepciones:** Control de flujos inesperados para garantizar la robustez del sistema.

---

## 📋 Bitácora de Commits y Evolución del Proyecto

A continuación se detalla la secuencia evolutiva de desarrollo registrada en la rama `feature/desarrollo`:

1. **`feat: creación de la clase vacía Vehiculo`**
   - Creación del archivo `vehiculo.py` con la estructura inicial de la clase `Vehiculo` usando `pass`.
2. **`feat: declaración de atributos patente, anio y _en_taller`**
   - Incorporación de la declaración explícita de atributos con anotación de tipos (`str`, `int`, `bool`).
3. **`feat: implementación del constructor __init__`**
   - Definición del método constructor `__init__(self, patente, anio)` inicializando `_en_taller = False` de forma predeterminada.
4. **`test: creación de main.py e instanciación inicial de Vehiculo`**
   - Creación del script `main.py` para instanciar el primer objeto `Vehiculo` y probar la salida de atributos por consola.
5. **`feat: agregado de métodos ingresar() y entregar()`**
   - Implementación de los métodos para modificar el estado `_en_taller` (`ingresar()` y `entregar()`) y actualización de pruebas en `main.py`.
6. **`refactor: encapsulamiento con atributos privados y métodos getter`**
   - Aplicación de encapsulamiento estricto: atributos privados (`__patente`, `__anio`, `__en_taller`), eliminación de declaraciones fuera del constructor y creación de métodos getter (`obtener_patente()`, `obtener_anio()`, `esta_en_taller()`).
7. **`test: prueba detallada de getters e ingreso/entrega`**
   - Reestructuración de `main.py` dividida por bloques de prueba explícitos para validar cada getter e ingresos/entregas.
8. **`refactor: uso del decorador @property para atributos de solo lectura`**
   - Sustitución de los getters por propiedades de solo lectura mediante el decorador `@property` (`patente`, `anio`, `en_taller`).
9. **`test: prueba de estado independiente con múltiples instancias v1 y v2`**
   - Instanciación de dos objetos distintos (`v1` y `v2`) comprobando la independencia del estado `en_taller` entre instancias.

---

## 🛠️ Estructura y Plan de Desarrollo

1. **Gestión de Vehículos:** Modelado de clases base y especializaciones (autos, camionetas, motocicletas, etc.).
2. **Gestión de Clientes y Personal:** Registro de propietarios, mecánicos y roles del taller.
3. **Órdenes de Trabajo y Servicios:** Ciclo de vida del mantenimiento, asignación de tareas y cálculo de tarifas.
4. **Inventario y Repuestos:** Control de insumos utilizados en las reparaciones.

---

## 🚀 Historial de Versiones

- **v0.1.0 (Inicial):** Estructura base del repositorio y documentación inicial del proyecto.
