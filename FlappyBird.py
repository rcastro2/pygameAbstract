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

ring2 = Animation("images\\ring2.png",64,game,64,64)
ring2.setSpeed(2,90)
pipeTop = Image("images\\pipe_top.png",game)
pipeTop.setSpeed(2,90)
pipeBottom = Image("images\\pipe_bot.png",game)
pipeBottom.setSpeed(2,90)

y = randint(200,300)
ring2.moveTo(game.width + 100,y)
pipeBottom.moveTo(game.width + 100, y + 175)
pipeTop.moveTo(game.width + 100, y - 175)

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

while not game.over:
    game.processInput()
    game.scrollBackground("left",2)

    bird.draw()
    bird.rotateTo(-10)
    bird.y += 2
    
    pipeTop.move()
    pipeBottom.move()
    ring2.move()
    bar.draw()
    ring.draw()
    
    if bird.collidedWith(pipeTop,"rectangle") or bird.collidedWith(pipeBottom,"rectangle") or bird.collidedWith(bar,"rectangle"):
        game.over = True
        endtitle.draw()
        
    if keys.Pressed[K_SPACE] :
        bird.y -= 5
        bird.rotateTo(10)    

    if bird.collidedWith(ring2):
        game.score += 1
        ring2.visible = False
 
    if pipeBottom.isOffScreen("left"):
        y = randint(200,300)
        ring2.moveTo(game.width + 100,y)
        pipeBottom.moveTo(game.width + 100, y + 175)
        pipeTop.moveTo(game.width + 100, y - 175)
        pipeTop.speed += 1
        pipeBottom.speed += 1
        ring2.speed +=1
        ring2.visible = True

    game.drawText(" x " + str(game.score),70,420, scoreFont)
    game.update(30)

game.drawText("Press [Enter] to Exit.",200,400, Font(black,40,green))
game.update()
game.wait(K_RETURN)
game.quit()

