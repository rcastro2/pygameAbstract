from gamelib2 import *

game = Game(700,500,"Game")
ball = Image("images\\beachball.png",game)
size = 100
ball.resizeTo(size,size)
ball.moveTo(game.width/2,game.height/2)
speed = 4

ball.setSpeed(speed,speed)

cross = Image("images\\crosshair.png",game)
bk = Image("images\\beach.jpg",game)
bk.moveTo(game.width/2,game.height/2)

t = 31
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
            ball.setSpeed(speed,speed)
        elif choice == 2:
            ball.moveTo(randint(ball.width,game.width - ball.width), randint(ball.height,game.height-ball.height))
        elif choice == 3:
            size -= 10
            ball.resizeTo(size,size)

    game.drawText("Time: " + str(int(t)),200,0,(255,255,255))
    game.drawText("Score: " + str(game.score),0,0,(255,255,255))
    t -= 1/60
    if t < 0:
        game.over = True
    game.update(60)
game.quit()
