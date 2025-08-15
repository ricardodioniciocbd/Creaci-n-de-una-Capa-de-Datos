import logging
from conexion import Conexion

log = logging.getLogger(__name__)

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor() # obtenemos el cursor de la conexion
        return self._cursor

    def __exit__(self, tipo_exepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta metodo exit __exit__')
        if valor_excepcion: # si el valor de la exception es diferente a Nulo..
            self._conexion.rollback() # Si la ejecucion de la setencia, salio mal, hacemos un rollback
            log.error(f'Ocurrio una excepcion, se hace rollback {valor_excepcion}, {tipo_exepcion}, {detalle_excepcion}')
        else:
            self._conexion.commit() # si la ejecucion de la sentencia salio bien, hacemos un commit y se guarda en la base de datos 
            log.debug(f'Commit de la transaccion ')
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall()) # recuperamos todos los registros de tipo persona     