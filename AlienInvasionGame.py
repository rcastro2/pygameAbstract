from gamelib import *

game = Game(900,500,"Alien Invasion",30)
bk = Image("images\\landscape.jpg",game)
bk.resizeTo(game.width, game.height)

robot = Animation("images\\robot\\robot ",30,game,frate=2)
robot.moveTo(game.width / 2, game.height - 60)

explosion = Animation("images\\explosion\\explosion ",22,game)
explosion.makeVisible(False)

volcanoes = []
bomb = Animation("images\\bomb\\bomb ",6,game,frate=4)
bomb.moveTo(randint(100,800),-100)
bomb.setSpeed(2,180)

while not game.over:
    game.processInput()
    bk.draw()
    bomb.move()
    for volcano in volcanoes:
        volcano.draw()

    robot.draw()
    explosion.draw(False)
    if keys.Pressed[K_LEFT] and robot.left > game.left:
        robot.moveX(-4)
    elif keys.Pressed[K_RIGHT] and robot.right < game.right:
        robot.moveX(4)

    if robot.collidedWith(bomb):
        explosion.moveTo(robot.x, robot.y)
        explosion.makeVisible(True)
        game.score += 10
        bomb.moveTo(randint(100,800),-100)
        bomb.speed += 0.25
        
    if bomb.bottom > game.height - 50:
        volcanoes.append(Animation("images\\volcano\\volcano ",8,game,frate=2))
        volcanoes[len(volcanoes)-1].moveTo(bomb.x,bomb.y)
        bomb.moveTo(randint(100,800),-100)

    if len(volcanoes) >= 10:
        game.over = True

    game.displayScore()
    game.update(30)
game.quit()
