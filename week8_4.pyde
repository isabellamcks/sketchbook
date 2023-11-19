def setup():
    global cube, cube2
    size(500, 500, P3D)
    colorMode(HSB)
    cube = Cube(0, 0 , 0, 1, 60) # creating the cube instance
    cube2 = Cube(-100, -100, 0, 2, 100)
    
def draw():
    global cube, cube2
    background(0)
    lights()
    translate(width / 2, height / 2)
    cube.render() # calling the render method on the cube
    cube2.render()

# a class consists of fields and methods
class Cube:
    
    # constructer
    def __init__(self, x, y, z, s, h): 
        # these are now fields! thats what the self word does
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.theta = 0
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.theta)
        rotateX(self.theta)
        scale(self.s)
        stroke(self.h, 255, 255)
        noFill()
        box(100)
        popMatrix()
        self.theta += 0.05
