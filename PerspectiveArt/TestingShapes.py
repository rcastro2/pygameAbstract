import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''
from gamelib import *

game = Game(1000,700,"Perspective Art")
box = [(200,400),(200,300),(100,300),(100,400)]
triangle = [(500,600),(600,600),(550,500)]
idk = [(400,250),(500,150),(450,100),(300,150)]

shapes = [box,triangle,idk]

point = (0,0)

def drawLine(sp,ep,color=black,width=1):
    pygame.draw.line(game.screen,color, sp, ep,width)

def drawFace(vertices):
  for i in range(len(vertices)+1):
    drawLine(vertices[i%len(vertices)],vertices[(i+1)%len(vertices)],width=2)

def drawEdge(shape1,shape2):
  for v1,v2 in zip(shape1,shape2):
    drawLine(v1,v2,width=2)

def drawShape(shape1,perspective_lines=False):
  shape2 = []
  drawFace(shape1)
  for v in shape1:
    nx = (v[0] - point[0]) * 0.2 + v[0]
    ny = (v[1] - point[1]) * 0.2 + v[1]
    shape2.append((nx,ny))
  drawFace(shape2)
  if perspective_lines:
    for v in shape2:
      drawLine(v,point,light_gray)
  drawEdge(shape1,shape2)


while not game.over:
  game.processInput()
  game.clearBackground(white)

  point = (mouse.x,mouse.y)

  for shape in shapes:
    drawShape(shape,True)

  if mouse.LeftClick:
    length = randint(50,100)
    x = mouse.x
    y = mouse.y
    new_box = [(x,y),(x+length,y),(x+length,y+length),(x,y+length)]
    shapes.append(new_box)

  if keys.Pressed[K_SPACE]:
    shapes = [box,triangle,idk]
    
  game.drawText("Move the vanishing point with the mouse",10,10,Font(red,20,black,"Comic Sans MS"))
  game.drawText("Left click to add a box to the perspective at the mouse location",10,40,Font(red,20,black,"Comic Sans MS"))
  game.drawText("Press [SPACE] to restore the original three objects",10,70,Font(red,20,black,"Comic Sans MS"))
  game.update(20)
game.quit()


