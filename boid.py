import pygame

class boid:
    def __init__(self,posx,posy,velx,vely):
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely
        self.length = 15
        self.height = 5

    def changepos(self, posx, posy):
        self.posx = posx
        self.posy = posy
