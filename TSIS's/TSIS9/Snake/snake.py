'''
Размер меню: 650x650
-------------------------------------------------

                Главное Меню:
                                Лучший результат
                   Start
                   Exit
                                    Общие очки

Exit - выход из игры
-------------------------------------------------

                  Старт Меню:
                                Лучший результат

        >1 Player<            >2 Player<

            <- Back to main menu

                                    Общие очки

-------------------------------------------------
                
                >1 Player< Меню
                                Лучший результат

                    >Easy<

                    >Medium<

                    >Hard<
                    
                                    Общие очки

-------------------------------------------------
                
                >2 Player< Меню
                                Лучший результат

                    >Easy<

                    >Medium<

                    >Hard<
                    
                                    Общие очки

-------------------------------------------------
Сложность Easy:
    1 Player:
        Размер карты: 650x650
        Скорость: обычная(8 FPS)
        Стены: нет
        Яблок: 3

    2 Player:
        Размер карты: 1050x650
        Скорость: обычная(8 FPS)
        Стены: нет
        Яблок: 5
-------------------------------------------------------------------------

Сложность Medium:
    1 Player:
        Размер карты: 650x650
        Скорость: ускоряющаяся(8 FPS, +1 после каждого второго яблока)
        Стены: есть
        Яблок: 2
    
    2 Player:
        Размер карты: 1050x650
        Скорость: ускоряющаяся(8 FPS, +1 после каждого второго яблока)
        Стены: есть
        Яблок: 4
-------------------------------------------------------------------------

Сложность Hard:
    1 Player:
        Размер карты: 650x650
        Скорость: ускоряющаяся(8 FPS, +1 после каждого яблока)
        Карта со стенами:
        [w, w, w, w, w, w, w, w, w, w, w, w, w]
        [w, W, 0, 0, 0, 0, W, 0, 0, 0, 0, W, w]
        [w, 0, 0, W, 0, 0, W, 0, 0, W, 0, 0, w]
        [w, 0, W, W, W, 0, 0, 0, W, W, W, 0, w]
        [w, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, w]
        [w, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, w]
        [w, W, W, 0, 0, W, W, W, 0, 0, W, W, w]
        [w, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, w]
        [w, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, w]
        [w, 0, W, W, W, 0, 0, 0, W, W, W, 0, w]
        [w, 0, 0, W, 0, 0, W, 0, 0, W, 0, 0, w]
        [w, W, 0, 0, 0, 0, W, 0, 0, 0, 0, W, w]
        [w, w, w, w, w, w, w, w, w, w, w, w, w]
        
        Яблок: 2
==============================

    2 Player:
        Размер карты: 1050x650
        Скорость: ускоряющаяся(8 FPS, +1 после каждого яблока)
        Карта со стенами:
        [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]
        [w, W, 0, 0, 0, 0, 0, W, 0, 0, W, 0, 0, W, 0, 0, 0, 0, 0, W, w]
        [w, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, w]
        [w, 0, W, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, W, 0, w]
        [w, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, w]
        [w, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, w]
        [w, W, W, 0, 0, 0, 0, 0, 0, W, W, W, 0, 0, 0, 0, 0, 0, W, W, w]
        [w, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, w]
        [w, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, w]
        [w, 0, W, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, W, 0, w]
        [w, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, w]
        [w, W, 0, 0, 0, 0, 0, W, 0, 0, W, 0, 0, W, 0, 0, 0, 0, 0, W, w]
        [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]

        Яблок: 3
'''
import re
import pygame
import os.path
from random import randrange

# map size
SIZE = WIDTH, HEIGHT = (1050, 650)
BLOCK = 50

# main control
x, y = (WIDTH - BLOCK) // 2, (HEIGHT - BLOCK) // 2
apple = randrange(BLOCK, WIDTH, BLOCK), randrange(BLOCK, HEIGHT, BLOCK)
snake = [(x, y)]
length = 1
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
fps = 10
dx, dy = 0, 0
score = 0
Running = True
cnt = 0

# Display
pygame.init()
surface = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('анаконда')
clock = pygame.time.Clock()

# Fonts
font_menu = pygame.font.Font('Data/Font/font.ttf', 85)
font_score = pygame.font.SysFont('Arial', 32, bold=True)
font_best_score = pygame.font.Font('Data/Font/font.ttf', 75)
font_end = pygame.font.SysFont('Arial', 100, bold=True)
font_back = pygame.font.Font('Data/Font/font.ttf', 45)

# Images
background_menu = pygame.image.load('Data/Images/menu_background.jpg').convert()
background_game = pygame.image.load('Data/Images/game_background.jpg').convert()
snake_img = pygame.image.load('Data/Images/snake_head.png').convert()
tail_img = pygame.image.load('Data/Images/tail.jpg').convert()

def game_over():
    while True: 
        render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
        surface.blit(render_end, ((WIDTH - BLOCK) // 4, (HEIGHT - BLOCK) // 2 - 20))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scores()
                exit()
        pygame.display.flip()

def play_menu():
    while True:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 10 and my >= 600\
                                                    and mx <= 150 and my <= 630:
                return main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 260 and my >= 550\
                                                    and mx <= 470 and my <= 610:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 560 and my >= 550\
                                                    and mx <= 770 and my <= 610:
                return 
        with open('Data/Scores/scores.txt') as txt:
            best_score = re.findall(r'Best score: (\d+)', txt.read())
        
        render_best_score = font_best_score.render(f'BEST SCORE: {best_score[0]}', 1, pygame.Color('black')) 
        surface.blit(background_menu, (0, 0))
        render_1Player = font_menu.render('>1 PLAYER', 1, pygame.Color('black'))
        render_2Player = font_menu.render('>2 PLAYER', 1, pygame.Color('black'))
        render_back = font_back.render('<-Main menu', 2, pygame.Color('black'))
        surface.blit(render_1Player, (260, 550))
        surface.blit(render_2Player, (560, 550))
        surface.blit(render_best_score, (10, 10))
        surface.blit(render_back, (10, 590))

        pygame.display.flip()
        clock.tick(fps)
        

def main_menu():
    while Running:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 300 and my >= 560\
                                                    and mx <= 430 and my <= 610:
                return play_menu()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 600 and my >= 560\
                                                    and mx <= 730 and my <= 610:
                exit()  

        with open('Data/Scores/scores.txt') as txt:
            best_score = re.findall(r'Best score: (\d+)', txt.read())
        render_best_score = font_best_score.render(f'BEST SCORE: {best_score[0]}', 1, pygame.Color('black')) 
        render_start = font_menu.render('>PLAY', 1, pygame.Color('black'))
        render_exit = font_menu.render('>EXIT', 1, pygame.Color('black'))
        surface.blit(background_menu, (0, 0))
        surface.blit(render_start, (300, 550))
        surface.blit(render_exit, (600, 550))
        surface.blit(render_best_score, (10, 10))

        pygame.display.flip()
        clock.tick(fps)

def scores():
    if os.path.exists('Data/Scores/scores.txt'):
        with open('Data/Scores/scores.txt') as best_score:
            lines = best_score.readlines()
            num, num1, num1_full, num_full = '', '', 0, 0
            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    if '0' <= lines[i][j] <= '9' and i == 0:
                        num += lines[i][j]
                    if '0' <= lines[i][j] <= '9' and i == 1:
                        num1 += lines[i][j]
            num_full = int(num)
            num1_full = int(num1)
            if num_full < score:
                lines[0] = f'Best score: {score}\n'
            lines[1] = f'Score: {score + num1_full}'
        with open('Data/Scores/scores.txt', 'w') as best:
            for i in range(len(lines)):
                best.write(lines[i])
    else:
        with open('Data/Scores/scores.txt', 'w') as best_score:
            best_score.write(f'Best score: {score}\nScore: {score}')

def One_Player():
    while True:
        surface.blit(background_game, (0, 0))

        # drawing snake's tail
        for i, j in snake:
            pygame.draw.rect(surface, pygame.Color('green'), (i, j, BLOCK, BLOCK))
            surface.blit(tail_img, (i, j))
            
        # apple
        pygame.draw.rect(surface, pygame.Color('red'), (*apple, BLOCK, BLOCK))
        
        # snake's head
        surface.blit(snake_img, (x, y)) 
            
        # show score
        render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
        surface.blit(render_score, (5, 5))

        # snake movement
        x += dx * BLOCK
        y += dy * BLOCK
        snake.append((x, y))
        snake = snake[-length:]

        # eating apple
        if snake[-1] == apple:
            apple = randrange(BLOCK, WIDTH, BLOCK), randrange(BLOCK, HEIGHT, BLOCK)
            length += 1
            score += 1

        # game over
        if x < 0 or x > WIDTH - BLOCK or y < 0 or y > HEIGHT - BLOCK or len(snake) != len(set(snake)):
            game_over()
            
        pygame.display.flip()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # control
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'A': True, 'S': False, 'D': True}
        elif key[pygame.K_s]:
            if dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'A': True, 'S': True, 'D': True}
        elif key[pygame.K_a]:
            if dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'A': True, 'S': True, 'D': False}
        elif key[pygame.K_d]:
            if dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'A': False, 'S': True, 'D': True}

main_menu()
while True:
    surface.blit(background_game, (0, 0))

    # drawing snake's tail
    for i, j in snake:
        pygame.draw.rect(surface, pygame.Color('green'), (i, j, BLOCK, BLOCK))
        surface.blit(tail_img, (i, j))
        
    # apple
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, BLOCK, BLOCK))
    
    # snake's head
    surface.blit(snake_img, (x, y)) 
        
    # show score
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))

    # snake movement
    x += dx * BLOCK
    y += dy * BLOCK
    snake.append((x, y))
    snake = snake[-length:]

    # eating apple
    if snake[-1] == apple:
        apple = randrange(BLOCK, WIDTH, BLOCK), randrange(BLOCK, HEIGHT, BLOCK)
        length += 1
        score += 1

    # game over
    if x < 0 or x > WIDTH - BLOCK or y < 0 or y > HEIGHT - BLOCK or len(snake) != len(set(snake)):
        game_over()
        
    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'A': True, 'S': False, 'D': True}
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'A': True, 'S': True, 'D': True}
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'A': True, 'S': True, 'D': False}
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'A': False, 'S': True, 'D': True}