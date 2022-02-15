#(OwO)
import pygame
import random
import math
from pygame import mixer
pygame.init()
mixer.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Inveders")
background = pygame.image.load("scr/background.png")
mixer.music.load('scr/background.mp3')
mixer.music.play(-1)
icon = pygame.image.load('scr/space-invaders.png')
pygame.display.set_icon(icon)
PlayerImg = pygame.image.load("scr/space-ship.png")
PlayerX = 370
PlayerY = 536
PlayerX_change = 0
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemys = 6
for i in range(num_of_enemys):
    EnemyImg.append(pygame.image.load("scr/ghost.png"))
    EnemyX.append(random.randint(50,750))
    EnemyY.append(random.randint(50,150))
    EnemyX_change.append(2)
    EnemyY_change.append(40)
Bulletimg = pygame.image.load("scr/bullet.png")
BulletX = 0
BulletY = 495
BulletX_change = 0
BulletY_change = 10
Bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf',25)
textX = 10
textY = 10
over_font = pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score = font.render("Score : " + str(score_value),True , (255,255,255))
    screen.blit(score, (x,y))
def game_over_text():
    over_text = over_font.render("GAME OVER" ,True , (255,255,255))
    screen.blit(over_text, (200,250))
def Player(x,y):
    screen.blit(PlayerImg,(x,y))
def Enemy(x,y ,i):
    screen.blit(EnemyImg[i],(x,y))
def fire_bullet (x,y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(Bulletimg,(x + 16,y +10))
def iscollision(EnemyX,EnemyY,BulletX,BulletY):
    distance = math.sqrt(math.pow(EnemyX - BulletX ,2) + math.pow(EnemyY - BulletY ,2))
    if distance < 27:
        return True
    else:
        return False
running  = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -2
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 2
            if event.key == pygame.K_SPACE:
                if Bullet_state is "ready":
                    bullet_sound = mixer.Sound("scr/shoot.wav")
                    bullet_sound.set_volume(0.7)
                    bullet_sound.play()
                    BulletX = PlayerX
                    fire_bullet(PlayerX,BulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0
    PlayerX += PlayerX_change
    if PlayerX <=0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736
    for i in range(num_of_enemys):
        if EnemyY[i] > 490:
            for j in range(num_of_enemys):
                EnemyY[j] = 2000
            game_over_text()
            break
        EnemyX[i] += EnemyX_change[i]
        if EnemyX[i] <=0:
            EnemyX_change[i] = 2
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -2
            EnemyY[i] += EnemyY_change[i]
        collision = iscollision(EnemyX[i],EnemyY[i],BulletX,BulletY)
        if collision:
            killed_sound = mixer.Sound("scr/killed.wav")
            killed_sound.set_volume(2)
            killed_sound.play()
            BulletY = 480
            Bullet_state = "ready"
            score_value += 1
            EnemyX[i] = random.randint(50,735)
            EnemyY[i] = random.randint(50,150)
        Enemy(EnemyX[i],EnemyY[i],i)
    if BulletY <= 0:
        BulletY = 480
        Bullet_state= "ready"
    if Bullet_state is "fire":
        fire_bullet(BulletX,BulletY)
        BulletY -= BulletY_change
    Player(PlayerX,PlayerY)
    show_score(textX,textY)
    pygame.display.update()
#(OwO)
