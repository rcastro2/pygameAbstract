import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
Above two lines of code are a hack inorder to keep gamelib in a common
location where I can update it for all games.  If you copy gamelib.py into
the same folder as the game then you don't need these lines and can simply
delete them.
'''

from gamelib import *

###########################
def drawScore():
    x = game.width / 2
    for d in str(game.score):
        numbers[int(d)].moveTo(x,50)
        numbers[int(d)].draw()
        x += numbers[int(d)].width
        
#####################
def intro():
    titleA = Image("images\\title1a.png",game)
    titleA.moveY(-110)
    titleB = Image("images\\title1b.png",game)
    titleB.moveY(-10)

    platforms[0].moveY(150)
    hero.moveTo(platforms[0].x,platforms[0].y-platforms[0].height/2-hero.height/2 + 18)

    platforms[0].setSpeed(6,90)

    hsemblem.moveTo(game.width - hsemblem.width / 2 - 40, game.height - hsemblem.height / 2 - 40)
    infoemblem.moveTo(infoemblem.width / 2 + 40, game.height - infoemblem.height / 2 - 40)
    game.time = 1
    while not game.over:
        game.processInput()

        game.scrollBackground("left",2)
        titleA.draw()
        titleB.draw()
        hsemblem.draw()
        infoemblem.draw()
        
        
        if game.time <= 0:
            game.drawText("Press [SPACE] to Start",game.width/2-175,game.height / 2 + 30,Font(black,32,red,'mael.ttf'))
            if keys.Pressed[K_SPACE]:
                game.over = True
                
        platforms[0].move(True)
        hero.moveTo(platforms[0].x,platforms[0].y-platforms[0].height/2-hero.height/2 + 20)
        c = red
        if pointer.collidedWith(hsemblem) and mouse.LeftButton:
            displayHighScore()
        elif pointer.collidedWith(hsemblem):
            c = yellow
        game.drawText("High Score",game.width - hsemblem.width / 2 - 95, game.height - hsemblem.height / 2 + 10 ,Font(black,20,c,'mael.ttf'))
        
        c = red
        if pointer.collidedWith(infoemblem) and mouse.LeftButton:
            about()
        elif pointer.collidedWith(infoemblem):
            c = yellow
        game.drawText("About",infoemblem.width / 2 + 15, game.height - infoemblem.height / 2 + 10 ,Font(black,20,c,'mael.ttf'))
        
        pointer.moveTo(mouse.x + pointer.width /2 - 10,mouse.y + pointer.height/2 - 10)
        game.update(30)
        
    game.over = False
###########################
def newHighScore():
    nhstitle = Image("images\\newhighscore.png",game)
    nhstitle.y = 50
    global last
    while not game.over:
        game.processInput()

        game.scrollBackground("left",1)

 
        game.drawText("Press [ESC] to Quit",game.width/2-175,game.height * .75,Font(black,32,red,'mael.ttf'))
        
        nhstitle.draw()
        
        if keys.Pressed[K_ESCAPE]:
            game.over = True

        game.update(30)
    game.over = False
###########################
def displayHighScore():
    hstitle = Image("images\\highscore.png",game)
    hstitle.y = 50
    global last
    game.time = 2
    while not game.over:
        game.processInput()

        game.scrollBackground("left",1)
        hstitle.draw()

        if game.time <= 0:
            c = red
            if pointer.collidedWith(returnemblem) and mouse.LeftButton:
                game.over = True
            elif pointer.collidedWith(returnemblem):
                c = yellow
            game.drawText("Return",game.width /2 - returnemblem.width / 2 + 15, game.height - returnemblem.height / 2 + 10 ,Font(black,20,c,'mael.ttf'))
            returnemblem.draw()
        
        pointer.moveTo(mouse.x + pointer.width /2 - 10,mouse.y + pointer.height/2 - 10)
        
        if keys.Pressed[K_ESCAPE]:
            game.over = True

        game.update(30)
    game.over = False
###########################
def about():
    abouttitle = Image("images\\about.png",game)
    abouttitle.y = 50
    global last
    game.time = 1
    while not game.over:
        game.processInput()

        game.scrollBackground("left",1)

        abouttitle.draw()
        
        if game.time <= 0:
            c = red
            if pointer.collidedWith(returnemblem) and mouse.LeftButton:
                game.over = True
            elif pointer.collidedWith(returnemblem):
                c = yellow
            game.drawText("Return",game.width / 2 - returnemblem.width / 2 + 15, game.height - returnemblem.height / 2 + 10 ,Font(black,20,c,'mael.ttf'))
            returnemblem.draw()
        
        pointer.moveTo(mouse.x + pointer.width /2 - 10,mouse.y + pointer.height/2 - 10)
        textFont = Font(black,24,red,'mael.ttf')
        game.drawText("Help Glitch escape the volcano by jumping across",100,120,textFont)
        game.drawText("the floating platforms to the teleportation rune.",100,160,textFont)
        game.drawText("Be wary of the various perils that challenge your escape.",100,200,textFont)
        game.drawText("Use the arrow keys to move and the spacebar to jump",100,240,textFont)

        if keys.Pressed[K_ESCAPE]:
            game.over = True

        game.update(30)
    game.over = False
###########################
def levelOne():
    jumping = False
    factor = 1
    landed = False
    currentrocklanded = -1
    challengeSpeed = 2
    global last
    fire.moveTo(randint(50,game.width-50),-fire.height)
    fire.speed = randint(4,8)

    #Start Game
    while not game.over:
        game.processInput()

        game.scrollBackground("left",1)
        drawScore()
              
        for obj in world:
            obj.x -= challengeSpeed
          
        onrock = False
        for index, platform in enumerate(platforms):
            platform.draw()
            #Recycle platforms
            if platform.isOffScreen("left"):
                platform.moveTo(platforms[last].x + platforms[last].width + 150,randint(200,300))
                last = index
            #Check if hero is on a rock
            if hero.collidedWith(platform,"rectangle") and hero.bottom < platform.top + 15 and hero.x > platform.left and hero.x < platform.right: 
                onrock = True
                if not landed and currentrocklanded != index:
                    game.score += 1
                    landed = True
                    currentrocklanded = index
                    
        if game.score >=1 :   
            fire.y += fire.speed
            fire.draw(False)
            if fire.isOffScreen("bottom") or not fire.visible:
                fire.moveTo(randint(50,game.width-50),-fire.height)
                fire.speed = randint(4,10)
                fire.visible = True
          
        #Jumping Logic
        if jumping:
            hero.y -= 18 * factor
            factor *= .95
            landed = False
            if factor < .18:
                jumping = False
                factor = 1
        if keys.Pressed[K_SPACE] and onrock and not jumping:
            jumping = True
            
        if not onrock:
            hero.y += 5
            
        #Prevent hero going off left side of the screen
        if hero.left <= game.left:
            hero.x = hero.width / 2
     
        if keys.Pressed[K_RIGHT]:
            hero.x += 4
            hero.nextFrame()
        elif keys.Pressed[K_LEFT]:
            hero.x -= 4
            hero.prevFrame()
        else:
            hero.draw()

        if hero.isOffScreen("bottom"):
            game.over = True
              
        game.update(30)

#####################
def gameover():
    endtitle = Image("images\\tgameover.png",game)
    game.over = False
    global last
    while not game.over:
        game.processInput()

        game.scrollBackground("left",1)
        for obj in world:
            obj.x -= 2

        for index, platform in enumerate(platforms):
            platform.draw()
            #Recycle platforms
            if platform.isOffScreen("left"):
                platform.moveTo(platforms[last].x + platforms[last].width + 150,randint(200,300))
                last = index
 
        game.drawText("Press [ESC] to Quit",game.width/2-175,game.height * .75,Font(black,32,red,'mael.ttf'))
        
        endtitle.draw()
        
        if keys.Pressed[K_ESCAPE]:
            game.over = True

        game.update(30)
        
#####################
game = Game(1008,440,"Glitch - The Lava Jumper")

platforms = []
size = 20
last = size -1

#Load  objects
bk = Image("images\\lavabk2.jpg",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)

hsemblem = Image("images\\highscoreemblem.png",game)
hsemblem.resizeBy(-60)
infoemblem = Image("images\\infoemblem.png",game)
infoemblem.resizeBy(-60)
returnemblem = Image("images\\return3.png",game)
returnemblem.resizeBy(-60)
returnemblem.y = game.height  - returnemblem.height / 2 - 40

pointer = Image("images\\pointer1.png",game)
pointer.resizeBy(-80)
mouse.visible = False

for times in range(size):
    f = randint(1,3)
    platforms.append(Image("images\\platform" + str(f) + ".png",game))

hero = Animation("images\\glitch_walker.png",16,game,832/8,228/2,5)
hero.stop()

numbers = []
for n in range(10):
    numbers.append(Image("images\\t" + str(n) + ".png",game))

fire = Animation("images\\fire.png",20,game,960/5,768/4,3)
    
#Play Intro
intro()

#Position objects
platforms[0].moveTo(game.width/2,randint(200,300))
for index in range(1,size):
    platforms[index].moveTo(platforms[index-1].x + platforms[index-1].width + 150,randint(200,300))

hero.moveTo(platforms[0].x,platforms[0].y-platforms[0].height/2-hero.height)

world = [hero]
world.extend(platforms)

#Play Game
levelOne()

gameover()

game.quit()




