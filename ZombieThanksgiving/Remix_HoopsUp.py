import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated it for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(1024,768,"Hoops Up!", 60)


player1 = Image("images\\player1.png", game)
player1.setSpeed(4,60)
player1.resizeBy(-60)

player2 = Image("images\\player2.png", game)
player2.setSpeed(3,90)
player2.resizeBy(-70)

ball = Image("images\\basketball.png", game)
ball.resizeBy(-95)

hoop = Image("images\\Basketball_Net.png",game)
hoop.resizeBy(-90)
hoop.moveTo(game.width / 2,200)

court = Image("images\\court.jpg",game)
court.resizeTo(game.width, game.height)

player1Score = 0
player2Score = 0
while not game.over:
    game.processInput()

    court.draw()
    hoop.draw()
    ball.moveTo(mouse.x, mouse.y)

    player1.move(True)
    player2.move(True)

    if ball.collidedWith(hoop):
        x = randint(100,900)
        y = randint(100,600)
        hoop.moveTo(x,y)
        player1.speed +=1
        player2.speed +=1
        game.score +=1

    if ball.collidedWith(player1):
        player1Score += 1
        
    if ball.collidedWith(player2):
        player2Score += 1
        
    if game.time <= 0:
        game.over = True

    game.drawText("Player: " + str(game.score), 5, 5)
    game.drawText("Frady: " + str(player1Score), 100, 5)
    game.drawText("Jordan: " + str(player2Score), 200, 5)
    
    game.displayTime(game.width - 80,5)
    game.update(60)
game.quit()

