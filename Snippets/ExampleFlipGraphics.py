import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(800,600,"Game",60)

zombie = Image("images\\zombie.png",game)
zombie.resizeBy(-80)
hero = Animation("images\\glitch_walker.png",16,game,832/8,228/2)

while not game.over:
    game.processInput()

    game.clearBackground(white)
    zombie.draw()
    hero.draw()
    if keys.Pressed[K_LEFT]:
        hero.flipV = True
        zombie.flipV = False
        zombie.x -= 2
    if keys.Pressed[K_RIGHT]:
        hero.flipV = False
        zombie.flipV = True
        zombie.x += 2
    if keys.Pressed[K_UP]:
        zombie.rotateBy(2)

    game.update(30)
game.quit()
