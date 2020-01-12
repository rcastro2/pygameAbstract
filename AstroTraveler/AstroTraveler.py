import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update it for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''

from gamelib import *

game = Game(800,600,"Space Traveler")
bk = Animation("images\\field_5.png",5,game,1000,1000)
game.setBackground(bk)

asteroids = []
gems = []
fuelpods = []

for num in range(150):
    asteroids.append(  Animation("images\\asteroid1t.gif",41,game,2173/41, 52, 2 )   )
for num in range(10):
    gems.append( Image("images\\gem1.png",game))
for num in range(10):
    fuelpods.append( Image("images\\gem2.png",game))
    
for asteroid in asteroids:
    x = game.width + randint(100 ,10500)
    y = randint(5 ,550)
    s = randint(4,8)
    asteroid.moveTo(x,y)
    asteroid.setSpeed(s,90)

for g in gems:
    g.resizeBy(-80)
    x = game.width + randint(100 ,10500)
    y = randint(5 ,550)
    s = randint(4,8)
    g.moveTo(x,y)
    g.setSpeed(s,90)

for f in fuelpods:
    f.resizeBy(-90)
    x = game.width + randint(100 ,10500)
    y = randint(5 ,550)
    s = randint(4,8)
    f.moveTo(x,y)
    f.setSpeed(s,90)

hero = Image("images\\hero.gif",game)
hero.rotateBy(90)

explosion = Animation("images\\explosion1.png",22,game,1254/22,64)
explosion.visible = False

fuel = 1000
#Start Screen
game.drawBackground()
game.drawText("Astro Traveler",game.width/4,game.height/2, Font(green,80,yellow,"arial bold") )
game.drawText("Press [SPACE] to Start",game.width/2,game.height/2 + 200, Font(white,32,yellow) )
game.update()
game.wait(K_SPACE)

#Game
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)

    if fuel > 0:
        fuel -= 1
    for asteroid in asteroids:
        asteroid.move()
        if hero.collidedWith(asteroid):
            hero.health -= 1
            explosion.moveTo(hero.x,hero.y)
            explosion.visible = True
            
    for g in gems:
        g.move()
        if hero.collidedWith(g):
            hero.health += 10
            g.visible = False
    for f in fuelpods:
        f.move()
        if hero.collidedWith(f):
            fuel += 100
            f.visible = False
            
    if hero.health < 0:
        game.over = True
        
    game.drawText("Health: " + str(hero.health),5,5)
    game.drawText("Fuel: " + str(fuel),105,5)
    hero.draw()
    explosion.draw(False)
    if keys.Pressed[K_LEFT] and fuel > 0 :
        hero.x -= 5
    if keys.Pressed[K_RIGHT] and fuel > 0:
        hero.x += 5
    if keys.Pressed[K_UP] and fuel > 0:
        hero.y -= 5
    if keys.Pressed[K_DOWN] and fuel > 0:
        hero.y += 5
    game.update(30)
    
#EndGame
game.drawText("Game Over",game.width/4,game.height/2, Font(green,80,yellow,"arial bold") )
game.drawText("Press [SPACE] to Quit",game.width/2,game.height/2 + 200, Font(white,32,yellow) )
game.update()
game.wait(K_SPACE)
game.quit()
