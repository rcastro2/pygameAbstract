import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(640,480,"Move and Rotate Towards")

bk = Image("images\\day.png",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)

bird = Animation("images\\bird.png",3,game,44,34,frate=6)

ring = Animation("images\\ring2.png",64,game,64,64)
ring.moveTo(35,430)

scoreFont = Font(black,36)

while not game.over:
    game.processInput()
    game.drawBackground()

    ring.moveTo(mouse.x,mouse.y)

    bird.rotateTowards(ring)

    bird.moveTowards(ring,2)
    
    game.update(30)

game.drawText("Press [Enter] to Exit.",200,400, Font(black,40,green))
game.update()
game.wait(K_RETURN)
game.quit()

