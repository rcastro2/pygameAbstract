import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *
game = Game(1600,900,"Collision Between Rotating Rectangles",60)
 

bar1 = Animation("images/bar.png",3,game,700,110,4)
bar1.x = 350
bar1.resizeTo(900,50)
bar1.collisionBorder = "vertices"

bar2 = Animation("images/bar.png",3,game,700,110,4)
bar2.x = game.width - 350
bar2.resizeTo(900,50)
bar2.collisionBorder = "vertices"

alien = Image("images/Alien2.gif",game)
alien.moveTo(500,500)
alien.collisionBorder = "vertices"

apple = Image("images/apple.png",game)
apple.collisionBorder = "vertices"
apple.resizeBy(-90)


while not game.over:
    game.processInput()
    game.clearBackground(white)

    bar1.draw()
    bar1.rotateBy(1)

    bar2.draw()
    bar2.rotateBy(-1)

    alien.draw()
    alien.moveTo(mouse.x,mouse.y)

    apple.draw()
    
    if bar1.collidedWith(alien,"vertices") or bar2.collidedWith(alien,"vertices"):
        game.drawText("Hit",game.width / 2,game.height / 2, Font(red,60,black))
        alien.health -= 5

    if bar1.collidedWith(apple,"vertices") or bar2.collidedWith(apple,"vertices"):
        x = randint(apple.width, game.width - apple.width)
        y = randint(apple.height, game.height - apple.height)
        apple.moveTo( x, y )

    if alien.collidedWith(apple,"vertices"):
        game.score += 5
        x = randint(apple.width, game.width - apple.width)
        y = randint(apple.height, game.height - apple.height)
        apple.moveTo( x, y )

    if alien.health < 0 or game.time < 0 or game.score >= 100:
        game.over = True

    game.drawText(f'Health: {alien.health}',30,40, Font(black))
    game.drawText(f'Score: {game.score}',30,70, Font(blue))
    game.displayTime(30,10, newFont = Font(black))
            
    game.update(30)
game.quit()
