import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(600,800,"Falling Through Gaps",60)
bk  = Image("images\\dirt.jpg",game)
alien = Image("images\\alien2.gif",game)
alien.y = 100
alien.vx = 4
alien.collisionBorder = "rectangle"

gravity = 4

bars = []
intervals = (game.width - 200) / 10
for i in range(8):
    gap = randint(0,intervals) * 10 + 100
    barR = Animation(r"images\bar.png",3,game,700,110,4)
    barR.y = game.height / 2 + i * 100
    barR.x = gap - 250
    barR.resizeTo(450,30)
    barR.vy = 2
    bars.append(barR)
    barL = Animation(r"images\bar.png",3,game,700,110,4)
    barL.y = game.height / 2 + i * 100
    barL.x = gap + 250
    barL.resizeTo(450,30)
    barL.vy = 2
    bars.append(barL)

while not game.over:
    game.processInput()

    bk.draw()
    alien.draw()

    onbar = False
    for bar in bars:
        bar.draw()
        bar.y -= bar.vy
        if alien.collidedWith(bar,"rectangle"):
            onbar = True
        if bar.y < 0:
            bar.y = game.height
            
        
    if alien.bottom < game.height and not onbar:
        alien.y += gravity
    elif onbar:
        alien.y -= bars[0].vy

    if keys.Pressed[K_LEFT] and onbar:
        alien.x -= alien.vx
    if keys.Pressed[K_RIGHT] and onbar:
        alien.x += alien.vx
            
    game.update(30)
game.quit()
