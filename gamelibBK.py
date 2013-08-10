import pygame,math
from pygame.locals import * 
from math import *
from random import randint

pygame.init()

class Game(object):
    keyDown = None
    keyUp = None
    mouseX = None
    mouseY = None
    mouseLB = None
    mouseRB = None
    over = False   
    def __init__(self,w,h,title):
        self.width,self.height = w,h
        pygame.display.set_caption(title)
        size = [w,h]
        self.screen = pygame.display.set_mode(size);
        self.clock = pygame.time.Clock()
        self.left, self.top, self.right, self.bottom = 0,0,w,h
        self.score = 0
        self.image = None
    def drawText(self,msg,x,y,c):
        font = pygame.font.Font(None,24)
        text = font.render(msg,True,c)
        self.screen.blit(text,[x,y])
    def increaseScore(self,amount):
        self.score += amount
    def setMusic(self,path):
        pygame.mixer.music.load(path)

    def playMusic(self):
        pygame.mixer.music.play(-1,0.0)

    def stopMusic(self):
        pygame.mixer.music.stop()
        
    def background(self,c):
        self.screen.fill(c)
        
    def update(self,fps):
        pygame.display.flip()
        self.clock.tick(fps)

    def viewMouse(self,visibility):
        pygame.mouse.set_visible(visibility)

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.over = True 
            if event.type == pygame.KEYDOWN:
                self.keyDown = event.key
            else:
                self.keyDown = None
            if event.type == pygame.KEYUP:
                self.keyUp = event.key
            else:
                self.keyUp = None
            pos = pygame.mouse.get_pos()
            self.mouseX=pos[0]
            self.mouseY=pos[1]
            button = pygame.mouse.get_pressed()
            self.mouseLB = button[0]
            self.mouseRB = button[2] 
    def quit(self):
        pygame.quit()
        
class Image(object):
    def __init__(self,path,game):
        self.game = game
        self.image = pygame.image.load(path)
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        print(self.w,self.h)
        self.original = self.image
        self.angle, self.da = 0,0
        self.x, self.y = 0,0
        self.left, self.top, self.right, self.bottom = 0,0,0,0
        self.bounce = False
        self.direction = "still"
        self.force = 0
        self.visible = True
    def collidedWith(self,obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        d = sqrt(pow(dx,2) + pow(dy,2))
        if d < self.w/3 + obj.w/3 and obj.visible:
            return True
        else:
            return False
    def draw(self):
        if self.visible:
            if self.direction == "left" or self.direction == "right":
                self.angle = self.angle + self.da
                self.image = pygame.transform.scale(self.original,(self.w,self.h))
                org_rect = self.image.get_rect()
                rot_img = pygame.transform.rotate(self.image,self.angle * 180 / math.pi)
                rot_rect = org_rect.copy()
                rot_rect.center = rot_img.get_rect().center
                self.image = rot_img.subsurface(rot_rect).copy()
            if self.force > 0:
                x = self.x + self.force * math.sin(self.angle)
                y = self.y + self.force * math.cos(self.angle)
                self.moveTo(x,y)
            self.left, self.top, self.right, self.bottom  = self.x,self.y, self.x + self.w, self.y + self.h
            self.game.screen.blit(self.image, [self.x - self.w/2,self.y - self.h/2])
    def moveTo(self,x,y):
        self.x,self.y = x,y
    def setSpeed(self,force,angle):
        rad = angle * math.pi / 180
        self.force, self.angle = force, rad
        self.dx, self.dy = force * math.sin(rad),force * math.cos(rad)
    def makeVisible(self,visibility = -999):
        if visibility == -999:
            visibility = not self.visible
        self.visible = visibility
    def move(self, bounce = False):
        if bounce:
            if self.left < self.game.left or self.right > self.game.right:
                self.changeXSpeed()
            if self.top < self.game.top or self.bottom > self.game.bottom:
                self.changeYSpeed()
        #self.x = self.x + self.dx
        #self.y = self.y + self.dy
        self.draw()
    def forward(self,speed):
        self.speed = speed
        
    def resizeTo(self,w,h):
        self.w = w
        self.h = h
        self.image = pygame.transform.scale(self.original,(self.w,self.h))
    def rotate(self,direction,angle=0):
        self.direction = direction
        if direction == "right":
            angle = -angle
        self.da = angle


class Animation(object):
    def __init__(self,path,sequence,game):
        self.game = game
        self.images = []
        self.original = []
        for i in range(sequence):
            self.images.append(pygame.image.load(path + str(i+1) + ".gif"))
            self.original.append(self.images[i])
        self.f = 0
        self.force, self.angle = 0,0
        self.x, self.y, self.dx, self.dy = 0,0,0,0
        self.left, self.top, self.right, self.bottom = 0,0,0,0
        self.w, self.h = 0,0
        self.visible = True
    def collidedWith(self,obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        d = sqrt(pow(dx,2) + pow(dy,2))
        if d < self.w/3 + obj.w/3 and obj.visible:
            return True
        else:
            return False
    def makeVisible(self,visibility = -999):
        if visibility == -999:
            visibility = not self.visible
        self.visible = visibility
    def draw(self, loop = True):
        if self.visible:
            self.w = self.images[self.f].get_width()
            self.h = self.images[self.f].get_height()
            self.left, self.top, self.right, self.bottom  = self.x,self.y, self.x + self.w, self.y + self.h
            self.game.screen.blit(self.images[self.f], [self.x - self.w/2,self.y - self.h/2])
            self.f = self.f + 1
            if self.force > 0:
                x = self.x + self.force * math.sin(self.angle - math.pi)
                y = self.y + self.force * math.cos(self.angle - math.pi)
                self.moveTo(x,y)
            if self.f > len(self.images)-1:
                self.f = 0
            if not loop and self.f == 0:
                self.visible = False
    def setSpeed(self,force,angle):
        self.force = force
        self.angle = angle
        rad = angle * math.pi / 180
        self.dx, self.dy = self.force * math.sin(rad),force * math.cos(rad)
    def changeXSpeed(self,dx = -999):
        if dx == -999:
            self.dx = -self.dx
        else:
            self.dx = dx
    def changeYSpeed(self,dy = -999):
        if dy == -999:
            self.dy = -self.dy
        else:
            self.dy = dy
    def move(self, bounce = False):
        if bounce:
            if self.left < self.game.left or self.right > self.game.right:
                self.changeXSpeed()
            if self.top < self.game.top or self.bottom > self.game.bottom:
                self.changeYSpeed()
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.draw()
    def moveTo(self,x,y):
        self.x,self.y = x,y
    def moveX(self,a):
        self.x = self.x + a
    def moveY(self,a):
        self.y = self.y + a
    def resizeTo(self,w,h):
        self.w = w
        self.h = h
        for i in range(len(self.images)-1):
            self.images[i] = pygame.transform.scale(self.original[i],(self.w,self.h))

   


