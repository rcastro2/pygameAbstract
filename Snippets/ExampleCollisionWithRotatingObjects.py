import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *
game = Game(900,900,"Collision Between Rotating Objects")
game.collisionBorder = "vertices"

bar1 = Animation("images/bar.png",3,game,700,110,4)
bar1.resizeTo(900,50)

bar2 = Shape("rectangle",game,900,50,gray)

bar3 = Image("images/plasmaball2.png",game)
bar3.resizeBy(25)

currentBar = bar3

alien = Image("images/Alien2.gif",game)
alien.moveTo(500,500)

apple = Image("images/apple.png",game)
apple.resizeBy(-90)
apple.moveTo(200,200)

while not game.over:
    game.processInput()
    game.clearBackground(white)

    currentBar.draw()
    currentBar.rotateBy(1)

    alien.moveTo(mouse.x,mouse.y)
    apple.draw()
    
    if currentBar.collidedWith(alien,"vertices") or currentBar.collidedWith(apple,"vertices"):
        game.drawText("Hit",game.width / 2,game.height / 2, Font(red,80,black))

            
    game.update(30)
game.quit()
