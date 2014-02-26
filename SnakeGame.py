from gamelib import *
from SnakeClass import *

game = Game(700,500,"Game",30)
bob = Snake("images\\greenCircle.png",5,30,game)
apple = Image("images\\apple.png",game)
apple.resizeTo(25,25)
apple.moveTo(randint(apple.width,game.width-apple.width),randint(apple.height,game.height-apple.height))

bk = Image("images\\dirt.jpg",game)

game.viewMouse(False)

while not game.over:
    game.processInput()
    bk.draw()
    apple.draw()
    bob.draw()
  
    if keys.Pressed[K_LEFT]:
        bob.adjustTail()
        bob.move(-10,0)
    if keys.Pressed[K_RIGHT]:
        bob.adjustTail()
        bob.move(10,0)
    if keys.Pressed[K_UP]:
        bob.adjustTail()
        bob.move(0,-10)
    if keys.Pressed[K_DOWN]:
        bob.adjustTail()
        bob.move(0,10)
    if bob.eats(apple):
        bob.addTail()
        apple.moveTo(randint(100,400),randint(100,400))
        game.increaseScore(10)

    if game.time <= 0:
        game.over = True

    game.displayScore(0,0)
    game.displayTime(200,0)
    game.update(20)
    
game.quit()
