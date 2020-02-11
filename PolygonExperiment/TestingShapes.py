import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''

from gamelib import *

game = Game(1400,700,"Testing Shapes",50)

triangle = Shape("polygon",game,3,30,cyan)

pentagon = Shape("polygon",game,5,20,magenta)

ellipse1 = Shape("ellipse",game,100,40,orange)

ellipse2 = Shape("ellipse",game,40,100,green)

bar1 = Shape("bar",game,100,20,black)

bar2 = Shape("bar",game,20, 100, pink)

rectangle1 = Shape("rectangle",game,200,50,blue)

rectangle2 = Shape("rectangle",game,50,200,gray)

box = Shape("bar",game,300,175,white)
box.moveTo(0,0)

shapes = [triangle,pentagon,ellipse1,ellipse2,bar1,bar2,rectangle1,rectangle2]
shapes_names = ["Triangle","Magenta Pentagon","Orange Ellipse","Green Ellipse","Black Bar","Pink Bar","Blue Rectangle", "Gray Rectangle"]

for index in range(len(shapes)):
    x,y = randint(100,1300), randint(100,600)
    shapes[index].moveTo(x,y)

current = 0
while not game.over:
    game.processInput()

    game.clearBackground(white)
    box.draw()
   
    for index in range(len(shapes)):
        shapes[index].move()
    if keys.Down and 48 < keys.Down < 57:
        current = keys.Down - 49

    if current != None and 0 <= current <= len(shapes_names)-1:
        v = "Visible" if shapes[current].visible else "Hidden"
        game.drawText("Shape " + str(current+1) + " ( " + v + " ): " + shapes_names[current],10,10,Font(red,24,black))
        if shapes[current].shape in ["polygon","rectangle"]:
            game.drawText("Controls:",10,40,Font(red,24,black))
            game.drawText("     Left - Rotate Left",10,70,Font(red,24,black))
            game.drawText("     Right - Rotate Right",10,100,Font(red,24,black))
            game.drawText("     Up - Forward",10,130,Font(red,24,black))
        else:
            game.drawText("Controls:",10,40,Font(red,24,black))
            game.drawText("Use arrows to move in that direction",10,70,Font(red,24,black))    
        
    if shapes[current].shape in ["polygon","rectangle"]:
        if keys.Pressed[K_LEFT]:
            shapes[current].rotateBy(4)
        elif keys.Pressed[K_RIGHT]:
            shapes[current].rotateBy(-4)

        if keys.Pressed[K_UP]:
            shapes[current].forward(4)
        else:
            shapes[current].stop(10)
    else:
        if keys.Pressed[K_LEFT]:
            shapes[current].x -= 4
        if keys.Pressed[K_RIGHT]:
            shapes[current].x += 4
        if keys.Pressed[K_UP]:
            shapes[current].y -= 4
        if keys.Pressed[K_DOWN]:
            shapes[current].y += 4
            
    if keys.Pressed[K_SPACE]:
        shapes[current].visible = False
    elif keys.Pressed[K_RETURN]:
        shapes[current].visible = True
        
    
    game.update(60)
    
game.quit()

