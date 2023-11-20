def setup():
    size(550, 500)
    background(33, 32, 248)  
    frameRate(100)
    noStroke()
    fill(255)
    rect(18, 30, 511, 422)
    
def draw():
    stroke(0)
    strokeWeight(3)
#backgrounds
    global drawing
    
    if mousePressed and mouseButton == LEFT:
        x, y = mouseX, mouseY
        line(x, y, pmouseX, pmouseY)
     
    noStroke()
    fill(9, 7, 54)
    rect(18, 30, 304, 88)
    fill(255)
    rect(20, 32, 300, 84)
    fill(104, 103, 145)
    rect(54, 34, 264, 80)
    fill(255)
    rect(54,34, 2, 2)
    rect(54, 112, 2, 2)
    rect(316, 34, 2, 2)
    rect(316, 112, 2, 2)
#colours
    fill(255)
    rect (58, 52, 36, 36)
    fill(7, 6, 72)  #main colour
    rect(60, 54, 32, 32)
#out lines 
    fill(9, 7, 54)# outline for all colours
    rect(98, 38, 130, 66)
    rect (232, 36, 70, 70)
    
#pics
    fill(255)
    rect (234, 38, 32, 32)
    rect (268, 38, 32, 32)
    rect (234, 72, 32, 32)
    rect (268, 72, 32, 32)
  
#dropper
    fill(9, 7, 54)
    rect(272, 62, 2, 4)
    rect(274, 60, 2, 2)
    rect(274, 64, 2, 2)
    rect(276, 54, 2, 6)
    rect(276, 62, 2, 2)
    rect(278, 52, 2, 2)
    rect(278, 60, 6, 2)
    rect(280, 50, 2, 2)
    rect(282, 58, 4, 2)
    rect(282, 44, 2, 6)
    rect(284, 44, 2, 2)
    rect(284, 56, 4, 2)
    rect(286, 42, 2, 2)
    rect(286, 46, 2, 2)
    rect(286, 54, 4,2)
    rect(288, 40, 6, 2)
    rect(288, 48, 2, 2)
    rect(290, 50, 2, 2)
    rect(290, 52, 4, 4)
    rect(294, 42, 2, 2)
    rect(294, 48, 2, 4)
    rect(296, 44, 2, 6)
    
    
#R
    fill(9, 7, 54)
    rect(236, 48, 8, 14)
    fill(255)
    rect(238, 50, 4, 4)
    rect(238, 56, 2, 2)
    rect(242, 56, 2, 2)
    rect(238, 58, 4, 4)
#G
    fill(9, 7, 54)
    rect(246, 48, 8, 14)
    fill(255)
    rect(248, 50, 6, 4)
    rect(248, 54, 2, 2)
    rect(248, 56, 4, 4)
#B
    fill(9, 7, 54)
    rect(256, 48, 8, 14)
    fill(255)
    rect(262, 48, 2, 2)
    rect(258, 50, 4, 4)
    rect(262, 54, 2, 2)
    rect(262, 60, 2, 2)
    rect(258, 56, 4, 4)
#2
    fill(9, 7, 54)
    rect(238, 82, 6, 14)
    fill(255)
    rect(238, 84, 4, 4)
    rect(240, 90, 4, 4)
#5
    fill(9, 7, 54)
    rect(246, 82, 6, 14)
    fill(255)
    rect(248, 84, 4, 4)
    rect(246, 90, 4, 4)
#6
    fill(9, 7, 54)
    rect(254, 82, 6, 14)
    fill(255)
    rect(256, 84, 4, 4)
    rect(256, 90, 2, 4)
#1
    fill(9, 7, 54)
    rect (278, 82, 2, 14)
    fill(255)
#6, 2 electric boogaloo
    fill(9, 7, 54)
    rect(282, 82, 6, 14)
    fill(255)
    rect(284, 84, 4, 4)
    rect(284, 90, 2, 4)
#cursor
    fill(9, 7, 54)
    rect(244, 250, 2, 26)
    rect(246, 250, 2, 2)
    rect(248, 252, 2, 2)
    rect(250, 254, 2, 2)
    rect(252, 256, 2, 2)
    rect(254, 258, 2, 2)
    rect(256, 260, 2, 2)
    rect(258, 262, 2, 2)
    rect(260, 264, 2, 2)
    rect(254, 266, 10, 2)
    rect(254, 268, 2, 2)
    rect(256, 270, 2, 4)
    rect(248, 270, 2, 2)
    rect(246, 272, 2, 2)
    rect(258, 274, 2, 4)
    rect(260, 278, 2, 2)
    
#colours
    fill(255)
    rect(98, 38, 34, 18)
    fill(7, 6, 72)
    rect(100, 40, 30, 14)
    fill(104, 103, 145)
    rect(132, 40, 30, 14)
    fill(32, 216, 6)
    rect(164, 40, 30, 14)
    fill(104, 246, 72)
    rect(196, 40, 30, 14)
    fill(32, 33, 245)
    rect(100, 56, 30, 14)
    fill(72, 102, 250)
    rect(132, 56, 30, 14)
    fill(170, 33, 14)
    rect(164, 56, 30, 14)
    fill(72, 215, 249)
    rect(196, 56, 30, 14)
    fill(242, 35, 3)
    rect(100, 72, 30, 14)
    fill(248, 103, 74)
    rect(132, 72, 30, 14)
    fill(216, 216, 6)
    rect(164, 72, 30, 14)
    fill(215, 219, 141)
    rect(196, 72, 30, 14)
    fill(31, 145, 6)
    rect(100, 88, 30, 14)
    fill(214, 72, 144)
    rect(132, 88, 30, 14)
    fill(179, 174, 144)
    rect(164, 88, 30, 14)
    fill(244, 248, 247)
    rect(196, 88, 30, 14)
