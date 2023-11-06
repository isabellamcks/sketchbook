def setup():
    size(500,500)
    global planets, aliens
    
    
    for planet in range(len(planets)):
        print(planet)
        
    for alien in range(len(aliens)):
        print(alien)
        
    for i in range (len(planets)):
        print(planets[i] + "\t" + str(aliens[i]))
        
    least_index=0
    for i in range(len(planets)):
        if aliens[i] < aliens[least_index]:
            least_index=i

        print("The planet with the least number of aliens is : " +str(planets[least_index]))
            
    most_index=0
    for i in range(len(planets)):
        print(i)
        if aliens[i] > aliens[most_index]:
            most_index=i
            print("most_index: " + str(i))

    print("The planet with the most number of aliens is : " +str(planets[most_index]))
    
    sum = 0
    for i in range(len(planets)):
        sum = sum + aliens[i]
    
    average = sum / len(planets)
    
    print("Total Aliens: " + str(sum))
    print("Average Aliens: " + str(average))
    
    
    
planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
aliens = [5,13,2,10,25,34,20,20,1]

def draw():
    global planets, aliens
    
    background(0)
    w = width / len(planets)
    noFill()
    stroke(255)
    for i in range(len(planets)):
        x = w * i
        rect(x, height, w, - aliens[i])
        # textMode(CENTER, CENTER)
        fill(255)
        text(planets[i], x + (w * 0.5), height - 20)
        
