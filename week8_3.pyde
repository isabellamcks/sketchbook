def setup():
    global cube
    size(500, 500, P3D)
    colorMode(HSB)
    cube = Cube(0, 0 , 0, 1, 60) # creating the cube instance
    
    
def draw():
    global cube
    background(0)
    lights()
    translate(width / 2, height / 2)
    cube.render() # calling the render method on the cube

# a class consists of fields and methods
class Cube:
    
    # constructer
    def __init__(self, x, y, z, s, h): 
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        
    def render(self):
        translate(self.pos.x, self.pos.y, self.pos.z)
        scale(self.s)
        stroke(self.h, 255, 255)
        noFill()
        box(100)
