def setup():
  size(500,500)
  colorMode(HSB)
  x = 0
  y = 0
  background(0)


x = 0
y = 0
c = 0
      

  
def draw():
    global x
    global y
    global c
    
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, 10)
    rect(0, 0, width * 4, height * 4)
    blendMode(BLEND)
    colorMode(HSB)
    
    noStroke()
    fill(c, 255, 255)
    circle(x, y, 50)
    x = x + 1
    y = y + 1
    c = c + 1
    
    if c > 255:
        c = 0
    
    # < >
    # ==
    # <=
    # >=
    # and &&
    # || or
    
    
        
        
