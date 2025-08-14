from logger_base import log
import psycopg2 as bd
import sys # tiene una funcion para terminar por completo nuestro programa


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
 
    # Metodos de clase de optener cursor y conexion
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
