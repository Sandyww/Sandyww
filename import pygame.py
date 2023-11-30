import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Shooter Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the player character
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_speed = 5
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Define the bullet properties
bullet_width = 5
bullet_height = 15
bullet_speed = 10
bullets = []

# Define the monster properties
monster_width = 50
monster_height = 50
monster_speed = 3
monsters = []

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot a bullet
                bullet_x = player.x + player.width // 2 - bullet_width // 2
                bullet_y = player.y
                bullet = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
                bullets.append(bullet)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < window_width - player_width:
        player.x += player_speed

    # Move the bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Spawn monsters
    if len(monsters) < 5:
        monster_x = random.randint(0, window_width - monster_width)
        monster_y = random.randint(-500, -monster_height)
        monster = pygame.Rect(monster_x, monster_y, monster_width, monster_height)
        monsters.append(monster)

    # Move the monsters
    for monster in monsters:
        monster.y += monster_speed
        if monster.y > window_height:
            monsters.remove(monster)

    # Check for collisions
    for bullet in bullets:
        for monster in monsters:
            if bullet.colliderect(monster):
                bullets.remove(bullet)
                monsters.remove(monster)

    # Clear the screen
    window.fill(BLACK)

    # Draw the player
    pygame.draw.rect(window, WHITE, player)

    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(window, WHITE, bullet)

    # Draw the monsters
    for monster in monsters:
        pygame.draw.rect(window, WHITE, monster)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()