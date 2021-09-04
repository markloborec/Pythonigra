import random


class World:
    def __init__(self,width,height,numberofenemies):
        self.width = width
        self.height = height
        self.hero = Hero(width//2,height//2)
        self.enemies = []
        for i in range(numberofenemies):
            enemy = Enemy(random.randint(0,width), random.randint(0,height))
            self.enemies.append(enemy)

class Hero:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy


class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy