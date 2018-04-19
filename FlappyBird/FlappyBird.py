import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(640,480,"Flappy Bird")

bk = Image("images\\day.png",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)

bird = Animation("images\\bird.png",3,game,44,34,6)

bar = Animation("images\\bar.png",3,game,700,110,3)
bar.resizeTo(game.width,bar.height)
bar.moveTo(game.width/2,game.height-50)

ring = Animation("images\\ring2.png",64,game,64,64)
ring.moveTo(35,430)

ring2 = Animation("images\\ring2.png",64,game,64,64)
y = randint(200,300)
ring2.moveTo(game.width,y)
ring2.setSpeed(2,90)

pipeTop = Image("images\\pipe_top.png",game)
pipeBottom = Image("images\\pipe_bot.png",game)



title = Image("images\\logo.png",game)
endtitle = Image("images\\flappybird_end.png",game)

bk.draw()
bar.draw()
title.draw()
game.font.shadowColor = black
game.drawText("Press [Space] to Start.",237,280)
game.update()
game.wait(K_SPACE)

scoreFont = Font(black,36)

while not game.over:
    game.processInput()
    game.scrollBackground("left",2)

    bird.draw()

    ring2.move()
    pipeBottom.moveTo(ring2.x, ring2.y + 175)
    pipeTop.moveTo(ring2.x, ring2.y - 175)

    bar.draw()
    ring.draw()
    
    if bird.collidedWith(pipeTop,"rectangle") or bird.collidedWith(pipeBottom,"rectangle") or bird.collidedWith(bar,"rectangle"):
        game.over = True
        endtitle.draw()
        
    if keys.Pressed[K_SPACE] :
        bird.y -= 5
        bird.rotateTo(10)
    else:
        bird.rotateTo(-10)
        bird.y += 2

    if bird.collidedWith(ring2):
        game.score += 1
        ring2.visible = False
 
    if pipeBottom.isOffScreen("left"):
        y = randint(200,300)
        ring2.moveTo(game.width,y)
        ring2.speed +=1
        ring2.visible = True

    game.drawText(" x " + str(game.score),70,420, scoreFont)
    game.update(30)

game.drawText("Press [Enter] to Exit.",200,400, Font(black,40,green))
game.update()
game.wait(K_RETURN)
game.quit()

