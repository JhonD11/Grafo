
class Informar:

    def volverAlMenuprincipal():
        print('')
        print("*****************************************************************")
        print("***  PRESIONES CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL  ***")
        print("*****************************************************************")
        input()


    def opcionInvalida():
        print('')
        print("*****************************************************************")
        print("***********************  OPCION INVALIDA  ***********************")
        print("*  PRESIONES CUALQUIER TECLA PARA VOLVER AL MENU Y REINTENTAR   *")
        print("*****************************************************************")
            

    def noHayRegistros():
        print('')
        print("*****************************************************************")
        print("                        NO HAY REGISTROS                         ")
        print("*****************************************************************")

    def noHayRegistroID(buscarID):
        print('')
        print("*****************************************************************")
        print(f"          NO HAY REGISTROS ASOCIADOS AL ID {buscarID}           ")
        print("*****************************************************************")
        print('')

    def noHayRegistroUsuario(buscarUsuario):
        print('')
        print("*****************************************************************")
        print(f"          NO HAY REGISTROS ASOCIADOS AL UDUARIO {buscarUsuario}           ")
        print("*****************************************************************")
        print('')

    def despedida():
        print(" ")
        print("****************************************************************")
        print("****************************************************************")
        print("********************** HASTA LA PROXIMA ************************")
        print("****************************************************************")
        print("*********************************** Att: Equipo de desarrollo***")
        print("****************************************************************")
        print(" ")
    
    pass

class SolicitarInformacion:

    def ingreseNumerodeID():
        print("****************************************************************")
        print("**************** BUSQUEDA DE REGISTROS POR ID ******************")
        print("********** Ingrese el numero de ID que esta buscando ***********")
        print("****************************************************************")
        print("")

    def IngreseNombreUsaurio():
        print("****************************************************************")
        print("********* BUSQUEDA DE REGISTROS POR NOMBRE DE USAURIO **********")
        print("    IMPORTANTE: se tiene en cuenta las mausculas y minusculas   ")
        print("****************************************************************")
        print("")

    def IngreseNombreDelUsuario():
        print("****************************************************************")
        print("************************ IDENTIFICACION ************************")
        print("****************** Ingrese su nombre de usuario ****************")
        print("***** En caso de querer estar como anonimo presione ENTRE ******")
        print("****************************************************************")
        print("")

    pass