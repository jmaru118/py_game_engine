# create, initialize, and run the 381 engine
import pygame
import dumbmenu as dm

pygame.init()
import engine
engine = engine.Engine()


#start menu
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255

#size = width, height = 480,480  
#screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode()
pygame.display.set_caption("118 Studios")
#screen.fill(blue)
img=pygame.image.load("robot.jpg") 
screen.blit(img,(0,0))
pygame.display.update()

#play intro music
pygame.mixer.music.fadeout(1000)
pygame.mixer.music.load("intro_song.wav")
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(1.0)

pygame.key.set_repeat(500,30)

choose = dm.dumbmenu(screen, [
                        'Start Game',
                        'Quit Game'], 64,64,None,64,1.7,(0,0,0),(0,0,0))

if choose == 0:
    print "You choose 'Start Game'."
    engine.init()
    engine.run()

elif choose == 1:
    print "You choose 'Options'."
elif choose == 2:
    print "You choose 'Manual'."
elif choose == 3:
    print "You choose 'Show Highscore'."
elif choose == 4:
    print "You choose 'Quit Game'."
pygame.quit()
exit()