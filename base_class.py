import random
import pygame
class Ball():
	def __init__(self,pos,speed,color):
		#self.Square = pygame.Rect(*pos,random.randrange(59,60),random.randrange(59,60))
		self.rad = random.randint(20,30)
		self.speed = speed
		self.pos = pos
		self.color = color
		self.SCarry = False
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, self.pos, self.rad)
	def moves(self):
		self.pos = self.pos[0]+self.speed[0], self.pos[1]+self.speed[1]
		if self.speed[1]<=0:
			self.speed = self.speed[0], self.speed[1] - 1
		if 	self.speed[0]<=0:
			self.speed = self.speed[0] - 1, self.speed[1]
		if self.speed[1]>0:
			self.speed = self.speed[0], self.speed[1] + 1
		#if 	self.speed[0]<0:
			#self.speed = self.speed[0] + 1, self.speed[1]

	'''def logic(self,surface):
		if self.pos[0]<self.rect.width//2:
			self.pos[0] = self.rect.width//2
			self.speed[0] = -self.speed[0]
		elif self.pos[0] > surface.get_width() - self.rect.width//2:
			self.pos[0] = surface.get_width() - self.rect.width//2
			self.speed[0] = -self.speed[0]
		if self.pos[1]<self.rect.height//2:
			self.pos[1] = self.rect.height//2
			self.speed[1] = -self.speed[1]
		elif self.pos[1] > surface.get_height() - self.rect.height//2:
			self.pos[1] = surface.get_height() - self.rect.height//2
			self.speed[1] = -self.speed[1]'''
