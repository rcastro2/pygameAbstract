from gamelib import *

game = Game(800,600,"Game",60)

spider = Animation("images\\spider_crawl.png",19,game,120,148)
spider.resizeTo(100,100)
spider.setSpeed(4,60)

game.viewMouse(False)

while not game.over:
    game.processInput()
    game.background(black)
    spider.move(True)
    spider.rotateBy(2)
    game.update(24)

game.quit()
