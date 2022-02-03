import pygame, sys
from random import randrange
import webbrowser

# pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((1423, 800))
icon_logo = pygame.image.load('img/png/icon.png')
pygame.display.set_icon(icon_logo)
surf = pygame.image.load('img/png/cursor.png')
color = pygame.cursors.Cursor((0, 0), surf)

prev_logo = pygame.image.load('img/png/main_logo.png').convert_alpha()
bg_menu = pygame.image.load('img/jpg/bg-menu.jpg').convert()
# btns_menu = pygame.image.load('img/png/btns.png').convert()
btn_1 = pygame.image.load('img/png/buttons/btn1.png').convert()
btn_2 = pygame.image.load('img/png/buttons/btn2.png').convert()
btn_3 = pygame.image.load('img/png/buttons/btn3.png').convert()
btn_1_act = pygame.image.load('img/png/buttons/btn1_act.png').convert()
btn_2_act = pygame.image.load('img/png/buttons/btn2_act.png').convert()
btn_3_act = pygame.image.load('img/png/buttons/btn3_act.png').convert()
btn_4 = pygame.image.load('img/png/buttons/btn4.png').convert()
btn_4_act = pygame.image.load('img/png/buttons/btn4_act.png').convert()

bg_training = pygame.image.load('img/jpg/bg-training.jpg').convert()
gg_heading_right = pygame.image.load('img/png/units/pitonist(r).png').convert_alpha()  
gg_heading_left = pygame.image.load('img/png/units/pitonist(l).png').convert_alpha()
US_heading_right = pygame.image.load('img/png/units/US(r).png').convert_alpha()
US_heading_left = pygame.image.load('img/png/units/US(l).png').convert_alpha()
js_heading_right = pygame.image.load('img/png/units/js(r).png').convert_alpha()
js_heading_left = pygame.image.load('img/png/units/js(l).png').convert_alpha()
box_with_guns = pygame.image.load('img/png/units/box.png').convert()
pitonist_with_USGUN_right = pygame.image.load('img/png/units/units-with-guns/pitonist-with-USGUN(r).png').convert_alpha()
pitonist_with_USGUN_left = pygame.image.load('img/png/units/units-with-guns/pitonist-with-USGUN(l).png').convert_alpha()
js_with_USGUN_right = pygame.image.load('img/png/units/units-with-guns/js-with-USGUN(r).png').convert_alpha()
js_with_USGUN_left = pygame.image.load('img/png/units/units-with-guns/js-with-USGUN(l).png').convert_alpha()

reclame = pygame.image.load('img/jpg/реклама.jpg').convert()

btn_pause = pygame.image.load('img/png/buttons/btn-pause.png').convert()
btn_restart = pygame.image.load('img/png/buttons/btn-restart.png').convert()

clock = pygame.time.Clock()
FPS = 60  

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

class Prev:
    def __init__(self):
        self.b = True

    def draw(self):
        if self.b:
            self.b = False
            for i in range(0, 255):
                screen.fill((0))
                prev_logo.set_alpha(i)  
                screen.blit(prev_logo, (230, 170))
                pygame.display.update(230, 170, 800, 460)    

    def e(self, event):
        global scene
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.time.delay(500)
            print('01')
            scene = Menu()     

class Menu:
    def __init__(self):
        self.b = True

    def draw(self):
        if self.b:
            self.b = False
            screen.blit(bg_menu, (0, 0))
            # screen.blit(btns_menu, (38, 99))

        mouse = pygame.mouse.get_pos()
        
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
        pygame.display.update()

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
        self.gg = GG()
        self.reclame = Reclame()
        print('02')

    def draw(self):
        screen.blit(bg_training, (0, 0))
        screen.blit(btn_pause, (5, 5))
        screen.blit(btn_restart, (45, 5))
        self.gg.draw()
        if not 1 <= self.reclame.t2 <= 9:
            self.gg.physics() == False
        self.reclame.draw()
        pygame.display.update()
        # pygame.display.update(gg.x, gg.y, gg.x, gg.y)

    def e(self, event):
        global scene
        mouse = pygame.mouse.get_pos()
        # click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        if (event.type == pygame.MOUSEBUTTONUP and 5 < mouse[0] < 37 and 5 < mouse[1] < 37) or keys[pygame.K_ESCAPE]:  # PAUSE
            # ПРОРИСОВКА ОСТАНАВЛИВАЕТСЯ!!!ДОЛЖНА ОСТАНАВЛИВАТЬСЯ, но пока сделаю так.
            scene = Pause()

        if (event.type == pygame.MOUSEBUTTONUP and 45 < mouse[0] < 77 and 5 < mouse[1] < 37) or keys[pygame.K_F5]:  # RESTART
            pygame.time.delay(100)
            scene = Training()
            # restart прорисовки
            print('ns lt,bk') #  наврятли нужен

        self.reclame.e(event)
        self.gg.e(event)

class Reclame:
    def __init__(self):
        self.t1 = 20
        self.t2 = 10
        self.timer = pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.Font('1.ttf', 20)

    def draw(self):
        if self.t1 != 0:
            timer_text = self.font.render('Реклама через  ' + str(self.t1), True, ((0)))
            screen.blit(timer_text, (1200, 20))
        else:
            if self.t2 != 0:
                    screen.blit(reclame, (10, 0))
                    screen.blit(self.font.render('Купить PREMIUM', True, (255, 215, 0)), (1200, 20))

    def e(self, event):
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.USEREVENT: 
            if self.t1 == 0:
                if self.t2 != 0:
                    self.timer = pygame.time.set_timer(pygame.USEREVENT, 1000)
                    self.t2 -= 1
            else:
                self.t1 -= 1
        if 0 < self.t2 < 10:
            if event.type == pygame.MOUSEBUTTONDOWN and 1200 < mouse[0] < 1400 and 20 < mouse[1] < 50:
                print('03')
                webbrowser.open('https://usual-browser-game-premium.web.app/hack-bank-account.html', new=0, autoraise=True)

class Pause:
    def __init__(self):
        self.b = True

    def draw(self):
        if self.b:
            self.b = False
            screen.blit(bg_menu, (0, 0))
            # screen.blit(btns_menu, (38, 99))
        mouse = pygame.mouse.get_pos()

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
        pygame.display.update()

    def e(self, event):
        global scene
        mouse = pygame.mouse.get_pos()

        if 120 < mouse[0] < 357 and 180 < mouse[1] < 217:
            if event.type == pygame.MOUSEBUTTONUP:
                self.b = True
                scene = Training()
        if 120 < mouse[0] < 357 and 250 < mouse[1] < 287:
            if event.type == pygame.MOUSEBUTTONUP:
                self.b = True
                pygame.time.delay(200)
                scene = Training()
        if 120 < mouse[0] < 357 and 320 < mouse[1] < 357:
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.time.delay(200)
                pygame.quit()
                sys.exit()

class GG:
    def __init__(self):

        self.x = 120
        self.y = 320
        self.image = [gg_heading_right, gg_heading_left]
        self.is_player_heading_right = True
        self.V = [0, 0]
        self.acceleration = [0, 0]
        self.guns = Guns()
        self.collision = False

        self.g = 0

    def draw(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            self.image = [gg_heading_right, gg_heading_left]
        if keys[pygame.K_2]:
            self.image = [js_heading_right, js_heading_left]
        if keys[pygame.K_3]:
            self.image = [US_heading_right, US_heading_left]

        if self.is_player_heading_right:
            screen.blit(self.image[0], (self.x, self.y)) 
        elif not self.is_player_heading_right:
            screen.blit(self.image[1], (self.x, self.y)) 

    def physics(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.is_player_heading_right = True
            self.x = (self.x + 80) % (1423 + 80) - 80
            if self.V[0] <= 10:
                self.V[0] += 2

        if keys[pygame.K_LEFT]:
            self.is_player_heading_right = False
            self.x = (self.x + 80) % (1423 + 80) - 80
            if self.V[0] >= -10:
                self.V[0] -= 2

        self.y += round(self.V[1]) 
        self.x += round(self.V[0])

        self.V[0] += self.acceleration[0] 
        self.V[1] += self.acceleration[1] 
        self.V[0] *= 0.90
        self.V[1] *= 0.99

        if keys[pygame.K_SPACE]:
            if self.y == 675: 
                self.V[1] -= 20
        self.guns.box()
        # 
        # print(self.guns.x_box, self.guns.y_box)
        if self.y > 675: 
            self.y = 675 
            self.acceleration[1] = 0 
            if self.V[1] > 4: 
                self.V[1] = -self.V[1]/8 
            else: 
                self.V[1] = 0 
        elif self.y < 675: 
            self.acceleration[1] = 1 

        if self.guns.time == 0:
            if self.y + 122 >= self.guns.y_box:
                if self.guns.x_box <= self.x <= self.guns.x_box + 48:
                    self.collision = True
                    self.g +=1 
                    print(self.g)
                elif self.guns.x_box <= self.x + 70 <= self.guns.x_box + 48:
                    self.collision = True
                    self.g +=1 
                    print(self.g)

        if self.collision:
            if self.image == [gg_heading_right, gg_heading_left]:
                self.image = [pitonist_with_USGUN_right, pitonist_with_USGUN_left]
                self.collision = False
            if self.image == [js_heading_right, js_heading_left]:
                self.image = [js_with_USGUN_right, js_with_USGUN_left]
                self.collision = False

    def e(self, event):
        self.guns.e(event)





class Guns:
    def __init__(self):
        self.x_box = randrange(20, 1400)
        self.y_box = randrange(100, 500)
        self.V = 20
        self.acceleration = 0
        self.time = randrange(1, 12)
        self.timer = pygame.time.set_timer(pygame.USEREVENT, 1000)

    def box(self):
        if self.time == 0:
            screen.blit(box_with_guns, (self.x_box, self.y_box))
            self.y_box += round(self.V) 
            self.V += self.acceleration
            self.V *= 1.03

            if self.y_box > 745: 
                self.y_box = 745
                self.acceleration = 0
                if self.V > 35: 
                    self.V = -self.V/8
                else: 
                    self.V = 0 
            elif self.y_box < 675: 
                self.acceleration = 1
        
            
    def e(self, event):
        if event.type == pygame.USEREVENT:
            if self.time != 0:
                self.time -= 1

    def shot(self):
        keys = pygame.key.get_pressed()
        pass
        
    

game = Game()

