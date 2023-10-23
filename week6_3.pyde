def setup():
    global cx, cy
    # size(500, 500)
    fullScreen()
    colorMode(HSB)
    cx = width / 2
    cy = height /2
    
cx = 0
cy = 0
r = 150
    
def draw():    
    global cx, cy
    global r
    num = 12
    theta = TWO_PI / 12
    
    background(0)
    noStroke()
    strokeWeight(5)
    for j in range(20):
        r = j * 20
        a = j * 10

        for i in range(num):
            angle = theta * i
            c = (i / float(num)) * 255
            cr = c
            print(c)
            fill(c, 255, a)
            
            x = cx + sin(angle) * r
            y = cy + cos(angle) * r
            stroke(200, 255, 255, a)
            line(cx, cy, x, y)
            noStroke()
            circle(x, y, cr) 
