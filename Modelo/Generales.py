import os

class General:

    def limpiarConsola():
        ''' 
        LIMPIA LA CONSOLA.

        Con el objetivo eliminar todos los datos anteriores de la consola 
        y facilitar la lectura del usuario.
        '''
        ## En caso contrario sera Windows.
        if os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system("cls")
        ## Para otros sistemas (MAC, Linux o similar).
        else:
            os.system("clear")
            pass

    pass