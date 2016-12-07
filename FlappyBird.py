from gamelib import *

game = Game(640,480,"Flappy Bird")

bk = Image("images\\day.png",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)

bird = Animation("images\\bird.png",3,game,44,34,frate=6)

bar = Animation("images\\bar.png",3,game,700,110,frate=3)
bar.resizeTo(game.width,bar.height)
bar.moveTo(game.width/2,game.height-50)

ring = Animation("images\\ring2.png",64,game,64,64)
ring.moveTo(35,430)

pipeTop = Image("images\\pipe_top.png",game)
pipeTop.setSpeed(2,90)
pipeBottom = Image("images\\pipe_bot.png",game)
pipeBottom.setSpeed(2,90)
y = randint(300,450)
pipeBottom.moveTo(game.width + 100, y)
pipeTop.moveTo(game.width + 100, y - 350)

title = Image("images\\logo.png",game)
endtitle = Image("images\\flappybird_end.png",game)

bk.draw()
bar.draw()
title.draw()
game.font.shadowColor = black
game.drawText("Press [Space] to Start.",237,280)
game.update(1)
game.wait(K_SPACE)

scoreFont = Font(black,36)

crossed = False
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)

    bird.draw()
    bird.rotateTo(-10)
    bird.y += 2
    
    pipeTop.move()
    pipeBottom.move()
    bar.draw()
    ring.draw()
    if bird.collidedWith(pipeTop,"rectangular") or bird.collidedWith(pipeBottom,"rectangular") or bird.collidedWith(bar,"rectangular"):
        game.over = True
        endtitle.draw()
    if keys.Pressed[K_SPACE] :
        bird.y -= 5
        bird.rotateTo(10)    

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
    game.drawText(" x " + str(game.score),70,420, scoreFont)
    game.update(30)

game.drawText("Press [Enter] to Exit.",200,400, Font(black,40,green))
game.update()
game.wait(K_RETURN)
game.quit()

