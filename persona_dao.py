# DAO: Data Access Object
# Es un patron de Disenio para comunicarse con una base de datos

# En esta clase tiene la responsabilidad de realizar las operaciones CRUD (Create, Read, Update, Delete)
# DAO tiene las operaciones de un CRUD

from conexion import Conexion
from persona import Persona
from logger_base import log
from cursor_del_pool import CursorDelPool

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create, Read, Update, Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        #cursor = Conexion.obtenerCursor()
        #with Conexion.obtenerConexion() as conexion:
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall() # Corrección del error tipográfico
            personas=[]
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
        
    @classmethod
    def insertar(cls, persona):
        #with Conexion.obtenerConexion() as conexion:
            #with conexion.cursor() as cursor: 
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada {persona}')
            return cursor.rowcount
            
    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Persona eliminada {persona}')
            return cursor.rowcount

if __name__ == '__main__':


    # Insertar Personas
    persona1 = Persona(nombre='Juancho', apellido='Nagera', email='pnagera@gmail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')
    
    # Actualizar un registro
    persona1 = Persona(id_persona=1, nombre='Pablo', apellido= 'Escobar', email='jescobar@gmail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas {personas_actualizadas}')

    # Eliminar un registro
    persona1 = Persona(id_persona=18)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas {personas_eliminadas}')

    # Seleccionar personas
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)






