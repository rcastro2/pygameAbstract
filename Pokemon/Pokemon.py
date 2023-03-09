#https://fontmeme.com/pokemon-font/
#https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon_by_color#White
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(1000,800,"Pokemon",60)
bk  = Image("images\\background7.jpg",game)
bk.resizeTo(1000,800)

logo = Image("images\\logo.png",game)
logo.y -= 100
logo.resizeBy(-50)

play = Image("images\\play1.png",game)
play.y += 150
play_on = Image("images\\play2.png",game)
play_off = Image("images\\play1.png",game)

ball = Image("images\\pokeball.png",game)
ball.resizeBy(-75)

pachirisu = Image("images\\Pachirisu.webp",game)
pachirisu.resizeBy(-60)

pokemon_files = ["Bulbasaur","Caterpie","Charmander","Pikachu","Mudkip"]
teamrocket_files = [{"name":"Jessie.png","resize":0},{"name":"James.png","resize":-80},{"name":"Meowth.webp","resize":-50}]
pokemons = []
teamrockets = []
for pokemon in pokemon_files:
    p = Image(f"images\\{pokemon}.webp",game)
    p.setSpeed(randint(2,4), randint(1,6) * 60)
    p.resizeBy(-80)              
    pokemons.append(p)

for member in teamrocket_files:
    r = Image(f"images\\{member['name']}",game)
    r.setSpeed(randint(2,4), randint(1,14) * 25)
    r.resizeBy(member['resize'])             
    teamrockets.append(r)

mouse.visible = False

while not game.over:
    game.processInput()

    bk.draw()
    logo.draw()
    play.draw()

    ball.moveTo(mouse.x,mouse.y)
    if ball.collidedWith(play,"rectangle"):
        play.setImage(play_on.image)
    else:
        play.setImage(play_off.image)

    if ball.collidedWith(play,"rectangle") and mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

pokemon = pokemons[randint(0,len(pokemons)-1)]
teamrocket = teamrockets[randint(0,len(teamrockets)-1)]


while not game.over:
    game.processInput()
    bk.draw()
    pokemon.move(True)
    teamrocket.move(True)
    
    ball.moveTo(mouse.x,mouse.y)
    
    if pokemon.collidedWith(mouse) and mouse.LeftClick:
        x = randint(pokemon.width,game.width-pokemon.width)
        y = randint(pokemon.height,game.height-pokemon.height)
        pokemon = pokemons[randint(0,len(pokemons)-1)]
        pokemon.setSpeed(randint(2,4), randint(1,6) * 60)
        pokemon.moveTo(x,y)
        teamrocket.speed += 1
        game.score += 10
        
    if teamrocket.collidedWith(pokemon):
        x = randint(pokemon.width,game.width-pokemon.width)
        y = randint(pokemon.height,game.height-pokemon.height)
        pokemon.moveTo(x,y)
        game.score -= 10
    
    if game.time <= 0:
        game.over = True
        
    game.displayTime(150,5)
    game.displayScore()
    game.update(30)
game.quit()
