# import re
# import pygame
# import sys
# import os.path
# from random import randrange

# # map size
# SIZE = WIDTH, HEIGHT = (1050, 650)
# BLOCK = 50

# # main control
# x, y = (WIDTH - BLOCK) // 2, (HEIGHT - BLOCK) // 2
# apple = randrange(BLOCK, WIDTH, BLOCK), randrange(BLOCK, HEIGHT, BLOCK)
# snake = [(x, y)]
# length = 1
# dirs = {'W': True, 'A': True, 'S': True, 'D': True}
# fps = 10
# dx, dy = 0, 0
# score = 0
# game_overed = False

# # Display
# pygame.init()
# surface = pygame.display.set_mode([WIDTH, HEIGHT])
# pygame.display.set_caption('анаконда')
# clock = pygame.time.Clock()

# # Fonts
# font_menu = pygame.font.Font('Data/Font/font.ttf', 85)
# font_difficult = pygame.font.Font('Data/Font/font.ttf', 75)
# font_best_score = pygame.font.Font('Data/Font/font.ttf', 75)
# font_back = pygame.font.Font('Data/Font/font.ttf', 45)
# font_end = pygame.font.Font('Data/Font/18076.ttf', 80)
# font_game_over = pygame.font.Font('Data/Font/18076.ttf', 130)
# font_end_game = pygame.font.Font('Data/Font/18076.ttf', 50)

# # Images
# background_menu = pygame.image.load('Data/Images/menu_background.jpg').convert()
# background_game = pygame.image.load('Data/Images/game_background.jpg').convert()
# snake_img = pygame.image.load('Data/Images/snake_head.png').convert()
# tail_img = pygame.image.load('Data/Images/tail.jpg').convert()

# def game_over_menu():
#     menu = True
#     while menu:
#         with open('Data/Scores/scores.txt') as txt:
#             best_score = re.findall(r'Best score: (\d+)', txt.read())

#         render_game_over = font_game_over.render('GAME OVER!', 1, pygame.Color('black'))
#         render_new_best = font_end.render('NEW BEST!', 1, pygame.Color('black'))
#         render_best = font_end.render(f'HIGH SCORE: {best_score[0]}', 1, pygame.Color('black'))
#         render_best1 = font_end.render(f'HIGH SCORE: {score}', 1, pygame.Color('black'))
#         render_main_menu = font_end_game.render('>MAIN MENU', 1, pygame.Color('black'))
#         render_new_game = font_end_game.render('>NEW GAME', 1, pygame.Color('black'))
#         surface.blit(render_game_over, (220, 150))
#         if score > int(best_score[0]):
#             surface.blit(render_new_best, (340, 280))
#             surface.blit(render_best1, (300, 370))
#             surface.blit(render_main_menu, (230, 470))
#             surface.blit(render_new_game, (580, 470))
#         else:
#             surface.blit(render_best, (300, 290))
#             surface.blit(render_main_menu, (230, 400))
#             surface.blit(render_new_game, (580, 400))

#         for event in pygame.event.get():
#             mx, my = pygame.mouse.get_pos()
#             if event.type == pygame.QUIT:
#                 scores()
#                 exit()
#             if score > int(best_score[0]):
#                 if event.type == pygame.MOUSEBUTTONDOWN and mx >= 230 and my >= 470\
#                                                         and mx <= 485 and my <= 510:
#                     menu = False
#                     scores()
#                     return main_menu()
#                 elif event.type == pygame.MOUSEBUTTONDOWN and mx >= 580 and my >= 470\
#                                                         and mx <= 815 and my <= 510:
#                     menu = False                                    
#                     scores()
#                     return True
#             if score <= int(best_score[0]):
#                 if event.type == pygame.MOUSEBUTTONDOWN and mx >= 230 and my >= 400\
#                                                         and mx <= 485 and my <= 440:
#                     menu = False
#                     scores()
#                     return main_menu()
#                 elif event.type == pygame.MOUSEBUTTONDOWN and mx >= 580 and my >= 400\
#                                                         and mx <= 815 and my <= 440:
#                     menu = False
#                     scores()
#                     return True
                
#         pygame.display.flip()
#         clock.tick(fps)    


# def diff_menu(players):
#     while True:
#         for event in pygame.event.get():
#             mx, my = pygame.mouse.get_pos()
#             if event.type == pygame.QUIT:
#                 exit()
#             if event.type == pygame.MOUSEBUTTONDOWN and mx >= 10 and my >= 600\
#                                                     and mx <= 90 and my <= 630:
#                 return play_menu()
#             if event.type == pygame.MOUSEBUTTONDOWN and mx >= 270 and my >= 560\
#                                                     and mx <= 383 and my <= 612:
#                 if players == 1:
#                     return '1 Player - easy'
#                 elif players == 2:
#                     return '2 Player - easy'
#             if event.type == pygame.MOUSEBUTTONDOWN and mx >= 445 and my >= 560\
#                                                     and mx <= 605 and my <= 612:
#                 if players == 1:
#                     return '1 Player - medium'
#                 elif players == 2:
#                     return '2 Player - meduim'
#             if event.type == pygame.MOUSEBUTTONDOWN and mx >= 670 and my >= 560\
#                                                     and mx <= 783 and my <= 612:
#                 if players == 1:
#                     return '1 Player - hard'
#                 elif players == 2:
#                     return '2 Player - hard'
            
#         with open('Data/Scores/scores.txt') as txt:
#             best_score = re.findall(r'Best score: (\d+)', txt.read())
        
#         render_best_score = font_best_score.render(f'BEST SCORE: {best_score[0]}', 1, pygame.Color('black')) 
#         render_easy = font_difficult.render('>EASY', 1, pygame.Color('black'))
#         render_normal = font_difficult.render('>MEDIUM', 1, pygame.Color('black'))
#         render_hard = font_difficult.render('>HARD', 1, pygame.Color('black'))
#         render_back = font_back.render('<-Back', 2, pygame.Color('black'))
#         surface.blit(background_menu, (0, 0))
#         surface.blit(render_easy, (270, 560))
#         surface.blit(render_normal, (445, 560))
#         surface.blit(render_hard, (670, 560))
#         surface.blit(render_best_score, (10, 10))
#         surface.blit(render_back, (10, 590))

#         pygame.display.flip()
#         clock.tick(fps)    

# def play_menu():
#     while True:
#         for event in pygame.event.get():
#             mx, my = pygame.mouse.get_pos()
#             if event.type == pygame.QUIT:
#                 exit()
#             if event.type == pygame.MOUSEBUTTONDOWN and mx >= 10 and my >= 600\
#                                                     and mx <= 150 and my <= 630:
#                 return main_menu()
#             if event.type == pygame.MOUSEBUTTONDOWN and mx >= 260 and my >= 550\
#                                                     and mx <= 470 and my <= 610:
#                 return diff_menu(1)
#             if event.type == pygame.MOUSEBUTTONDOWN and mx >= 560 and my >= 550\
#                                                     and mx <= 770 and my <= 610:
#                 return diff_menu(2)
#         with open('Data/Scores/scores.txt') as txt:
#             best_score = re.findall(r'Best score: (\d+)', txt.read())
        
#         render_best_score = font_best_score.render(f'BEST SCORE: {best_score[0]}', 1, pygame.Color('black')) 
#         surface.blit(background_menu, (0, 0))
#         render_1Player = font_menu.render('>1 PLAYER', 1, pygame.Color('black'))
#         render_2Player = font_menu.render('>2 PLAYER', 1, pygame.Color('black'))
#         render_back = font_back.render('<-Main menu', 2, pygame.Color('black'))
#         surface.blit(render_1Player, (260, 550))
#         surface.blit(render_2Player, (560, 550))
#         surface.blit(render_best_score, (10, 10))
#         surface.blit(render_back, (10, 590))

#         pygame.display.flip()
#         clock.tick(fps)

# def main_menu():
#     menu = True
#     while menu:
#         for event in pygame.event.get():
#             mx, my = pygame.mouse.get_pos()
#             if event.type == pygame.QUIT:
#                 exit()
#             if event.type == pygame.MOUSEBUTTONDOWN and mx >= 300 and my >= 560\
#                                                     and mx <= 430 and my <= 610:
#                 menu = False
#                 return play_menu()
#             if event.type == pygame.MOUSEBUTTONDOWN and mx >= 600 and my >= 560\
#                                                     and mx <= 730 and my <= 610:
#                 exit()  

#         with open('Data/Scores/scores.txt') as txt:
#             best_score = re.findall(r'Best score: (\d+)', txt.read())
#         render_best_score = font_best_score.render(f'BEST SCORE: {best_score[0]}', 1, pygame.Color('black')) 
#         render_start = font_menu.render('>PLAY', 1, pygame.Color('black'))
#         render_exit = font_menu.render('>EXIT', 1, pygame.Color('black'))
#         surface.blit(background_menu, (0, 0))
#         surface.blit(render_start, (300, 550))
#         surface.blit(render_exit, (600, 550))
#         surface.blit(render_best_score, (10, 10))

#         pygame.display.flip()
#         clock.tick(fps)

# def scores():
#     if os.path.exists('Data/Scores/scores.txt'):
#         with open('Data/Scores/scores.txt') as best_score:
#             lines = best_score.readlines()
#             num, num1, num1_full, num_full = '', '', 0, 0
#             for i in range(len(lines)):
#                 for j in range(len(lines[i])):
#                     if '0' <= lines[i][j] <= '9' and i == 0:
#                         num += lines[i][j]
#                     if '0' <= lines[i][j] <= '9' and i == 1:
#                         num1 += lines[i][j]
#             num_full = int(num)
#             num1_full = int(num1)
#             if num_full < score:
#                 lines[0] = f'Best score: {score}\n'
#             lines[1] = f'Score: {score + num1_full}'
#         with open('Data/Scores/scores.txt', 'w') as best:
#             for i in range(len(lines)):
#                 best.write(lines[i])
#     else:
#         with open('Data/Scores/scores.txt', 'w') as best_score:
#             best_score.write(f'Best score: {score}\nScore: {score}')

# difficult = main_menu()
# run = True
# if difficult == '1 Player - easy' or difficult == 'return game':
#     while run:
#         game_over = False
#         # surface.blit(background_game, (0, 0))
#         surface.fill(pygame.Color('lightgreen'))
#         # drawing snake's tail  
#         for i, j in snake:
#             pygame.draw.rect(surface, pygame.Color('green'), (i, j, BLOCK - 1, BLOCK - 1))
            
#         # apple
#         pygame.draw.rect(surface, pygame.Color('red'), (*apple, BLOCK, BLOCK))
        
#         # snake's head
#         # surface.blit(snake_img, (x, y)) 
            
#         # show score
#         render_score = font_menu.render(f'SCORE: {score}', 1, pygame.Color('black'))
#         surface.blit(render_score, (5, 5))

#         # snake movement
#         x += dx * BLOCK
#         y += dy * BLOCK
#         snake.append((x, y))
#         snake = snake[-length:]

#         # eating apple
#         if snake[-1] == apple:
#             apple = randrange(BLOCK, WIDTH, BLOCK), randrange(BLOCK, HEIGHT, BLOCK)
#             length += 1
#             score += 1

#         if x < 0 or x > WIDTH - BLOCK or y < 0 or y > HEIGHT - BLOCK or len(snake) != len(set(snake)):
#             game_over = True
        
#         if game_over == True:
#             x, y = (WIDTH - BLOCK) // 2, (HEIGHT - BLOCK) // 2
#             apple = randrange(BLOCK, WIDTH, BLOCK), randrange(BLOCK, HEIGHT, BLOCK)
#             snake = [(x, y)]
#             length = 1
#             dx, dy = 0, 0
#             if game_over_menu() == True:
#                 game_over == False
#             score = 0

#         pygame.display.flip()
#         clock.tick(fps)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#         key = pygame.key.get_pressed()
#         if key[pygame.K_w]:
#             if dirs['W']:
#                 dx, dy = 0, -1
#                 dirs = {'W': True, 'A': True, 'S': False, 'D': True}
#         elif key[pygame.K_s]:
#             if dirs['S']:
#                 dx, dy = 0, 1
#                 dirs = {'W': False, 'A': True, 'S': True, 'D': True}
#         elif key[pygame.K_a]:
#             if dirs['A']:
#                 dx, dy = -1, 0
#                 dirs = {'W': True, 'A': True, 'S': True, 'D': False}
#         elif key[pygame.K_d]:
#             if dirs['D']:
#                 dx, dy = 1, 0
#                 dirs = {'W': True, 'A': False, 'S': True, 'D': True}
tupik = (400, 600)
print(tupik, tupik[0])