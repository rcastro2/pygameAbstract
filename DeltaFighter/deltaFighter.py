import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''
from gamelib import *

#Game Functions
def controls():
    if keys.Pressed[K_LEFT]:
        hero.x -= 5
    if keys.Pressed[K_RIGHT]:
        hero.x += 5
    if keys.Pressed[K_UP]:
        hero.y -= 5
    if keys.Pressed[K_DOWN]:
        hero.y += 5
      
#Game Program
game = Game(800,600,"Delta Fighter")

bk = Animation("images\\field_5.png",5,game,1000,1000)
game.setBackground(bk)

title = Image("images\\logo.png",game)
title.y = 100
play = Image("images\\play.png",game)
play.resizeBy(-25)
play.y = 350

howto = Image("images\\howtoplay.png",game)
howto.resizeBy(-25)
howto.y = 425

story = Image("images\\story.png",game)
story.resizeBy(-25)
story.y = 500

storyImage = Image("images\\storyImage.png",game)
storyImage.visible = False

howtoImage = Image("images\\howtoImage.png",game)
howtoImage.visible = False

boss = Image("images\\aliensh.png",game)
boss.y = -100
boss.setSpeed(0.5,180)
hero = Animation("images\\hero2.png",3,game,288 / 3, 96, 2)

#game.collisionBorder = "circle"

bullet = Animation("images\\plasmaball1.png",11,game,352 / 11, 32)
bullet.visible = False
bullet.setSpeed(8,0)
explosion = Animation("images\\explosion1.png",22,game,1254 / 22, 64)
explosion.visible = False

asteroids = []
for index in range(60):
    a = Animation("images\\asteroid1t.gif", 41, game, 2173 / 41, 52)
    asteroids.append( a )
for index in range(len(asteroids)):
    x = randint(100,700)
    y = randint(100, 5000)
    asteroids[index].moveTo(x,-y)
    s = randint(4,8)
    asteroids[index].setSpeed(s,180)

plasmaballs = []
for index in range(20):
    p = Animation("images\\plasmaball1.png",11,game,352 / 11, 32)
    plasmaballs.append(p)
    
for index in range(len(plasmaballs)):
    x = randint(100,700)
    y = randint(100, 5000)
    plasmaballs[index].moveTo(x,-y)
    s = randint(4,8)
    plasmaballs[index].setSpeed(s,180)

healthpods = []
for index in range(20):
    h = Animation("images\\firstaid.png",40,game,1285/5,2000/8)
    healthpods.append(h)

for index in range(20):
    x = randint(100,700)
    y = randint(100, 5000)
    healthpods[index].moveTo(x,-y)
    s = randint(4,8)
    healthpods[index].setSpeed(s,180)
    healthpods[index].resizeBy(-85)
    
minions = []
for index in range(40):
    m = Image("images\\alien2.png",game)
    minions.append( m )
    
for index in range(len(minions)):
    x = randint(100,700)
    y = randint(100, 5000)
    minions[index].moveTo(x,-y)
    minions[index].setSpeed(5,180)
    minions[index].resizeBy(-50)

#Start Screen
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)
    title.draw()
    play.draw()
    howto.draw()
    story.draw()
    storyImage.draw()
    howtoImage.draw()
     
    if mouse.collidedWith(play,"rectangle") and mouse.LeftClick:
        game.over = True
    elif storyImage.visible and mouse.LeftClick:
        storyImage.visible = False
    elif mouse.collidedWith(story,"rectangle") and mouse.LeftClick:
        storyImage.visible = True
    elif mouse.collidedWith(howtoImage,"rectangle") and mouse.LeftClick:
        howtoImage.visible = False  
    elif mouse.collidedWith(howto,"rectangle") and mouse.LeftClick:
        howtoImage.visible = True

    game.update(30)

#Level 1 Screen
game.over = False
hero.ammo = 0
game.level1progress = 0
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)
    hero.draw()
    explosion.draw(False)
    game.drawText("Ammo: " + str(hero.ammo),hero.x - 30, hero.y + 70)
    game.drawText("Health: " + str(hero.health),hero.x - 30, hero.y + 50)
    for index in range(len(plasmaballs)):
        plasmaballs[index].move()
        if plasmaballs[index].collidedWith(hero):
            hero.ammo += 2
            plasmaballs[index].visible = False
            
    for index in range(len(asteroids)):
        asteroids[index].move()
        if asteroids[index].y > game.height + 100 and asteroids[index].visible:
            game.level1progress += 1
            asteroids[index].visible = False
        if asteroids[index].collidedWith(hero):
            hero.health -= 10
            game.level1progress +=1
            asteroids[index].visible = False
            explosion.moveTo(hero.x, hero.y)
            explosion.visible = True

    for index in range(len(healthpods)):
        healthpods[index].move()
        if healthpods[index].collidedWith(hero):
            hero.health += 5
            healthpods[index].visible = False
            
    controls()

    if game.level1progress == len(asteroids) or hero.health <= 0:
        game.over = True
        
    game.update(30)

#Level 2 Screen
game.over = False
for index in range(len(plasmaballs)):
    x = randint(100,700)
    y = randint(100, 10000)
    plasmaballs[index].moveTo(x,-y)
    s = randint(4,8)
    plasmaballs[index].setSpeed(s,180)
    plasmaballs[index].visible = True

while not game.over and hero.health > 0:
    game.processInput()
    game.scrollBackground("down",2)
    hero.draw()
    boss.move()
    bullet.move()
    explosion.draw(False)
    
    for index in range(len(minions)):
        minions[index].move()
        if minions[index].collidedWith(bullet):
            bullet.visible = False
            minions[index].visible = False
            explosion.moveTo(minions[index].x, minions[index].y)
            explosion.visible = True
        if minions[index].collidedWith(hero):
            hero.health -= 10
            minions[index].visible = False
            explosion.moveTo(minions[index].x, minions[index].y)
            explosion.visible = True
            
    for index in range(len(plasmaballs)):
        plasmaballs[index].move()
        if plasmaballs[index].collidedWith(hero):
            hero.ammo += 1
            plasmaballs[index].visible = False
            
    if keys.Pressed[K_SPACE] and not bullet.visible and hero.ammo > 0 :
        bullet.moveTo( hero.x, hero.y )
        hero.ammo -= 1
        bullet.visible = True
        
    if bullet.collidedWith(boss):
        bullet.visible = False
        boss.health -= 10
        explosion.moveTo(bullet.x, bullet.y)
        explosion.visible = True
        
    if bullet.y < 0:
        bullet.visible = False
    if boss.health < 0:
        game.over = True
    if boss.collidedWith(hero):
        hero.health = 0
        
    controls()
    
    game.drawText("Ammo: " + str(hero.ammo),hero.x - 30, hero.y + 70)
    game.drawText("Health: " + str(hero.health),hero.x - 30, hero.y + 50)
    game.drawText("Health: " + str(boss.health),5,5)
    game.update(30)
    
# Game Over Screen
game.over = False
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)
    game.drawText("Game Over", 120,150, Font(white, 140))
    if hero.health > 0:
        msg = "You Win"
    else:
        msg = "You Lose"
    game.drawText(msg, 120,290, Font(white, 140))
    game.update(30)
game.quit()

