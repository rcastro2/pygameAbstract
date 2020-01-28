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
    heroHPBar.moveTo(hero.x - 30, hero.y + 50)
    heroHPBar.width = hero.health / 2
    heroAmmoBar.moveTo(hero.x - 30, hero.y + 70)
    heroAmmoBar.width = hero.ammo * 2

def positionObjects(objects):
    for index in range(len(objects)):
        x = randint(100,700)
        y = randint(100, 5000)
        objects[index].moveTo(x,-y)
        s = randint(4,8)
        objects[index].setSpeed(s,180)
        objects[index].visible = True
      
#Game Program
game = Game(800,600,"Delta Fighter")

bk = Animation("images\\field_5.png",5,game,1000,1000)
game.setBackground(bk)

title = Image("images\\title.png",game)
title.y = 100

story = Image("images\\story1.png",game)
story.y = 400
story_off = Image("images\\story1.png",game)
story_on = Image("images\\story2.png",game)

howto = Image("images\\howtoplay1.png",game)
howto.y = 475
howto_off = Image("images\\howtoplay1.png",game)
howto_on = Image("images\\howtoplay2.png",game)

play = Image("images\\play1.png",game)
play.y = 550
play_off = Image("images\\play1.png",game)
play_on = Image("images\\play2.png",game)

storyImage = Image("images\\storyImage.png",game)
storyImage.visible = False

howtoImage = Image("images\\howtoImage.png",game)
howtoImage.visible = False

boss = Image("images\\aliensh.png",game)
boss.y = -100
boss.setSpeed(0.5,180)

hero = Animation("images\\hero2.png",3,game,288 / 3, 96, 2)

gameover = Image("images\\gameover.png",game)
gameover.y = 100

mission_accomplished = Image("images\\mission_accomplished.png",game)
mission_accomplished.resizeBy(-25)
mission_failed = Image("images\\mission_failed.png",game)
mission_failed.resizeBy(-25)
#game.collisionBorder = "circle"

bullet = Animation("images\\plasmaball1.png",11,game,352 / 11, 32)
bullet.visible = True
bullet.setSpeed(8,0)
explosion = Animation("images\\explosion1.png",22,game,1254 / 22, 64)
explosion.visible = False
explosion2 = Animation("images\\explosion2.png",6,game,750/3,441/2,use_alpha=False)

progressBar = Shape("bar",game,200,20,green)
progressBar.moveTo(10,10)
heroHPBar = Shape("bar",game,50,10,green)
heroAmmoBar = Shape("bar",game,2,10,blue)
bossHPBar = Shape("bar",game,100,10,green)

select_menu = Sound("sounds\\tick.wav",1)
explosion_boss = Sound("sounds\\explosion_boss.wav",2)
explosion_other = Sound("sounds\\explosion_other.wav",3)
blast = Sound("sounds\\blaster.wav",4)
collect_ammo = Sound("sounds\\collect_ammo.wav",5)
collect_hp = Sound("sounds\\collect_hp.wav",6)

asteroids = []
for index in range(50):
    a = Animation("images\\asteroid1t.gif", 41, game, 2173 / 41, 52)
    asteroids.append( a )
positionObjects(asteroids)

plasmaballs = []
for index in range(20):
    p = Animation("images\\plasmaball1.png",11,game,352 / 11, 32)
    plasmaballs.append(p)
positionObjects(plasmaballs)

healthpods = []
for index in range(20):
    h = Animation("images\\firstaid.png",40,game,1285/5,2000/8)
    healthpods.append(h)
    healthpods[len(healthpods)-1].resizeBy(-85)
positionObjects(healthpods)
    
minions = []
for index in range(40):
    m = Image("images\\alien2.png",game)
    minions.append( m )
    minions[len(minions)-1].resizeBy(-50)
positionObjects(minions)    

mouse.visible = False
menu = ""
#Start Screen
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)
    title.draw()
    story.draw()
    howto.draw()
    play.draw()
    hero.draw()
    storyImage.draw()
    howtoImage.draw()
    bullet.moveTo(mouse.x, mouse.y)

    explosion2.draw()
    story.setImage(story_off.image)
    howto.setImage(howto_off.image)
    play.setImage(play_off.image)
    if bullet.collidedWith(play,"rectangle"):
        play.setImage(play_on.image)
        if menu != "play":
            select_menu.play()
            menu = "play"
    elif bullet.collidedWith(story,"rectangle"):
        story.setImage(story_on.image)
        if menu != "story":
            select_menu.play()
            menu = "story"
    elif bullet.collidedWith(howto,"rectangle"):
        howto.setImage(howto_on.image)
        if menu != "howto":
            select_menu.play()
            menu = "howto"
        
    if storyImage.visible and mouse.LeftClick:
        storyImage.visible = False
    elif bullet.collidedWith(story,"rectangle") and mouse.LeftClick:
        storyImage.visible = True
    elif howtoImage.visible and mouse.LeftClick:
        howtoImage.visible = False  
    elif bullet.collidedWith(howto,"rectangle") and mouse.LeftClick:
        howtoImage.visible = True
    elif bullet.collidedWith(play,"rectangle") and mouse.LeftClick:
        game.over = True

    game.update(30)

#Level 1 Screen
game.over = False
hero.ammo = 2
game.level1progress = 0
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)
    progressBar.draw()
    hero.draw()
    explosion.draw(False)
    
    for index in range(len(plasmaballs)):
        plasmaballs[index].move()
        if plasmaballs[index].collidedWith(hero):
            hero.ammo += 2
            plasmaballs[index].visible = False
            collect_ammo.play()
            
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
            explosion_other.play()

    for index in range(len(healthpods)):
        healthpods[index].move()
        if healthpods[index].collidedWith(hero):
            hero.health += 5
            healthpods[index].visible = False
            collect_hp.play()
                
    progressBar.width = 200 - game.level1progress * 4
    if game.level1progress == len(asteroids) or hero.health <= 0:
        game.over = True

    controls()    
    game.update(30)

#Level 2 Screen
game.over = False
bullet.visible = False
positionObjects(plasmaballs)

while not game.over and hero.health > 0:
    game.processInput()
    game.scrollBackground("down",2)
    hero.draw()
    boss.move()
    bossHPBar.width = boss.health 
    bossHPBar.y = boss.bottom
    bossHPBar.x = boss.x - bossHPBar.width / 2
    bossHPBar.draw()
    bullet.move()
    explosion.draw(False)
    
    for index in range(len(minions)):
        minions[index].move()
        if minions[index].collidedWith(bullet):
            bullet.visible = False
            minions[index].visible = False
            explosion.moveTo(minions[index].x, minions[index].y)
            explosion.visible = True
            explosion_other.play()
        if minions[index].collidedWith(hero):
            hero.health -= 10
            minions[index].visible = False
            explosion.moveTo(minions[index].x, minions[index].y)
            explosion.visible = True
            explosion_other.play()
            
    for index in range(len(plasmaballs)):
        plasmaballs[index].move()
        if plasmaballs[index].collidedWith(hero):
            hero.ammo += 1
            plasmaballs[index].visible = False
            collect_ammo.play()
            
    if keys.Pressed[K_SPACE] and not bullet.visible and hero.ammo > 0 :
        bullet.moveTo( hero.x, hero.y )
        hero.ammo -= 1
        bullet.visible = True
        blast.play()
        
    if bullet.collidedWith(boss):
        bullet.visible = False
        boss.health -= 5
        explosion.moveTo(bullet.x, bullet.y)
        explosion.visible = True
        explosion_boss.play()
        
    if bullet.y < 0:
        bullet.visible = False
    if boss.health < 0:
        game.over = True
    if boss.collidedWith(hero):
        hero.health = 0
        
    controls()
    
    game.update(30)
    
# Game Over Screen
game.over = False
positionObjects(healthpods)
positionObjects(plasmaballs)
positionObjects(minions)
positionObjects(asteroids)
hero.moveTo(game.width / 2, game.height - hero.height * 2)
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)
    gameover.draw()
    if hero.health > 0:
        for h in healthpods:
            h.move()
        for p in plasmaballs:
            p.move()
        hero.draw()
        mission_accomplished.draw()
    else:
        for m in minions:
            m.move()
        for a in asteroids:
            a.move()
        explosion.draw(False)
        if not explosion.visible:
            x = randint(explosion.width , game.width - explosion.width)
            y = randint(explosion.height, game.height - explosion.height)
            explosion.moveTo(x, y)
            explosion.visible = True
            
        mission_failed.draw()
    
    game.update(30)
game.quit()

