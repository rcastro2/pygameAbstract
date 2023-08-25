from gamelib import *
import copy

game = Game(600,400,"SpongeBob Adventure")
game.status = "play"

def processIngredient(item):
  #Taking advantange that Python allows the following conditional instead of using "and"
  #print(krabbypatty)
  if item.name == krabbypatty["required"] == "bottombun":
    caught_bottombun = Image("bottombun.png",game)
    caught_bottombun.resizeBy(-88)
    caught_bottombun.y = spongewalk.y - len(caught_ingredients) * 8
    caught_ingredients.append(caught_bottombun)
    krabbypatty["required"] = "lettuce"
  elif item.name == krabbypatty["required"] == "lettuce":
    caught_lettuce = Image("lettuce.png",game)
    caught_lettuce.resizeBy(-88)
    caught_lettuce.y = spongewalk.y - len(caught_ingredients) * 8
    caught_ingredients.append(caught_lettuce)
    krabbypatty["required"] = "patty"
  elif item.name == krabbypatty["required"] == "patty":
    caught_patty = Image("patty.png",game)
    caught_patty.resizeBy(-81)
    caught_patty.y = spongewalk.y - len(caught_ingredients) * 8
    caught_ingredients.append(caught_patty)
    krabbypatty["required"] = "cheese"
  elif item.name == krabbypatty["required"] == "cheese":
    caught_cheese = Image("cheese.png",game)
    caught_cheese.resizeBy(-90)
    caught_cheese.y = spongewalk.y - len(caught_ingredients) * 8
    caught_ingredients.append(caught_cheese)
    krabbypatty["required"] = "tomato"
  elif item.name == krabbypatty["required"] == "tomato":
    caught_tomato = Image("tomato.png",game)
    caught_tomato.resizeBy(-90)
    caught_tomato.y = spongewalk.y - len(caught_ingredients) * 8
    caught_ingredients.append(caught_tomato)
    krabbypatty["required"] = "topbun"
  elif item.name == krabbypatty["required"] == "topbun":
    caught_topbun = Image("topbun.png",game)
    caught_topbun.resizeBy(-88)
    caught_topbun.y = spongewalk.y - len(caught_ingredients) * 8
    caught_ingredients.append(caught_topbun)
    krabbypatty["required"] = ""

ingredients = [] #Provide the ability to random selects ingredients to drop
caught_ingredients = []
krabbypatty = {}
krabbypatty["required"] = "bottombun"

topbun = Image("topbun.png",game)
topbun.name = "topbun"
topbun.resizeBy(-88)
ingredients.append( topbun )

lettuce = Image("lettuce.png",game)
lettuce.name = "lettuce"
lettuce.resizeBy(-88)
ingredients.append(lettuce)

tomato = Image("tomato.png",game)
tomato.name = "tomato"
tomato.resizeBy(-90)
ingredients.append(tomato)

cheese = Image("cheese.png",game)
cheese.name = "cheese"
cheese.resizeBy(-90)
ingredients.append(cheese)

patty = Image("patty.png",game)
patty.name = "patty"
patty.resizeBy(-81)
ingredients.append(patty)

bottombun = Image("bottombun.png",game)
bottombun.name = "bottombun"
bottombun.resizeBy(-85)
ingredients.append(bottombun)

krustykrabBK = Image("krustykrabBK.jpg",game)
krustykrabBK.resizeTo(game.width, game.height)

spongewalk = Animation("spongewalk3.png",13,game,1700/13,124)
spongewalk.resizeBy(-20)
spongewalk.stop()
spongewalk.y = game.height - 60

krabbycar = Image("krabbycar.png",game)
krabbycar.resizeBy(-65)

squidward = Animation("squidWardSprite.png",7,game,418/5,305/2,2) 
squidward.resizeBy(-35)
squidward.moveTo(40,game.height/2)

jellyfishes = []
for i in range(40):
  jellyfish = Image("jellyfish.png",game)
  jellyfish.resizeBy(-90)
  x = randint(100, game.width - 100)
  y = randint(100, 4000)
  jellyfish.moveTo(x,-y)
  s = randint(2, 6)
  jellyfish.setSpeed(s,180)
  jellyfishes.append(jellyfish)
road = Image("road.png",game)
road.resizeTo(game.width,game.height)

krabbycar.healthBar = Shape("bar",game, krabbycar.health, 10, green)

poof = Animation("poofSprite.png",10, game, 608 / 5, 152 / 2, 2)
poof.resizeBy(-50)
poof.visible = False

mrspuff = Image("mrspuff.webp",game)
mrspuff.resizeBy(-65)
mrspuff.setSpeed(2,0)
mrspuff.x = randint(100, game.width - 100)
mrspuff.y = game.height + randint(100, 500)

logo = Image("SpongeBob_Logo.png",game)
logo.resizeBy(-70)
logo.y -= 100

titleBK = Image("titleBK.jpg",game)

playButton = Animation("playSpriteSheet.png",25,game,1700/5,1139/5)
playButton.resizeBy(-60)
playButton.y += 120

krustykrabicon = Image("krustykrabicon.png",game)
krustykrabicon.resizeBy(-20)
krustykrabicon.moveTo(game.width - 60, 3000)
krustykrabicon.setSpeed(2,0)
#Ideal ending y coordinate for Krusty Krab: game.height - 131

bikinibottom = Image("bikiniBottomBK.jpg",game)
bikinibottom.resizeTo(game.width, game.height)
spongesun = Animation("spongeSun.png",50,game,2560/5,26624/52)
spongesun.resizeBy(-30)
spongesun.moveTo(100,100)

intro_message1 = Image("introLevel1Message1.png",game)
intro_message1.resizeBy(-45)
intro_message1.y += 55
intro_message2 = Image("introLevel1Message2.png",game)
intro_message2.resizeBy(-45)
intro_message2.y += 60

#Start Screen
while not game.over:
  game.processInput()
  titleBK.draw()
  logo.draw()
  playButton.draw()

  if playButton.collidedWith(mouse) and mouse.LeftClick:
    game.over = True

  game.update(30)

#Level 1 - Intro Screen
t = 0
message = "first"
game.over = False
while not game.over:
  game.processInput()
  bikinibottom.draw()
  spongesun.draw()

  t += 1
  if message == "first" and t <= 200:
    if mouse.LeftClick or t == 200:
      message = "second"
    intro_message1.draw()
  elif message == "second" and t <= 500:
    if mouse.LeftClick or t == 500:
      game.over = True
    intro_message2.draw()

  game.update(30)

'''
Level 1 - Get to work
Spongebob must drive himself and Patrick to the Krusty Krab.  While driving Spongebob must,
1) Avoid the jellyfish as they destroy the car
2) Avoid Squidward because he will prevent you from moving
3) Avoid Mrs Puff because she will drag you backwards
'''

#Level 1 - Get to the Krusty Krab
game.over = False
game.setBackground(copy.copy(road))

while not game.over:
  game.processInput()
  if krustykrabicon.y > game.height - 131:
    game.scrollBackground("up",2)
    krustykrabicon.move()
  else:
    game.over = True
  krabbycar.draw()
  poof.draw(False)
  mrspuff.move()  
  
  if mrspuff.y < -100:
    mrspuff.x = randint(100, game.width - 100)
    mrspuff.y = game.height + randint(100, 500)

  if mrspuff.collidedWith(krabbycar):
    krabbycar.y -= 2
    
  for jellyfish in jellyfishes:
    jellyfish.move()
    if jellyfish.collidedWith(krabbycar):
      jellyfish.visible = False
      krabbycar.health -= 20
      poof.moveTo(jellyfish.x, jellyfish.y)
      poof.visible = True
      
  if krabbycar.health <= 0:
    game.over = True
    game.status = "loselevel1"
    
  squidward.flipV = True
  squidward.setSpeed(3,-90)
  squidward.move()
  if squidward.x > game.width:
    squidward.moveTo(40,randint(0,game.height))
    
  if not krabbycar.collidedWith(squidward,"rectangle"):    
    if keys.Pressed[K_LEFT]:
      krabbycar.x -= 5
    if keys.Pressed[K_RIGHT]:
      krabbycar.x += 5
    if keys.Pressed[K_DOWN]:
      krabbycar.y +=5
    if keys.Pressed[K_UP]:
      krabbycar.y -= 5

  krabbycar.healthBar.draw()
  krabbycar.healthBar.width = krabbycar.health
  krabbycar.healthBar.x = krabbycar.x - krabbycar.healthBar.width / 2
  krabbycar.healthBar.y = krabbycar.top - 20

  game.update(30)

#Level 2 Setup ===================================================
mrkrabs = Animation("krabSpriteSM.png",59,game,816/5,1958/12,2)
mrkrabs.moveTo(game.width - 100, game.height - 100)
mrkrabsMessage = Image("mrkrabsMessage.png",game)
mrkrabsMessage.resizeBy(-25)
mrkrabsMessage.y -= 50
mrkrabsMessage.x -= 50
mrkrabsMessage2 = Image("mrkrabsMessage2.png",game)
mrkrabsMessage2.resizeBy(-25)
mrkrabsMessage2.y -= 45
mrkrabsMessage2.x -= 50

patrick = Animation("patrickSprite.png", 6, game, 1460 / 5, 588 / 2, 3)
patrick.resizeBy(-55)
patrick.moveTo(50, game.height - 75)
patrick.flipV = True
patrickMessage = Image("patrickMessage.png",game)
patrickMessage.resizeBy(-40)
patrickMessage.x -= 90
patrick.visible = False

imhungry = Image("imhungry.png",game)
imhungry.resizeBy(-25)
imhungry.x = patrick.x + 100
imhungry.y += 20
imstarving = Image("imstarving.png",game)
imstarving.resizeBy(-25)
imstarving.x = patrick.x + 100
imstarving.y += 20
nevermind = Image("nevermind.png",game)
nevermind.resizeBy(-25)
nevermind.x = patrick.x + 100
nevermind.y += 20

plankton = Image("planktonTiny.png",game)
a = randint(0,7) * 45 + 30
plankton.setSpeed(3, a)

#Level 2 - Intro to Level 2
t = 0
message = "first"
game.over = False
while not game.over and game.status == "play":
  game.processInput()
  krustykrabBK.draw()
  patrick.draw()
  mrkrabs.draw()
  spongewalk.draw()
  
  t += 1
  if message == "first" and t <= 200:
    if mouse.LeftClick or t == 200:
      message = "second"
    mrkrabsMessage.draw()
  elif message == "second" and t <= 400:
    if mouse.LeftClick or t == 400:
      message = "three"
      patrick.visible = True
      mrkrabs.visible = False
    mrkrabsMessage2.draw()
  elif message == "three" and t <= 600:
    if mouse.LeftClick or t == 600:
      game.over = True
    patrickMessage.draw()
    
  game.update(30)

'''
Level 2 - Patrick is hungry
Spongebob must make Patrick Krabby Patties.  
1) Catch the ingredients for the Krabby Patty in the right order.
2) Avoid Plankton because he will prevent you from moving
'''

#Level 2 - Making three krabby patties for Patrick
game.over = False

def getIngredient():
  choice = randint(0,len(ingredients)-1)
  newIngredient = copy.copy(ingredients[choice])
  x = randint(100, game.width - 100)
  y = -randint(0, 500)
  newIngredient.moveTo(x,y)
  return newIngredient
  
activeIngredients = []
for i in range(6):
  activeIngredients.append(getIngredient())
t = 0
patrick.hamburgers = 0
while not game.over and game.status == "play":
  game.processInput()
  krustykrabBK.draw()
  patrick.draw()
  t += 1
  if 200 < t < 300:
    imhungry.draw()
  elif 550 < t < 650:
    imstarving.draw()
  elif 900 < t < 1000:
    nevermind.draw()
  elif t >= 1000:
    game.status = "loselevel2"
  lettuce.draw()
  tomato.draw()
  cheese.draw()
  topbun.draw()
  bottombun.draw()
  plankton.move(True)
  poof.draw(False)
  
  
  for i in range(len(activeIngredients)):
    activeIngredients[i].draw()
    activeIngredients[i].y += 5
    if activeIngredients[i].y > game.height - 50 and activeIngredients[i].visible:
      poof.visible = True
      poof.moveTo(activeIngredients[i].x, activeIngredients[i].y)
      activeIngredients[i] = getIngredient()
      
    if spongewalk.collidedWith(activeIngredients[i],"rectangle"):
      poof.visible = True
      poof.moveTo(activeIngredients[i].x, activeIngredients[i].y)
      processIngredient(activeIngredients[i])
      activeIngredients[i] = getIngredient()

  if not plankton.collidedWith(spongewalk,"rectangle"):    
    if keys.Pressed[K_LEFT]:
      spongewalk.x -= 10
      spongewalk.nextFrame() #allows you to pause the animation and have you control the frame
      if not spongewalk.flipV:
        spongewalk.flipV = True #flips the animation vertically 
    elif keys.Pressed[K_RIGHT]:
      spongewalk.x += 10
      spongewalk.nextFrame()
      if spongewalk.flipV:
        spongewalk.flipV = False
    else:
      spongewalk.draw()
  else:
    spongewalk.draw()

  if spongewalk.collidedWith(patrick,"rectangle") and len(caught_ingredients) == 6:
    print("Thank you Spongebob!")
    caught_ingredients = []
    t = 0
    patrick.hamburgers += 1
    krabbypatty["required"] = "bottombun"
   
  for item in caught_ingredients:
    item.x = spongewalk.x
    item.draw()
    
  if patrick.hamburgers == 3:
    game.over = True
    
  game.update(30)
  
game.over = False
bikinibottom = Image("bikinibottom.jpg",game)
bikinibottom.resizeTo(game.width,game.height)
spongeWin1 = Animation("spongeWinSprite.png",4,game,1250/5,333,3)
spongeWin1.resizeBy(-60)
spongeWin2 = Animation("spongebobWin2.png",41,game,2375/5,4320/9,3)
spongeWin2.resizeBy(-60)
spongeWin2.y += 100
spongeLoseLVL1 = Animation("spongebobLoseLevel1.png",12,game,2400/5,1440/3,3)
spongeLoseLVL1.resizeBy(-70)
spongeLoseLVL1.y += 100
spongeLoseLVL1.x += 50
spongeLoseLVL2 = Animation("spongebobLoseLevel2.png",12,game,2400/5,1440/3,3)
spongeLoseLVL2.resizeBy(-60)
spongeLoseLVL2.y += 75
spongeLoseLVL2.x += 100
level1LoseMessage = Image("level1LoseMessage.png",game)
level1LoseMessage.resizeBy(-20)
level1LoseMessage.x -= 150
level2LoseMessage = Image("level2LoseMessage.png",game)
level2LoseMessage.resizeBy(-30)
level2LoseMessage.y += 40
level2LoseMessage.x -= 85

youwin = Image("youwin3.png",game)
youwin.resizeBy(-40)
youwin.y = 150
youlose = Image("youlose3.png",game)
youlose.resizeBy(-40)
youlose.y = 100

gary = Image("snail.jpeg",game)

#game.status = "play"
while not game.over: 
  game.processInput()
  road.draw()
  if game.status == "loselevel1":
    road.draw()
    youlose.draw()
    level1LoseMessage.draw()
    spongeLoseLVL1.draw()
    pass
  elif game.status == "loselevel2":
    krustykrabBK.draw()
    youlose.draw()
    level2LoseMessage.draw()
    spongeLoseLVL2.draw()
  else:
    titleBK.draw()
    youwin.draw()
    spongeWin2.draw()

  game.update(30)
game.quit()