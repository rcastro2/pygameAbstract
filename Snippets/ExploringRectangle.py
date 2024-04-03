import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''

from gamelib import *
    
game = Game(800,700,"Shapes",50)
cx = game.width / 2
cy = game.height / 2

def drawPolarAxis():
    for index in range(4):
        x = cx + 300 * math.cos(math.pi / 2 * index)
        y = cy + 300 * math.sin(math.pi / 2 * index)
        pygame.draw.line(game.screen,black,(cx,cy),(x,y),2)
        game.drawText(str(int(math.degrees(math.pi / 2 * index))) + " degree", x,y, Font(black,24))

w, h = 100, 100
size = math.sqrt(w**2 + h**2)/2
a1 = math.atan(w/h)
a2 = math.atan(h/w)
ra1 = math.pi - 2*a1
ra2 = math.pi - 2*a2
ra = [ra1/2,ra2,ra1,ra2]
rt = [0,0,0,0]

c = [red,yellow,green,pink]


rotation = 0
da = math.pi / 360
while not game.over:
    game.processInput()

    game.clearBackground(white)

    theta = 0
    for index in range(4):
        theta += ra[index]
        rt[index] = (cx + size * math.cos(theta + rotation), cy + size * math.sin(theta + rotation))
        x = cx + (size + 50) * math.cos(theta + rotation)
        y = cy + (size + 50) * math.sin(theta + rotation)
        pygame.draw.line(game.screen,black,(cx,cy),(x,y),2)
        game.drawText(str(int(math.degrees(theta + rotation))) + " degree", x,y, Font(blue,26,white))

    pygame.draw.polygon(game.screen,blue,rt)
    for index in range(4):
        pygame.draw.circle(game.screen,c[index],(int(rt[index][0]),int(rt[index][1])),10)
        game.drawText((int(rt[index][0]),int(rt[index][1])),int(rt[index][0]),int(rt[index][1]),Font(black,24))

    drawPolarAxis()
      
    if keys.Pressed[K_LEFT]:
        rotation -= da
    elif keys.Pressed[K_RIGHT]:
        rotation += da

    if keys.Pressed[K_a]:
        w += 1
    elif keys.Pressed[K_d]:
        w -= 1
    if keys.Pressed[K_w]:
        h += 1
    elif keys.Pressed[K_s]:
        h -= 1

    size = math.sqrt(w**2 + h**2)/2
    a1 = math.atan(w/h)
    a2 = math.atan(h/w)
    ra1 = math.pi - 2*a1
    ra2 = math.pi - 2*a2
    ra = [ra1/2,ra2,ra1,ra2]

    game.drawText("Reference Angle RA1: " + str(int(math.degrees(ra1))),5,5,Font(black,24))
    game.drawText("Reference Angle RA2: " + str(int(math.degrees(ra2))),5,25,Font(black,24))
    game.drawText("Reference Angle A1: " + str(int(math.degrees(a1))),5,45,Font(black,24))
    game.drawText("Reference Angle A2: " + str(int(math.degrees(a2))),5,65,Font(black,24))
    game.drawText("Rotation Angle: " + str(int(math.degrees(rotation))),5,85,Font(black,24))
    
    game.update(60)
    
game.quit()

