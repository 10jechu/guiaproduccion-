# 🚀 NutriBox API – Taller Práctico con FastAPI

Este documento es una guía rápida para configurar y explorar la API RESTful del proyecto **NutriBox**, desarrollada como taller de *Producción de Software*.

---

## 👤 Autor

**Jesús Manuel Vilardi González**  
Estudiante de Ingeniería de Sistemas  
Universidad Católica de Colombia  

---

## 💡 Objetivo del Taller

Implementar y gestionar una API RESTful con **FastAPI** para manejar la información central usando el proyecto de esta materia ( NutriBox),este incluye los modelos : 

- Usuarios  
- Hijos  
- Catálogo de alimentos  
- Gestión de loncheras  

---

## 💻 Tecnologías Utilizadas

- **Python 3.11 o superior**  
- **FastAPI**  
- **Uvicorn** (servidor ASGI)  
- **Pydantic** (validación de datos)  
- **Swagger UI** (documentación interactiva)

---

## ⚙️ Instalación y Configuración

Sigue estos pasos en tu terminal (se recomienda Git Bash) para levantar el servidor localmente:

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/10jechu/guiaproduccion-.git
cd guiaproduccion-

2️⃣ Crear y Activar el Entorno Virtual
python -m venv .venv
source .venv/Scripts/activate

3️⃣ Instalar Dependencias
pip install fastapi "uvicorn[standard]" pydantic[email]

4️⃣ Ejecutar el Servidor
uvicorn app.main:app --reload
5️⃣ Documentación Interactiva (Swagger UI)

Una vez que el servidor esté activo, abre tu navegador en:

http://127.0.0.1:8000/docs

📁 Estructura del Proyecto
guiaproduccion-/
│
├── app/
│   ├── main.py                     # Configuración y arranque de la aplicación
│   ├── models/                     # Esquemas de modelos de datos
│   │   ├── usuario.py
│   │   ├── hijo.py
│   │   ├── alimento.py
│   │   └── lonchera.py
│   └── routes/                     # Definición de los endpoints de la API
│       ├── usuario_routes.py
│       ├── hijo_routes.py
│       ├── alimento_routes.py
│       └── lonchera_routes.py
│
├── .venv/
├── requirements.txt
└── README.md

🗺️ Endpoints Disponibles (CRUD Básico)

Usuarios

| Método | Ruta             | Descripción              |
| :----: | :--------------- | :----------------------- |
|   GET  | `/usuarios`      | Lista todos los usuarios |
|  POST  | `/usuarios`      | Crea un nuevo usuario    |
|   PUT  | `/usuarios/{id}` | Actualiza un usuario     |
| DELETE | `/usuarios/{id}` | Elimina un usuario       |

Alimentos 

| Método | Ruta              | Descripción               |
| :----: | :---------------- | :------------------------ |
|   GET  | `/alimentos`      | Lista todos los alimentos |
|  POST  | `/alimentos`      | Crea un nuevo alimento    |
|   PUT  | `/alimentos/{id}` | Actualiza un alimento     |
| DELETE | `/alimentos/{id}` | Elimina un alimento       |

Hijos 

| Método | Ruta          | Descripción           |
| :----: | :------------ | :-------------------- |
|   GET  | `/hijos`      | Lista todos los hijos |
|  POST  | `/hijos`      | Crea un nuevo hijo    |
|   PUT  | `/hijos/{id}` | Actualiza un hijo     |
| DELETE | `/hijos/{id}` | Elimina un hijo       |

Loncheras

| Método | Ruta              | Descripción               |
| :----: | :---------------- | :------------------------ |
|   GET  | `/loncheras`      | Lista todas las loncheras |
|  POST  | `/loncheras`      | Crea una nueva lonchera   |
|   PUT  | `/loncheras/{id}` | Actualiza una lonchera    |
| DELETE | `/loncheras/{id}` | Elimina una lonchera      |

✅ Estado del taller 

 funciona con endpoints CRUD y documentación activa en Swagger UI.
Desarrollado como práctica de Producción de Software para reforzar conceptos de APIs con FastAPI y Pydantic
