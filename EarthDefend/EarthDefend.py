import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update it for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''

from gamelib import *

game = Game(800,600,"Earth Defend")
game.setMusic("sound\\starwars.wav")
city = Image("images\\city.png",game)
city.moveTo(game.width / 2, game.height - 200)

bk = Animation("images\\field_5.png",5,game,1000,1000)
game.setBackground(bk)
            
asteroids = [] #Empty List

for times in range(50):
    asteroids.append( Animation("images\\asteroid1t.gif",41,game,371/7,312/6) )

for a in asteroids:
    x = randint(100,700)
    y = -randint(100,5000)
    s = randint(1,3)
    a.moveTo(x,y)
    a.setSpeed(s,180)

hero = Image("images\\hero.gif",game)

explosion = Animation("images\\explosion.png",22,game, 285/5, 320/5)
explosion.visible = False
plasma = Animation("images\\plasmaball1.png",11,game,352/11,32)
plasma.visible = False

fires = []
game.drawBackground()
city.draw()
hero.draw()
game.drawText("Earth Defend",game.width/4 ,game.height/4,Font(green,90,yellow))
game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update()
game.wait(K_SPACE)

shoot = Sound("sound\\blaster.wav",1)
fly = Sound("sound\\fly1.wav",2)
boom = Sound("sound\\Arcade Explo A.wav",3)
game.playMusic()

while not game.over:
    game.processInput()
    game.scrollBackground("down",1)

    
    city.draw()
    hero.move()
    explosion.draw(False) 
    plasma.move()

    for a in asteroids:
        a.move()
        if a.collidedWith(plasma):
            a.visible = False
            explosion.visible = True
            explosion.moveTo(a.x,a.y)
            boom.play()
        if a.collidedWith(city,"rectangle") and a.y > 500 :
            a.visible = False
            fires.append( Animation("images\\fire2.png",16,game, 200, 200) )       
            fires[len(fires)-1].moveTo(a.x,a.y + randint(0,70))    
            city.damage += 1
            boom.play()
        if a.collidedWith(hero):
            hero.health -= 20
            explosion.visible = True
            explosion.moveTo(hero.x,hero.y)
            boom.play()
            a.visible = False

    for  f in fires:
        f.draw()

    if city.damage >= 20 or hero.health == 0:
        game.over = True
    
    if keys.Pressed[K_LEFT] or joy.pad[E]:
        hero.rotateBy(4,"left")
    if keys.Pressed[K_RIGHT] or joy.pad[W]:
        hero.rotateBy(4,"right")
 
    if keys.Pressed[K_UP] or joy.button[4]:
        hero.forward(4)
        fly.play()
    else:
        hero.speed *= 0.99
        
    if keys.Pressed[K_SPACE] or joy.button[5]:
        plasma.visible = True
        plasma.moveTo(hero.x,hero.y)
        plasma.setSpeed(10 , hero.getAngle())
        shoot.play()

    game.drawText("City Damage: " + str(city.damage),5,5)
    game.drawText("Health: " + str(hero.health),155,5)
    game.update(60)

game.drawText("Game Over",game.width/4,game.height/3,Font(green,90,yellow))
game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update()
game.wait(K_ESCAPE)
game.quit()
