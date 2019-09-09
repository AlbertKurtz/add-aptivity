import time, numpy
import tkinter as tk 
from animated import *
from world import *


def main():
    deltat = 1
    t = 0

    height = 60   
    width = 60

    root = tk.Tk()
    myCanvas = tk.Canvas(root, width= width*10, height=height*10)
    myCanvas.pack()


    world = World(height, width, canvasName=myCanvas)
    list_of_animated = []

    for i in range(20):
        list_of_animated.append(red_ball(position= numpy.random.uniform(0, 50, 2)))
        list_of_animated.append(yellow_ball(position= numpy.random.uniform(0, 50, 2)))
        list_of_animated.append(green_ball(position= numpy.random.uniform(0, 50, 2)))
        list_of_animated.append(blue_ball(position= numpy.random.uniform(0, 50, 2) ))
        list_of_animated.append(black_ball(position= numpy.random.uniform(0, 50, 2) ))
        #list_of_animated.append(animated(position= [23,14],mass= 5, canvasName=myCanvas))

    world.draw_all(list_of_animated)
    rand_force = numpy.random.uniform(-10, 10, 2)
    for man in list_of_animated:    
        man.move(rand_force, deltat)

    while (True):
        
        world.boundaries(list_of_animated)
        world.collisions(list_of_animated, deltat)
        world.move_all(list_of_animated, deltat)

        #time.sleep(0.1)
        t += deltat
        

if __name__ == "__main__":
    main()