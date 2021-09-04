import random

from src.domain import World


class Console:
    def __init__(self,width,height):
        self.world = World(width,height,10)
    def draw(self):
        for y in range(self.world.height):
            for x in range(self.world.width):
                if self.world.hero.x == x and self.world.hero.y == y:
                    print("h", end='')
                    continue

                isenemyDrawn = False
                for enemy in self.world.enemies:
                    if enemy.x == x and enemy.y == y:
                        print("E", end="")
                        isenemyDrawn = True
                        break
                if isenemyDrawn:
                    continue
                print("*",end='')
            print()
    def nextiteration(self):
        dx = int(input("Vnesi dx:"))
        dy = -int(input("Vnesi dy:"))
        self.world.hero.move(dx,dy)
        for enemy in self.world.enemies:
            enemy.move(random.randint(-5,5),random.randint(-5,5))







