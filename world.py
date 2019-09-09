import numpy
import itertools

class World ():
    #define the world grid
    height = None
    width = None
    canvasName = None
    list_of_figures = []

    def __init__(self, height, width, canvasName):
        self.height = height
        self.width = width
        self.canvasName = canvasName

    def grid_position(self, animated):
        return round(animated.position[0],4), round(animated.position[1],4)
    
    def animated_on_border(self, animated):
        x, y = self.grid_position(animated) 
        if  x <= 0:
            animated.position[0] = 0 + 0.01
            animated.velocity[0] *= -1
        if x >= self.width:
            animated.position[0] = self.width - 0.01
            animated.velocity[0] *= -1
        if  y <= 0:
            animated.position[1] = 0 + 0.01
            animated.velocity[1] *= -1
        if y >= self.height:
            animated.position[1] = self.height - 0.01
            animated.velocity[1] *= -1

    def boundaries(self, animated_list):
        for animated in animated_list:
            self.animated_on_border(animated)
    
    def distance(self, animated1, animated2):
        return numpy.sqrt((animated1.position[0] - animated2.position[0])**2 
        + (animated1.position[1] - animated2.position[1])**2)

    def collisions(self, animated_list, deltat):
        for a1, a2 in itertools.combinations(animated_list, 2):
            x1, y1 = a1.position
            x2, y2 = a2.position
            dist = self.distance(a1, a2)
            mm = a1.mass * a2.mass
            coeff = 0.01
            if  dist < 2:
                f1 = numpy.array([(x1-x2)*1/(dist**2 + 0.01), (y1-y2)*1/(dist**2 + 0.01)])
                f2 = numpy.array([(x2-x1)*1/(dist**2 + 0.01), (y2-y1)*1/(dist**2 + 0.01)])
                a1.move(mm*coeff*f2, deltat)
                a2.move(mm*coeff*f1, deltat)

    def move_all(self, animated_list, deltat):
        viscosity = .001
        for man in animated_list:
            f_visc = - viscosity*man.velocity *man.mass
            man.move(f_visc, deltat)
        self.draw_move_all(animated_list, deltat)
    
    def draw_circle(self, animated):
        r = 10
        x0 = animated.position[0]*10 - r
        y0 = animated.position[1]*10 - r
        x1 = animated.position[0]*10 + r
        y1 = animated.position[1]*10 + r
        return self.canvasName.create_oval(x0, y0, x1, y1, fill= animated.color)

    def draw_all(self, animated_list):
        for man in animated_list:
            self.list_of_figures.append(self.draw_circle(man))
    
    def draw_move_all(self, animated_list, deltat):
        for (man, figure) in zip(animated_list, self.list_of_figures):
            self.canvasName.move(figure, 10*man.velocity[0]*deltat, 10*man.velocity[1]*deltat)
            self.canvasName.update_idletasks()
            self.canvasName.update() 
        