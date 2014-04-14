from gamelib import *

game = Game(700,500,"Pop the BeachBall",10)
ball = Image("images\\beachball.png",game)
ball.resizeTo(ball.width / 2, ball.height / 2)

ball.setSpeed(2,60)

cross = Image("images\\crosshair.png",game)
bk = Image("images\\beach.jpg",game)
bk.resizeTo(game.width, game.height)

game.viewMouse(False)

#Game Loop
while not game.over:
        game.processInput()
        bk.draw()
        ball.move(True) 
        cross.moveTo(mouse.x,mouse.y)
        if mouse.LeftButton and ball.collidedWith(mouse):
                game.score += 10
                x = randint(ball.width,game.width - ball.width)
                y = randint(ball.height,game.height-ball.height)
                ball.moveTo(x, y)
                choice = randint(1,3)
                if choice == 1:
                        ball.speed += 4
                        game.time += 5
                elif choice == 2:
                        ball.width -= 10
                        ball.height -= 10
                       
        game.displayTime(200,0)
        game.displayScore(0,0)
        if game.time <= 0:
                game.over = True
        game.update(60)
#End Loop
game.drawText("Press [Space] to exit.",250,250,white,True)
game.wait(K_SPACE)

game.quit()
