
# Manejo de un POOL DE CONEXIONES 

from logger_base import log
from psycopg2 import pool
import sys # tiene una funcion para terminar por completo nuestro programa


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None  # Variable de clase para almacenar el pool de conexiones

    
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD, 
                                                      port = cls._DB_PORT, 
                                                      database = cls._DATABASE)
                log.debug(f'Creacion del pool exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._pool


    # Obtener una conexión de Pool de Conexiones 
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool {conexion}')
        return conexion
    
    # Liberar la conexion al pool, cuando ya no estamos ocupando la conexion 
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion) #  put - poner o colocar. PUTCONN: Para regresar el objetoconexion que no estamos utilizando al PUL de conexiones
        log.debug(f'liberamos la conexion al pool')

    # Metodo para Cerrar el objeto el pul de conexiones 
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

 
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()






'''
from logger_base import log
import psycopg2 as bd
import sys # tiene una funcion para terminar por completo nuestro programa


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None  # Variable de clase para almacenar la conexion

    
   
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE
                                           )
                log.debug(f'Conexion exitosa: {cls._conexion}')
            except Exception as e:
                log.error(f'Ocurrio un error al obtener la conexion {e}')
                sys.exit()
        return cls._conexion
 
    # Metodo para obtener un cursor
    @classmethod
    def obtenerCursor(cls):
        try:
            cursor = cls.obtenerConexion().cursor()
            log.debug(f'Se abrio correctamente el cursor: {cursor}')
            return cursor
        except Exception as e:
            log.error(f'Ocurrio un error al obtener el cursor {e}')
            sys.exit()
 
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()


'''
