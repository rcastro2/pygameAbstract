import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''

from gamelib import *

game = Game(700,700,"Click and Drag")

triangle = Shape("polygon",game,3,30,cyan)

pentagon = Shape("polygon",game,5,20,magenta)

ellipse1 = Shape("ellipse",game,100,40,orange)

ellipse2 = Shape("ellipse",game,40,100,green)

bar1 = Shape("bar",game,100,20,black)

bar2 = Shape("bar",game,20, 100, pink)

rectangle1 = Shape("rectangle",game,200,50,blue)

rectangle2 = Shape("rectangle",game,50,200,gray)

zombie = Image("images\\zombie.png",game)
zombie.resizeBy(-85)
hero = Animation("images\\glitch_walker.png",16,game,832/8,228/2,frate=2)

objects = [zombie,hero,triangle,pentagon,ellipse1,ellipse2,bar1,bar2,rectangle1,rectangle2]

for index in range(len(objects)):
    x,y = randint(100,600), randint(100,600)
    objects[index].moveTo(x,y)

current_object = None
while not game.over:
    game.processInput()

    game.clearBackground(white)

    if current_object:
        current_object.moveTo(mouse.x, mouse.y)
        
    if not mouse.LeftButton:
        current_object = None
        
    for index in range(len(objects)):
        objects[index].draw()
        if mouse.collidedWith(objects[index],"rectangle") and mouse.LeftClick:
            current_object = objects[index]
    
    game.update(30)
    
game.quit()

