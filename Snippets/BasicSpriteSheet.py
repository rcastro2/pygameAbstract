import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(800,600,"Game",60)

spider = Animation("images\\spider_crawl.png",19,game,120,148)
spider.resizeTo(100,100)
spider.setSpeed(4,60)

game.viewMouse(False)

while not game.over:
    game.processInput()
    game.clearBackground(black)
    
    spider.move(True)
    
    spider.rotateBy(1)
    
    game.update(24)
game.quit()
