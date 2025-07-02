import pygame
import random
import sys
import sqlite3

conn = sqlite3.connect('snake_madrid.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE)')
c.execute('CREATE TABLE IF NOT EXISTS user_score (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, score INTEGER, level INTEGER, FOREIGN KEY(user_id) REFERENCES user(id))')
conn.commit()

def get_or_create_user(username):
    c.execute('SELECT id FROM user WHERE username = ?', (username,))
    user = c.fetchone()
    if user:
        return user[0]
    else:
        c.execute('INSERT INTO user (username) VALUES (?)', (username,))
        conn.commit()
        return c.lastrowid

def get_user_score(user_id):
    c.execute('SELECT score, level FROM user_score WHERE user_id = ? ORDER BY id DESC LIMIT 1', (user_id,))
    return c.fetchone()

def save_user_score(user_id, score, level):
    c.execute('INSERT INTO user_score (user_id, score, level) VALUES (?, ?, ?)', (user_id, score, level))
    conn.commit()

pygame.init()
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Madrid")
clock = pygame.time.Clock()

username = input("Enter your username: ")
user_id = get_or_create_user(username)
previous_score = get_user_score(user_id)
if previous_score:
    print(f"Welcome back, {username}! Previous Score: {previous_score[0]}, Level: {previous_score[1]}")
else:
    print(f"Welcome, {username}! Starting a new game.")

snake = [(5, 5)]
snake_dir = (1, 0)
food = None
food_weight = 1
food_timer = 0
FOOD_LIFETIME = 40
score = previous_score[0] if previous_score else 0
paused = False

def generate_food():
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            return pos

def generate_food_with_weight():
    global food_weight, food_timer
    pos = generate_food()
    food_weight = random.choice([1, 3])
    food_timer = 0
    return pos

food = generate_food_with_weight()
running = True

while running:
    level = score // 4 + 1
    speed = 10 + (level - 1) * 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_user_score(user_id, score, level)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_user_score(user_id, score, level)
                    print("Game Paused and Saved.")

    if paused:
        pygame.time.wait(100)
        continue

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or new_head in snake):
        print("Game Over! Final Score:", score)
        save_user_score(user_id, score, level)
        running = False
        continue

    snake.insert(0, new_head)

    if new_head == food:
        score += food_weight
        food = generate_food_with_weight()
    else:
        snake.pop()

    food_timer += 1
    if food_timer > FOOD_LIFETIME:
        food = generate_food_with_weight()

    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    color = RED if food_weight == 1 else BLUE
    pygame.draw.rect(screen, color, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"User: {username} Score: {score} Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()
