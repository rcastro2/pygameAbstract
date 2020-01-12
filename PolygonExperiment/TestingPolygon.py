import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''

from gamelib import *

game = Game(1400,700,"Shapes")

triangle = Polygon(3,30,game,red)

shapes = []
for index in range(20):
    r,g,b = randint(0,255),randint(0,255),randint(0,255)
    side = randint(4,8)
    size = randint(10,30)
    s = Polygon(side,size,game,(r,g,b))
    shapes.append( s )

for index in range(len(shapes)):
    x,y = randint(100,1300), randint(100,600)
    shapes[index].moveTo(x,y)
    s,a = randint(2,6), randint(0,360)
    shapes[index].setSpeed( s, a)

while not game.over:
    game.processInput()

    game.clearBackground(white)

    triangle.move()
    for index in range(len(shapes)):
        shapes[index].move(True)
        if shapes[index].collidedWith(triangle):
                shapes[index].visible = False
      
    if keys.Pressed[K_LEFT]:
        triangle.rotateBy(4)
    elif keys.Pressed[K_RIGHT]:
        triangle.rotateBy(-4)

    if keys.Pressed[K_UP]:
        triangle.forward(4)
    else:
        triangle.stop()
    
    game.update(60)




    
game.quit()

