import pygame, sys, random
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

pygame.init()

# images
WINDOWWIDTH,WINDOWHEIGHT = 1366, 768
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
# background=pygame.image.load("flippyboard.png").convert()
background = pygame.Surface(screen.get_size())
background.fill((0,0,0))
xmargin = 20
ymargin = 100
gapsize = 20
boxsizel = 150
boxsizeh = 150

player1=pygame.image.load("img_acoustics.jpg")
player2=pygame.image.load("img_control.jpg")
player3=pygame.image.load("img_sp.jpg")
player4=pygame.image.load("img_comm.jpg")
player5=pygame.image.load("img_network.jpg")
player6=pygame.image.load("img_vgis.jpg")
player7=pygame.image.load("img_soundmusic.jpg")
player8=pygame.image.load("img_soundmusic.jpg")

player1 = pygame.transform.scale(player1,(boxsizel,boxsizeh))
player2 = pygame.transform.scale(player2,(boxsizel,boxsizeh))
player3 = pygame.transform.scale(player3,(boxsizel,boxsizeh))
player4 = pygame.transform.scale(player4,(boxsizel,boxsizeh))
player5 = pygame.transform.scale(player5,(boxsizel,boxsizeh))
player6 = pygame.transform.scale(player6,(boxsizel,boxsizeh))
player7 = pygame.transform.scale(player7,(boxsizel,boxsizeh))
player8 = pygame.transform.scale(player8,(boxsizel,boxsizeh))

rect1 = Rect(xmargin + 0*boxsizel + 0*gapsize,ymargin,boxsizel,boxsizeh)
rect2 = Rect(xmargin + 1*boxsizel + 1*gapsize,ymargin,boxsizel,boxsizeh)
rect3 = Rect(xmargin + 2*boxsizel + 2*gapsize,ymargin,boxsizel,boxsizeh)
rect4 = Rect(xmargin + 3*boxsizel + 3*gapsize,ymargin,boxsizel,boxsizeh)
rect5 = Rect(xmargin + 4*boxsizel + 4*gapsize,ymargin,boxsizel,boxsizeh)
rect6 = Rect(xmargin + 5*boxsizel + 5*gapsize,ymargin,boxsizel,boxsizeh)
rect7 = Rect(xmargin + 6*boxsizel + 6*gapsize,ymargin,boxsizel,boxsizeh)
rect8 = Rect(xmargin + 7*boxsizel + 7*gapsize,ymargin,boxsizel,boxsizeh)

randombutton=pygame.image.load("gameicon.png")
randombutton = pygame.transform.scale(randombutton,(100,100))
rectrandom = Rect(350, 270, 100, 100 )

randomwinner = background

player1status = True
player2status = True
player3status = True
player4status = True
player5status = True
player6status = True
player7status = True
player8status = True

# fps
FPS = 50 # frames per second setting
fpsClock = pygame.time.Clock()

# text
GREEN = (0, 255, 0)
HIGHLIGHTCOLOR = GREEN
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Random Generator!?!', True, GREEN)
textroll = font.render('ROLL THE DICE ->', True, GREEN)
textpos = text.get_rect(centerx=WINDOWWIDTH/2)
# background.blit(text, textpos)

# sound
soundObj = pygame.mixer.Sound('beeps.wav')
# soundObj.play()
# import time
# time.sleep(1) # wait and let the sound play for 1 second
# soundObj.stop()

# background sound
pygame.mixer.music.load('backgroundmusic.wav')
pygame.mixer.music.play(-1, 0.0)
# pygame.mixer.music.stop()
musicPlaying = True

def findwinner():
   number = random.randint(1,8)
   if number == 1:
      if player1status:
         return player1
   elif number == 2:
      if player2status:
         return player2
   elif number == 3:
      if player3status:
         return player3
   elif number == 4:
      if player4status:
         return player4
   elif number == 5:
      if player5status:
         return player5
   elif number == 6:
      if player6status:
         return player6
   elif number == 7:
      if player7status:
         return player7
   elif number == 8:
      if player8status:
         return player8
   return background


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
         if rect1.collidepoint(event.pos):
            player1status = not player1status
            soundObj.play()
         elif rect2.collidepoint(event.pos):
            player2status = not player2status
            soundObj.play()
         elif rect3.collidepoint(event.pos):
            player3status = not player3status
            soundObj.play()
         elif rect4.collidepoint(event.pos):
            player4status = not player4status
            soundObj.play()
         elif rect5.collidepoint(event.pos):
            player5status = not player5status
            soundObj.play()
         elif rect6.collidepoint(event.pos):
            player6status = not player6status
            soundObj.play()
         elif rect7.collidepoint(event.pos):
            player7status = not player7status
            soundObj.play()
         elif rect8.collidepoint(event.pos):
            player8status = not player8status
            soundObj.play()
      
      if event.type == MOUSEBUTTONUP:
         if randomwinner == player1:
            soundObj.play()
         if randomwinner == player2:
            soundObj.play()

   if pygame.mouse.get_pressed()[0] and rectrandom.collidepoint(event.pos):
      randomwinner = findwinner()
      if player1status or player2status or player3status or player4status or player5status or player6status or player7status or player8status:
         randomwinner = pygame.transform.scale(randomwinner,(2*boxsizeh,2*boxsizel))
         screen.blit(randomwinner,(WINDOWWIDTH/2-boxsizel,WINDOWHEIGHT/2))
         pygame.time.delay(75)


   screen.blit(background, (0,0))
   screen.blit(text, textpos)
   screen.blit(player1, (xmargin + 0*boxsizel + 0*gapsize,ymargin))
   screen.blit(player2, (xmargin + 1*boxsizel + 1*gapsize,ymargin))
   screen.blit(player3, (xmargin + 2*boxsizel + 2*gapsize,ymargin))
   screen.blit(player4, (xmargin + 3*boxsizel + 3*gapsize,ymargin))
   screen.blit(player5, (xmargin + 4*boxsizel + 4*gapsize,ymargin))
   screen.blit(player6, (xmargin + 5*boxsizel + 5*gapsize,ymargin))
   screen.blit(player7, (xmargin + 6*boxsizel + 6*gapsize,ymargin))
   screen.blit(player8, (xmargin + 7*boxsizel + 7*gapsize,ymargin))
   screen.blit(textroll, (25,275))
   screen.blit(randombutton,(350,270))
   screen.blit(randomwinner,(WINDOWWIDTH/2-boxsizel,WINDOWHEIGHT/2))

   hiborder = 2
   hiborderwidth = 2*hiborder
   if player1status:
      pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect1.left - hiborder, rect1.top - hiborder, rect1.width + 2*hiborder, rect1.height + 2*hiborder), hiborderwidth)
   if player2status:
      pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect2.left - hiborder, rect2.top - hiborder, rect2.width + 2*hiborder, rect2.height + 2*hiborder), hiborderwidth)
   if player3status:
      pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect3.left - hiborder, rect3.top - hiborder, rect3.width + 2*hiborder, rect3.height + 2*hiborder), hiborderwidth)
   if player4status:
      pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect4.left - hiborder, rect4.top - hiborder, rect4.width + 2*hiborder, rect4.height + 2*hiborder), hiborderwidth)
   if player5status:
      pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect5.left - hiborder, rect5.top - hiborder, rect5.width + 2*hiborder, rect5.height + 2*hiborder), hiborderwidth)
   if player6status:
      pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect6.left - hiborder, rect6.top - hiborder, rect6.width + 2*hiborder, rect6.height + 2*hiborder), hiborderwidth) 
   if player7status:
      pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect7.left - hiborder, rect7.top - hiborder, rect7.width + 2*hiborder, rect7.height + 2*hiborder), hiborderwidth) 
   if player8status:
      pygame.draw.rect(screen, HIGHLIGHTCOLOR, (rect8.left - hiborder, rect8.top - hiborder, rect8.width + 2*hiborder, rect8.height + 2*hiborder), hiborderwidth) 

   pygame.display.update()
   fpsClock.tick(FPS)
