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
y = randint(300,500)
pipeBottom.moveTo(game.width + 100, y)
pipeTop.moveTo(game.width + 100, y - 400)

bird = Animation("images\\bird\\bird ",3,game)
bar = Animation("images\\bar\\bar ",3,game)
bar.moveTo(300,450)

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
    if bird.collidedWith(pipeTop,"rectangular") or bird.collidedWith(pipeBottom,"rectangular"):
        game.over = True
    if keys.Pressed[K_SPACE] :
        bird.y -= 3
    if bird.collidedWith(bar,"rectangular"):
        game.over = True

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
        pipeTop.moveTo(game.width + 100, y - 400)
        pipeTop.speed += 1
        pipeBottom.speed += 1
        crossed = False
    game.displayScore()
    game.update(30)
game.quit()

game.over = True

