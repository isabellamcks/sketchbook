def setup():
    global cx, cy
    size(750, 750)
    cx = width / 2
    cy = height / 2
    
cx = 0
cy = 0
r = 150

def draw():
    global cx, cy
    global r
    num = 8
    theta = TWO_PI / 8
    
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
            fill(255, 192, 203)
            
            x = cx + sin(angle) * r
            y = cy + cos(angle) * r
            stroke(255, 192, 203, a)
            line(cx, cy, x, y)
            noStroke()
            circle(x, y, cr) 
            
            circle(375, 350, 200)
            fill(119, 221, 119)
            
        
        
        
