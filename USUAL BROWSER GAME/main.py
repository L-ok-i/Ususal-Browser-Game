import pygame
import sys


# pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((1423, 800))
surf = pygame.image.load('img/png/cursor.png')
color = pygame.cursors.Cursor((0, 0), surf)

img_logo = pygame.image.load('img/png/main_logo.png').convert_alpha()

bg_menu = pygame.image.load('img/jpg/bg-menu.jpg').convert()
# btns_menu = pygame.image.load('img/png/btns.png').convert_alpha()
btn_1 = pygame.image.load('img/png/buttons/btn1.png').convert_alpha()
btn_2 = pygame.image.load('img/png/buttons/btn2.png').convert_alpha()
btn_3 = pygame.image.load('img/png/buttons/btn3.png').convert_alpha()
btn_1_act = pygame.image.load('img/png/buttons/btn1_act.png') .convert_alpha()
btn_2_act = pygame.image.load('img/png/buttons/btn2_act.png').convert_alpha()
btn_3_act = pygame.image.load('img/png/buttons/btn3_act.png').convert_alpha()
btn_4 = pygame.image.load('img/png/buttons/btn4.png').convert_alpha()
btn_4_act = pygame.image.load('img/png/buttons/btn4_act.png').convert_alpha()

bg_training = pygame.image.load('img/jpg/bg-training.jpg').convert()
gg_heading_right = pygame.image.load('img/png/units/pitonist(r).png')
gg_heading_left = pygame.image.load('img/png/units/pitonist(l).png')

btn_pause = pygame.image.load('img/png/buttons/btn-pause.png').convert_alpha()
btn_restart = pygame.image.load('img/png/buttons/btn-restart.png').convert_alpha()

clock = pygame.time.Clock()
FPS = 60  

b = True

x = 120
y = 620
speed = 4
is_player_heading_right = True





class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_cursor(color)
        pygame.display.set_caption('Мы Русские с нами pygame!')
        pygame.mixer.music.load('music/music_menu.mp3')
        global scene
        scene = Prev()
        while 1:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                scene.e(event)
            scene.draw()

                

            pygame.display.update()

class Prev:
    def draw(self):
        global b
        if b:
            b = False
            screen.blit(img_logo, (230, 170))
        
    def e(self, event):
        global scene
        if event.type == pygame.MOUSEBUTTONUP:
            # pygame.time.delay(800)
            print('01')
            scene = Menu()
            

class Menu:
    def draw(self):
        global b

        if not b:
            b = True
            screen.blit(bg_menu, (0, 0))
            # screen.blit(btns_menu, (38, 99))

        mouse = pygame.mouse.get_pos()
        # click = pygame.mouse.get_pressed()

        if 120 < mouse[0] < 357 and 180 < mouse[1] < 217:
            screen.blit(btn_1_act, (120, 180))
                
        else:
            screen.blit(btn_1, (120, 180))
        if 120 < mouse[0] < 357 and 250 < mouse[1] < 287:
            screen.blit(btn_2_act, (120, 250))
        else:
            screen.blit(btn_2, (120, 250))
        if 120 < mouse[0] < 357 and 320 < mouse[1] < 357:
            screen.blit(btn_3_act, (120, 320))
        else:
            screen.blit(btn_3, (120, 320))

    def e(self, event):
        global scene
        mouse = pygame.mouse.get_pos()

        if 120 < mouse[0] < 357 and 180 < mouse[1] < 217:
            pass
            # if event.type == pygame.MOUSEBUTTONUP: # кампания
            #
        if 120 < mouse[0] < 357 and 250 < mouse[1] < 287:
            if event.type == pygame.MOUSEBUTTONUP:
                     pygame.time.delay(200)
                     scene = Training()
        if 120 < mouse[0] < 357 and 320 < mouse[1] < 357:
            if event.type == pygame.MOUSEBUTTONUP:
                    pygame.time.delay(200)
                    pygame.quit()
                    sys.exit()






class Training:
    def __init__(self):
        gg = GG()
        print('02')

    def draw(self):
        global p
        screen.blit(bg_training, (0, 0))
        screen.blit(btn_pause, (5, 5))
        screen.blit(btn_restart, (45, 5))
        gg = GG()

        
    def e(self, event):
        global scene
        mouse = pygame.mouse.get_pos()
        # click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        if (event.type == pygame.MOUSEBUTTONUP and 5 < mouse[0] < 37 and 5 < mouse[1] < 37) or keys[pygame.K_ESCAPE]:  # PAUSE
            # ПРОРИСОВКА ОСТАНАВЛИВАЕТСЯ!!!ДОЛЖНА ОСТАНАВЛИВАТЬСЯ, но пока сделаю так.
            pygame.time.delay(100)
            scene = Pause()
        if (event.type == pygame.MOUSEBUTTONUP and 45 < mouse[0] < 77 and 5 < mouse[1] < 37) or keys[pygame.K_F5]:  # RESTART
            pygame.time.delay(100)
            # .....................
            # restart прорисовки
            print('ns lt,bk') #  наврятли нужен
        
        
class Pause:
    def draw(self):
        global b, p
        if b:
            b = False
            screen.blit(bg_menu, (0, 0))
            # screen.blit(btns_menu, (38, 99))
        mouse = pygame.mouse.get_pos()
        # click = pygame.mouse.get_pressed()

        if 120 < mouse[0] < 357 and 180 < mouse[1] < 217:
            screen.blit(btn_4_act, (120, 180))
        else:
            screen.blit(btn_4, (120, 180))
        if 120 < mouse[0] < 357 and 250 < mouse[1] < 287:
            screen.blit(btn_2_act, (120, 250))
        else:
            screen.blit(btn_2, (120, 250))
        if 120 < mouse[0] < 357 and 320 < mouse[1] < 357:
            screen.blit(btn_3_act, (120, 320))
        else:
            screen.blit(btn_3, (120, 320))

    def e(self, event):
        global b, scene
        mouse = pygame.mouse.get_pos()

        if 120 < mouse[0] < 357 and 180 < mouse[1] < 217:
            if event.type == pygame.MOUSEBUTTONUP:
                b = True
                scene = Training()
        if 120 < mouse[0] < 357 and 250 < mouse[1] < 287:
            if event.type == pygame.MOUSEBUTTONUP:
                b = True
                pygame.time.delay(200)
                scene = Training()
        if 120 < mouse[0] < 357 and 320 < mouse[1] < 357:
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.time.delay(200)
                pygame.quit()
                sys.exit()

class GG:
    def __init__(self):
        global x, y, speed, is_player_heading_right
        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            is_player_heading_right = True
            x += speed
        if keys[pygame.K_LEFT]:
            is_player_heading_right = False
            x -= speed
        if keys[pygame.K_UP]:
            y -= 4

        if is_player_heading_right:
            screen.blit(gg_heading_right, (x, y)) 
        elif not is_player_heading_right:
            screen.blit(gg_heading_left, (x, y)) 
    

Game()
