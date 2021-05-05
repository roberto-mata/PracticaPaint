from turtle import *
from freegames import vector
import turtle

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circulo(start, end):
    "Draw circle from start to end."
    distancia = end.x - start.x
    begin_fill()
    circle(distancia)
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    begin_fill()
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    end_fill()
    
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        #saca, extrae el valor que tiene la var state en la llave 'shape'
        shape = state['shape']
        
        #crea un objeto de tipo vector con x,y y lo guarda en la var end
        end = vector(x, y)
        
        #el contenido de shape indica la función que se ejecutará
        shape(start, end)
        
        #reinicia start con None - para/indicar que lo sig es nuevo
        state['start'] = None
def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
#función que sirve para crear una ventana de ancho 420, alto 420
#los ultimos 2 argumentos indica posición en esquina sup izq
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y') #Color agregado por mi#
onkey(lambda: color('#F5B7B1'), 'Q') #Nuevo color agregado#
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

