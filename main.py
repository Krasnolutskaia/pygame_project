import os
import sys
import pygame_gui
import pygame
import pickle

pygame.init()
size = weight, height = (800, 500)
pygame.display.set_caption("Game. Just game.")
screen = pygame.display.set_mode(size)
chosen_square = "blue_square.png"
squares = [[50, False, 'red_square.png'], [140, False, 'yellow_square.png'], [200, False, 'brown_square']]


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


def check_current_level():
    if current_level == 1:
        level_1()
    if current_level == 2:
        level_2()


def draw_small_background(mngr):
    screen.blit(small_background, (300, 130))
    small_background.fill(pygame.Color(50, 50, 50), pygame.Rect(0, 0, 200, 40))
    font = pygame.font.Font(None, 24)
    if mngr == pause_manager:
        text = font.render("Pause", True, (150, 150, 255))
    if mngr == gameover_manager:
        text = font.render("Try again!", True, (255, 100, 100))
    if mngr == win_manager:
        text = font.render("Congrats! You win!", True, (150, 255, 150))
    text_x = 100 - text.get_width() // 2
    text_y = 20 - text.get_height() // 2
    small_background.blit(text, (text_x, text_y))


def char_custom():
    menu_background.fill((200, 200, 200))
    global choose_square, squares
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
    font = pygame.font.Font(None, 22)
    text = font.render(str(squares[0][0]), True, (20, 20, 20))
    menu_background.blit(text, (392, 378))
    text = font.render(str(squares[1][0]), True, (20, 20, 20))
    menu_background.blit(text, (497, 378))
    text = font.render(str(squares[2][0]), True, (20, 20, 20))
    menu_background.blit(text, (602, 378))
    choose_square.add(blue, green, red, yellow, brown, coin1, coin2, coin3, coin4)


def buy(n):
    global squares, balance, chosen_square
    if squares[n][1]:
        chosen_square = squares[n][2]
    elif balance >= squares[n][0]:
        all_unselect()
        balance -= squares[n][0]
        squares[n][1] = True
        squares[n][0] = 0
        chosen_square = squares[n][2]
        menu_background.fill(pygame.Color(220, 220, 220))
        char_custom()


def all_unselect():
    select_blue_square.set_text('Select')
    select_green_square.set_text('Select')
    select_yellow_square.set_text('Select')
    select_brown_square.set_text('Select')
    select_red_square.set_text('Select')


def level_1():
    global all_sprites, horizontal_borders, vertical_borders, balls_group, coins_group, char, finish_group, door_group
    all_sprites = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    balls_group = pygame.sprite.Group()
    coins_group = pygame.sprite.Group()
    finish_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    Finish(700, 200, 100, 100)
    char = Character(10, 225, 50, 6)

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


def level_2():
    global all_sprites, horizontal_borders, vertical_borders, balls_group, coins_group, char, finish_group, key_group, \
        door_group
    all_sprites = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    balls_group = pygame.sprite.Group()
    coins_group = pygame.sprite.Group()
    finish_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    Finish(700, 350, 100, 100)
    LockedDoor(650, 350, 30, 100)
    Key(590, 215)
    char = Character(10, 60, 50, 6)

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
    def __init__(self, x, y, sz, coins):
        super().__init__(all_sprites)
        self.size = sz
        self.coins = coins
        self.collected_coins = 0
        self.key = False
        self.image = pygame.transform.scale(load_image(chosen_square), (50, 50))
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


menu_manager = pygame_gui.UIManager(size)  # менеджер для ГИ в главном меню
game_manager = pygame_gui.UIManager(size)  # менеджер для ГИ во время прохождения уровня
pause_manager = pygame_gui.UIManager(size)  # менеджер для ГИ во время паузы
gameover_manager = pygame_gui.UIManager(size)  # менеджер для ГИ проигрыша
win_manager = pygame_gui.UIManager(size)  # менеджер для ГИ победы

small_background = pygame.Surface((200, 150))  # бг для паузы, победы и проигрыша
small_background.fill(pygame.Color(220, 220, 220))
small_background.fill(pygame.Color(50, 50, 50), pygame.Rect(0, 0, 200, 40))

menu_background = pygame.Surface(size)
menu_background.fill(pygame.Color(220, 220, 220))

gameover_btn1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 195), (100, 20)),
    text='Restart',
    manager=gameover_manager)
gameover_btn2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 230), (100, 20)),
    text='Main menu',
    manager=gameover_manager)
win_btn3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 185), (100, 20)),
    text='Next',
    manager=win_manager)
win_btn1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 213), (100, 20)),
    text='Restart',
    manager=win_manager)
win_btn2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 240), (100, 20)),
    text='Main menu',
    manager=win_manager)
menu_btn1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 100), (100, 20)),
    text='1 level',
    manager=menu_manager)
menu_btn2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 150), (100, 20)),
    text='2 level',
    manager=menu_manager)
select_blue_square = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((150, 400), (80, 20)),
    text='Select',
    manager=menu_manager)
select_green_square = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((255, 400), (80, 20)),
    text='Select',
    manager=menu_manager)
select_red_square = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((360, 400), (80, 20)),
    text='Select',
    manager=menu_manager)
select_yellow_square = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((465, 400), (80, 20)),
    text='Select',
    manager=menu_manager)
select_brown_square = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((570, 400), (80, 20)),
    text='Select',
    manager=menu_manager)
game_btn = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (25, 25)),
    text='||',
    manager=game_manager)
pause_btn1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 185), (100, 20)),
    text='Continue',
    manager=pause_manager)
pause_btn2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 213), (100, 20)),
    text='Restart',
    manager=pause_manager)
pause_btn3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 240), (100, 20)),
    text='Main menu',
    manager=pause_manager)

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
char_custom()
char = Character(0, 0, 0, 0)

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
fps = 330
clock = pygame.time.Clock()
running = True
while running:
    screen.fill('white')
    time_delta = clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not pause and game:
                pause = True
                game = False
            elif event.key == pygame.K_ESCAPE and pause and not game:
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
                    pickle.dump((chosen_square, squares, balance), file)
            elif event.key == pygame.K_l and event.mod & pygame.KMOD_CTRL:
                with open("data/save.dat", 'rb') as file:
                    unpickler = pickle.Unpickler(file)
                    chosen_square, squares, balance = unpickler.load()
                char_custom()
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
                if event.ui_element == pause_btn1:
                    pause = False
                    game = True
                if event.ui_element == pause_btn2:
                    pause = False
                    game = True
                    check_current_level()
                if event.ui_element == game_btn:
                    pause = True
                    game = False
                if event.ui_element == pause_btn3:
                    pause = False
                    menu = True
                    pygame.mixer.music.load('data/Menu.mp3')
                    pygame.mixer.music.play(-1)
                if event.ui_element == menu_btn1:
                    level_1()
                    current_level = 1
                    game = True
                    menu = False
                    pygame.mixer.music.load('data/Spider Dance.mp3')
                    pygame.mixer.music.play(-1)
                if event.ui_element == menu_btn2:
                    level_2()
                    current_level = 2
                    game = True
                    menu = False
                    pygame.mixer.music.load('data/Spider Dance.mp3')
                    pygame.mixer.music.play(-1)
                if event.ui_element == gameover_btn1:
                    game = True
                    gameover = False
                    check_current_level()
                if event.ui_element == gameover_btn2:
                    gameover = False
                    menu = True
                    pygame.mixer.music.load('data/Menu.mp3')
                    pygame.mixer.music.play(-1)
                if event.ui_element == win_btn3:
                    if current_level == 1:
                        level_2()
                        current_level = 2
                    elif current_level == 2:
                        level_1()
                        current_level = 1
                    win = False
                    game = True
                if event.ui_element == win_btn1:
                    win = False
                    game = True
                    check_current_level()
                if event.ui_element == win_btn2:
                    menu = True
                    win = False
                    pygame.mixer.music.load('data/Menu.mp3')
                    pygame.mixer.music.play(-1)
                if event.ui_element == select_blue_square:
                    chosen_square = "blue_square.png"
                    all_unselect()
                    select_blue_square.set_text('Selected')
                if event.ui_element == select_green_square:
                    chosen_square = "green_square.png"
                    all_unselect()
                    select_green_square.set_text('Selected')
                if event.ui_element == select_red_square:
                    buy(0)
                    if squares[0][1]:
                        all_unselect()
                        select_red_square.set_text('Selected')
                if event.ui_element == select_yellow_square:
                    buy(1)
                    if squares[1][1]:
                        all_unselect()
                        select_yellow_square.set_text('Selected')
                if event.ui_element == select_brown_square:
                    buy(2)
                    if squares[2][1]:
                        all_unselect()
                        select_brown_square.set_text('Selected')
        if game:
            game_manager.process_events(event)
        if pause:
            pause_manager.process_events(event)
        if menu:
            menu_manager.process_events(event)
        if gameover:
            gameover_manager.process_events(event)
        if win:
            win_manager.process_events(event)

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
    game_manager.update(time_delta)
    game_manager.draw_ui(screen)
    all_sprites.draw(screen)
    if pause:
        draw_small_background(pause_manager)
        pause_manager.update(time_delta)
        pause_manager.draw_ui(screen)
    if menu:
        screen.blit(menu_background, (0, 0))
        choose_square.draw(screen)
        menu_manager.update(time_delta)
        menu_manager.draw_ui(screen)
    if gameover:
        draw_small_background(gameover_manager)
        gameover_manager.update(time_delta)
        gameover_manager.draw_ui(screen)
    if win:
        draw_small_background(win_manager)
        win_manager.update(time_delta)
        win_manager.draw_ui(screen)
    if pygame.mouse.get_focused():
        cursor.rect.x, cursor.rect.y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        cursor_group.draw(screen)
    text = font.render(str(balance), True, (20, 20, 20))
    screen.blit(text, (750, 10))
    pygame.display.flip()

pygame.quit()
