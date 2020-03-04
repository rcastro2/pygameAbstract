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

hero = Animation("images\\herostanding.png",5,game,960/5,128,frate=4)
hero_standing = Animation("images\\herostanding.png",5,game,960/5,128)
hero_walking = Animation("images\\herowalking.png",12,game,960/5,384/3)
hero_slashing = Animation("images\\SlashSprite.png",12,game,1875/5,750/3)
hero_slashing.resizeBy(-48)
hero.collisionBorder = "rectangle"

while not game.over:
    game.processInput()

    game.clearBackground(white)
    hero.draw()
    if keys.Pressed[K_RIGHT]:
        hero.images = hero_walking.images
        hero.x += 2
        hero.offsetX = -25
        hero.flipV = False
    elif keys.Pressed[K_LEFT]:
        hero.flipV = True
        hero.images = hero_walking.images
        hero.x -= 2
        hero.offsetX = -75
    elif keys.Pressed[K_SPACE]:
        hero.images = hero_slashing.images
        hero.offsetX = -50
    else:
        hero.images = hero_standing.images
        if hero.flipV:
            hero.offsetX = -100
        else:
            hero.offsetX = 0      


    game.update(30)
game.quit()
