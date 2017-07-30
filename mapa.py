from pygame import *
import random
from base_class import *
from WORLD import *
WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

def main():
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY)
	pygame.display.set_caption("Balls_game")
	bg = Surface((WIN_WIDTH,WIN_HEIGHT))
				#    Speed : pos
	pizdaball = Ball((9,9),(20,20),pygame.Color("green"))
	bg.fill(Color(BACKGROUND_COLOR))
	while 1:
		for e in pygame.event.get():
				if e.type == QUIT:
					raise SystemExit
		screen.fill(pygame.Color("black"))
		pizdaball.draw(screen)
		pizdaball.moves()
		pygame.display.flip()
		pygame.event.wait()

#while 1:
#	pass
if __name__ == "__main__":
    main()
