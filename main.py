import os
import sys
import pygame_gui
import pygame
import pickle

pygame.init()
SIZE = WEIGHT, HEIGHT = (800, 500)
pygame.display.set_caption("Game. Just game.")
SCREEN = pygame.display.set_mode(SIZE)

FPS = 330


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def remake_level(lvl, next=False):
    if lvl == 1:
        if next:
            level_2()
            return 2
        level_1()
    if lvl == 2:
        if next:
            level_1()
            return 1
        level_2()


def draw_small_background(txt, scrn, bg, color):
    scrn.blit(bg, (300, 130))
    small_background.fill(pygame.Color(50, 50, 50), pygame.Rect(0, 0, 200, 40))
    f = pygame.font.Font(None, 24)
    txt = f.render(txt, True, color)
    text_x = 100 - txt.get_width() // 2
    text_y = 20 - txt.get_height() // 2
    bg.blit(txt, (text_x, text_y))


def draw_menu(bg, group, price):
    bg.fill((200, 200, 200))
    blue, green, red, yellow, brown, coin1, coin2, coin3, coin4 = (pygame.sprite.Sprite(), pygame.sprite.Sprite(),
                                                                   pygame.sprite.Sprite(), pygame.sprite.Sprite(),
                                                                   pygame.sprite.Sprite(), pygame.sprite.Sprite(),
                                                                   pygame.sprite.Sprite(), pygame.sprite.Sprite(),
                                                                   pygame.sprite.Sprite())
    blue.image = load_image("blue_square.png")
    blue.rect = blue.image.get_rect()
    blue.rect.x, blue.rect.y = 157, 300
    green.image = load_image("green_square.png")
    green.rect = green.image.get_rect()
    green.rect.x, green.rect.y = 262, 300
    red.image = load_image("red_square.png")
    red.rect = red.image.get_rect()
    red.rect.x, red.rect.y = 368, 300
    yellow.image = load_image("yellow_square.png")
    yellow.rect = yellow.image.get_rect()
    yellow.rect.x, yellow.rect.y = 472, 300
    brown.image = load_image("brown_square.png")
    brown.rect = brown.image.get_rect()
    brown.rect.x, brown.rect.y = 577, 300
    coin1.image = pygame.transform.scale(load_image('Coin 64-64 1.png', -1), (30, 30))
    coin1.rect = coin1.image.get_rect()
    coin1.rect.x, coin1.rect.y = 719, 3
    coin2.image = pygame.transform.scale(load_image('Coin 64-64 1.png', -1), (30, 30))
    coin2.rect = coin2.image.get_rect()
    coin2.rect.x, coin2.rect.y = 364, 368
    coin3.image = pygame.transform.scale(load_image('Coin 64-64 1.png', -1), (30, 30))
    coin3.rect = coin3.image.get_rect()
    coin3.rect.x, coin3.rect.y = 469, 368
    coin4.image = pygame.transform.scale(load_image('Coin 64-64 1.png', -1), (30, 30))
    coin4.rect = coin4.image.get_rect()
    coin4.rect.x, coin4.rect.y = 574, 368
    f = pygame.font.Font(None, 22)
    t = f.render(str(price[0][0]), True, (20, 20, 20))
    bg.blit(t, (392, 378))
    t = f.render(str(price[1][0]), True, (20, 20, 20))
    bg.blit(t, (497, 378))
    t = f.render(str(price[2][0]), True, (20, 20, 20))
    bg.blit(t, (602, 378))
    group.add(blue, green, red, yellow, brown, coin1, coin2, coin3, coin4)


def buy_and_choose(n, shop, blnc, chosen_sqr, btn):
    if blnc >= squares_in_shop[n][0]:
        all_unselect()
        blnc -= squares_in_shop[n][0]
        squares_in_shop[n][1] = True
        squares_in_shop[n][0] = 0
        chosen_sqr = squares_in_shop[n][2]
        menu_background.fill(pygame.Color(220, 220, 220))
        draw_menu(menu_background, choose_square, squares_in_shop)
    if squares_in_shop[n][1]:
        chosen_sqr = squares_in_shop[n][2]
        all_unselect()
        btn.set_text('Selected')
    return shop, blnc, chosen_sqr


def all_unselect():
    select_blue_square.set_text('Select')
    select_green_square.set_text('Select')
    select_yellow_square.set_text('Select')
    select_brown_square.set_text('Select')
    select_red_square.set_text('Select')


def level_1():
    all_spr = pygame.sprite.Group()
    hor_borders = pygame.sprite.Group()
    vert_borders = pygame.sprite.Group()
    balls_g = pygame.sprite.Group()
    coins_g = pygame.sprite.Group()
    finish_g = pygame.sprite.Group()
    door_g = pygame.sprite.Group()
    key_g = pygame.sprite.Group()
    Finish(700, 200, 100, 100)
    char = Character(10, 225, 50, 6, chosen_square)

    Border(100, 50, 700, 50, 'top')
    Border(700, 50, 700, 200, 'right')
    Border(700, 200, 800, 200, 'top')
    Border(800, 200, 800, 300, 'right')
    Border(700, 300, 800, 300, 'bottom')
    Border(700, 300, 700, 450, 'right')
    Border(100, 450, 700, 450, 'bottom')
    Border(100, 300, 100, 450, 'left')
    Border(0, 200, 100, 200, 'top')
    Border(0, 200, 0, 300, 'left')
    Border(100, 50, 100, 200, 'left')
    Border(0, 300, 100, 300, 'bottom')

    Coin(200, 55, 10)
    Coin(550, 55, 10)
    Coin(375, 55, 10)
    Coin(200, 410, 10)
    Coin(550, 410, 10)
    Coin(375, 410, 10)
    Coin(719, 3, 0, size=30)

    Ball(200, 200, 0, 1.2)
    Ball(550, 200, 0, 1.2)
    Ball(375, 200, 0, -1.2)
    return all_spr, hor_borders, vert_borders, balls_g, coins_g, char, finish_g, door_g, key_g


def level_2():
    all_spr = pygame.sprite.Group()
    hor_borders = pygame.sprite.Group()
    vert_borders = pygame.sprite.Group()
    balls_g = pygame.sprite.Group()
    coins_g = pygame.sprite.Group()
    finish_g = pygame.sprite.Group()
    door_g = pygame.sprite.Group()
    key_g = pygame.sprite.Group()
    Finish(700, 350, 100, 100)
    LockedDoor(650, 350, 30, 100)
    Key(590, 215)
    char = Character(10, 60, 50, 6, chosen_square)

    Border(0, 50, 650, 50, 'top')
    Border(650, 50, 650, 350, 'right')
    Border(650, 350, 800, 350, 'top')
    Border(800, 350, 800, 450, 'right')
    Border(70, 450, 800, 450, 'bottom')
    Border(70, 120, 70, 450, 'left')
    Border(0, 50, 0, 120, 'left')
    Border(0, 120, 70, 120, 'bottom')

    Coin(70, 130, 20)
    Coin(70, 220, 20)
    Coin(70, 310, 20)
    Coin(375, 130, 20)
    Coin(375, 220, 20)
    Coin(375, 310, 20)
    Coin(719, 3, 0, size=30)

    Ball(590, 120, -1, 0)
    Ball(70, 210, 1, 0)
    Ball(590, 300, -1, 0)
    return all_spr, hor_borders, vert_borders, balls_g, coins_g, char, finish_g, door_g, key_g


def hide(btns):
    for btn in btns:
        btn.hide()


def show(btns):
    for btn in btns:
        btn.show()


class Key(pygame.sprite.Sprite):
    image = load_image("Key.jpg", -1)

    def __init__(self, x, y):
        super().__init__(all_sprites)

        self.image = pygame.transform.scale(Key.image, (50, 25))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.add(key_group)

    def update(self):
        if pygame.sprite.collide_mask(self, char):
            char.key = True
            pygame.sprite.spritecollide(char, key_group, True)


class LockedDoor(pygame.sprite.Sprite):
    def __init__(self, x, y, len_x, len_y):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.len_x = len_x
        self.len_y = len_y
        self.color = (200, 200, 200)
        self.image = pygame.Surface((self.len_x, self.len_y))
        self.image.fill(self.color)
        self.rect = pygame.Rect(self.x, self.y, self.len_x, self.len_y)
        self.add(door_group)


class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y, len_x, len_y):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.len_x = len_x
        self.len_y = len_y
        self.color = (200, 255, 200)
        self.image = pygame.Surface((self.len_x, self.len_y))
        self.image.fill(self.color)
        self.rect = pygame.Rect(self.x, self.y, self.len_x, self.len_y)
        self.add(finish_group)


class Ball(pygame.sprite.Sprite):
    image = load_image("spear3.png", -1)

    def __init__(self, x, y, vx, vy):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(Ball.image, (60, 60))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy
        self.add(balls_group)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
        if pygame.sprite.collide_mask(self, char):
            global gameover, game
            gameover = True
            game = False
            show([restart_btn, main_menu_btn])
            gameover_sound.play()


class Coin(pygame.sprite.Sprite):
    image = load_image("Coin 64-64 1.png", -1)

    def __init__(self, x, y, points, size=37):
        super().__init__(all_sprites)
        self.points = points
        self.image = pygame.transform.scale(Coin.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.add(coins_group)

    def update(self):
        if pygame.sprite.collide_mask(self, char):
            pygame.sprite.spritecollide(char, coins_group, True)
            char.collected_coins += 1
            global balance
            balance += self.points
            coin_sound.play()


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, sz, coins, image):
        super().__init__(all_sprites)
        self.size = sz
        self.coins = coins
        self.collected_coins = 0
        self.key = False
        self.image = pygame.transform.scale(load_image(image), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, direction):
        if direction == 'right':
            self.rect.x += 1
        elif direction == 'left':
            self.rect.x -= 1
        elif direction == 'up':
            self.rect.y -= 1
        elif direction == 'down':
            self.rect.y += 1

    def update(self):
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.rect.y += pygame.sprite.spritecollideany(self, horizontal_borders).coeff
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.rect.x += pygame.sprite.spritecollideany(self, vertical_borders).coeff
        if pygame.sprite.spritecollideany(self, finish_group) and self.coins == self.collected_coins:
            global win, game
            win = True
            game = False
            show([restart_btn, main_menu_btn, next_btn])
            win_sound.play()
        if pygame.sprite.spritecollideany(self, door_group) and not self.key:
            self.rect.x -= 1


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, side):
        super().__init__(all_sprites)
        if side == 'right' or side == 'bottom':
            self.coeff = -1
        else:
            self.coeff = 1
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


chosen_square = "blue_square.png"
squares_in_shop = [[50, False, 'red_square.png'], [140, False, 'yellow_square.png'], [200, False, 'brown_square.png']]

manager = pygame_gui.UIManager(SIZE)
restart_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 185), (100, 20)), text='Restart',
                                           manager=manager)
main_menu_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 230), (100, 20)), text='Main menu',
                                             manager=manager)
next_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 213), (100, 20)), text='Next',
                                        manager=manager)
continue_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 208), (100, 20)), text='Continue',
                                            manager=manager)
pause_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (22, 22)), text='||',
                                         manager=manager)
level_1_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 100), (100, 20)), text='1 level',
                                           manager=manager)
level_2_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 150), (100, 20)), text='2 level',
                                           manager=manager)
select_blue_square = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 400), (80, 20)), text='Select',
                                                  manager=manager)
select_green_square = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((255, 400), (80, 20)), text='Select',
                                                   manager=manager)
select_red_square = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((360, 400), (80, 20)), text='Select',
                                                 manager=manager)
select_yellow_square = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((465, 400), (80, 20)), text='Select',
                                                    manager=manager)
select_brown_square = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((570, 400), (80, 20)), text='Select',
                                                   manager=manager)

hide([restart_btn, next_btn, main_menu_btn, pause_btn, restart_btn, continue_btn])

small_background = pygame.Surface((200, 150))  # бг для паузы, победы и проигрыша
small_background.fill(pygame.Color(220, 220, 220))
small_background.fill(pygame.Color(50, 50, 50), pygame.Rect(0, 0, 200, 40))

menu_background = pygame.Surface(SIZE)  # бг для меню
menu_background.fill(pygame.Color(220, 220, 220))

all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
balls_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()
finish_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
key_group = pygame.sprite.Group()
choose_square = pygame.sprite.Group()
cursor_group = pygame.sprite.Group()
draw_menu(menu_background, choose_square, squares_in_shop)
char = Character(0, 0, 0, 0, chosen_square)

font = pygame.font.Font(None, 26)
coin_sound = pygame.mixer.Sound('data/Coin.mp3')
gameover_sound = pygame.mixer.Sound('data/death.mp3')
win_sound = pygame.mixer.Sound('data/win.mp3')
pygame.mixer.music.load('data/Menu.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

cursor = pygame.sprite.Sprite()
cursor.image = pygame.transform.scale(load_image("cursor1.png"), (50, 50))
cursor.rect = cursor.image.get_rect()
cursor_group.add(cursor)

current_level = 0
balance = 0
mute = False
pause = False
game = False
menu = True
gameover = False
win = False
clock = pygame.time.Clock()
running = True
while running:
    SCREEN.fill('white')
    time_delta = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not pause and game:
                show([continue_btn, restart_btn, main_menu_btn])
                pause = True
                game = False
            elif event.key == pygame.K_ESCAPE and pause and not game:
                hide([continue_btn, restart_btn, main_menu_btn])
                pause = False
                game = True
            elif event.key == pygame.K_m and not mute:
                coin_sound.set_volume(0)
                win_sound.set_volume(0)
                gameover_sound.set_volume(0)
                pygame.mixer.music.set_volume(0)
                mute = True
            elif event.key == pygame.K_m and mute:
                coin_sound.set_volume(1)
                win_sound.set_volume(1)
                gameover_sound.set_volume(1)
                pygame.mixer.music.set_volume(0.2)
                mute = False
            elif event.key == pygame.K_s and event.mod & pygame.KMOD_CTRL:
                with open("data/save.dat", 'wb') as file:
                    pickle.dump((chosen_square, squares_in_shop, balance), file)
            elif event.key == pygame.K_l and event.mod & pygame.KMOD_CTRL:
                with open("data/save.dat", 'rb') as file:
                    unpickler = pickle.Unpickler(file)
                    if len(file.read()) != 0:
                        chosen_square, squares_in_shop, balance = unpickler.load()
                draw_menu(menu_background, choose_square, squares_in_shop)
                if chosen_square == 'blue_square.png':
                    select_blue_square.set_text('Selected')
                elif chosen_square == 'green_square.png':
                    select_green_square.set_text('Selected')
                elif chosen_square == 'yellow_square.png':
                    select_yellow_square.set_text('Selected')
                elif chosen_square == 'red_square.png':
                    select_red_square.set_text('Selected')
                else:
                    select_brown_square.set_text('Selected')
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == restart_btn:
                    remake_level(current_level)
                    hide([restart_btn, next_btn, main_menu_btn, restart_btn, continue_btn])
                    pause, gameover, win = False, False, False
                    game = True
                if event.ui_element == main_menu_btn:
                    hide([restart_btn, next_btn, main_menu_btn, pause_btn, restart_btn, continue_btn])
                    show([level_2_btn, level_1_btn, select_blue_square, select_green_square, select_brown_square,
                          select_yellow_square, select_red_square])
                    game, pause, gameover, win = False, False, False, False
                    menu = True
                if event.ui_element == continue_btn:
                    hide([continue_btn, restart_btn, main_menu_btn])
                    game = True
                    pause = False
                if event.ui_element == pause_btn:
                    if pause:
                        hide([continue_btn, restart_btn, main_menu_btn])
                        pause = True
                        game = False
                    else:
                        show([continue_btn, restart_btn, main_menu_btn])
                        pause = True
                        game = False
                if event.ui_element == next_btn:
                    current_level = remake_level(current_level, True)
                    hide([next_btn, restart_btn, main_menu_btn])
                    game = True
                    win = False
                if event.ui_element == level_1_btn:
                    level_1()
                    show([pause_btn])
                    hide([level_2_btn, level_1_btn, select_blue_square, select_green_square, select_brown_square,
                          select_yellow_square, select_red_square])
                    current_level = 1
                    menu = False
                    game = True
                if event.ui_element == level_2_btn:
                    level_2()
                    show([pause_btn])
                    hide([level_2_btn, level_1_btn, select_blue_square, select_green_square, select_brown_square,
                          select_yellow_square, select_red_square])
                    current_level = 2
                    menu = False
                    game = True
                if event.ui_element == select_blue_square:
                    chosen_square = "blue_square.png"
                    all_unselect()
                    select_blue_square.set_text('Selected')
                if event.ui_element == select_green_square:
                    chosen_square = "green_square.png"
                    all_unselect()
                    select_green_square.set_text('Selected')
                if event.ui_element == select_red_square:
                    squares_in_shop, balance, chosen_square = buy_and_choose(0, squares_in_shop, balance, chosen_square,
                                                                             select_red_square)
                if event.ui_element == select_yellow_square:
                    squares_in_shop, balance, chosen_square = buy_and_choose(1, squares_in_shop, balance, chosen_square,
                                                                             select_yellow_square)
                if event.ui_element == select_brown_square:
                    squares_in_shop, balance, chosen_square = buy_and_choose(2, squares_in_shop, balance, chosen_square,
                                                                             select_brown_square)
        manager.process_events(event)
    if game:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            char.move('up')
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            char.move('left')
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            char.move('down')
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            char.move('right')
        all_sprites.update()
    manager.update(time_delta)
    manager.draw_ui(SCREEN)
    all_sprites.draw(SCREEN)
    if pause:
        draw_small_background("Pause", SCREEN, small_background, (150, 150, 255))
    if menu:
        SCREEN.blit(menu_background, (0, 0))
        choose_square.draw(SCREEN)
    if gameover:
        draw_small_background("Try again!", SCREEN, small_background, (255, 100, 100))
    if win:
        draw_small_background("Congrats! You win", SCREEN, small_background, (150, 255, 150))
    text = font.render(str(balance), True, (20, 20, 20))
    SCREEN.blit(text, (750, 10))
    manager.update(time_delta)
    manager.draw_ui(SCREEN)
    if pygame.mouse.get_focused():  # курсор
        cursor.rect.x, cursor.rect.y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        cursor_group.draw(SCREEN)
    pygame.display.flip()

pygame.quit()
