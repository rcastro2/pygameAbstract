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

while not game.over:
    game.processInput()

    game.drawBackground()
    if keys.Pressed[K_LEFT]:
        game.scrollBackground("left",8)
    if keys.Pressed[K_RIGHT]:
        game.scrollBackground("right",8)
    if keys.Pressed[K_UP]:
        game.scrollBackground("down",8)
    if keys.Pressed[K_DOWN]:
        game.scrollBackground("up",8)
        
    game.update(30)
game.quit()

    
