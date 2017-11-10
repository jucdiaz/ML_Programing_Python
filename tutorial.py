# -*- coding: utf-8 -*-
"""
Created on Tue May 16 07:59:08 2017

@author: jucadiaz
"""

# este es el primer comentario

spam = 1
text = "#Este no es un mentario"

################################################################################
###################### python como calculadora##################################
################################################################################

2 + 2

50 - 5*6

(50 - 5*6)/4

8/5 # siempre retonrna un numero punto flotante

17/3

17//3  # deja solo la parte entera de un numero

17%3  # devuelve el modulo de la division

2 ** 4

ancho = 20
largo = 5*9
ancho*largo

impuesto=12.5/100
precio=100.5
precio*impuesto
precio+ _
round(_,2) # el simbolo _ sirve como el ans de las calculadoras (ultimo valor obtenido)


################################################################################
###################### Cadenas de caracteres##################################
################################################################################

'huevos y pan'
'doesn\'t' # con \ puedo meter comillas en los comentarios cuando son comillas simples
"doesn't" # si utilizo comillas dobles puedos utilizar dentro de ellas comillas simples
'"Si," le dijo.' # si utilizo comillas simples dentro puedo utilizar dobles
"\"Si,\" le dijo." # en comillas dobles puedo  utilizar comillas dobles dentro con el \ antes

# todo lo que se ponga despues \ se interpreta como caracter especial, si no queremos
# que sea asi anteponer al r

'C:\algun\nombre'
r'C:\algun\nombre'

print("""\
Uso: algo [OPTIONS]
-h Muestra el mensaje de uso
-H nombrehost Nombre del host al cual conectarse
""") # con triple comilla puedo hacer cambio de linea


3 * 'un' +'ium' # con el simbolo + concateno pero * es como un rep en r pero para
# una cadena de carateres

'Py' 'thon' # una linea de comentarios entre comillas y otra separa das por un 
#espacio son contenadas

prefix = 'Py'
#prefix 'thon' #no se puede concatenar con espacio debe serr con +

prefix + 'thon'

texto = ('Poné muchas cadenas dentro de paréntesis '
'para que ellas sean unidas juntas.')
texto

palabra='Python'
palabra[0] # devuelde el caracter en la posicion 0
palabra[3]

palabra[-1] # devuelve la posicion del caracter pero de derecha a izquierda
palabra[-2]
palabra[-6]

palabra[0:2] # caracteres desde la posición 0 (incluída) hasta la 2 (excluída)

palabra[:2] + palabra[2:] # el valor por defecto para :2 es cero y para 2: el
# dato faltante es la longitud de la cadena

palabra[-2:] # desde el final hasta 2 por la derecha pero incluye la 2
palabra[-2] # no incluye la 2

palabra[4:42]

palabra[42:] # con un numero muy grande por fuera de la cadena de caracteres
# funciona si esta con :

palabra[0] = 'J' # las cadenas son inmutables no se pueden reemplazar caracteres por otros, al menos no asi

'J' + palabra[1:] # crea una cadena nueva a partir de otra, como si la hubiera reemplazado

s = 'supercalifrastilisticoespialidoso'
len(s) # devuelve el la cantidad de caracteres


################################################################################
###################### LISTAS##################################################
################################################################################

cuadrados = [1, 4, 9, 16, 25] # esto es una lista, parecido a vector de R
cuadrados

cuadrados[0] # tambien se pueden indexar y rebanar
cuadrados[-1]
cuadrados[-3:] # esta genera una nueva lista a partir de la otra
cuadrados[:]

cuadrados + [36, 49, 64, 81, 100] # tambien se pueden concatenar listas con otras por medio de +
(3*cuadrados) + [36, 49, 64, 81, 100] # repite la primera cadena tres veces y luego la concatena

cubos = [1, 8, 27, 65, 125] 

cubos[3] = 4**3 # las listas si son mutables es decir se puede reemplazar su contenido
cubos

cubos.append(216) # agrega al final de la lista otro valor

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # lista de caracteres
letras

letras[2:5] = ['C', 'D', 'E'] # reemplazo algunos valores
letras

letras[2:5] = [] # borar una parte de la lista
letras

letras[:] = [] # reemplazar la lista por una vacia
letras

letras = ['a', 'b', 'csas', 'd']
len(letras) # me da la cantidad de elementoos dentro de la lista


a = ['a', 'bc', 'c']

n = [1, 2, 3]

x = [a, n] # es posible anidar listas: es decir listas que contengan otras listas
x

len(x) # cantidad de listas que estan dentro de la lista x
len(x[0]) # cantidad de elemento en la primera lista
len(x[1]) # cantidad de elementos contenidos en la segunda lista
len(x[0][1]) # caantidad de caracteres que tiene la cadena en la lista 1 en la posicion 1


################################################################################
###################### Primeros pasos hacia la programación#####################
################################################################################

a, b = 0, 1 # asignacion multiple
while b < 10:
    print(b)
    a, b = b, a+b # debe ir con tab las funciones que van dentro del while
    # se puede asignar valores dentro de una misma linea
# operaciones logicas con usada como < > == <= >= !=
# Nota: al final del bucle dejar una linea en blanco y tratar de utilizar un tab
# para cada bucle
    
i = 256*256
print('El valor de i es', i) # se imprime sin comillas

#####While

a, b = 0, 1
while b < 1000:
    print(b, end=',') # con la funcion end evitamos que la salida tenga el salto de linea
    a, b = b, a+b # y se le agrega un caracter para separar cada salida


x = int(input("Ingresa un entero, por favor: ")) # Permite solicitar un numero al usuario

#####IF
if x < 0:
    x = 0
    print('Negativo cambiado a cero')
elif x==0: # es una abreviacion de la sentencia else if
    print('Cero')
elif x==1:
    print('Simple')
else: # este else final es opcional, la sentencia if elif sustituye al case when de sql
    print('Más')

#### For
palabras = ['gato', 'ventana', 'defenestrado']
for p in palabras: # itera en secuencia segun como aparezca la lista ingresada al for
    print(p, len(p)) # p regresenta el valor en la posicion i de la lista palabras
    # es decir que p=palabras[i] donde i varia de 1 a el tamaño de la lista

len(palabras[1])

# si se va a modificar el la lista dentro del ciclo es recomendable hacer una copia mediante las rebanadas

for p in palabras[:]: # hace una copia por rebanada de toda la lista
    if len(p) > 6:
        palabras.insert(0, p) #inserta la palabra p en la primera posicion de palabras,
        # la primera palabra que se coloca en la primera posicion es ventana luego desplaza todo
        #la lista una pocision para insertar en la primera posicion la segunda palabra con logitud
        #mayor a 6 que es defenestrado
palabras

for i in range(5): # si necesitamos iterar sobre una secuencia de numeros es bueno utilizar la funcion range
    print(i, end=' ') # el valor final del range nunca es incluido es de cir 5 no se incluye


z = range(5, 10) # range es parecido a la funcion seq de R.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n/x)
            break # el break rompe el ciclo al encontrar la primera sentencia verdadera
    else: # este else te permite hacer una accion una vez terminado el primer ciclo, este else es del for
            # sigue el bucle sin encontrar un factor
            print(n, 'es un numero primo')

for num in range(2, 10):
    if num % 2 == 0:
        print("Encontré un número par", num)
        continue # la sentencia continue continua con la iteracion del siguiente ciclo, 
        #sin volver a empezar el ciclo
    print("Encontré un número", num)
    

####DEFINICION DE FUNCIONES
###########################

def fib(n): # escribe la seir fibinacci hasta n, # la palabra def se usa para definir funciones
    """Escribe la serie fibonacci hasta n""" # esta linea se puede dejar como documentacion de la funcion (docstring)
    a, b = 0, 1
    while a<n:
        print(a, end=' ')
        a, b= b, a+b
    print()
    
## llamamos la funcion
    fib(2000)
# Cumple con las mismas especificaciones de definicion de ambientes de variables que R en las funciones.

fib

f=fib # Se pueden heredar funciones mediante el =

fib(0)

def fib2(n): # escribe la seir fibinacci hasta n, # la palabra def se usa para definir funciones
    """Escribe la serie fibonacci hasta n""" # esta linea se puede dejar como documentacion de la funcion (docstring)
    result=[]    # definicion por default en vacio la lista para llenar
    a, b = 0, 1
    while a<n:
        result.append(a) # agrega por debajo, este llama un metodo de los objetos tipos listas
        #un metodo es una funcion que pertenece a una clase de objetos y se convoca como onj.methodname
        #donde obj es algun obj methodname es el nombre del metodo definido a aplicar sobre obj
        a, b= b, a+b
    return result # devuelve un valor el resultado
    
# distintos tipos definen distintos objetos propios
f100=fib2(100)
f100  
type(f100) # nos devuelve la clase de objeto que es


# definicion de funciones con argumentos dados por valores por omision
def pedir_confirmacion(prompt, reintentos=4, recordatorio='Por favor, intente nuevamente!'):
    while True:
        ok = input(prompt) # la funcion input solicita al usuario ingresarun valor
        #con el string prompt definido antes y se le asigna al objeto ok
        if ok in ('s', 'S', 'si', 'Si', 'SI'): # permite saber si una secuencia contien o no uno o varios determinados valores
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise ValueError('respuesta de usuario inválida') # rompe el ciclo e inclye como un posible error el string descrito
        print(recordatorio)


pedir_confirmacion('¿Realmente queres salir?')
pedir_confirmacion('¿Sobreescribir archivo?', 2)
pedir_confirmacion('¿Sobreescribir archivo?', 2, "Vamos, solo si o no")


def f(a, L=[1]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

# el valor de L no se pone de nuevo en vacio si no que utiliza de nuevo el valor en objetos de tipo mutable 
#como la lista diccionario o instaci de la mayoria de las clases

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))

# por el problema anterior para objetos mutables se debe hacer el truco anterior con el none para que tome como valor 
#del objeto que uno quiera que tome siempre por defecto si no se define y que no utilice los valores anteriores

del(x) # elimina el valor del objeto



def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")
    
# Todas estas son posibles llamados de la anteior funcion
loro(1000) # 1 argumento posicional
loro(tension=1000) # 1 argumento nombrado
loro(tension=1000000, accion='VOOOOOM') # 2 argumentos nombrados
loro(accion='VOOOOOM', tension=1000000) # 2 argumentos nombrados
loro('un millón', 'despojado de vida', 'saltar') # 3 args posicionales
loro('mil', estado='viendo crecer las flores desde abajo') # uno y uno

# Estas son las llamadas de la funcion de una manera incorrecta
loro() # falta argumento obligatorio
loro(tension=5.0, 'muerto') # argumento posicional luego de uno nombrado
loro(110, tension=220) # valor duplicado para el mismo argumento
loro(actor='Juan Garau') # nombre del argumento desconocido

def funcion(a):
    pass

funcion(0, a=0)
# No se pueden pasar multiples valores a un mismo argumento a una funcion

def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print("-- ¿Tiene", tipo, "?")
    print("-- Lo siento, nos quedamos sin", tipo)
    for arg in argumentos:
        print(arg)
        print("-" * 40)
        claves = sorted(palabrasclaves.keys())
        for c in claves:
            print(c, ":", palabrasclaves[c])
    


ventadequeso("Limburger", "Es muy liquido, sr.",
"Realmente es muy muy liquido, sr.",
cliente="Juan Garau",
vendedor="Miguel Paez",
puesto="Venta de Queso Argentino") # el objeto argumentos recibe los valores hasta encontrar los que
#empiezan con definicion de objetos con igual, por lo que palabrasclaves recibira una lista con los valores de 
# cliente vendedor y puesto

def concatenar(*args, sep="/"):
    return sep.join(args)

# con el * antes del nombrel del objeto se quiere tener un objeto en el que puede resivir una lista de tamaño variante sin nombres claves
# con el ** antes del nombrel del objeto se quiere tener un objeto en el que puede resivir una lista de tamaño variante con nombres claves

concatenar("tierra", "marte", "venus")

concatenar("tierra", "marte", "venus", sep=".")

list(range(3, 6)) # llamada normal con argumentos separados

args = [3, 6]
list(range(*args)) # llamada con argumentos desempaquetados de la lista

#cuando el objeto lista no se encuentra empaquetado, es decir, no fue definido por * entonces ese ojeto se
# puede desempaquetar o separar como valores con el mismo simpolo * anteponiendolo al nombre del objeto


def loro(tension, estado='rostizado', accion='explotar'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.", end=' ')
    print("Está", estado, "!")



d = {"tension": "cinco mil", "estado": "demacrado","accion": "VOLAR"}
loro(**d) # Una lista se puede convertir en un diccionario si se define el nombre de la variable en la lista con 
# dos puntos y el significado y luego se utiliza con la antelacion de **

def hacer_incrementador(n):
    return lambda x: x + n

f = hacer_incrementador(42) #asocia la funcion con el valor de n = 42 
f(0) # ya que f tiene la funcion con el valor en en n=42, x se supone como null

f(1)
f(3)



# Como documentar una funcion

def mi_funcion():
    """No hace mas que documentar la funcion.
    
    No, de verdad. No hace nada.
    """
    pass

print(mi_funcion.__doc__)

################################################################################
######################Estructura de Datos ######################################
################################################################################

### Mas sobre Listas

#list.append (x) := agrega el valor x en la lista al final

#list.extend (L) := agrega todos los elementos de una lista L al final parecido a coladd en R

#list.insert (i, x) := inserta un valor x en la posicion dada i

#list.remove (x) := elimina el primer valor x en la lista, si la lista no contiene el valor x saldra error

#list.pop ([, i]) := euita el valor x en la posicion dada de la lista, y lo devuelve. 
#si no se especifica la posicion quita y devuelve el ultimo valor de la lista

a = [1,2,5,8]
a.pop(2)
a

# list.clear () := quita todos los elementos de la lista

# list.index (x[, start[, end]]) := Devuelve un índice basado en cero en la lista del primer ítem cuyo valor sea x.
#Levanta una excepción ValueError si no existe tal ítem.
#Los argumentos opcionales start y end son interpetados como la notación de rebanadas y se usan para limitar la
#búsqueda a una subsecuencia particular de x. El index retornado se calcula de manera relativa al inicio de la secuencia
#completa en lugar de con respecto al argumento start.

a.index(5)


# list.count (x) := cuenta el numero de elementos x en la lista

# list.sort (key=None, reverse=False) := ordena los valores de la lista

# list.reverse () := invierte el sentido de la lista

# list.copy () := devuelve una copia superficial de la lista

## UN ejemplo

frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']
frutas.count('manzana')

frutas.count('mandarina')

frutas.index('banana')

frutas.index('banana', 4) # Find next banana starting a position 4

frutas.reverse()

frutas.append('uva')

frutas.sort()

frutas.pop()




