import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated it for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(700,600,"Block Breaker")
paddle = Image("images\\paddle.png",game)
paddle.moveTo(game.width / 2, game.height - 40)
ball = Image("images\\ball.png",game)
ball.setSpeed(3,45)

while not game.over:
    game.processInput()
    game.clearBackground(yellow)
    paddle.draw()
    ball.move(True)
    if keys.Pressed[K_LEFT] and paddle.left > game.left:
        paddle.moveX(-4)
    elif keys.Pressed[K_RIGHT] and paddle.right < game.right:
        paddle.moveX(4)

    if ball.bottom > paddle.top + 5 and ball.right > paddle.left and ball.left < paddle.right:
        ball.changeYSpeed()        

    if ball.top > paddle.bottom:
        game.over = True

    game.update(60)
game.quit()
