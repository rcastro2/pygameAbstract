import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated it for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(800,600,"Scrolling Background")

bk = Image("images\\day.png",game)
bk.resizeTo(game.width,game.height)

game.setBackground(bk)

while not game.over:
    game.processInput()

    game.scrollBackground("left",1)

    game.update(60)
game.quit()

    
