<<<<<<< HEAD
🚀 NutriBox API – Taller Práctico con FastAPI: Este documento es una guía rápida para configurar y explorar la API RESTful del proyecto NutriBox, desarrollada como taller de Producción de Software.
AutorJesús Manuel Vilardi González Estudiante de Ingeniería de Sistemas
Universidad Católica de Colombia💡 
este  Taller Implementa y gestionar una API RESTful con FastAPI para manejar la información central de la aplicación NutriBox, incluyendo usuarios, hijos, catálogo de alimentos y gestión de loncheras.
💻 Tecnologías Utilizadas:
Python 🐍: 3.11 o superior
FastAPI 🚀
Uvicorn (Servidor ASGI)
Pydantic (Validación de datos)
Swagger UI (Documentación interactiva)

⚙️ Instalación y Configuración
1. Clonar el RepositorioBashgit clone https://github.com/10jechu/guiaproduccion-.git
cd guiaproduccion-
2. Crear y Activar el Entorno VirtualBashpython -m venv .venv
source .venv/Scripts/activate
3. Instalar Dependencias Bash
4. pip install fastapi "uvicorn[standard]" pydantic[email]
5. Ejecución del Servidor
6. Ejecutar el siguiente comando para iniciar el servidor en modo desarrollo:Bash
7. uvicorn app.main:app --reload
9. 📁 Estructura del Proyectoguiaproduccion-/
│
├── app/
│   ├── main.py                     # Configuración y arranque de la aplicación
│   ├── models/                     # Esquemas de modelos de datos (ej. SQL)
│   │   ├── usuario.py
│   │   ├── hijo.py
│   │   ├── alimento.py
│   │   └── lonchera.py
│   └── routes/                     # Definición de todos los endpoints de la API
│       ├── usuario_routes.py
│       ├── hijo_routes.py
│       ├── alimento_routes.py
│       └── lonchera_routes.py
│
├── .venv/
├── requirements.txt
└── README.md
🗺️ Endpoints Disponibles (CRUD Básico)ModeloMétodoRutaDescripciónUsuariosGET/usuariosLista todos los usuariosPOST/usuariosCrea un nuevo usuarioPUT/usuarios/{id}Actualiza un usuarioDELETE/usuarios/{id}Elimina un usuarioAlimentosGET/alimentosLista todos los alimentosPOST/alimentosCrea un nuevo alimentoPUT/alimentos/{id}Actualiza un alimentoDELETE/alimentos/{id}Elimina un alimentoHijosGET/hijosLista todos los hijosPOST/hijosCrea un nuevo hijoPUT/hijos/{id}Actualiza el hijoDELETE/hijos/{id}Elimina un hijoLoncherasGET/loncherasLista todas las loncherasPOST/loncherasCrea una nueva loncheraPUT/loncheras/{id}Actualiza una loncheraDELETE/loncheras/{id}Elimina una lonchera
=======
# NutriBox API – Proyecto FastAPI

Este proyecto implementa una API RESTful con FastAPI para gestionar información de usuarios, hijos, alimentos y loncheras dentro de la aplicación NutriBox.

---

## Tecnologías utilizadas

- Python 3.11 o superior  
- FastAPI  
- Uvicorn (servidor ASGI)  
- Pydantic (validación de datos)  
- Swagger UI (documentación interactiva)

---

## Instalación y configuración

1. Clonar el repositorio:

```bash
git clone https://github.com/10jechu/guiaproduccion-.git
cd guiaproduccion-

>>>>>>> 810d988 (Agrega README final de la guia con  NutriBox)
