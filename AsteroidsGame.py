from gamelib import *

game = Game(700,500,"Game",60)
asteroid = Animation("images\\asteroid1\\asteroid1 ",41,game)
asteroid.setSpeed(4,45)

hero = Image("images\\hero.gif",game)

explode = Animation("images\\explosion\\explosion ",22,game)
explode.makeVisible(False)

plasma = Animation("images\\plasmaball1\\plasmaball1 ",11,game)

bk = Animation("images\\field\\field ",5,game)

game.viewMouse(False)

while not game.over:
    game.processInput()
    bk.draw()
    hero.move()
    asteroid.move(True)
    explode.draw(False)
    
    if keys.Pressed[K_LEFT]:
        hero.rotateBy(2,"left")
    if keys.Pressed[K_RIGHT]:
        hero.rotateBy(2,"right")
    if not keys.Pressed[K_LEFT] and not keys.Pressed[K_RIGHT]:
        hero.rotateBy(0,"still")
    if keys.Pressed[K_UP]:
        hero.forward(2)
    else:
        hero.forward(hero.speed *0.99)
    
    if asteroid.collidedWith(plasma):
        plasma.makeVisible(False)
        game.score += 10
        explode.moveTo(asteroid.x,asteroid.y)
        explode.makeVisible(True)
        asteroid.moveTo(randint(asteroid.width,game.width-asteroid.width),randint(asteroid.height,game.height-asteroid.height))
    if asteroid.collidedWith(hero):
        hero.damage += 10
        explode.moveTo(hero.x,hero.y)
        explode.makeVisible(True)
        asteroid.moveTo(randint(asteroid.width,game.width-asteroid.width),randint(asteroid.height,game.height-asteroid.height))
        
    if plasma.visible:
        plasma.move()
    if plasma.isOffScreen():
        plasma.makeVisible(False)
    
    if keys.Pressed[K_SPACE] and not plasma.visible:
        plasma.makeVisible(True)
        plasma.moveTo(hero.x,hero.y)
        plasma.setSpeed(5,hero.getAngle())
        
    if hero.damage == 100 or game.time <= 0:
        game.over = True
    
    game.displayScore(0,0)
    game.displayTime(0,20)
    game.drawText("Damage: " + str(hero.damage),0,40)   
    game.update(100)
    
game.quit()
