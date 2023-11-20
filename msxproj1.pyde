def setup():
    size(550, 500, P3D)
    colorMode(HSB, 360, 100, 100)
    noStroke()
    lights()

def draw():
    background(0)
    
    # Set the fill color based on mouse position
    hue_value = map(mouseX, 0, width, 0, 360)
    saturation_value = map(mouseY, 0, height, 0, 100)
    brightness_value = 100
    
    fill(hue_value, saturation_value, brightness_value)
    
    # Draw a cuboid in the center of the canvas
    strokeWeight(2)
    stroke(255)
    
    pushMatrix()
    
    translate(width/2, height /2)
    rotateX(frameCount * 0.05)
    rotateY(frameCount * 0.05)
    box(400,150,100)
    popMatrix()
    
    
    # Second cuboid on top
    pushMatrix()
    translate(width / 2, height / 2, 50)  
    rotateX(frameCount * 0.05)
    rotateY(frameCount * 0.05)
    box(400,75,100)
    popMatrix()
    
    
