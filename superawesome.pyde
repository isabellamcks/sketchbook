numsegments = 4 
segmentheight = 150
segmentwidth = 100

white = color(252, 253, 255)
reed = color(250, 0, 4)

colorlist = (white, reed)


def setup():
    
    size(1000, 1000)
    noStroke()
    background(206, 210, 240)
    
        
    
def draw_towers(x, y):
    
    fill(252, 253, 255)
    colorcount = 0
    for i in range(numsegments):
        fill(colorlist[colorcount])
        rect(x, y + (segmentheight * i), segmentwidth, segmentheight)
        colorcount += 1
        
        if (colorcount > 1):
            colorcount = 0
    
def draw():
    

    
    draw_towers(675, 200)
    draw_towers(200, 300)
    
    fill(23, 26, 46)
    rect(150, 850, 450, 150)
    rect(600, 750, 250, 250)
        
        
        
