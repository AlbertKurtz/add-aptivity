"""

Usage:
  add_aptivity.py
Options:
  -h, --help    Show this screen.
  --version     Show version.
"""

__author__ = 'Alberto Flor'
__credits__ = ['Alberto Flor']
__license__ = 'GPL3+'
__version__ = '0.0.1'
__maintainer__ = 'Alberto Flor'
__email__ = 'albert.flor.mail@gmail.com'
__status__ = 'Development'

import time, numpy
import tkinter as tk 
from classes.animated import *
from classes.world import *


def main():
	#define the dt interval of time
    deltat = 1
    t = 0
	
	#dimension of the grid
	#note that on drawing, the number of pixel is (height*10 x width*10)
    height = 60   
    width = 60

    root = tk.Tk()
    myCanvas = tk.Canvas(root, width= width*10, height=height*10)
    myCanvas.pack()


    world = World(height, width, canvasName=myCanvas)
    list_of_animated = []
	
	#spawn all the animated objects
    for i in range(20):
        list_of_animated.append(red_ball(position= numpy.random.uniform(0, 50, 2)))
        list_of_animated.append(yellow_ball(position= numpy.random.uniform(0, 50, 2)))
        list_of_animated.append(green_ball(position= numpy.random.uniform(0, 50, 2)))
        list_of_animated.append(blue_ball(position= numpy.random.uniform(0, 50, 2) ))
        list_of_animated.append(black_ball(position= numpy.random.uniform(0, 50, 2) ))

    world.draw_all(list_of_animated)
    
    #starting random force for all animated objects
    rand_force = numpy.random.uniform(-10, 10, 2)
    for man in list_of_animated:    
        man.move(rand_force, deltat)

    while (True):
        
        world.boundaries(list_of_animated)
        world.collisions(list_of_animated, deltat)
        world.move_all(list_of_animated, deltat)

        t += deltat
        

if __name__ == "__main__":
    main()
