import pygame
import random
import math

from pygame import mixer
pygame.init()  # we need to initialize pygame
screen = pygame.display.set_mode((800, 600))  # create screen and give the height and width
# background
background = pygame.image.load("background.png")

# background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Space Raiders")  # set the title
icon = pygame.image.load("spaceshipIcon.png")  # .image accesses the pygame image module and .load loads the image
pygame.display.set_icon(icon)  # icon size should always be 32 x 32 pixels

# player
playerIcon = pygame.image.load("shootingShip.png")
playerIconX = 370
playerIconY = 520
playerIconX_change = 0

# enemy
enemyIcon = []
enemyIconX = []
enemyIconY = []
enemyIconX_change = []
enemyIconY_change = []
n_enemies = 6
for i in range(n_enemies):
    enemyIcon.append(pygame.image.load("enemy.png"))
    enemyIconX.append(random.randint(0, 746))
    enemyIconY.append(random.randint(50, 150))
    enemyIconX_change.append(2)
    enemyIconY_change.append(20)

# bullet
bulletIcon = pygame.image.load("bullet.png")
bulletIconX = 0
bulletIconY = 520
bulletIconX_change = 0
bulletIconY_change = 11
bullet_state = "ready"  # you cant see the bullet on the screen

# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 30)  # display font
textX = 10
textY = 10

#game over text
over_font = pygame.font.Font("freesansbold.ttf", 70)


def show_score(x, y):
    score = font.render("score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (300, 350))
def player(x, y):
    screen.blit(playerIcon, (x, y))  # blit means to draw


def enemy(x, y, i):
    screen.blit(enemyIcon[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIcon, (x + 1, y + 0))


def isCollision(enemyIconX, enemyIconY, bulletIconX, bulletIconY):
    distance = math.sqrt((math.pow(enemyIconX - bulletIconX, 2)) + (math.pow(enemyIconY - bulletIconY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop: this is an infinite loop that ensure the game keeps running and the window does not close down
# anything you want to be consistent must be in this loop
running = True
while running:
    # change the color of the background
    screen.fill((128, 0, 0))  # RBG colors
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():  # ensures all events happening get into this loop
        if event.type == pygame.QUIT:  # to check if the event is closed
            running = False

    # keystroke / key binding: check whether the keystroke is left or right
    if event.type == pygame.KEYDOWN:  # when key is pressed down
        print("key pressed")
        if event.key == pygame.K_LEFT:
            playerIconX_change = -5
        if event.key == pygame.K_RIGHT:
            playerIconX_change = 5
        if event.key == pygame.K_CAPSLOCK:
            if bullet_state is "ready":
               bullet_sound = mixer.Sound("laser.wav")
               bullet_sound.play()
            bulletIconX = playerIconX
            fire_bullet(bulletIconX, bulletIconY)

    if event.type == pygame.KEYUP:  # when key is released
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  #
            playerIconX_change = 0

    # player boundary
    playerIconX += playerIconX_change

    if playerIconX <= 0:
        playerIconX = 0
    elif playerIconX >= 736:
        playerIconX = 736

    # enemy movement
    for i in range(n_enemies):
        # game over
        if enemyIconY[i] > 470:
            for j in range(n_enemies):
                enemyIconY[j] = 2000
            game_over_text()
            break

        enemyIconX[i] += enemyIconX_change[i]
        if enemyIconX[i] <= 0:
            enemyIconX_change[i] = 2
            enemyIconY[i] += enemyIconY_change[i]
        elif enemyIconX[i] >= 736:
            enemyIconX_change[i] = -2
            enemyIconY[i] += enemyIconY_change[i]

        # collision

        collision = isCollision(enemyIconX[i], enemyIconY[i], bulletIconX, bulletIconY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletIconY = 520
            bullet_state = "ready"
            score_value += 1
            enemyIconX[i] = random.randint(0, 746)
            enemyIconY[i] = random.randint(50, 150)

        enemy(enemyIconX[i], enemyIconY[i], i)

    # bullet movement
    if bulletIconY <= 0:
        bulletIconY = 520  # allows to shoot multiple bullet
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletIconX, bulletIconY)
        bulletIconY -= bulletIconY_change

    # collision

    '''collision = isCollision(enemyIconX, enemyIconY, bulletIconX, bulletIconY)
    if collision:
        bulletIconY = 520
        bullet_state = "ready"
        score += 1
        enemyIconX = random.randint(0, 746)
    enemyIconY = random.randint(50, 150)
    '''
    player(playerIconX, playerIconY)  # always draw after screen to
    show_score(textX, textY)
    pygame.display.update()
