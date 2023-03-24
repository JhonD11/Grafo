

class Validacion:

    def validarCasillaVacia(variable):
        '''
        VALIDA SI LA VARIABLE ESTA VACIA.

        Arg:        variable    Varible que se desea comprobar si esta vacia.

        Retorna:    True        Si la varible esta vacia o tiene un solo espacio.
                    False       Si la varible NO esta vacia.
        '''
        if variable=="" or variable==" ":
            print("No se a digitado ningun valor, vuelva a intentarlo:")
            return True
        else:
            return False

    def validarNumero(variable):
        '''
        VALIDA SI EL VALOR DE LA VARIABLE ES UN NUMERO.

        Arg:        variable    Varible que se desea comprobar si es un numero.

        Retorna:    True        Si la variable es un numero.
                    False       Si la variable NO es un numero.
        '''
        if variable.isdigit():
            return True
        else:
            print("Solo se permiten valores numericos, por favor vuelva a intentarlo:")
            return False
            
    def validarPalabras(variable):
        '''
        CONVIERTE EL VALOR DE LA VARIABLE RECIBIDA EN MAYUSCULA Y REMUEVE LOS ACENTOS.

        Arg:        variable    Varible que se desea convertir a mayuscula y eliminar acentos.

        Retorna:    La variable recibida pero en mayuscula y sin acentos.
        '''
        reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        )
        for a, b in reemplazos:
            variable = variable.replace(a, b)
        return variable.upper()

