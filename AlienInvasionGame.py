from gamelib import *

game = Game(900,500,30,"Alien Invasion")
bk = Image("images\\landscape.jpg",game)
bk.resizeTo(game.width, game.height)
bk.moveTo(game.width/2,game.height/2)

robot = Animation("images\\robot\\robot ",30,2,game)
robot.moveTo(game.width / 2, game.height - 60)

explosion = Animation("images\\explosion\\explosion ",22,1,game)
explosion.makeVisible(False)

volcanoes = []
bomb = Animation("images\\bomb\\bomb ",6,4,game)
bomb.moveTo(randint(100,800),-100)
speed = 2
bomb.setSpeed(180,speed)

while not game.over:
    game.processInput()
    bk.draw()
    bomb.move()
    for volcano in volcanoes:
        volcano.draw()

    robot.draw()
    explosion.draw(False)
    if game.keysPressed[K_LEFT] and robot.left > game.left:
        robot.moveX(-4)
    elif game.keysPressed[K_RIGHT] and robot.right < game.right:
        robot.moveX(4)

    if robot.collidedWith(bomb):
        explosion.moveTo(robot.x, robot.y)
        explosion.makeVisible(True)
        game.increaseScore(10)
        bomb.moveTo(randint(100,800),-100)
        speed += 0.25
        bomb.setSpeed(180,speed)
        
    if bomb.bottom > game.height - 50:
        volcanoes.append(Animation("images\\volcano\\volcano ",8,2,game))
        volcanoes[len(volcanoes)-1].moveTo(bomb.x,bomb.y)
        bomb.moveTo(randint(100,800),-100)

    if len(volcanoes) >= 10:
        game.over = True

    game.displayScore()
    game.update(60)
game.quit()
