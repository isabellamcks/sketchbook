def setup():
    global planets, aliens
    size(500, 500)

    
    # planets[20] = "hello"
    
    for i in range(len(planets)):
         print(planets[i] + " " + str(aliens[i]))    

    for planet in planets:
         print(planet)

    for alien in aliens:
        print(alien)
        
    # Reverse the array
    planets.reverse()
    
    # Reverse it again
    planets.reverse()
    

    # Iterate backwards using range
    for i in range(len(planets) -1, 0, -1):
        print(planets[i] + " " + str(aliens[i]))
    

    # Iterate forwards
    for i in range(len(planets)):
        print(planets[i] + " " + str(aliens[i]))    
    
    
    
planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
aliens = [5, 13, 2, 10, 25, 34, 20, 20, 1]
    
def draw():
    pass
