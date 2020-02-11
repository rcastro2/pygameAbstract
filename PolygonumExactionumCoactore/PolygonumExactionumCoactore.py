import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''

from gamelib import *

game = Game(1400,700,"Polygonum Exactionum Coactore",50)

triangle = Shape("polygon",game,3,30,red)
triangle.x = game.width - triangle.width - 50
ellipse1 = Shape("ellipse",game,100,40)
ellipse1.dw = -8
ellipse2 = Shape("ellipse",game,40,100)
ellipse2.dh = -8
health = Shape("bar",game,200,20,orange)
health.moveTo(10,10)
progress = Shape("bar",game,0, 20, pink)
progress.moveTo(10,40)
timebar = Shape("bar",game,0, 20, blue)
timebar.moveTo(10,70)
graybar = Shape("bar",game,200,20,gray)

shapes = []
for index in range(20):
    r,g,b = randint(0,255),randint(0,255),randint(0,255)
    side = randint(4,8)
    size = randint(10,30)
    s = Shape("polygon",game,side,size,(r,g,b))
    shapes.append( s )

for index in range(len(shapes)):
    x,y = randint(100,1300), randint(100,600)
    shapes[index].moveTo(x,y)
    s,a = randint(2,6), randint(0,360)
    shapes[index].setSpeed( s, a)

while not game.over:
    game.processInput()

    game.clearBackground(white)

    graybar.moveTo(health.x, health.y)
    health.draw()
    graybar.moveTo(progress.x, progress.y)
    progress.draw()
    graybar.moveTo(timebar.x, timebar.y)
    timebar.draw()
    timebar.width = game.time * 4

    ellipse1.draw()
    ellipse1.width += ellipse1.dw
    if ellipse1.width < 10 or ellipse1.width > game.width * 0.75: ellipse1.dw = -ellipse1.dw

    ellipse2.draw()
    ellipse2.height += ellipse2.dh
    if ellipse2.height < 10 or ellipse2.height > game.height * 0.75: ellipse2.dh = -ellipse2.dh

    triangle.move()
    pygame.draw.line(game.screen,black,triangle.points[0],triangle.points[1],4)
    pygame.draw.line(game.screen,black,triangle.points[1],triangle.points[2],4)
    
    
    for index in range(len(shapes)):
        shapes[index].move(True)
        if shapes[index].collidedWith(triangle):
                shapes[index].visible = False
                progress.width += 10
    if triangle.collidedWith(ellipse1,"rectangle") or triangle.collidedWith(ellipse2,"rectangle"):
        health.width -= 1

    if health.width <= 0 or progress.width == 200 or game.time <= 0:
        game.over = True
    
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

