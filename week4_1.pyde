def setup():
    size(500,500)
    
    
    
distance = 12.0
angle = 53
flag_height = 0


def draw():
    global distance
    global angle
    global flag_height
    
    flag_height= tan(radians(angle)) * distance
    
    background(0)
    
    distance = mouseX / 10
    
    border = 50
    stroke(255)
    line(border, height - border, border + (distance * 10 ), height - border)
    line(border, height - border, border + (distance * 10) , height - border - flag_height * 10)
    
    textAlign(LEFT,CENTER)
    
    x = border + (distance * 10) + 20
    y = (height - border) - (flag_height * 5)
    fill(255)
    text("Flag height: " + str(flag_height), x, y)
    

    
    
    
