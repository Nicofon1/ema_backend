# EMA Backend API

Este repositorio contiene el código fuente del backend para la aplicación **EMA (Espacio de Monitoreo y Apoyo)**. El propósito de este servidor es proveer los datos necesarios sobre estudiantes y plantillas de sondeos a través de una API RESTful, permitiendo que el frontend consuma y muestre la información de manera dinámica.

Este proyecto representa un "esqueleto funcional" (walking skeleton) para el primer avance del curso, demostrando la comunicación exitosa entre un frontend web, un backend y una base de datos.

## Integrantes

**Sergio Nicolas Fonseca Niño:** 000532259.

**Luisa García Gallego:** 000531822.

**Salomé Trujillo Berrío:** 000530107.

**Valentina Martínez Tribiño:** 000509695.

## Tecnologías Utilizadas

*   **Lenguaje:** Python 3.9+
*   **Framework:** FastAPI
*   **Servidor ASGI:** Uvicorn
*   **Base de Datos:** SQLite
*   **ORM:** SQLAlchemy

---

## Getting Started: Puesta en Marcha

Sigue estas instrucciones paso a paso para configurar y ejecutar el servidor en tu máquina local.

### Prerrequisitos

*   Tener [Python 3.9](https://www.python.org/downloads/) o una versión superior instalada.
*   Tener [Git](https://git-scm.com/downloads) instalado.

### 1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina local.

```bash
git clone [URL_DE_TU_REPOSITORIO_DE_GITHUB]
cd ema_backend # O el nombre de la carpeta raíz
```

### 2. Configurar el Entorno Virtual

Es una buena práctica usar un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
.\venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```

### 3. Instalar Dependencias

Instala todas las librerías necesarias que se encuentran en el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Inicializar la Base de Datos

Este proyecto utiliza SQLite. Se incluye un script para crear la base de datos (`ema_app.db`) y poblarla con datos de prueba (estudiantes y plantillas de sondeos).

**Este paso solo necesitas hacerlo una vez.**

```bash
python seed_db.py
```
Al finalizar, verás un nuevo archivo llamado `ema_app.db` en la raíz del proyecto.

---

## Ejecutar el Servidor

Una vez que el entorno está configurado y la base de datos inicializada, puedes iniciar el servidor.

```bash
uvicorn main:app --reload
```

El comando iniciará el servidor de desarrollo. La opción `--reload` hace que el servidor se reinicie automáticamente cada vez que guardes un cambio en el código.

Verás un mensaje en la terminal indicando que el servidor está corriendo, usualmente en:
`http://127.0.0.1:8000`

---

## Uso y Prueba

Con el servidor local corriendo, ahora puedes probar la aplicación.

### Método 1: Usar la Aplicación Web (Frontend)

La forma principal de interactuar con el backend es a través del cliente web, que ya está desplegado.

1.  **Asegúrate de que tu servidor local esté corriendo.**
2.  **Abre tu navegador web y dirígete a la siguiente URL:**

    [**https://nicofon1.github.io/ema_webApp/**](https://nicofon1.github.io/ema_webApp/)

La aplicación web está configurada para comunicarse con tu servidor local en `http://127.0.0.1:8000`. Podrás ver la lista de estudiantes y cargar los cuestionarios directamente desde la interfaz.

### Método 2: Probar la API Directamente

FastAPI genera automáticamente una documentación interactiva de la API. Es una excelente herramienta para probar los endpoints de forma aislada.

1.  **Con el servidor corriendo, abre tu navegador y ve a:**

    `http://127.0.0.1:8000/docs`

2.  Desde esta interfaz, podrás ver todos los endpoints disponibles, sus parámetros y probarlos directamente para ver las respuestas en formato JSON.
