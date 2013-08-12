from gamelib import *

game = Game(700,600,0,"Block Breaker")
paddle = Image("images\\paddle.png",game)
paddle.moveTo(game.width / 2, game.height - 40)
ball = Image("images\\ball.png",game)
ball.moveTo(game.width / 2, game.height / 2)
ball.setSpeed(45,3)

while not game.over:
    game.processInput()
    game.background(yellow)
    ball.move(True)
    if game.keysPressed[K_LEFT] and paddle.left > game.left:
        paddle.moveX(-4)
    elif game.keysPressed[K_RIGHT] and paddle.right < game.right:
        paddle.moveX(4)
    else:
        paddle.draw()

    if ball.bottom > paddle.top + 5 and ball.right > paddle.left and ball.left < paddle.right:
        ball.changeYSpeed()        

    if ball.top > paddle.bottom:
        game.over = True

    game.update(60)
game.quit()
