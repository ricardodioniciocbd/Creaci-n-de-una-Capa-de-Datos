# Capa de Datos - Sistema de Gestión de Personas y Usuarios

Sistema de capa de datos desarrollado en Python para gestión de personas y usuarios con conexión a PostgreSQL.

## Características

- **Gestión de Personas**: CRUD completo para entidad Persona
- **Gestión de Usuarios**: CRUD completo para entidad Usuario  
- **Pool de Conexiones**: Manejo eficiente de conexiones a PostgreSQL
- **Logging**: Sistema de logs configurado
- **Patrón DAO**: Implementación del patrón Data Access Object

## Estructura del Proyecto

```
├── Assets/                 # Recursos (diagramas, imágenes)
├── conexion.py            # Configuración de conexión a BD
├── cursor_del_pool.py     # Manejo del pool de conexiones
├── logger_base.py         # Configuración de logging
├── persona.py             # Modelo de datos Persona
├── persona_dao.py         # DAO para Persona
├── usuario.py             # Modelo de datos Usuario
├── usuario_dao.py         # DAO para Usuario
└── menu_app_usuario.py    # Aplicación de menú principal
```

## Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd capa_datos_persona
```

2. Crea un entorno virtual:
```bash
python -m venv venv
```

3. Activa el entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Configuración

1. Configura tu base de datos PostgreSQL
2. Actualiza los parámetros de conexión en `conexion.py`

## Uso

Ejecuta la aplicación principal:
```bash
python menu_app_usuario.py
```

## Dependencias

- **psycopg2-binary**: Adaptador PostgreSQL para Python

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request
