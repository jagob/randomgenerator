# Randomgenerator - When in doubt, go random
#
# Place images in project folder 
# dependencies: python2-pygame python2-numarray

import pygame, sys, random, os
from pygame.locals import *
import numpy as np

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

pygame.init()

# fps
FPS = 50 # frames per second setting
fpsClock = pygame.time.Clock()

# images
WINDOWWIDTH,WINDOWHEIGHT = 1366, 768
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
# background=pygame.image.load("flippyboard.png").convert()
background = pygame.Surface(screen.get_size())
background.fill((0,0,0))
randomwinner = background

player = []
i = 0
for files in os.listdir('.'):
    if (files.endswith('.jpg') or files.endswith('.png')):
        print "File #" + str(i) + ": " + files
        player.append(pygame.image.load(files))
        i += 1


if (len(player) <= 5):
    boxsizel = WINDOWWIDTH/(5+1)
else:
    boxsizel = WINDOWWIDTH/(len(player)+1)
ymargin = 50
gapsize = (WINDOWWIDTH-(len(player)*boxsizel))/(len(player)+1)
boxsizeh = boxsizel
xmargin = gapsize
randomwinnerboxsize = WINDOWHEIGHT-3*ymargin-boxsizeh

hiborder = 2
hiborderwidth = 2*hiborder

rect = range(len(player))
i = 0
for players in player:
    player[i] = pygame.transform.scale(player[i],(boxsizel,boxsizeh))
    rect[i] = Rect(xmargin + i*boxsizel + i*gapsize,ymargin,boxsizel,boxsizeh)
    i+=1
    

playerstatus = range(len(player))
playerstatus = np.array(playerstatus)
i = 0
for players in playerstatus:
    playerstatus[i] = True 
    i+=1

# text
GREEN = (0, 255, 0)
HIGHLIGHTCOLOR = GREEN
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Random Generator!?!', True, GREEN)
textroll = font.render('SPIN THAT SHIT ->', True, GREEN)
textpos = text.get_rect(centerx=WINDOWWIDTH/2)
# background.blit(text, textpos)
randombutton=pygame.image.load("resources/gameicon.png")
randombutton = pygame.transform.scale(randombutton,(100,100))
rectrandom = Rect(350, 300, 100, 100 )

# Sounds
soundObj = pygame.mixer.Sound('resources/beeps.wav')
pygame.mixer.music.load('resources/backgroundmusic.wav')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
# pygame.mixer.music.stop() 

def findwinner():
  while True:
      winner = random.randint(0,len(player)-1)
      if playerstatus[winner] == True:
          return player[winner]

# Game Loop
while True: 
   for event in pygame.event.get():
      if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
      if event.type == KEYDOWN and event.key == K_m:
         if musicPlaying:
            pygame.mixer.music.stop()
            musicPlaying = not musicPlaying
         else:
            pygame.mixer.music.play(-1, 0.0)
            musicPlaying = not musicPlaying

      if event.type == MOUSEBUTTONDOWN:
         i = 0
         for players in player:
            if rect[i].collidepoint(event.pos):
                playerstatus[i] = not playerstatus[i]
                soundObj.play()
            i += 1

   if pygame.mouse.get_pressed()[0] and rectrandom.collidepoint(event.pos):
      if playerstatus.max():
         randomwinner = findwinner()
         randomwinner = pygame.transform.scale(randomwinner,(randomwinnerboxsize,randomwinnerboxsize))
         pygame.time.delay(75)
      else:
         randomwinner = background

# Draw Screen
   screen.blit(background, (0,0))
   screen.blit(text, textpos)
   i = 0
   for players in player:
      screen.blit(player[i], (xmargin + i*boxsizel + i*gapsize,ymargin))
      i += 1

   i = 0
   for players in player:
      if playerstatus[i]:
         pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect[i].left - hiborder, rect[i].top - hiborder, rect[i].width + 2*hiborder, rect[i].height + 2*hiborder), hiborderwidth)
      i += 1

   screen.blit(textroll, (xmargin,300))
   screen.blit(randombutton,(350,250))
   screen.blit(randomwinner,(WINDOWWIDTH/2-randomwinnerboxsize/2,2*ymargin+boxsizeh))

   pygame.display.update()
   fpsClock.tick(FPS)
