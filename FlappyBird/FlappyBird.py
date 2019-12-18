import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(800,600,"Flappy Bird")

day = Image("images\\day.png",game)
day.resizeTo(game.width, game.height)
night = Image("images\\night.png",game)
night.resizeTo(game.width, game.height)
game.setBackground(day)

bird = Animation("images\\bird.png",3,game,44,34,6)

bar = Animation("images\\bar.png",3,game,700,110,3)
bar.width = game.width
bar.y = game.height - 50

ring = Animation("images\\ring2.png",64,game,64,64)
ring.moveTo(35,game.height - 50)

ring2 = Animation("images\\ring2.png",64,game,64,64)
ring2.x = game.width + 100
ring2.setSpeed(2,90)

pipeTop = Image("images\\pipe_top.png",game)
pipeBottom = Image("images\\pipe_bot.png",game)

title = Image("images\\logo.png",game)
title.y = bird.y - 150
endtitle = Image("images\\flappybird_end.png",game)
endtitle.y = bird.y - 150

#Start Screen
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)

    bird.draw()
    title.draw()
    bar.draw()
    if keys.Pressed[K_SPACE]:
        game.over = True
    if keys.Pressed[K_n]:
        game.setBackground(night)
    if keys.Pressed[K_d]:
        game.setBackground(day)
    game.drawText("Press [SPACE] to begin",bird.x - 180, game.height - 70, Font(red,36,black,"Comic Sans MS"))
    game.update(30)
game.over = False

#Game Screen
while not game.over:
    game.processInput()
    game.scrollBackground("left",ring2.speed)

    bird.draw()

    ring2.move()
    pipeBottom.moveTo(ring2.x, ring2.y + 200)
    pipeTop.moveTo(ring2.x, ring2.y - 200)

    bar.draw()
    ring.draw()
    
    if bird.collidedWith(pipeTop,"rectangle") or bird.collidedWith(pipeBottom,"rectangle") or bird.collidedWith(bar,"rectangle"):
        game.over = True
        endtitle.draw()
        
    if keys.Pressed[K_SPACE] :
        bird.y -= 4
        bird.rotateTo(10)
    else:
        bird.rotateTo(-10)
        bird.y += 2

    if bird.collidedWith(ring2):
        game.score += 1
        ring2.visible = False
 
    if ring2.x < -100:
        y = randint(200,300)
        ring2.moveTo(game.width + 100,y)
        ring2.speed +=1
        ring2.visible = True

    game.drawText(" x " + str(game.score),65,game.height - 85, Font(red,48,black,"Comic Sans MS"))
    game.update(30)

#Game Over
game.over = False
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)

    bird.draw()
    endtitle.draw()
    bar.draw()
    if keys.Pressed[K_ESCAPE]:
        game.over = True
    game.drawText("Press [ECAPE] to end",bird.x - 180, game.height - 80, Font(red,36,black,"Comic Sans MS"))
    game.update(30)
game.over = False
game.quit()

