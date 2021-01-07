import os
import sys
import pygame_gui
import pygame

pygame.init()
size = weight, height = (800, 500)
screen = pygame.display.set_mode(size)


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


def level_1():
    global all_sprites, horizontal_borders, vertical_borders, balls_group, coins_group, char, finish_group
    all_sprites = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    balls_group = pygame.sprite.Group()
    coins_group = pygame.sprite.Group()
    finish_group = pygame.sprite.Group()
    Finish(700, 200, 100, 100, 6)
    char = Character(10, 225, 50, 6)
    screen.fill(pygame.Color(155, 255, 220), pygame.Rect(0, 200, 100, 100))

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

    Coin(200, 55)
    Coin(550, 55)
    Coin(375, 55)
    Coin(200, 410)
    Coin(550, 410)
    Coin(375, 410)

    Ball(200, 200, 0, 1.2)
    Ball(550, 200, 0, 1.2)
    Ball(375, 200, 0, -1.2)


class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y, len_x, len_y, coins):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.coins = coins
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

        self.image = pygame.transform.scale(Ball.image, (65, 65))
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


class Coin(pygame.sprite.Sprite):
    image = load_image("Coin 64-64 1.png", -1)

    def __init__(self, x, y, points=10):
        super().__init__(all_sprites)
        self.points = points
        self.image = Coin.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.add(coins_group)

    def update(self):
        if pygame.sprite.collide_mask(self, char):
            pygame.sprite.spritecollide(char, coins_group, True)
            char.coins += 1
            coin_sound.play()


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, sz, coins):
        super().__init__(all_sprites)
        self.size = sz
        self.x = x
        self.y = y
        self.coins = coins
        self.color = (220, 220, 255)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self, direction):
        if direction == 'right':
            self.x += 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.y = int(self.y) + pygame.sprite.spritecollideany(self, horizontal_borders).coeff
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.x = int(self.x) + pygame.sprite.spritecollideany(self, vertical_borders).coeff
        if pygame.sprite.spritecollideany(self, finish_group) and\
                self.coins == pygame.sprite.spritecollideany(self, finish_group).coins:
            global win, game
            win = True
            game = False


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

small_background = pygame.Surface((200, 250))  # бг для паузы, победы и проигрыша
small_background.fill(pygame.Color(220, 220, 220))
small_background.fill(pygame.Color(50, 50, 50), pygame.Rect(0, 0, 200, 40))

menu_background = pygame.Surface(size)
menu_background.fill(pygame.Color(220, 220, 220))

gameover_btn1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 200), (100, 20)),
    text='Restart',
    manager=gameover_manager
)
gameover_btn2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 250), (100, 20)),
    text='Main menu',
    manager=gameover_manager
)
win_btn1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 190), (100, 20)),
    text='Next level',
    manager=win_manager
)
win_btn2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 220), (100, 20)),
    text='Restart',
    manager=win_manager
)
win_btn3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 250), (100, 20)),
    text='Main menu',
    manager=win_manager
)
menu_btn1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 190), (100, 20)),
    text='1 level',
    manager=menu_manager
)
game_btn = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (25, 25)),
    text='||',
    manager=game_manager
)
pause_btn1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 190), (100, 20)),
    text='Continue',
    manager=pause_manager
)
pause_btn2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 220), (100, 20)),
    text='Restart',
    manager=pause_manager
)
pause_btn3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 250), (100, 20)),
    text='Main menu',
    manager=pause_manager
)

all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
balls_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()
finish_group = pygame.sprite.Group()
char = Character(0, 0, 0, 0)
coin_sound = pygame.mixer.Sound('data/Coin.mp3')
# финиш, проигрыш, выигрыш, пару уровней, (кастом квадратика), громкость музыки, курсор
pygame.mixer.music.load('data/Menu.mp3')
pygame.mixer.music.play()
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
            if event.key == pygame.K_ESCAPE and not pause:
                pause = True
                game = False
            elif event.key == pygame.K_ESCAPE and pause:
                pause = False
                game = True

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pause_btn1:
                    pause = False
                    game = True
                if event.ui_element == pause_btn2:
                    level_1()
                    pause = False
                    game = True
                if event.ui_element == game_btn:
                    pause = True
                    game = False
                if event.ui_element == pause_btn3:
                    pause = False
                    menu = True
                    pygame.mixer.music.load('data/Menu.mp3')
                    pygame.mixer.music.play()
                if event.ui_element == menu_btn1:
                    level_1()
                    game = True
                    menu = False
                    pygame.mixer.music.load('data/Spider Dance.mp3')
                    pygame.mixer.music.play()
                if event.ui_element == gameover_btn1:
                    level_1()
                    game = True
                    gameover = False
                if event.ui_element == gameover_btn2:
                    gameover = False
                    menu = True
                    pygame.mixer.music.load('data/Menu.mp3')
                    pygame.mixer.music.play()
                if event.ui_element == win_btn2:
                    level_1()
                    win = False
                    game = True
                if event.ui_element == win_btn3:
                    menu = True
                    win = False
                    pygame.mixer.music.load('data/Menu.mp3')
                    pygame.mixer.music.play()
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
        if keys[pygame.K_UP]:
            char.move('up')
        if keys[pygame.K_LEFT]:
            char.move('left')
        if keys[pygame.K_DOWN]:
            char.move('down')
        if keys[pygame.K_RIGHT]:
            char.move('right')
        all_sprites.update()
    game_manager.update(time_delta)
    game_manager.draw_ui(screen)
    all_sprites.draw(screen)

    if pause:
        screen.blit(small_background, (300, 100))
        pause_manager.update(time_delta)
        pause_manager.draw_ui(screen)
    if menu:
        screen.blit(menu_background, (0, 0))
        menu_manager.update(time_delta)
        menu_manager.draw_ui(screen)
    if gameover:
        screen.blit(small_background, (300, 100))
        gameover_manager.update(time_delta)
        gameover_manager.draw_ui(screen)
    if win:
        screen.blit(small_background, (300, 100))
        win_manager.update(time_delta)
        win_manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()
