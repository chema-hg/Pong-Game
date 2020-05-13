#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''Clasico juego del Pong desarrollado con Turtle'''

from turtle import *
import os # Lo importamos para darle efectos de sonido.
from time import sleep, process_time # para regular la velocidad.

velocidad=0.02

# ventana donde se desarrollara el juego. 
ventana=Screen()
ventana.title("Pong by @chema")
ventana.bgcolor("black")  # ventana con fondo negro
ventana.setup(800,600)  # tamaño de la ventana
ventana.tracer(0)  # maximo de velocidad de renderizado en turtle.
# .tracer(n=None, delay=None) Si ponemos n en cero o off, hace que la tortuga desaparecezca y que comandos como
# setx,sety o goto vayan muchisimo mas rapido. El segundo argumento establece el retraso.

# Score - Establece los marcadores a cero a comienzo de la partida.
score_a=0
score_b=0


# Pala A
pala_a = Turtle()
# no es la velocidad del movimiento sino de la animación de la pala. 1 = lento; 10=el mas rapido.
# Si el valor es 0, entra en un modo especial que hace que se realice lo mas rapido posible
pala_a.speed(0) 
pala_a.shape("square")
pala_a.color("white")
# por defecto el tamaño en pixels es de 20*20 pixeles, le cambiamos el tamaño
pala_a.shapesize(stretch_wid=5, stretch_len=1)
pala_a.penup()  # levantar el lapiz para que no trace el recorrido.
# posicionamos en la ventana, -350 pixeles a la izquierda y en el centro
pala_a.goto(-350,0)

# pala B
pala_b = Turtle()
# no es la velocidad del movimiento sino de la animación de la pala. 0 es el maximo
pala_b.speed(0)
pala_b.shape("square")
pala_b.color("white")
# por defecto el tamaño en pixels es de 20*20 pixeles, le cambiamos el tamaño
pala_b.shapesize(5, 1)
pala_b.penup()  # levantar el lapiz para que no trace el recorrido.
# posicionamos en la ventana, 350 pixeles a la derecha y en el centro
pala_b.goto(350, 0)

# Bola
bola = Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx=2 # Creamos esta variable en nuestra clase para definir cuantos pixeles en x se movera en cada loop
bola.dy=2 # Creamos esta variable en nuestra bola para definir cuantos pixeles en y se movera en cada loop
# cada vez que la bola se tenga que mover lo hara 2 pixeles en x y 2 pixeles en y

# Marcador
marcador = Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle() # Esconde la tortuga para que no la veamos moverse
marcador.goto(0,260)
marcador.write("Player A: 0  |  Player B: 0", align="center", font=(30)) #escribe texto en pantalla.

# funciones
def pala_a_arriba():
    "Funcion para mover hacia arriba la pala a"
    y = pala_a.ycor()
    y += 30
    pala_a.sety(y) #cambia la coordenada y del objeto pala_a

def pala_a_abajo():
    "Funcion para mover hacia abajo la pala a"
    y = pala_a.ycor()
    y -= 30
    pala_a.sety(y)
    
def pala_b_arriba():
    "Funcion para mover hacia arriba la pala b"
    y = pala_b.ycor()
    y += 30
    pala_b.sety(y) #cambia la coordenada y del objeto pala_a

def pala_b_abajo():
    "Funcion para mover hacia abajo la pala b"
    y = pala_b.ycor()
    y -= 30
    pala_b.sety(y)

# teclado
ventana.listen() #escucha las pulsaciones del teclado
ventana.onkeypress(pala_a_arriba, "w") # si la tecla detectada es la w ejecuta la funcion pala_a_arriba
ventana.onkeypress(pala_a_abajo,"s") 
ventana.onkeypress(pala_b_arriba, "Up") # si la tecla detectada es flecha arriba
ventana.onkeypress(pala_b_abajo,"Down") # si la tecla detectada es flecha abajo

tiempo1=process_time()

# bucle principal del juego
# el centro (0,0) estara en la mitad de la ventana.
while True:
    ventana.update()  # cada vez que se ejecute el bucle se actualice la ventana

    # movimiento de la bola
    bola.setx(bola.xcor()+bola.dx)
    bola.sety(bola.ycor()+bola.dy)
    
    # Controlando los limites de la pantalla - bordes.
    # BORDE SUPERIOR
    if bola.ycor() > 290: #teniendo en cuenta que el 0,0 esta en el centro y
        # por tanto 300 seria el limite del borde superior. 
        bola.sety(290) # Volvemos a poner la bola en y=290
        bola.dy *=-1 # Invertimos el signo de la variable que controla el movimiento
        #en el eje y , y por tanto la pelota rebotará.
        os.system("aplay golpe_borde.wav&")
        
    # BORDE INFERIOR
    if bola.ycor() < -290: #teniendo en cuenta que el 0,0 esta en el centro y
        # por tanto -290 seria el limite del borde inferior. 
        bola.sety(-290) # Volvemos a poner la bola en y=-290
        bola.dy *=-1 # Invertimos el signo de la variable que controla el movimiento
        #en el eje y , y por tanto la pelota rebotará.
        os.system("aplay golpe_borde.wav&")
    
    # BORDE DERECHO
    if bola.xcor() > 390: # como la pantalla tiene 800 de ancho y el centro esta en el
    # (0,0) para que la bola no se salga por la derecha lo limitaremos a 390 p.ej.
        bola.goto(0,0) # si se sale del limite x, es punto y vuelve al 0,0
        bola.dx*=-1
        score_a+=1 # Al salirse por la derecha es punto para el jugador a
        marcador.clear() # Limpia el marcador ya que si no se sobrescribirian los numeros.
        marcador.write(f"Player A: {score_a}  |  Player B: {score_b}", align="center", font=(30))
                
    # BORDE IZQUIERDO
    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx*=-1
        score_b+=1 # Al salirse por la izquierda es punto para el jugador b
        marcador.clear()
        marcador.write(f"Player A: {score_a}  |  Player B: {score_b}", align="center", font=(30))
        
    # COLISIONES DE PALAS Y BOLAS
    if (bola.xcor()>340 and bola.xcor()<350) and (bola.ycor()<pala_b.ycor()+50 and \
                                                 bola.ycor()>pala_b.ycor()-50):
        bola.setx(340)
        bola.dx*=-1
        os.system("aplay golpe_pala.wav&") #reproduce un sonido al chocar la bola y la pala.
                                            # la instrucción varia dependiendo del sistema operativo
                                            # En linux es aplay y el & final despues del archivo es para que no
                                            # se pare el movimiento al reproducir el sonido.
    
    if (bola.xcor()<-340 and bola.xcor()>-350) and (bola.ycor()<pala_a.ycor()+50 and \
                                                 bola.ycor()>pala_a.ycor()-50):
        bola.setx(-340)
        bola.dx*=-1
        os.system("aplay golpe_pala.wav&")
    
    # Aumento de velocidad cada +- 6 segundos
    
    if (process_time()-tiempo1) > 0.3: # Regula cada cuanto tiempo se aumentara la velocidad
                                        # a mayor numero mas tiempo tarda en cambiar la velocidad.
        velocidad-= 0.001 #como cada vez el retardo es menor, la velocidad es mayor por tanto.
        tiempo1=process_time()
        if velocidad<0.005:
            velocidad=0.005 # limita la velocidad a un minimo, para que sea jugable.
               
    # El primer jugador que llega a 10 puntos gana.
    if score_a==10 or score_b==10:
        if score_a>score_b:
            marcador.clear()
            marcador.write(f"Player A: {score_a}  |  Player B: {score_b}\nEL JUGADOR A GANA", align="center", font=(30))
        else:
            marcador.clear()
            marcador.write(f"Player A: {score_a}  |  Player B: {score_b}\nEL JUGADOR B GANA", align="center", font=(30))
        os.system("aplay aplauso.wav&")
        sleep(1)
        break

    sleep(velocidad)
