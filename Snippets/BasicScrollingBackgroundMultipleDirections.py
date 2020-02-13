import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(800,800,"Scrolling Background")

bk = Image("images\\grid.png",game)
bk.resizeTo(game.width,game.height)

game.setBackground(bk)
game.collisionBorder = "rectangle"

while not game.over:
    game.processInput()

    game.scrollBackground("still")
    if keys.Pressed[K_LEFT]:
        game.scrollBackground("right",4)
    if keys.Pressed[K_RIGHT]:
        game.scrollBackground("left",4)
    if keys.Pressed[K_UP]:
        game.scrollBackground("down",4)
    if keys.Pressed[K_DOWN]:
        game.scrollBackground("up",4)
    for x in range(3):
        game.drawText(str(game.backgroundXY[x]),5,5 + x * 15,Font(black))
        
    game.update(60)
game.quit()

    
