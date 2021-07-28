import re
import pygame
import sys
import os
import os.path
from random import randrange

# map size
SIZE = WIDTH, HEIGHT = (1050, 650)
BLOCK = 50

# main control
x, y = (WIDTH - BLOCK) // 2, (HEIGHT - BLOCK) // 2
apple = randrange(BLOCK, WIDTH - BLOCK, BLOCK), randrange(BLOCK, HEIGHT - BLOCK, BLOCK)
apple1 = randrange(BLOCK, WIDTH - BLOCK, BLOCK), randrange(BLOCK, HEIGHT - BLOCK, BLOCK)
snake = [(x, y)]
length = 1
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
fps = 10
dx, dy = 0, 0
score = 0

# Display
pygame.mixer.init()
pygame.init()
surface = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('анаконда')
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Fonts
font_menu = pygame.font.Font('Data/Font/font.ttf', 85)
font_difficult = pygame.font.Font('Data/Font/font.ttf', 75)
font_best_score = pygame.font.Font('Data/Font/font.ttf', 75)
font_back = pygame.font.Font('Data/Font/font.ttf', 45)
font_end = pygame.font.Font('Data/Font/18076.ttf', 80)
font_game_over = pygame.font.Font('Data/Font/18076.ttf', 130)
font_end_game = pygame.font.Font('Data/Font/18076.ttf', 50)
font_won = pygame.font.Font('Data/Font/18076.ttf', 100)

# Images
background_menu = pygame.image.load('Data/Images/menu_background.jpg').convert()
background_game = pygame.image.load('Data/Images/game_background.jpg').convert()
snake_img = pygame.image.load('Data/Images/snake_head.png').convert()
tail_img = pygame.image.load('Data/Images/tail.jpg').convert()

# Sounds
mouseclick = pygame.mixer.Sound("Data/Sounds/mouseclick.mp3")
gamemenu = pygame.mixer.Sound("Data/Sounds/gamemenu.mp3")
death = pygame.mixer.Sound("Data/Sounds/death.mp3")
wasted = pygame.mixer.Sound("Data/Sounds/wasted.mp3")
eat = pygame.mixer.Sound("Data/Sounds/eat.wav")
game = pygame.mixer.Sound("Data/Sounds/game.mp3")
gamemenu.play()

def player1_game_over_menu():
    menu = True
    while menu:
        best_score = '0'
        if os.path.exists('Data/Saved/scores.txt'):
            with open('Data/Saved/scores.txt') as txt:
                txt = txt.read()
                if 'easy' in difficult:
                    best_score = re.findall(r'Easy: (\d+)', txt)
                if 'medium' in difficult:
                    best_score = re.findall(r'Medium: (\d+)', txt)
                if 'hard' in difficult:
                    best_score = re.findall(r'Hard: (\d+)', txt)

        render_game_over = font_game_over.render('GAME OVER!', 1, pygame.Color('black'))
        render_new_best = font_end.render('NEW BEST!', 1, pygame.Color('black'))
        if best_score:
            render_best = font_end.render(f'HIGH SCORE: {best_score[0]}', 1, pygame.Color('black'))
        render_best1 = font_end.render(f'HIGH SCORE: {score}', 1, pygame.Color('black'))
        render_new_game = font_end_game.render('>NEW GAME', 1, pygame.Color('black'))
        render_exit = font_end_game.render('>EXIT', 1, pygame.Color('black'))
        surface.blit(render_game_over, (220, 150))
        if score > int(best_score[0]):
            surface.blit(render_new_best, (340, 280))
            surface.blit(render_best1, (300, 370))
            surface.blit(render_new_game, (260, 470))
            surface.blit(render_exit, (645, 470))
        else:
            if best_score:
                surface.blit(render_best, (300, 290))
            surface.blit(render_new_game, (260, 400))
            surface.blit(render_exit, (645, 400))

        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                scores()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick.play()
            if score > int(best_score[0]):
                if event.type == pygame.MOUSEBUTTONDOWN and mx >= 260 and my >= 470\
                                                        and mx <= 495 and my <= 510:
                    menu = False
                    scores()
                    return True
                elif event.type == pygame.MOUSEBUTTONDOWN and mx >= 645 and my >= 470\
                                                        and mx <= 750 and my <= 510:
                    scores()
                    exit()
            if score <= int(best_score[0]):
                if event.type == pygame.MOUSEBUTTONDOWN and mx >= 260 and my >= 400\
                                                        and mx <= 495 and my <= 440:
                    menu = False
                    scores()
                    return True
                elif event.type == pygame.MOUSEBUTTONDOWN and mx >= 645 and my >= 400\
                                                        and mx <= 750 and my <= 440:
                    scores()
                    exit()
                
        pygame.display.flip()
        clock.tick(fps)    

def player2_game_over_menu():
    menu = True
    while menu:
        render_player1_win = font_won.render('PLAYER 1 WON!', 1, pygame.Color('black'))
        render_player2_win = font_won.render('PLAYER 2 WON!', 1, pygame.Color('black'))
        render_draw = font_won.render('DRAW!', 1, pygame.Color('black'))
        render_new_game = font_end_game.render('>NEW GAME', 1, pygame.Color('black'))
        render_exit = font_end_game.render('>EXIT', 1, pygame.Color('black'))
        if score_snake1 > score_snake2:
            surface.blit(render_player1_win, (230, 150))
        if score_snake1 < score_snake2:
            surface.blit(render_player2_win, (230, 150))
        if score_snake1 == score_snake2:
            surface.blit(render_draw, (400, 150))

        surface.blit(render_new_game, (260, 300))
        surface.blit(render_exit, (645, 300))

        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick.play()
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 260 and my >= 300\
                                                    and mx <= 495 and my <= 340:
                menu = False
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN and mx >= 645 and my >= 300\
                                                    and mx <= 750 and my <= 340:
                exit()
                
        pygame.display.flip()
        clock.tick(fps)

def diff_menu(players):
    while True:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick.play()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 10 and my >= 600\
                                                    and mx <= 90 and my <= 630:
                return play_menu()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 270 and my >= 560\
                                                    and mx <= 383 and my <= 612:
                if players == 1:
                    return '1 Player - easy'
                elif players == 2:
                    return '2 Player - easy'
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 445 and my >= 560\
                                                    and mx <= 605 and my <= 612:
                if players == 1:
                    return '1 Player - medium'
                elif players == 2:
                    return '2 Player - medium'
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 670 and my >= 560\
                                                    and mx <= 783 and my <= 612:
                if players == 1:
                    return '1 Player - hard'
                elif players == 2:
                    return '2 Player - hard'

        best_score = False
        if os.path.exists('Data/Saved/scores.txt'):
            with open('Data/Saved/scores.txt') as txt:
                best_score = re.findall(r'Best score: (\d+)', txt.read())
        
        if best_score:
            render_best_score = font_best_score.render(f'BEST SCORE: {best_score[0]}', 1, pygame.Color('black')) 
        render_easy = font_difficult.render('>EASY', 1, pygame.Color('black'))
        render_normal = font_difficult.render('>MEDIUM', 1, pygame.Color('black'))
        render_hard = font_difficult.render('>HARD', 1, pygame.Color('black'))
        render_back = font_back.render('<-Back', 2, pygame.Color('black'))
        surface.blit(background_menu, (0, 0))
        surface.blit(render_easy, (270, 560))
        surface.blit(render_normal, (445, 560))
        surface.blit(render_hard, (670, 560))
        if best_score:
            surface.blit(render_best_score, (10, 10))
        surface.blit(render_back, (10, 590))

        pygame.display.flip()
        clock.tick(fps)    

def play_menu():
    while True:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick.play()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 10 and my >= 600\
                                                    and mx <= 150 and my <= 630:
                return main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 260 and my >= 550\
                                                    and mx <= 470 and my <= 610:
                return diff_menu(1)
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 560 and my >= 550\
                                                    and mx <= 770 and my <= 610:
                return diff_menu(2)

        best_score = False
        if os.path.exists('Data/Saved/scores.txt'):
            with open('Data/Saved/scores.txt') as txt:
                best_score = re.findall(r'Best score: (\d+)', txt.read())
        
        if best_score:
            render_best_score = font_best_score.render(f'BEST SCORE: {best_score[0]}', 1, pygame.Color('black')) 
        surface.blit(background_menu, (0, 0))
        render_1Player = font_menu.render('>1 PLAYER', 1, pygame.Color('black'))
        render_2Player = font_menu.render('>2 PLAYER', 1, pygame.Color('black'))
        render_back = font_back.render('<-Main menu', 2, pygame.Color('black'))
        surface.blit(render_1Player, (260, 550))
        surface.blit(render_2Player, (560, 550))
        if best_score:
            surface.blit(render_best_score, (10, 10))
        surface.blit(render_back, (10, 590))

        pygame.display.flip()
        clock.tick(fps)

def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick.play()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 550 and my >= 560\
                                                    and mx <= 680 and my <= 610:
                menu = False
                return play_menu()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 750 and my >= 560\
                                                    and mx <= 880 and my <= 610:
                exit()  
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 130 and my >= 560\
                                                    and mx <= 490 and my <= 610:
                if os.path.exists('Data/Saved/savegame.txt'):
                    return 'continue'
                else:
                    return play_menu()

        best_score = False
        if os.path.exists('Data/Saved/scores.txt'):
            with open('Data/Saved/scores.txt') as txt:
                best_score = re.findall(r'Best score: (\d+)', txt.read())
        if best_score:
            render_best_score = font_best_score.render(f'BEST SCORE: {best_score[0]}', 1, pygame.Color('black')) 
        render_play = font_menu.render('>PLAY', 1, pygame.Color('black'))
        render_exit = font_menu.render('>EXIT', 1, pygame.Color('black'))
        render_continue = font_menu.render('>CONTINUE GAME', 1, pygame.Color('black'))

        surface.blit(background_menu, (0, 0))
        surface.blit(render_play, (550, 550))
        surface.blit(render_exit, (750, 550))
        surface.blit(render_continue, (130, 550))
        if best_score:
            surface.blit(render_best_score, (10, 10))

        pygame.display.flip()
        clock.tick(fps)

def scores():
    if os.path.exists('Data/Saved/scores.txt'):
        with open('Data/Saved/scores.txt') as txt:
            txt = txt.read()
            best_score_all = int(re.findall(r'Best score: (\d+)', txt)[0])
            easy_score = int(re.findall(r'Easy: (\d+)', txt)[0])
            medium_score = int(re.findall(r'Medium: (\d+)', txt)[0])
            hard_score = int(re.findall(r'Hard: (\d+)', txt)[0])

            if score > best_score_all:
                best_score_all = score
                with open('Data/Saved/scores.txt', 'w') as new:
                    new.write(f'Best score: {best_score_all}\nEasy: {easy_score}\nMedium: {medium_score}\nHard: {hard_score}')
            
            if difficult == '1 Player - easy' and score > easy_score:
                easy_score = score
                with open('Data/Saved/scores.txt', 'w') as new:
                    new.write(f'Best score: {best_score_all}\nEasy: {easy_score}\nMedium: {medium_score}\nHard: {hard_score}')

            if difficult == '1 Player - medium' and score > medium_score:
                medium_score = score
                with open('Data/Saved/scores.txt', 'w') as new:
                    new.write(f'Best score: {best_score_all}\nEasy: {easy_score}\nMedium: {medium_score}\nHard: {hard_score}')

            if difficult == '1 Player - hard' and score > hard_score:
                hard_score = score
                with open('Data/Saved/scores.txt', 'w') as new:
                    new.write(f'Best score: {best_score_all}\nEasy: {easy_score}\nMedium: {medium_score}\nHard: {hard_score}')

    else:
        with open('Data/Saved/scores.txt', 'w') as txt:
            if difficult == '1 Player - easy':
                txt.write(f'Best score: {score}\nEasy: {score}\nMedium: 0\nHard: 0')
            elif difficult == '1 Player - medium':
                txt.write(f'Best score: {score}\nEasy: 0\nMedium: {score}\nHard: 0')
            elif difficult == '1 Player - hard':
                txt.write(f'Best score: {score}\nEasy: 0\nMedium: 0\nHard: {score}')

def apple_spawn(apple):
    while apple in snake:
        apple = randrange(BLOCK, WIDTH - BLOCK, BLOCK), randrange(BLOCK, HEIGHT - BLOCK, BLOCK)
    if 'medium' in difficult or 'hard' in difficult:
        while ((apple[0] == 150 and apple[1] == 150) or (apple[0] == 150 and apple[1] == 200)\
        or (apple[0] == 200 and apple[1] == 150)) or ((apple[0] == 150 and apple[1] == 400)\
        or (apple[0] == 150 and apple[1] == 450) or (apple[0] == 200 and apple[1] == 450))\
        or ((apple[0] == 800 and apple[1] == 150) or (apple[0] == 850 and apple[1] == 150)\
        or (apple[0] == 850 and apple[1] == 200)) or ((apple[0] == 850 and apple[1] == 400)\
        or (apple[0] == 800 and apple[1] == 450) or (apple[0] == 850 and apple[1] == 450)):
            apple = randrange(BLOCK, WIDTH - BLOCK, BLOCK), randrange(BLOCK, HEIGHT - BLOCK, BLOCK)
    if 'hard' in difficult:
        while (apple[0] == 50 and apple[1] == 300) or (apple[0] == 500 and apple[1] == 50)\
        or (apple[0] == 950 and apple[1] == 300) or (apple[0] == 500 and apple[1] == 550):
            apple = randrange(BLOCK, WIDTH - BLOCK, BLOCK), randrange(BLOCK, HEIGHT - BLOCK, BLOCK)
    if '2 Player' in difficult:
        while apple in snake1 or apple in snake2:
            apple = randrange(BLOCK, WIDTH - BLOCK, BLOCK), randrange(BLOCK, HEIGHT - BLOCK, BLOCK)
    return apple

def save():
    with open('Data/Saved/savegame.txt', 'w') as txt:
        txt.write(f'difficult = {difficult}\n')
        txt.write(f'apple = {apple}\n')
        if apple1:
            txt.write(f'apple1 = {apple1}\n')
        txt.write(f'fps = {fps}\n')
        txt.write(f'score = {score}\n')
        txt.write(f'x, y = {x}, {y}\n')
        txt.write(f'length = {length}\n')
        txt.write(f'snake = {snake}\n')
        txt.write(f'dirs = {dirs}')

def game_menu():
    menu = True
    snake1_ready = False
    snake2_ready = False    
    while menu:
        render_start = font_end.render('PRESS BUTTONS TO START!', 1, pygame.Color('black'))
        render_control = font_end.render('CONTROL', 1, pygame.Color('black'))
        render_W = font_end.render('W', 1, pygame.Color('black'))
        render_A = font_end.render('A', 1, pygame.Color('black'))
        render_S = font_end.render('S', 1, pygame.Color('black'))
        render_D = font_end.render('D', 1, pygame.Color('black'))
        render_pause = font_end.render('P - PAUSE', 1, pygame.Color('black'))
        render_save = font_end_game.render('>SAVE AND EXIT', 1, pygame.Color('black'))

        surface.blit(render_start, (120, 140))
        surface.blit(render_control, (50, 240))
        surface.blit(render_W, (140, 320))
        surface.blit(render_A, (70, 400))
        surface.blit(render_S, (150, 400))
        surface.blit(render_D, (220, 400))
        surface.blit(render_pause, (70, 500))
        surface.blit(render_save, (700, 600))

        if '2 Player' in difficult:
            render_I = font_end.render('I', 1, pygame.Color('black'))
            render_J = font_end.render('J', 1, pygame.Color('black'))
            render_K = font_end.render('K', 1, pygame.Color('black'))
            render_L = font_end.render('L', 1, pygame.Color('black'))
            surface.blit(render_I, (850, 320))
            surface.blit(render_J, (780, 400))
            surface.blit(render_K, (850, 400))
            surface.blit(render_L, (920, 400))

        if 'medium' in difficult:
            render_increase = font_end_game.render('SPEED INCREASING', 1, pygame.Color('black'))
            surface.blit(render_increase, (450, 10))
        if 'hard' in difficult:
            render_increase = font_end_game.render('SPEED RAPIDLY INCREASING', 1, pygame.Color('black'))
            surface.blit(render_increase, (270, 10))

        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                scores()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick.play()
            if event.type == pygame.MOUSEBUTTONDOWN and mx >= 700 and my >= 600\
                                                        and mx <= 990 and my <= 650:
                save()
                exit()

        key = pygame.key.get_pressed()
        if '1 Player' in difficult:
            if key[pygame.K_w]:
                return 'W'
                menu = False
            elif key[pygame.K_s]:
                return 'S'
                menu = False
            elif key[pygame.K_a]:
                return 'A'
                menu = False
            elif key[pygame.K_d]:
                return 'D'
                menu = False
        
        elif '2 Player' in difficult:
            if key[pygame.K_w]:
                snake1_ready = True
            elif key[pygame.K_s]:
                snake1_ready = True
            elif key[pygame.K_a]:
                snake1_ready = True
            elif key[pygame.K_d]:
                snake1_ready = True
            if key[pygame.K_i]:
                snake2_ready = True
            elif key[pygame.K_j]:
                snake2_ready = True
            elif key[pygame.K_k]:
                snake2_ready = True
            elif key[pygame.K_l]:
                snake2_ready = True

        if snake1_ready == True and snake2_ready == True:
            menu = False
        if snake1_ready == True:
            render_P1 = font_end.render('P1 READY!', 1, pygame.Color('green'))
            surface.blit(render_P1, (400, 240))
        if snake2_ready == True:
            render_P2 = font_end.render('P2 READY!', 1, pygame.Color('blue'))
            surface.blit(render_P2, (400, 320))

        pygame.display.flip()
        clock.tick(fps)

difficult = main_menu()
value = 0
if difficult == 'continue':
    with open('Data/Saved/savegame.txt') as txt:
        txt = txt.read()
        difficult = re.findall(r'difficult = (.+)', txt)[0]
        apple = int(re.findall(r'apple = \((\d+)', txt)[0]), int(re.findall(r'apple = \(\d+, (\d+)', txt)[0])
        apple1 = int(re.findall(r'apple1 = \((\d+)', txt)[0]), int(re.findall(r'apple1 = \(\d+, (\d+)', txt)[0])
        fps = int(re.findall(r'fps = (\d+)', txt)[0])
        score = int(re.findall(r'score = (\d+)', txt)[0])
        x, y = int(re.findall(r'x, y = (\d+)', txt)[0]), int(re.findall(r'x, y = \d+, (\d+)', txt)[0])
        length = int(re.findall(r'length = (\d+)', txt)[0])
        dirs = {'W': bool(re.findall(r"[WASD]': ([TrueFals]+)", txt)[0]),
                'A': bool(re.findall(r"[WASD]': ([TrueFals]+)", txt)[1]),
                'S': bool(re.findall(r"[WASD]': ([TrueFals]+)", txt)[2]),
                'D': bool(re.findall(r"[WASD]': ([TrueFals]+)", txt)[1])}
        snake_str = re.findall(r'\((\d+)\, (\d+)\)', txt)
        snake = []
        for i in range(2, len(snake_str)):
            snake.append((int(snake_str[i][0]), int(snake_str[i][1])))
        value = 1

run = True
if '1 Player' in difficult:
    stop = False
    counter = 0
    menu = True
    while run:
        game_over = False
        apple = apple_spawn(apple)
        apple1 = apple_spawn(apple1)
        
        surface.blit(background_game, (0, 0))

        # drawing snake's tail  
        for i, j in snake:
            pygame.draw.rect(surface, pygame.Color('green'), (i, j, BLOCK - 1, BLOCK - 1))
            
        # apple
        pygame.draw.rect(surface, pygame.Color('red'), (*apple, BLOCK, BLOCK))
        if 'easy' in difficult or 'medium' in difficult:
            pygame.draw.rect(surface, pygame.Color('red'), (*apple1, BLOCK, BLOCK))
        
        # walls
        if 'medium' in difficult or 'hard' in difficult:
            # стенки
            pygame.draw.rect(surface, pygame.Color('gray'), (0, 0, BLOCK * 21, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (0, 600, BLOCK * 21, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (0, 50, BLOCK, BLOCK * 11))
            pygame.draw.rect(surface, pygame.Color('gray'), (1000, 50, BLOCK, BLOCK * 11))
            # левый верхний угольник
            pygame.draw.rect(surface, pygame.Color('gray'), (150, 150, BLOCK * 2, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (150, 200, BLOCK, BLOCK))
            # левый нижний угольник
            pygame.draw.rect(surface, pygame.Color('gray'), (150, 450, BLOCK * 2, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (150, 400, BLOCK, BLOCK))
            # правый верхний угольник
            pygame.draw.rect(surface, pygame.Color('gray'), (800, 150, BLOCK * 2, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (850, 200, BLOCK, BLOCK))
            # правый нижний угольник
            pygame.draw.rect(surface, pygame.Color('gray'), (800, 450, BLOCK * 2, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (850, 400, BLOCK, BLOCK))
        if 'hard' in difficult:
            pygame.draw.rect(surface, pygame.Color('gray'), (50, 300, BLOCK, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (500, 50, BLOCK, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (950, 300, BLOCK, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (500, 550, BLOCK, BLOCK))

        # show score
        render_score = font_difficult.render(f'SCORE: {score}', 1, pygame.Color('black'))
        surface.blit(render_score, (5, 0))
        # snake movement
        x += dx * BLOCK
        y += dy * BLOCK
        snake.append((x, y))
        snake = snake[-length:]

        # eating apple
        if snake[-1] == apple:
            eat.play()
            apple = apple_spawn(apple)
            length += 1
            score += 1
            if 'medium' in difficult and score % 4 == 0 and score != 0:
                fps += 1
            if 'hard' in difficult and score % 2 == 0 and score != 0:
                fps += 1

        # eating apple1
        if 'easy' in difficult or 'medium' in difficult:
            if snake[-1] == apple1:
                eat.play()
                apple1 = apple_spawn(apple1)
                length += 1
                score += 1

        #game over
        if value == 0:
            if x < 0 or x > WIDTH - BLOCK or y < 0 or y > HEIGHT - BLOCK or len(snake) != len(set(snake)):
                game_over = True
        else:
            if stop:
                if x < 0 or x > WIDTH - BLOCK or y < 0 or y > HEIGHT - BLOCK or len(snake) != len(set(snake)):
                    game_over = True
            else: 
                if x < 0 or x > WIDTH - BLOCK or y < 0 or y > HEIGHT - BLOCK:
                    game_over = True

        if 'medium' in difficult or 'hard' in difficult:
            if (x < BLOCK or x > WIDTH - BLOCK * 2 or y < BLOCK or y > HEIGHT - BLOCK * 2)\
            or ((x == 150 and y == 150) or (x == 150 and y == 200) or (x == 200 and y == 150))\
            or ((x == 150 and y == 400) or (x == 150 and y == 450) or (x == 200 and y == 450))\
            or ((x == 800 and y == 150) or (x == 850 and y == 150) or (x == 850 and y == 200))\
            or ((x == 850 and y == 400) or (x == 800 and y == 450) or (x == 850 and y == 450)):
                game_over = True
        if 'hard' in difficult:
            if (x == 50 and y == 300) or (x == 500 and y == 50)\
            or (x == 950 and y == 300) or (x == 500 and y == 550):
                game_over = True
    
        # game over scene
        if game_over == True:
            game.stop()
            death.play()
            if os.path.exists('Data/Saved/savegame.txt'):
                os.remove('Data/Saved/savegame.txt')
            x, y = (WIDTH - BLOCK) // 2, (HEIGHT - BLOCK) // 2
            length = 1
            dx, dy = 0, 0
            dirs = {'W': True, 'A': True, 'S': True, 'D': True}
            fps = 10
            wasted.play()
            if player1_game_over_menu() == True:
                wasted.stop()
                game.play()
                game_over == False
            score = 0

        pygame.display.update()
        clock.tick(fps)

        if menu: 
            start = game_menu()
            menu = False
            gamemenu.stop()
            game.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                if game_over == False:
                    save()
            if event.type == pygame.USEREVENT:
                counter += 1
                if counter >= 2: stop = True
        # control
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            game_menu()
        elif key[pygame.K_w]:
            if dirs['W'] or start == 'W':
                dx, dy = 0, -1
                dirs = {'W': True, 'A': True, 'S': False, 'D': True}
        elif key[pygame.K_s]:
            if dirs['S'] or start == 'S':
                dx, dy = 0, 1
                dirs = {'W': False, 'A': True, 'S': True, 'D': True}
        elif key[pygame.K_a]:
            if dirs['A'] or start == 'A':
                dx, dy = -1, 0
                dirs = {'W': True, 'A': True, 'S': True, 'D': False}
        elif key[pygame.K_d]:
            if dirs['D'] or start == 'D':
                dx, dy = 1, 0
                dirs = {'W': True, 'A': False, 'S': True, 'D': True}


if '2 Player' in difficult:
    menu = True
    x, y = (WIDTH - BLOCK) // 4, (HEIGHT - BLOCK) // 2
    u, v = WIDTH - (WIDTH - BLOCK) // 4, (HEIGHT - BLOCK) // 2
    snake1 = [(x, y)]
    snake2 = [(u, v)]
    length_snake1 = 1
    length_snake2 = 1
    dirs_snake1 = {'W': True, 'A': True, 'S': True, 'D': True}
    dirs_snake2 = {'I': True, 'J': True, 'K': True, 'L': True}
    dx, dy = 0, 0
    du, dv = 0, 0
    score_snake1 = 0
    score_snake2 = 0
    death1 = 0
    death2 = 0

    while run:
        apple = apple_spawn(apple)
        apple1 = apple_spawn(apple1)
        
        game_over = False
        game_over_snake1 = False
        game_over_snake2 = False

        surface.blit(background_game, (0, 0))

        # drawing snake's tail  
        for i, j in snake1:
            pygame.draw.rect(surface, pygame.Color('green'), (i, j, BLOCK - 1, BLOCK - 1))
            
        for i, j in snake2:
            pygame.draw.rect(surface, pygame.Color('blue'), (i, j, BLOCK - 1, BLOCK - 1))

        # apple
        pygame.draw.rect(surface, pygame.Color('red'), (*apple, BLOCK, BLOCK))
        if 'easy' or 'medium' in difficult:
            pygame.draw.rect(surface, pygame.Color('red'), (*apple1, BLOCK, BLOCK))

        # walls
        if 'medium' in difficult or 'hard' in difficult:
            # стенки
            pygame.draw.rect(surface, pygame.Color('gray'), (0, 0, BLOCK * 21, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (0, 600, BLOCK * 21, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (0, 50, BLOCK, BLOCK * 11))
            pygame.draw.rect(surface, pygame.Color('gray'), (1000, 50, BLOCK, BLOCK * 11))
            # левый верхний угольник
            pygame.draw.rect(surface, pygame.Color('gray'), (150, 150, BLOCK * 2, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (150, 200, BLOCK, BLOCK))
            # левый нижний угольник
            pygame.draw.rect(surface, pygame.Color('gray'), (150, 450, BLOCK * 2, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (150, 400, BLOCK, BLOCK))
            # правый верхний угольник
            pygame.draw.rect(surface, pygame.Color('gray'), (800, 150, BLOCK * 2, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (850, 200, BLOCK, BLOCK))
            # правый нижний угольник
            pygame.draw.rect(surface, pygame.Color('gray'), (800, 450, BLOCK * 2, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (850, 400, BLOCK, BLOCK))
        if 'hard' in difficult:
            pygame.draw.rect(surface, pygame.Color('gray'), (50, 300, BLOCK, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (500, 50, BLOCK, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (950, 300, BLOCK, BLOCK))
            pygame.draw.rect(surface, pygame.Color('gray'), (500, 550, BLOCK, BLOCK))
        
        # show score
        render_score_snake1 = font_difficult.render(f'SCORE: {score_snake1}', 1, pygame.Color('black'))
        surface.blit(render_score_snake1, (5, 0))
        render_score_snake2 = font_difficult.render(f'SCORE: {score_snake2}', 1, pygame.Color('black'))
        surface.blit(render_score_snake2, (860, 0))

        # snake movement
        x += dx * BLOCK
        y += dy * BLOCK
        snake1.append((x, y))
        snake1 = snake1[-length_snake1:]
        u += du * BLOCK
        v += dv * BLOCK
        snake2.append((u, v))
        snake2 = snake2[-length_snake2:]

        # eating apple
        if snake1[-1] == apple:
            eat.play()
            apple = apple_spawn(apple)
            length_snake1 += 1
            score_snake1 += 1
        elif snake1[-1] == apple1:
            eat.play()
            apple1 = apple_spawn(apple1)
            length_snake1 += 1
            score_snake1 += 1
        elif snake2[-1] == apple:
            eat.play()
            apple = apple_spawn(apple)
            length_snake2 += 1
            score_snake2 += 1
        elif snake2[-1] == apple1:
            eat.play()
            apple1 = apple_spawn(apple1)
            length_snake2 += 1
            score_snake2 += 1        

        if x < 0 or x > WIDTH - BLOCK or y < 0 or y > HEIGHT - BLOCK or len(snake1) != len(set(snake1)):
            game_over_snake1 = True
        if 'medium' in difficult or 'hard' in difficult:
            if (x < BLOCK or x > WIDTH - BLOCK * 2 or y < BLOCK or y > HEIGHT - BLOCK * 2)\
            or ((x == 150 and y == 150) or (x == 150 and y == 200) or (x == 200 and y == 150))\
            or ((x == 150 and y == 400) or (x == 150 and y == 450) or (x == 200 and y == 450))\
            or ((x == 800 and y == 150) or (x == 850 and y == 150) or (x == 850 and y == 200))\
            or ((x == 850 and y == 400) or (x == 800 and y == 450) or (x == 850 and y == 450)):
                game_over_snake1 = True
        if 'hard' in difficult:
            if (x == 50 and y == 300) or (x == 500 and y == 50)\
            or (x == 950 and y == 300) or (x == 500 and y == 550):
                game_over_snake1 = True

        if u < 0 or u > WIDTH - BLOCK or v < 0 or v > HEIGHT - BLOCK or len(snake2) != len(set(snake2)):
            game_over_snake2 = True
        if 'medium' in difficult or 'hard' in difficult:
            if (u < BLOCK or u > WIDTH - BLOCK * 2 or v < BLOCK or v > HEIGHT - BLOCK * 2)\
            or ((u == 150 and v == 150) or (u == 150 and v == 200) or (u == 200 and v == 150))\
            or ((u == 150 and v == 400) or (u == 150 and v == 450) or (u == 200 and v == 450))\
            or ((u == 800 and v == 150) or (u == 850 and v == 150) or (u == 850 and v == 200))\
            or ((u == 850 and v == 400) or (u == 800 and v == 450) or (u == 850 and v == 450)):
                game_over_snake2 = True
        if 'hard' in difficult:
            if (u == 50 and v == 300) or (u == 500 and v == 50)\
            or (u == 950 and v == 300) or (u == 500 and v == 550):
                game_over_snake2 = True
        
        if snake1[-1] in snake2:
            game_over_snake1 = True
        if snake2[-1] in snake1:
            game_over_snake2 = True

        if game_over_snake1 == True:
            x, y = WIDTH, HEIGHT
            length_snake1 = 1
            dx, dy = 0, 0
            death1 += 1
        elif game_over_snake2 == True:
            u, v = WIDTH, HEIGHT
            length_snake2 = 1
            du, dv = 0, 0
            death2 += 1

        if death1 == 1:
            death.play()
        if death2 == 1:
            death.play()

        if game_over_snake2 == True and game_over_snake1 == True:
            game.stop()
            wasted.play()
            game_over == True
            x, y = (WIDTH - BLOCK) // 4, (HEIGHT - BLOCK) // 2
            u, v = WIDTH - (WIDTH - BLOCK) // 4, (HEIGHT - BLOCK) // 2
            length_snake1 = 1
            length_snake2 = 1
            dx, dy = 0, 0
            du, dv = 0, 0
            dirs_snake1 = {'W': True, 'A': True, 'S': True, 'D': True}
            dirs_snake2 = {'I': True, 'J': True, 'K': True, 'L': True}
            death1 = 0
            death2 = 0
            if player2_game_over_menu() == True:
                wasted.stop()
                game.play()
                game_over == False
            score_snake1 = 0
            score_snake2 = 0
        pygame.display.flip()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if menu:
            start = game_menu()
            menu = False
            gamemenu.stop()
            game.play()

        # control
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            game_menu()
        elif key[pygame.K_w]:
            if dirs_snake1['W']:
                dx, dy = 0, -1
                dirs_snake1 = {'W': True, 'A': True, 'S': False, 'D': True}
        elif key[pygame.K_s]:
            if dirs_snake1['S']:
                dx, dy = 0, 1
                dirs_snake1 = {'W': False, 'A': True, 'S': True, 'D': True}
        elif key[pygame.K_a]:
            if dirs_snake1['A']:
                dx, dy = -1, 0
                dirs_snake1 = {'W': True, 'A': True, 'S': True, 'D': False}
        elif key[pygame.K_d]:
            if dirs_snake1['D']:
                dx, dy = 1, 0
                dirs_snake1 = {'W': True, 'A': False, 'S': True, 'D': True}

        if key[pygame.K_i]:
            if dirs_snake2['I']:
                du, dv = 0, -1
                dirs_snake2 = {'I': True, 'J': True, 'K': False, 'L': True}
        elif key[pygame.K_k]:
            if dirs_snake2['K']:
                du, dv = 0, 1
                dirs_snake2 = {'I': False, 'J': True, 'K': True, 'L': True}
        elif key[pygame.K_j]:
            if dirs_snake2['J']:
                du, dv = -1, 0
                dirs_snake2 = {'I': True, 'J': True, 'K': True, 'L': False}
        elif key[pygame.K_l]:
            if dirs_snake2['L']:
                du, dv = 1, 0
                dirs_snake2 = {'I': True, 'J': False, 'K': True, 'L': True}