def setup():
    size(500, 500, P3D)
    
theta = 0
    
def draw():
    global theta
    background(0)
    lights()
    stroke(255)
    strokeWeight(5)
    noFill()
    translate(width / 2, height / 2)
    rotateX(theta)
    rotateY(theta)
    rotateZ(theta)
    box(100)
    theta += 0.01
