
# ** Programa de grafos **

## El programa esta diseñado para crear un grafo y analizarlos, asi como las rutas mas largas o cortas que este disponibles.


## 1. Identificacion basica
### Inicio del programa
### Al momento de ingresar se va a requerir que los usuarios se identifiquen para facilitar el historial del usuario.
### En caso de no ingresar un nombre de usuario, le se asignara como nombre de usuario "Anonimo".

## 2.Menú Principal
### 2.1El programa  con un ciclo infinito que muestra el siguiente menú de operaciones 
###    2.1 - Inicio del programa (inicia el programa preguntando por las rutas)
###    2.2- Consulta de rutas
###    2.3- Mostrar todos los registros del JSON (muestra todos los registros del JSON)
###    2.4- Mostrar un registro por Id o nombre de usuario (busca el registro por Id)
###    2.5- Salir del programa (Finaliza el programa)
###    Colocar cada uno de los puntos solicitados en la presentación con su código y captura de pantalla con los resultados

## 3.Inicio del programa
### 3.1 Proceso de creacion del grafo.
### 3.2 Al finalizar el grafo, se le mostrara la siguien te informacion:
###       3.2.1 Nodo final
###       3.2.2 Rutas
###       3.2.3 Cantidad de nodos
###       3.2.4 Cantidad de rutas
###       3.2.5 La ruta con más recorrido
###       3.2.6 La ruta con menos recorrido
### 3.3 El grafo podra ser modificado sin problemas y los datos mostrados vuelto a calcular.

## 4. Consulta de rutas
### 4.1 Se puede verificar todos los grafos guardados de la siguiente forma:
###       4.1.1 Ver todo los datos guardados (Sin filtos)
###       4.1.2 ver un grafos espesifico por ID
###       4.1.3 ver todos los grafos de un usuario espesifico 

## 5. El programa cuenta con las siguientes validaciones basicas:
###    5.1- Validación de campos vacíos: Se debe verificar que, al momento de digitar cualquier dato, este no debe contener algún elemento diferente al espacio. En caso contrario, debe preguntar hasta que ingrese un dato correcto.
###    5.2- Validación de números: Se debe validar que, al momento de digitar un número, sea solo número ya que, al digitar un carácter diferente debe indicar un mensaje y preguntar nuevamente.
###    5.3- Validación de palabras: Al momento de preguntar por caminos a crear, las opciones deben ser si y no en todas sus combinaciones (mayúsculas, minúsculas, tildes) o aplicar alguna técnica para mejorar este proceso (no se puede digitar 1 para si y 2 para no).
###    5.4- Mensajes más detallados: Los mensajes a mostrar deben ser muy detallado aplicando estética, concatenación, ortografía. Lo ideal es que los mensajes sean los más claro posible.
###    5.5- Eliminar un elemento del nodo: Se debe tener la opción en alguna parte del programa que permita eliminar un elemento del nodo en la parte de la creación de rutas.
###    Colocar cada uno de los puntos solicitados en la presentación con su código y captura de pantalla con los resultados


## 6. Datos almacenados
### los datos se almacenan en formato JSON.
### 6.1 La estructura del formato JSON es la Siguiente:
###     6.1.1 ID
###     6.1.2 Usuario
###     6.1.3 Cantidad_nodos
###     6.1.4 Rutas
###     6.1.5 Numero_de_rutas
###     6.1.6 Rutas_mas_larga
###     6.1.7 Rutas_mas_corta

## El programa es creado con un fin educativo.
