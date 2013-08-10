from gamelib2 import *
from SnakeClass import *

game = Game(700,500,"Game")
bob = Snake("greenCircle.png",5,30,game)
apple = Image("apple.png",game)
apple.resizeTo(25,25)
apple.moveTo(randint(apple.width,game.width-apple.width),randint(apple.height,game.height-apple.height))

bk = Image("dirt.jpg",game)
bk.moveTo(game.width/2,game.height/2)

game.viewMouse(False)

while not game.over:
    game.processInput()
    bk.draw()
    apple.draw()
    bob.draw()
  
    if game.keysPressed[K_LEFT]:
        bob.adjustTail()
        bob.move(-10,0)
    if game.keysPressed[K_RIGHT]:
        bob.adjustTail()
        bob.move(10,0)
    if game.keysPressed[K_UP]:
        bob.adjustTail()
        bob.move(0,-10)
    if game.keysPressed[K_DOWN]:
        bob.adjustTail()
        bob.move(0,10)
    if bob.eats(apple):
        bob.addTail()
        apple.moveTo(randint(100,400),randint(100,400))
        game.increaseScore(10)
    
    game.drawText("Score: " + str(game.score),0,0,(255,255,255))
    game.update(20)
game.quit()
