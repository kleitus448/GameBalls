import pygame
class Game_world:
	'''World in game'''
	def __init__(self, msec, tickevent = pygame.USEREVENT):
		self.msec = msec
		self.tickevent = tickevent
	def Start(self):
		pygame.time.set_timer(self.tickevent, self.msec)

	def Finish(self):
		pygame.time.set_timer(self.tickevent, 0)
