import numpy

class animated():
    position = numpy.zeros(2)
    velocity = numpy.zeros(2)
    mass = None
    health = None
    color = "red"
    shape_name = None

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

        new_x = x + vx*deltat + .5*ax*deltat*deltat
        new_y = y + vy*deltat + .5*ay*deltat*deltat

        new_vx = vx + ax*deltat
        new_vy = vy + ay*deltat

        
        self.position = numpy.array([new_x, new_y])
        self.velocity = numpy.array([new_vx, new_vy])

    def move_n_draw (self, force, deltat):
        x, y = self.position
        vx, vy = self.velocity
        ax, ay= force/self.mass

        new_x = x + vx*deltat + .5*ax*deltat*deltat
        new_y = y + vy*deltat + .5*ay*deltat*deltat

        new_vx = vx + ax*deltat
        new_vy = vy + ay*deltat

        
        self.position = numpy.array([new_x, new_y])
        self.velocity = numpy.array([new_vx, new_vy])
        #self.draw_movement((new_x-x)*10, (new_y - y)*10)
    
       
