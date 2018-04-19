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

player = Image("images\\greenCircle.png",game)
player.resizeBy(-85)

floor = Animation("images\\bar.png",3,game,700,110,frate=3)
floor.resizeTo(game.width,floor.height)
floor.moveTo(game.width/2,game.height-50)

jumping = False
landed = False
factor = 1
while not game.over:
    game.processInput()
    game.clearBackground(white)

    player.draw()
    floor.draw()
    if jumping:
        jumping = True
        landed = False
        player.y -= 12 * factor
        factor *= .96
        if factor < 0.05:
            jumping = False
            factor = 1

    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping = True
            
    if not player.collidedWith(floor,"rectangle"):
        player.y += 2
    if player.collidedWith(floor,"rectangle"):
        landed = True
    
    game.update(60)
game.quit()
