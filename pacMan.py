import pygame
from pygame.locals import *
from random import randint
from classes import *

if __name__ == "__main__" or __name__ == "pacman":
    GAME = Maze()
    HERO = Pacman()
    VILLAN = Ghost()
    VILLAN2 = Ghost()
    VILLAN3 = Ghost()
    VILLAN4 = Ghost()
    VILLAN5 = Ghost()
    VILLAN6 = Ghost()
    VILLAN7 = Ghost()
    VILLAN8 = Ghost()
    pygame.init()
    GAME.scorefont = pygame.font.Font(None, 30)
    done = False
    clock = pygame.time.Clock()

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == K_q:
                    done = True

        HERO.pacPosition(GAME)
        GAME.screen.fill(GAME.BLACK)
        VILLAN.ghostPosition(GAME)
        VILLAN2.ghostPosition(GAME)
        VILLAN3.ghostPosition(GAME)
        VILLAN4.ghostPosition(GAME)
        VILLAN5.ghostPosition(GAME)
        VILLAN6.ghostPosition(GAME)
        VILLAN7.ghostPosition(GAME)
        VILLAN8.ghostPosition(GAME)
        move = randint(0,3)
        GAME.countfinal = 0
        GAME.dispmaze()
        GAME.drawwalls()
        HERO.pos(GAME)
        VILLAN.pos(GAME)
        VILLAN2.pos(GAME)
        VILLAN3.pos(GAME)
        VILLAN4.pos(GAME)
        VILLAN5.pos(GAME)
        VILLAN6.pos(GAME)
        VILLAN7.pos(GAME)
        VILLAN8.pos(GAME)

        if HERO.checkGhost(VILLAN) or HERO.checkGhost(VILLAN2) or HERO.checkGhost(VILLAN3) or HERO.checkGhost(VILLAN4) or HERO.checkGhost(VILLAN5) or HERO.checkGhost(VILLAN6) or HERO.checkGhost(VILLAN7) or HERO.checkGhost(VILLAN8):
            done = True
            print("Final Score = "+(str)(GAME.score))
        elif GAME.countfinal == 1200 : 
            GAME.reset()
            HERO.resetpacman()
            VILLAN.resetghost()    
            VILLAN2.resetghost()    
            VILLAN3.resetghost()    
            VILLAN4.resetghost()    
            VILLAN5.resetghost()    
            VILLAN6.resetghost()    
            VILLAN7.resetghost()    
            VILLAN8.resetghost()    
            GAME.level += 1

        GAME.scoredisp()    
        GAME.leveldisp()
        clock.tick(10)
        pygame.display.flip()

    pygame.quit()    