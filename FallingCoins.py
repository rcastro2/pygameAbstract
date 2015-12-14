from gamelib import *

game = Game(800,600,"Falling Coins")

#Animation via a collection of images
bk = Animation("images\\field\\field ",5,game,frate=3)

#Animation via a spritesheet
one_ring = Animation("images\\ring.png",10,game,70,90,2)
#Look at the init definition for Animation to learn more about the parameters


#Create an empty array
rings = []
#Fill the array.  40 represents how many items we will put in the array
for index in range(40):
    #Append a new ring animation to the array
    rings.append(Animation("images\\ring.png",10,game,70,90,2))
    
    #Lets position each ring to a random location off the top of the screen
    x = randint(0,game.width)
    y = -randint(0,game.height)
    rings[index].moveTo(x,y) #rings[index] is how you access a ring from rings
    #Because we want the rings to move we must set the speed
    speed = randint(2,6) #Might as well let it be a random speed
    rings[index].setSpeed(speed,180)
    

while not game.over:
    game.processInput()
    bk.draw() #Demonstrate drawing an animation; Collection of Images
    one_ring.draw() #Demonstrate drawing an animatino; Spritesheet
    #Notice how the syntax is the same as an Image.  That was done purposely

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
