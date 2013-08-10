from gamelib2 import *

game = Game(700,500,"Game")
asteroid = Animation("asteroid1\\asteroid1 ",41,2,game)
asteroid.setSpeed(4,4)

hero = Image("hero.gif",game)
hero.moveTo(game.width/2,game.height/2)

explode = Animation("explosion\\explosion ",22,1,game)
explode.makeVisible(False)

plasma = Animation("plasmaball1\\plasmaball1 ",11,3,game)

bk = Animation("field ",5,3,game)
bk.moveTo(game.width/2,game.height/2)
game.viewMouse(False)

damage = 0
while not game.over:
    game.processInput()
    bk.draw()
    hero.move()
    asteroid.move(True)
    explode.draw(False)
    
    if asteroid.collidedWith(plasma):
        plasma.makeVisible(False)
        game.increaseScore(10)
        explode.moveTo(asteroid.x,asteroid.y)
        explode.makeVisible(True)
        asteroid.moveTo(randint(asteroid.width,game.width-asteroid.width),randint(asteroid.height,game.height-asteroid.height))
    if asteroid.collidedWith(hero):
        damage += 10
        explode.moveTo(hero.x,hero.y)
        explode.makeVisible(True)
        asteroid.moveTo(randint(asteroid.width,game.width-asteroid.width),randint(asteroid.height,game.height-asteroid.height))
        
    if plasma.visible:
        plasma.move()
    if plasma.isOffScreen():
        plasma.makeVisible(False)

    if game.keysPressed[K_LEFT]:
        hero.rotateTo("left",4)
    if game.keysPressed[K_RIGHT]:
        hero.rotateTo("right",4)
    if not game.keysPressed[K_LEFT] and not game.keysPressed[K_RIGHT]:
        hero.rotateTo("still",0)
    if game.keysPressed[K_UP]:
        hero.forward(3)
    else:
        hero.forward(hero.thrust *0.99)

    if game.keysPressed[K_SPACE] and not plasma.visible:
        plasma.makeVisible(True)
        plasma.moveTo(hero.x,hero.y)
        plasma.setSpeed(5*math.sin(hero.angle+math.pi),5*math.cos(hero.angle+math.pi))

    if damage == 100:
        game.over = True

    game.drawText("Score: " + str(game.score),0,0,(255,255,255))
    game.drawText("Damage: " + str(damage),200,0,(255,255,255))        
    game.update(60)
#game.wait(K_ESCAPE)
game.quit()
