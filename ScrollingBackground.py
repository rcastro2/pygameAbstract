from gamelib import *

game = Game(800,600,"Scroll")

bk = Image("images\\day.png",game)
bk.resizeTo(game.width,game.height)

game.setBackground(bk)

while not game.over:
    game.processInput()

    game.scrollBackground("down",1)

    game.update(60)
game.quit()

    
