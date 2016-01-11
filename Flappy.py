from gamelib import *

game = Game(650,450,"Flappy Bird")
bk1 = Image("images\\day.png",game)
bk1.setSpeed(2,90)
bk2 = Image("images\\day.png",game)
bk2.setSpeed(2,90)
bk2.moveTo(bk1.x + bk1.width,bk1.y)

pipeTop = Image("images\\pipe_top.png",game)
pipeTop.setSpeed(2,90)
pipeBottom = Image("images\\pipe_bot.png",game)
pipeBottom.setSpeed(2,90)
y = randint(300,480)
pipeBottom.moveTo(game.width + 100, y)
pipeTop.moveTo(game.width + 100, y - 350)

bird = Animation("images\\bird\\bird ",3,game)
bar = Animation("images\\bar\\bar ",3,game)
bar.moveTo(300,400)

title = Image("images\\logo.png",game)
endtitle = Image("images\\flappybird_end.png",game)
ring = Animation("images\\ring2.png",64,game,64,64)
ring.moveTo(35,410)

bk1.draw()
bar.draw()
title.draw()
game.update(1)
game.drawText("Press [Space] to Start.",240,260,white,26,True)
game.wait(K_SPACE)

crossed = False
while not game.over:
    game.processInput()
    game.background(black)

    bk1.move()
    bk2.move()
    
    bird.draw()
    bird.y += 1
    
    pipeTop.move()
    pipeBottom.move()
    bar.draw()
    ring.draw()
    if bird.collidedWith(pipeTop,"rectangular") or bird.collidedWith(pipeBottom,"rectangular") or bird.collidedWith(bar,"rectangular"):
        game.over = True
        endtitle.draw()
    if keys.Pressed[K_SPACE] :
        bird.y -= 3

    if bk1.x + bk1.width/2 < 0:
        bk1.moveTo(bk2.x + bk2.width,bk2.y)
    if bk2.x + bk2.width/2 < 0:
        bk2.moveTo(bk1.x + bk1.width,bk1.y)

    if bird.left > pipeTop.right and not crossed:
        crossed = True
        game.score += 1

    if pipeBottom.right < 0:
        y = randint(300,500)
        pipeBottom.moveTo(game.width + 100, y)
        pipeTop.moveTo(game.width + 100, y - 350)
        pipeTop.speed += 1
        pipeBottom.speed += 1
        crossed = False
    game.drawText(" x " + str(game.score),70,400,black,36)
    game.update(30)

game.drawText("Press [Enter] to Exit.",240,400,black,36,True)
game.wait(K_RETURN)
game.quit()

