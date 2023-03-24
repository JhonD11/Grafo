
import time
import json
from Vista.Opciones import Menus
from Vista.MSJinformativo import Informar
from Vista.MSJinformativo import SolicitarInformacion
from Modelo.Validaciones import Validacion
from Modelo.Generales import General

class __main__:

    usuario=str()
    graph = dict()
    cantidadNodos = int(0)
    nodo_conexiones = list()
    valor = str("")
    rpta = str("")
    nodoInicial = int(0)
    nodoFinal = int(0)
    cantidadNodos = int(0)
    rutas = list(())
    cantidadRutas = int(0)
    rutaLarga = int(0)
    rutaCorta = int(0)
    contador = int(0)
    

    def __init__(self):
        self.registroNombre()
        self.menuPrincipal()

    
    
    def agregarNodo(self, n):
        '''
        AGREGAR NODO.

        Esta funcion agrega un nodo al grafo uno por uno.
        '''
        print("******* Digite el nombre del nodo '"+str(n)+str("' *******"))
        # En este ciclo slicitamos el dato requerido y nos aseguramos de informar si es correcto.
        while (True):
            valor=input()
            if(Validacion.validarCasillaVacia(valor)):
                continue
            else:
                break
        
        # Agregamos todos los caminos del nodo creado.
        self.agregarCamino()
        
        # Actualizamos el grafo y se o mostramos al usuario.
        self.graph.update({valor: set(self.nodo_conexiones)})
        self.nodo_conexiones.clear()
        print(self.graph)

    def agregarCamino(self):
        '''
        AGREGAR LOS CAMINOS DE UN NODO.

        Este es un ciclo para agregar todos los caminos del nodo que se necesite.
        '''
        print("Desea agregar nodo de caminos, escriba SI o NO   ")
        # En este ciclo slicitamos el dato requerido y nos aseguramos de informar si es correcto.
        while (True):
            self.rpta=input()
            if(Validacion.validarCasillaVacia(self.rpta)):
                continue
            else:
                self.rpta=Validacion.validarPalabras(self.rpta)
                if(self.rpta=="SI" or self.rpta=="NO" ):
                    break
                else:
                    print("OPCION ERRONEA, las Opciones permitidas son SI o NO, vuelva a seleccionar una opcion: ")
                continue
        if(self.rpta=="SI"):
            print(("Digite el nombre del nodo camino:   "))
            while (True):
                nodo_unir=input()
                if(Validacion.validarCasillaVacia(nodo_unir)):
                    continue
                else:
                    break
            self.nodo_conexiones.append(nodo_unir)
            print(self.nodo_conexiones)
            ## Volvemos a repetir el proceso para agregar mas caminos.
            self.agregarCamino()
        elif(self.rpta=="NO"):
            print("No agrega nodos camino")
            print("")
        else:
            print("OPCION INCORRECTA")

    def eliminarNodo(self):
        '''
        ELIMINAR NODO DEL GRAFO.

        Consulta y verifica el nodo que se desea eliminar, asi como realiza la eminacion de este.
        '''
        print("Digite el nodo a eliminar: ")
        eliminarNodo=""
        while (True):
            eliminarNodo=input()
            if (eliminarNodo in self.graph):
                break
            else:
                print("No nodo ingresado no existe, Vuelvalo a intentar:")
                continue
        try:
            del self.graph[eliminarNodo]
            print(f"El nodo '{eliminarNodo}' fue correctamente eliminado.")
        except:
            print(f"Error al eliminar el nodo {eliminarNodo}, EL NODO NO PUDE SER ELIMINADO.")
        
        Informar.volverAlMenuprincipal()

    def llenar(self):
        '''
        LLENAR GRAFO.

        Inicia el proceso de agregar un grupo de nodos.
        '''
        ## Limpiar consola.
        General.limpiarConsola()

        #para depdir solo numeros
        print("Digite la cantidad de nodos  ")

        # En este ciclo slicitamos el dato requerido y nos aseguramos de informar si es correcto.
        while True:
            self.cantidadNodos=input()
            if(Validacion.validarCasillaVacia(self.cantidadNodos)):
                continue
            elif Validacion.validarNumero(self.cantidadNodos):
                break
            else:
                continue
        
        # Ciclo ara agregar la cantidad de nodos que requiere el usuario.
        for i in range(int(self.cantidadNodos)):
            self.agregarNodo(i)

    def consultarRecorridoGrafo(self):
        '''
        CONSULTA LOS EL NODO INICIAL Y FINAL DEL RECORRIDO.

        Consulta el nodo desde el cual deseamos iniciar nuestro recorrido, asi como el nodo donde finalizara.
        '''
        print("Digite el nodo inicial del recorrido    ")
        while True:
            temp=input()
            # Comprobaciones (Verificar si la casilla esta en blanco y si el nodo existe).
            if(Validacion.validarCasillaVacia(self.nodoInicial)):
                continue
            elif(temp in self.graph):
                    # Comprobaciones correctas, almacenamos el valor en la variable correspondiente y cerramos ciclo.
                    self.nodoInicial=temp
                    break
            else:
                print("No nodo ingresado no existe, Vuelvalo a intentar:")
                continue
            
        print("Digite el nodo final del recorrido    ")
        while True:
            temp=input()
            # Comprobaciones (Verificar si la casilla esta en blanco y si el nodo existe).
            if(Validacion.validarCasillaVacia(self.nodoFinal)):
                continue
            elif(temp in self.graph):
                    # Comprobaciones correctas, almacenamos el valor en la variable correspondiente y cerramos ciclo.
                    self.nodoFinal=temp
                    break
            else:
                print("No nodo ingresado no existe, Vuelvalo a intentar:")
                continue
        
        
    def analisis_Y_Calculos(self):
        '''
        ANALISIS Y CALCULO DEL GRAFO.

        Calculo de toda la informacion que se mostrara al usuario.
        '''
        ## En caso de que el nodo final sea igual al iniciar, la aplicacion no se cerrara, solo las rutas daran 0.
        if(self.nodoInicial==self.nodoFinal):
            self.rutas = list(())
        else:
            self.rutas = list(self.dfs_paths(self.nodoInicial, self.nodoFinal))

        # Calculo de informacion.
        self.cantidadNodos = len(self.graph)
        self.cantidadRutas = len(self.rutas)
        if len(self.rutas) > 0:
            self.rutaLarga = max(self.rutas, key=len)
            self.rutaCorta = min(self.rutas, key=len)
        else:
            self.rutaLarga = 0
            self.rutaCorta = 0
        self.cantidadRutas = len(self.rutas)

    def guardarGrafo(self):
        '''
        GUARDA INFORMACION DEL GRAFO EN UN JSON.

        Para facilitar la busqueda del historal, de almacenara los datos en un archivo externo
        Ubicado en la misma carperta de este archivo .py
        '''

        # Contador del ID.
        self.contador = 1 

        # Creacion de JSON
        data = {}
        data['Grafos'] = []
        
        # Crear archivo en caso de no estar creado.
        try:
            # Verficar ID si el archivo esta creado.
            try:
                # Si el archivo esta creado, tomara el ultimo ID.
                with open('Registro de Grafos.json') as file:
                    data = json.load(file)

                for Grafo in data['Grafos']:
                    self.contador = Grafo['Id']
                # Verificamos que el contador sea un numero, en caso contrario se reinicia.
                if not self.contador.isdigit():
                    self.contador = 1 

            except:
                pass
        # Si el archivo no esta creado, de crea.
        except:
            open('Registro de Grafos.json', "w")
        
        # Agregar el grafo al archivo JSON.
        data['Grafos'].append({
            "Id": self.contador+1,
            "Usuario": self.usuario,
            "Cantidad_nodos": self.cantidadNodos,
            "Recorrido": f"{self.nodoInicial} => {self.nodoFinal}",
            "Rutas": self.rutas,
            "Numero_de_rutas": self.cantidadRutas,
            "Rutas_mas_larga": self.rutaLarga,
            "Rutas_mas_corta": self.rutaCorta
            })
        
        with open('Registro de Grafos.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        # Cerrar el archivo.
        file.close()

    def limpiarDatos(self):
        '''
        LIMPIAR VARIABLES.

        Restaura todos los atributos.
        '''
        self.graph = dict()
        self.cantidadNodos = int(0)
        self.nodo_conexiones = list()
        self.valor = str("")
        self.rpta = str("")
        self.nodoInicial = int(0)
        self.nodoFinal = int(0)
        self.cantidadNodos = int(0)
        self.rutas = list(())
        self.cantidadRutas = int(0)
        self.rutaLarga = int(0)
        self.rutaCorta = int(0)

    def mostrarInformacionOpcionesGrafo(self):
        '''
        MUESTRA AL USUARIO TODA LA INFORMACION DEL GRAFO Y LAS OPCIONES LAS MODIFICACIONES DISPONIBLE.
        '''
        General.limpiarConsola()
        Menus.menuGrafo(self.nodoInicial, self.nodoFinal, self.graph, self.cantidadNodos, self.cantidadRutas, self.rutaLarga, self.rutaCorta)
        
        print("Seleccione una opcion: ")
        while True:
            temp=input()
            if(Validacion.validarCasillaVacia(temp)):
                continue
            elif Validacion.validarNumero(temp):
                m2Opcion=temp
                break
            else:
                continue

        # Ejecucion de la opcion seleccionada.
        if (int(m2Opcion)==1):
            self.agregarNodo(self.cantidadNodos+1)
            self.analisis_Y_Calculos()
            self.mostrarInformacionOpcionesGrafo()
        elif (int(m2Opcion)==2):
            self.eliminarNodo()
            self.analisis_Y_Calculos()
            self.mostrarInformacionOpcionesGrafo()
        elif (int(m2Opcion)==3):
            self.consultarRecorridoGrafo()
            self.analisis_Y_Calculos()
            self.mostrarInformacionOpcionesGrafo()
        elif (int(m2Opcion)==4):
            self.guardarGrafo()
            self.limpiarDatos()
            self.menuPrincipal()
        elif (int(m2Opcion)==5):
            self.limpiarDatos()
            self.menuPrincipal()
        elif (int(m2Opcion)==6):
            self.menuOpcion_3()
        else:
            Informar.opcionInvalida()
            self.mostrarInformacionOpcionesGrafo()

        

    # Return all graphs from start to goal
    def dfs_paths(self, start, goal):
        # Define stack variable
        stack = [[start]]
        # Do the process while there are paths to follow
        while stack:
            path = stack.pop()
            node = path[-1]
            # En caso de fallo cerramos el ciclo.
            try:
                for next in self.graph[node] - set(path):
                    print(self.graph[node])
                    # If a correct path is founded, then return the path with the generator
                    # else write a new path and follow iterating.
                    if next == goal:
                        yield path + [next]
                    else:
                        stack.append(path + [next])
            except:
                break
    
    def menuOpcion_1(self):
        '''
        OPCION 1 DEL MENU PRINCIPAL.
        
        Creacion del grafo, recorrido y analisis de este.
        '''
        ## Llenar grafo
        self.llenar()

        ## Consulta requerida para recorrido.
        self.consultarRecorridoGrafo()

        ## Analisis y calculos.
        self.analisis_Y_Calculos()
        
        self.mostrarInformacionOpcionesGrafo()
        

    def menuOpcion_2(self):
        '''
        OPCION 2 DEL MENU PRINCIPAL.
        '''
        General.limpiarConsola()
        Menus.menuConsultarRuta()
        m3Opcion=input("Seleccione una opcion: ")

        if (m3Opcion=="1"):

            try:
                with open('Registro de Grafos.json') as file:
                    data = json.load(file)

                for Grafo in data['Grafos']:
                    print('')
                    print('Id:', Grafo['Id'])
                    print('Usuario:', Grafo['Usuario'])
                    print('Cantidad_nodos:', Grafo['Cantidad_nodos'])
                    print('Recorrido:', Grafo['Recorrido'])
                    print('Rutas:', Grafo['Rutas'])
                    print('Numero_de_rutas:', Grafo['Numero_de_rutas'])
                    print('Rutas_mas_larga:', Grafo['Rutas_mas_larga'])
                    print('Rutas_mas_corta:', Grafo['Rutas_mas_corta'])
                    print('')
            except:
                Informar.noHayRegistros()
                pass

            Informar.volverAlMenuprincipal()
            
            self.menuPrincipal()

                
        elif (m3Opcion=="2"):

            SolicitarInformacion.ingreseNumerodeID()

            buscarID = input ("ID: ")

            try:

                with open('Registro de Grafos.json') as file:
                    data = json.load(file)

                for Grafo in data['Grafos']:
                    if(int(buscarID)==int(Grafo['Id'])):
                        print(" ")
                        print("****************************************************************")
                        print('Id:', Grafo['Id'])
                        print('Usuario:', Grafo['Usuario'])
                        print('Cantidad_nodos:', Grafo['Cantidad_nodos'])
                        print('Recorrido:', Grafo['Recorrido'])
                        print('Rutas:', Grafo['Rutas'])
                        print('Numero_de_rutas:', Grafo['Numero_de_rutas'])
                        print('Rutas_mas_larga:', Grafo['Rutas_mas_larga'])
                        print('Rutas_mas_corta:', Grafo['Rutas_mas_corta'])
                        print("****************************************************************")
                    else:
                        pass
            except:
                Informar.noHayRegistroID(buscarID)

            Informar.volverAlMenuprincipal()

            self.menuPrincipal()


        elif (m3Opcion=="3"):

            SolicitarInformacion.IngreseNombreUsaurio()
            buscarUsuario = input ("NOMBRE DE USUARIO: ")

            try:

                with open('Registro de Grafos.json') as file:
                    data = json.load(file)

                for Grafo in data['Grafos']:
                    if buscarUsuario == Grafo['Usuario']:
                        print(" ")
                        print("****************************************************************")
                        print('Id:', Grafo['Id'])
                        print('Usuario:', Grafo['Usuario'])
                        print('Cantidad_nodos:', Grafo['Cantidad_nodos'])
                        print('Recorrido:', Grafo['Recorrido'])
                        print('Rutas:', Grafo['Rutas'])
                        print('Numero_de_rutas:', Grafo['Numero_de_rutas'])
                        print('Rutas_mas_larga:', Grafo['Rutas_mas_larga'])
                        print('Rutas_mas_corta:', Grafo['Rutas_mas_corta'])
                        print("****************************************************************")
                    else:
                        pass
            except:

                Informar.noHayRegistroUsuario(buscarUsuario)

            Informar.volverAlMenuprincipal()

            self.menuPrincipal()

        elif (m3Opcion=="4"):
            self.menuPrincipal()

        else:
            Informar.opcionInvalida()
            input()
            self.menuOpcion_2()

    def menuOpcion_3(self):
        '''
        OPCION 3 DEL MENU PRINCIPAL.

        Finaliza la aplicacion.
        '''
        General.limpiarConsola()
        Informar.despedida()

        time.sleep(5)
        exit()

    def menuPrincipal(self):
        ''' 
        MENU PRINCIPAL.

        Menu principal de la aplicacion y el primero al que se ingresa cuando se abre el programa.
        '''
        while (True):
            General.limpiarConsola()
            Menus.menuPrincipal()
            opcion=input("Seleccione una opcion: ")
            
            if(Validacion.validarCasillaVacia(opcion)):
                continue
            elif(not Validacion.validarNumero(opcion)):
                continue

            elif(opcion=="1"):
                self.menuOpcion_1()
                break
            elif(opcion=="2"):
                self.menuOpcion_2()
                break
            elif(opcion=="3"):
                self.menuOpcion_3()
                break
            else:
                Informar.volverAlMenuprincipal()
                pass
            time.sleep(3)
            continue

    def registroNombre(self):
        General.limpiarConsola()
        SolicitarInformacion.IngreseNombreDelUsuario()
        usuario = input ("Ingrese su nombre: ")

        if(usuario==""):
            usuario="Anonimo"
        else:
            self.usuario=usuario
                
                
# Ejecutamos la aplicacion.
__main__()
