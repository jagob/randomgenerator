# Randomgenerator - When in doubt, go random
#
# Place images in project folder
# dependencies: python2-pygame python2-numarray

import pygame, sys, random
from pygame.locals import *
from numarray import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

pygame.init()

# FPS
FPS = 50 # frames per second setting
fpsClock = pygame.time.Clock()

# Setup screen
WINDOWWIDTH,WINDOWHEIGHT = 1366, 768
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
# background=pygame.image.load("flippyboard.png").convert()
background = pygame.Surface(screen.get_size())
background.fill((0,0,0))
randomwinner = background

# Load players based on images in folder
playerOriginal = []
i = 0
for files in os.listdir('.'):
    if (files.endswith('.jpg') or files.endswith('.png') or files.endswith('.bmp')):
        print "File #" + str(i) + ": " + files
        playerOriginal.append(pygame.image.load(files))
        i += 1
player = range(i)

# Calculate spacing
if (len(playerOriginal) <= 5):
    boxsizel = WINDOWWIDTH/(5+1)
else:
    boxsizel = WINDOWWIDTH/(len(playerOriginal)+1)
ymargin = 50
gapsize = (WINDOWWIDTH-(len(playerOriginal)*boxsizel))/(len(playerOriginal)+1)
boxsizeh = boxsizel
xmargin = gapsize
randomwinnerboxsize = WINDOWHEIGHT-3*ymargin-boxsizeh

hiborder = 2
hiborderwidth = 2*hiborder

# Preview pictures
rect = range(len(playerOriginal))
i = 0
for players in playerOriginal:
    player[i] = pygame.transform.scale(playerOriginal[i],(boxsizel,boxsizeh))
    rect[i] = Rect(xmargin + i*boxsizel + i*gapsize,ymargin,boxsizel,boxsizeh)
    i+=1
    
# Convert from list to array
playerstatus = range(len(player))
playerstatus = array(playerstatus)
i = 0
for players in playerstatus:
    playerstatus[i] = True 
    i+=1

# Display text
GREEN = (0, 255, 0)
HIGHLIGHTCOLOR = GREEN
font            = pygame.font.Font('freesansbold.ttf', 32)
txt_title       = font.render('Random Generator!?!', True, GREEN)
txt_title_pos   = txt_title.get_rect(centerx=WINDOWWIDTH/2)
txt_spin        = font.render('SPIN THAT SHIT', True, GREEN)
txt_spin_pos    = txt_spin.get_rect(centerx=WINDOWWIDTH/2,centery=300)
randombutton    = pygame.image.load("resources/gameicon.png")
randombutton    = pygame.transform.scale(randombutton,(175,175))
randombutton_pos= randombutton.get_rect(centerx=WINDOWWIDTH/2,centery=450)
rectrandom    = Rect(WINDOWWIDTH/2-randomwinnerboxsize/2,2*ymargin+boxsizeh,randomwinnerboxsize,randomwinnerboxsize)

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
            return playerOriginal[winner]

# Game Loop
while True: 
    # Handle key input
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

   # Handle mouse input
    if pygame.mouse.get_pressed()[0] and rectrandom.collidepoint(event.pos):
        if playerstatus.max():
            randomwinner = findwinner()
            randomwinner = pygame.transform.scale(randomwinner,(randomwinnerboxsize,randomwinnerboxsize))
            pygame.time.delay(75)
        else:
            randomwinner = background

   # Draw screen from top down
    screen.blit(background, (0,0))
    screen.blit(txt_title, txt_title_pos)
    i = 0
    for players in player:
        # Draw players
        screen.blit(player[i], (xmargin + i*boxsizel + i*gapsize,ymargin))
        # Highligt active players
        if playerstatus[i]:
            pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect[i].left - hiborder, rect[i].top - hiborder, rect[i].width + 2*hiborder, rect[i].height + 2*hiborder), hiborderwidth)
        i += 1

    screen.blit(txt_spin, txt_spin_pos)
    screen.blit(randombutton, randombutton_pos)
    if randomwinner != background:
        screen.blit(randomwinner,(WINDOWWIDTH/2-randomwinnerboxsize/2,2*ymargin+boxsizeh))

    pygame.display.update()
    fpsClock.tick(FPS)
# End of game loop
