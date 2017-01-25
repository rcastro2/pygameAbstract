from gamelib import *
class Snake(object):
    def __init__(self,path,segments,size,game):
        self.snake = []
        self.game = game
        self.image = path
        self.size = size
        for segment in range(segments):
            self.snake.append(Image(path,game))
            self.snake[segment].resizeTo(size,size)
            self.snake[segment].moveTo(100+segment*10,100/2)
    def adjustTail(self):
        ln = len(self.snake)-1
        for p in range(0,ln):
            self.snake[ln-p].moveTo(self.snake[ln-p-1].x,self.snake[ln-p-1].y)
    def draw(self):
        ln = len(self.snake)-1
        for p in range(0,ln):
            self.snake[ln-p].draw()
    def addTail(self):
        self.snake.append(Image(self.image,self.game))
        self.snake[len(self.snake)-1].resizeTo(self.size,self.size)
        self.adjustTail()
    def eats(self,obj):
        return self.snake[0].collidedWith(obj)
    def move(self,dx,dy):
        self.snake[0].moveX(dx)
        self.snake[0].moveY(dy)

