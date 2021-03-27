import pygame
import time
clock = pygame.time.Clock()

FPS = 60
 
pygame.init()
sc = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("GAME1")
y2 = 290
x2 = 100
y = 290
x = 250
pygame.display.update()

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
beriz = (0, 255, 247)
lite_green = (0, 255, 17)
play = True
while play:
	sc.fill(beriz)
	a = pygame.event.get()
	for i in a:
		if i.type == pygame.QUIT:
			exit()
		elif i.type == pygame.KEYDOWN:
			if i.key == pygame.K_DOWN:
				y+=10
			elif i.key == pygame.K_UP:
				y-=10
			elif i.key == pygame.K_RIGHT:
				x+=10
			elif i.key == pygame.K_LEFT:
				x-=10


			elif i.key == pygame.K_s:
				y2+=10
			elif i.key == pygame.K_w:
				y2-=10
			elif i.key == pygame.K_d:
				x2+=10
			elif i.key == pygame.K_a:
				x2-=10
                
	pygame.draw.rect(sc, red, (x,  y, 100, 100))
	font = pygame.font.Font(None, 35)
	text = font.render("1 Игрок", 1, white)
	place = text.get_rect(center=(x+50, y+50))
	sc.blit(text, place)
	pygame.draw.rect(sc, blue, (x2,  y2, 100, 100))
	font = pygame.font.Font(None, 35)
	text = font.render("2 Игрок", 1, white)
	place = text.get_rect(center=(x2+50, y2+50))
	sc.blit(text, place)
	pygame.display.update()

	if y <= 0:
		sc.fill(lite_green)
		font = pygame.font.Font(None, 65)
		text = font.render("Выиграл 1 игрок", 1, (0, 100, 0))
		place = text.get_rect(center=(200, 150))
		sc.blit(text, place)
		pygame.display.update()
		time.sleep(3)
		play = False
	if y2 <= 0:
		sc.fill(lite_green)
		font = pygame.font.Font(None, 65)
		text = font.render("Выиграл 2 игрок", 1, (0, 100, 0))
		place = text.get_rect(center=(200, 150))
		sc.blit(text, place)
		pygame.display.update()
		time.sleep(3)
		play = False
	clock.tick(FPS)	