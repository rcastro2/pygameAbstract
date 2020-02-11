import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(400,200,"Fighter")
bk = Image("images//bridge.gif",game)

chunliwalk = Animation("images//chunli//chun_lee_walk ",12,game)
chunliultra = Animation("images//chunli//chun_lee_explosion ",34,game)
chunlikick = Animation("images//chunli//vslightningkick ",42,game)
chunliwalk.moveTo(300,150)
chunliwalk.stop()


while not game.over:
    game.processInput()

    bk.draw()
    if keys.Pressed[K_LEFT]:
        chunliwalk.nextFrame()
        chunliwalk.x -= 8
    elif keys.Pressed[K_RIGHT]:
        chunliwalk.prevFrame()
        chunliwalk.x += 8
    elif keys.Pressed[K_e]:
        chunliultra.moveTo(chunliwalk.x - 20,chunliwalk.y - 50)
        chunliultra.draw()
    elif keys.Pressed[K_k]:
        chunlikick.moveTo(chunliwalk.x - 15,chunliwalk.y - 15)
        chunlikick.draw()
    else:
        chunliwalk.draw()

    game.update(16)
game.quit()


