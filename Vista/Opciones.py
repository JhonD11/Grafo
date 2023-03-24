

class Menus:

    def menuPrincipal():
        print(" ")
        print("****************************************************************")
        print("****************************  MENU  ****************************")
        print(" 1. Inicio del programa  ***************************************")
        print(" 2. Consultar rutas      ***************************************")
        print(" 3. Salir del programa   ***************************************")
        print("****************************************************************")
        print(" ")

    def menuConsultarRuta():
        print(" ")
        print("****************************************************************")
        print("****************************  MENU  ****************************")
        print(" 1. Mostrar todos los registros guardados         **************")
        print(" 2. Mostrar un registro por Id                    **************")
        print(" 3. Mostrar un registro por nombre de usuario     **************")
        print(" 4. Volver al menu principal                      **************")
        print("****************************************************************")
        print(" ")

    def menuGrafo(nodoInicial, nodoFinal, graph, cantidadNodos, cantidadRutas, rutaLarga, rutaCorta):
        print(" ")
        print("****************************************************************")
        print("************************  INFORMACION  *************************")
        print(f" - Nodo inicial:                 {nodoInicial}            ")
        print(f" - Nodo final:                   {nodoFinal}              ")
        print(f" - Rutas:                        {graph}                  ")
        print(f" - Cantidad de nodos:            {cantidadNodos}          ")
        print(f" - Cantidad de rutas:            {cantidadRutas}          ")
        print(f" - La ruta con más recorrido:    {rutaLarga}              ")
        print(f" - La ruta con menos recorrido:  {rutaCorta}              ")
        print("****************************************************************")
        print("*************************** OPCIONES ***************************")
        print(" 1. Agregar un nodo                     ************************")
        print(" 2. Eliminar un nodo                    ************************")
        print(" 3. Realizar otro recorrido             ************************")
        print(" 4. Ir al menu principal y GUARDAR      ************************")
        print(" 5. Ir al menu principal y NO GUARDAR   ************************")
        print(" 6. Cerrar aplicacion                   ************************")
        print("****************************************************************")



    pass