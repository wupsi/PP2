import pygame
import os.path
from random import randrange
import pygame as pg

SIZE = WIDTH, HEIGHT = (1050, 650)
BLOCK = 50

x, y = (WIDTH - BLOCK) // 2, (HEIGHT - BLOCK) // 2
apple = randrange(BLOCK, WIDTH, BLOCK), randrange(BLOCK, HEIGHT, BLOCK)
snake = [(x, y)]
length = 1
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
fps = 10
dx, dy = 0, 0
score = 0

pygame.init()
surface = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('анаконда')
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 32, bold=True)
font_end = pygame.font.SysFont('Arial', 100, bold=True)
background_img = pygame.image.load('background.jpg').convert()
snake_img = pygame.image.load('snake.png').convert()
tail_img = pygame.image.load('tail.jpg').convert()

Class Main_menu():
    def __init__(self):


def scores():
    if os.path.exists('scores.txt'):
        with open('scores.txt') as best_score:
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
        with open('scores.txt', 'w') as best:
            for i in range(len(lines)):
                best.write(lines[i])
    else:
        with open('scores.txt', 'w') as best_score:
            best_score.write(f'Best score: {score}\nScore: {score}')

def game_over():
    while True: 
        render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
        surface.blit(render_end, ((WIDTH - BLOCK) // 4, (HEIGHT - BLOCK) // 2 - 20))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scores()
                exit()
        pygame.display.flip()

Running = True
while Running:
    surface.blit(background_img, (0, 0))
    
    # drawing snake's tail
    for i, j in snake:
        pygame.draw.rect(surface, pygame.Color('green'),
                      (i, j, BLOCK, BLOCK))
        surface.blit(tail_img, (i, j))
    
    # apple
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, BLOCK, BLOCK))
    
    # snake's head
    surface.blit(snake_img, (x, y)) 
    
    # show score
    render_score = font_score.render(
        f'SCORE: {score}', 1, pygame.Color('orange'))
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
