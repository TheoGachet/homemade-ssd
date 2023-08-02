# Simulation réalisée dans le but de vulgariser l'électronique
# réalisée par Théo Gachet dans le cadre du projet ISA EI22 par AREM

import sys, pygame, random

def aleatoire(x):
	x-= 300
	x = 100 - x
	y = random.random()*x/random.randrange(100, 150)
	return (round(y))

def signe():
	x = random.randrange(-1, 100000)
	if x >50005:
		return -1
	return 1

pygame.init()
taille = largeur, hauteur = 1200, 750
ecran = pygame.display.set_mode(taille)

BLANC = 255, 255, 255
NOIR = 0, 0, 0
ROUGE = 255, 0, 0
BLEU = 30, 30, 130
GRIS = 128, 128, 128
GRIS_CLAIR = 230, 230, 230
JAUNE = 255, 255, 0

cycleI = 0
yElectrons = 0
animation = 0

calibri = pygame.font.SysFont("calibri", 80)
P = calibri.render("P", 1, BLEU)
N = calibri.render("N", 1, ROUGE)

partieP = pygame.Rect(50, 300, 1100, 400)
partieP_Surface = pygame.Surface((1100, 400))
partieP_Surface.fill(ROUGE)

partieNGauche = pygame.Rect(100, 300, 300, 120)
partieNGauche_Surface = pygame.Surface ((300, 120))
partieNGauche_Surface.fill(BLEU)

partieNDroite = pygame.Rect(800, 300, 300, 80)
partieNDroite_Surface = pygame.Surface ((300, 120))
partieNDroite_Surface.fill(BLEU)

porteFlottante = pygame.Rect(350, 240, 500, 50)
porteFlottante_Surface = pygame.Surface((500, 50))
porteFlottante_Surface.fill(GRIS)

porteControle = pygame.Rect(350, 175, 500, 50)
porteControle_Surface = pygame.Surface((500, 50))
porteControle_Surface.fill(GRIS)

oxydeSilicium = pygame.Rect(300, 0, 600, 300)
oxydeSilicium_Surface = pygame.Surface((600, 300))
oxydeSilicium_Surface.fill(GRIS_CLAIR)

source = pygame.Rect(120, 0, 80, 300)
source_Surface = pygame.Surface((80, 300))
source_Surface.fill(JAUNE)

drain = pygame.Rect(1000, 0, 80, 300)
drain_Surface = pygame.Surface((80, 300))
drain_Surface.fill(JAUNE)

electron = pygame.image.load("electron.png")
electronRect = electron.get_rect()

eclair = pygame.image.load("eclair.png")
eclair_surface = eclair.get_rect()
eclair_surface.top = 10

while 1:
	cycleI += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if animation == 0 and event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				animation = 1
			elif event.key == pygame.K_UP:
				animation = 2
			elif event.key == pygame.K_RETURN:
				animation = 3
				electrons = []
				for i in range(0, 20):
					electrons.append(electron.get_rect())
					electrons[i].left = 160
					electrons[i].top = -35 -40*i
				clock = 0
				
	if animation == 1 and cycleI %2 == 0:
		if yElectrons == 65: animation = 0
		else: yElectrons += 1
	
	elif animation == 2 and cycleI %2 == 0:
		if yElectrons == 0: animation = 0
		else: yElectrons -= 1
	
	ecran.fill(NOIR)
	ecran.blit(partieP_Surface, partieP)
	ecran.blit(partieNGauche_Surface, partieNGauche)
	ecran.blit(partieNDroite_Surface, partieNDroite)
	ecran.blit(oxydeSilicium_Surface, oxydeSilicium)
	ecran.blit(porteFlottante_Surface, porteFlottante)
	ecran.blit(porteControle_Surface, porteControle)
	ecran.blit(source_Surface, source)
	ecran.blit(drain_Surface, drain)
	ecran.blit(P, (575, 450))
	ecran.blit(N, (110, 305))
	ecran.blit(N, (1038, 305))
	

	if animation == 3:
		clock += 1
		for i in range (0, 20):
			if electrons[i].left < 350 and electrons[i].top < 300:
				electrons[i] = electrons[i].move([0, 4])
			elif electrons[i].top >= 300:
				if electrons[i].left < 1010 and yElectrons == 0:
					electrons[i] = electrons[i].move([4, 0])
				elif electrons[i].left >= 1010:
					electrons[i] = electrons[i].move([0, -4])
				elif electrons[i].left < 400:
					a = aleatoire(electrons[i].left)
					electrons[i] = electrons[i].move([a,signe()*(4-a)])
					if electrons[i].top > 380 : electrons[i] = electrons[i].move([-1, -4])
					if (clock == 500) :
						animation = 0
					
			elif electrons[i].left > 500 and electrons[i].top <= 300:
				electrons[i] = electrons[i].move([0, -4])

			
			ecran.blit(electron, electrons[i])
		if (clock == 600) :
			animation = 0
	
	for i in range(360, 850, 50):
		electronRect.top = 185 + yElectrons
		electronRect.left = i
		ecran.blit(electron, electronRect)
	
	if animation == 1 or animation == 2:
		for i in range(350, 900, 150):
			eclair_surface.left = i
			ecran.blit(eclair, eclair_surface)
	
	pygame.display.flip()
