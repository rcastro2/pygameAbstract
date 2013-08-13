from gamelib import *

game = Game(700,500,30,"Pop the BeachBall")
ball = Image("images\\beachball.png",game)
size = 200
ball.resizeTo(size,size)
ball.moveTo(game.width/2,game.height/2)
speed = 2
ball.setSpeed(60,speed)

cross = Image("images\\crosshair.png",game)
bk = Image("images\\beach.jpg",game)
bk.resizeTo(game.width, game.height)
bk.moveTo(game.width/2,game.height/2)

game.viewMouse(False)
while not game.over:
    game.processInput()
    bk.draw()
    ball.move(True) 
    cross.moveTo(game.mouseX,game.mouseY)
    if game.mouseLB and ball.collidedWith("mouse"):
        game.increaseScore(10)
        choice = randint(1,4)
        if choice == 1:
            speed += 1
            ball.setSpeed(math.degrees(ball.angle),speed)
        elif choice == 2:
            ball.moveTo(randint(ball.width,game.width - ball.width), randint(ball.height,game.height-ball.height))
        elif choice == 3:
            size -= 10
            ball.resizeTo(size,size)

    game.displayTime(200,0)
    game.displayScore(0,0)
    if game.time <= 0:
        game.over = True
    game.update(60)
game.quit()
