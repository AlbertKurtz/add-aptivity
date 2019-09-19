import numpy

#class for animated objects
class animated():
    position = numpy.zeros(2)
    velocity = numpy.zeros(2)
    mass = None
    health = None
    color = "red"
    shape_name = None
    radius = 1

    def __init__(self, position, mass, color):
        self.position = position
        self.mass = mass
        self.color = color
        self.spawn(self.position)

    def set_location(self, coordinates):
        self.position = coordinates

    def spawn(self, coordinates):
        self.health = 100
        self.set_location(coordinates)
        #self.draw_circle()

    def move (self, force, deltat):
        x, y = self.position
        vx, vy = self.velocity
        ax, ay= force/self.mass
		
		#newton equations of motion
        new_x = x + vx*deltat + .5*ax*deltat*deltat
        new_y = y + vy*deltat + .5*ay*deltat*deltat

        new_vx = vx + ax*deltat
        new_vy = vy + ay*deltat

        
        self.position = numpy.array([new_x, new_y])
        self.velocity = numpy.array([new_vx, new_vy])
    
       
class yellow_ball(animated):
    def __init__(self, position):
        self.position = position
        self.mass = 12
        self.color = "yellow"
        self.radius = self.mass
        self.spawn(self.position)

class red_ball(animated):
    def __init__(self, position):
        self.position = position
        self.mass = 10
        self.color = "red"
        self.radius = self.mass
        self.spawn(self.position)

class blue_ball(animated):
    def __init__(self, position):
        self.position = position
        self.mass = 5
        self.color = "blue"
        self.radius = self.mass
        self.spawn(self.position)

class green_ball(animated):
    def __init__(self, position):
        self.position = position
        self.mass = 20
        self.color = "green"
        self.radius = self.mass
        self.spawn(self.position)

class black_ball(animated):
    def __init__(self, position):
        self.position = position
        self.mass = 5
        self.color = "black"
        self.radius = 11
        self.spawn(self.position)

