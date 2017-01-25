import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated it for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(800,600,"Falling Coins")

bk = Animation("images\\field_5.png",5,game,1000,1000,frate=3)

#Create an empty array
rings = []
#Fill the array.  40 represents how many items we will put in the array
for index in range(40):
    #Append a new ring animation to the array
    rings.append(Animation("images\\ring.png",10,game,70,90,2))
    
    #Lets position each ring to a random location off the top of the screen
    x = randint(0,game.width)
    y = -randint(0,game.height)
    rings[index].moveTo(x,y) #index represents the position of the ring we just appended to the list

    #Because we want the rings to move we must set the speed
    speed = randint(2,6) #Might as well let it be a random speed
    rings[index].setSpeed(speed,180)
    
while not game.over:
    game.processInput()
    bk.draw() #Demonstrate drawing an animation; Collection of Images

    for ring in rings: #Traverse each ring in rings
        ring.move(False)
        #Once a ring moves off the bottom of the screen lets "recycle" them back to the top
        #To the player it will appear as though there is an endless stream of rings falling.
        if ring.isOffScreen("bottom"):
            x = randint(0,game.width)
            y = -randint(0,game.height)
            ring.moveTo(x,y)
        
    game.update(60)
game.quit()
