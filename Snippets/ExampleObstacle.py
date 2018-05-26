import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(640,480,"Obstacle",60)
bk  = Image("images\\dirt.jpg",game)
alien = Image("images\\alien2.gif",game)
apples = []
for i in range(20):
    apples.append(Image("images\\apple.png",game))

for apple in apples: 
    apple.resizeBy(-90)
    apple.moveTo(randint(apple.width,game.width-apple.width),randint(apple.height,game.height-apple.height))
    apple.collisionBorder = "rectangle"
    
alien.collisionBorder = "rectangle"

while not game.over:
    game.processInput()

    bk.draw()
    alien.draw()
    if keys.Pressed[K_LEFT]:
        alien.x -= 2
    if keys.Pressed[K_RIGHT]:
        alien.x += 2
    if keys.Pressed[K_UP]:
        alien.y -= 2
    if keys.Pressed[K_DOWN]:
        alien.y += 2

    for apple in apples:
        apple.draw()
        if keys.Pressed[K_LEFT] and alien.collidedWith(apple,"rectangle") and alien.x > apple.x and alien.left < apple.right and alien.bottom > apple.top and alien.top < apple.bottom:
                alien.x += 2
        if keys.Pressed[K_RIGHT] and alien.collidedWith(apple,"rectangle") and alien.x < apple.x and alien.right > apple.left and alien.bottom > apple.top and alien.top < apple.bottom:
                alien.x -= 2     
        if keys.Pressed[K_UP] and alien.collidedWith(apple,"rectangle") and alien.y > apple.y and alien.top < apple.bottom and alien.left < apple.right and alien.right > apple.left:
                alien.y += 2
        if keys.Pressed[K_DOWN] and alien.collidedWith(apple,"rectangle") and alien.y < apple.y and alien.bottom > apple.top and alien.left < apple.right and alien.right > apple.left:
                alien.y -= 2
            
    game.update(30)
game.quit()
