from random import randint
import math
def positionAsteroids(asteroids,earth,game):
    for a in asteroids:
        x = randint(10,game.width*10)
        y = randint(10,game.height*10)
        speed = randint(1,3)
        chance = randint(0,8)

        if chance == 0:
            a.moveTo(x,-y)
        elif chance == 1:
            a.moveTo(-x,y)
        elif chance == 2:
            a.moveTo(x,game.height + y)
        elif chance == 3:
            a.moveTo(game.width + x,y)
        elif chance == 4:
            a.moveTo(game.width + x,game.height + y)
        elif chance == 5:
            a.moveTo(-x,-y)
        elif chance == 6:
            a.moveTo(game.width + x, -y)
        else:
            a.moveTo(-x,game.height + y)
     
        a.moveTowards(earth,speed)
