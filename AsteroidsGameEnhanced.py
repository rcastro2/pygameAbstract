from gamelib import *

game = Game(800,600,"Game",60)
game.setMusic("starwars.wav")
game.playMusic()

shot = Sound("blaster.wav")
fly = Sound("fly1.wav")
boom = Sound("Arcade Explo A.wav")

asteroid = Animation("images\\asteroid1\\asteroid1 ",41,game)
asteroid.setSpeed(4,45)

hero = Image("images\\hero.gif",game)
hero.moveTo(game.width/2,game.height/2)

explode = Animation("images\\explosion\\explosion ",22,game)
explode.makeVisible(False)

plasma = Animation("images\\plasmaball1\\plasmaball1 ",11,game)

bk = Animation("images\\field ",5,game)

game.viewMouse(False)

while not game.over:
    game.processInput()
    bk.draw()
    hero.move()
    asteroid.move(True)
    explode.draw(False)
    
    if keys.Pressed[K_LEFT] or joy.pad[E]:
        hero.rotateBy(2,"left")
    if keys.Pressed[K_RIGHT] or joy.pad[W]:
        hero.rotateBy(2,"right")
    if not keys.Pressed[K_LEFT] and not keys.Pressed[K_RIGHT] and joy.pad[C]:
        hero.rotateBy(0,"still")
    if keys.Pressed[K_UP] or joy.button[4]:
        hero.forward(1)
        fly.play()
    else:
        hero.forward(hero.speed *0.99)
    
    if asteroid.collidedWith(plasma):
        boom.play()
        plasma.makeVisible(False)
        game.score += 10
        explode.moveTo(asteroid.x,asteroid.y)
        explode.makeVisible(True)
        asteroid.moveTo(randint(asteroid.width,game.width-asteroid.width),randint(asteroid.height,game.height-asteroid.height))
    if asteroid.collidedWith(hero):
        boom.play()
        hero.damage += 10
        explode.moveTo(hero.x,hero.y)
        explode.makeVisible(True)
        asteroid.moveTo(randint(asteroid.width,game.width-asteroid.width),randint(asteroid.height,game.height-asteroid.height))
    if hero.x < 0 : hero.x = game.width
    if hero.x > game.width : hero.x = 0
    if hero.y < 0 : hero.y = game.height
    if hero.y > game.height : hero.y = 0
        
    if plasma.visible:
        plasma.move()
    if plasma.isOffScreen():
        plasma.makeVisible(False)
    
    if (keys.Pressed[K_SPACE] or joy.button[5]) and not plasma.visible:
        shot.play()
        plasma.makeVisible(True)
        plasma.moveTo(hero.x,hero.y)
        plasma.setSpeed(8,hero.getAngle())
        
    if hero.damage == 100 or game.time <= 0:
        game.over = True
    
    game.displayScore(0,0)
    game.displayTime(0,20)
    game.drawText("Damage: " + str(hero.damage),0,40)  
    game.update(60)
    
game.quit()
