# MANEJO DE LOGGING
import logging as log

# handler  = Manejador. Es un recurso donde vamos a mandar esta informacion, sirve para registrar mensajes sobre la ejecuacion del programa (debug, info, warning, error, critical), ayudan a depurar, monitorear errores o eventos en archivos o consla
log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                        log.FileHandler('capadatos.log'), # Agrega informacion a un archivo .log
                        log.StreamHandler() # Agrega informacion la consola
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning') # apartir de aquí, aparecen por defecto
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critico')
