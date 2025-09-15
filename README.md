# EMA Backend API

Este repositorio contiene el código fuente del backend para la aplicación **EMA (Espacio de Monitoreo y Apoyo)**. Este servidor provee los datos necesarios sobre estudiantes y plantillas de sondeos a través de una API RESTful, permitiendo que el frontend consuma y muestre la información.

Este proyecto es un "esqueleto funcional" para el primer avance del curso, contiene la comunicación entre un frontend web, un backend y una base de datos.

## Integrantes

**Sergio Nicolas Fonseca Niño:** 000532259.

**Luisa García Gallego:** 000531822.

**Salomé Trujillo Berrío:** 000530107.

**Valentina Martínez Tribiño:** 000509695.

## UML implementación actual

<img width="3840" height="1389" alt="Untitled diagram _ Mermaid Chart-2025-09-14-210630" src="https://github.com/user-attachments/assets/9cc7c726-5ff2-4053-9e2a-6200393ed2ab" />


## Tecnologías Utilizadas

*   **Lenguaje:** Python 3.9+
*   **Framework:** FastAPI
*   **Servidor ASGI:** Uvicorn
*   **Base de Datos:** SQLite
*   **ORM:** SQLAlchemy

---

## Puesta en Marcha

Sigue estas instrucciones paso a paso para configurar y ejecutar el servidor en tu máquina local.

### Prerrequisitos

Tener [Python 3.9](https://www.python.org/downloads/) o una versión superior instalada.
+ **¡Muy Importante para Windows!** Durante la instalación de Python, asegúrate de marcar la casilla que dice **"Add Python to PATH"**. Si no lo haces, los comandos `python` y `pip` no funcionarán en la terminal.


### 1. Descarga el Repositorio

Primero, descaga este repositorio en tu máquina local y descomprimelo.

Despues en tu cmd dirigete a la direccion del proyecto.
```bash
cd ema_backend # O el nombre de la carpeta raíz
```

### 2. Configurar el Entorno

Crear el entorno virtual.

```bash
python -m venv venv
```
Activar el entorno virtual
+ En Windows:
```bash
.\venv\Scripts\activate
```
+ En Mac/Linux:
```bash
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

---

## Ejecutar el Servidor

Una vez que el entorno está configurado y la base de datos inicializada, puedes iniciar el servidor.

```bash
uvicorn main:app --reload
```

---

## Uso y Prueba

Con el servidor local corriendo, ahora puedes probar la aplicación.

### Usar la Aplicación Web (Frontend)

La forma principal de interactuar con el backend es a través del cliente web, que ya está desplegado.

1.  **Asegúrate de que tu servidor local esté corriendo.**
2.  **Abre tu navegador web y dirígete a la siguiente URL:**

    [**https://nicofon1.github.io/ema_webApp/**](https://nicofon1.github.io/ema_webApp/)

La aplicación web está configurada para comunicarse con tu servidor local en `http://127.0.0.1:8000`. Podrás ver la lista de estudiantes y cargar los cuestionarios directamente desde la interfaz.
