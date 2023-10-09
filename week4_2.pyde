def setup ():
    global cx
    global cy
    global px
    global py
    global r
    global theta
    size(500,500)
    cx = width / 2
    cy = height / 2
    
    px = cx
    py = 0
    background(0)
    
    
cx = 0
cy = 0
r  = 1
theta = 0

px = 0
py = 0

def draw():
    global cx
    global cy
    global px
    global py
    global r
    global theta
    x = cx + sin(theta) * r
    y = cy + cos(theta) * r
    
    stroke(255)
    line( px, py, x, y)

    
    r = r + 1
    theta = theta + 0.1
