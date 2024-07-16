import pygame
import random
import math
from pygame import mixer
import time
import sys
import os

pygame.init()

# Main Screen
screen = pygame.display.set_mode((1920, 1080)) 
wallpaper = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\wallpaper.jpg')
mixer.music.load('D:\Programming\Python\Projects\Spacewar\sounds\\background.mp3')
mixer.music.play(-1)

# Menu
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 45)
resume_text = font.render("Resume", True, white)
exit_text = font.render("Exit", True, white)
resume_rect = resume_text.get_rect(center=(1920 // 2, 1.2*1080 // 3))
exit_rect = exit_text.get_rect(center=(1920 // 2, 1.4*1080 // 3))
menu = True

# Title and Icon
pygame.display.set_caption("Space War")
icon = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\icon.png')
pygame.display.set_icon(icon)

# Player 
player1 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\player1.png')
player2 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\player2.png')
player3 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\player3.png')
player4 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\player4.png')
playerImg = player1
w = playerImg.get_width()
h = playerImg.get_height()
playerX = 960
playerY = 840
playerX_change = 0 
playerY_change = 0.1 

# Enemy 
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = [] 
enemyY_change = [] 
num_of_enemies = 10
for i in range(num_of_enemies):
    enemyType = random.randint(1,4)
    if enemyType == 1 :
        enemyImg.append(pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\enemy1.png'))
    elif enemyType == 2 :
        enemyImg.append(pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\enemy2.png'))
    elif enemyType == 3 :
        enemyImg.append(pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\enemy3.png'))
    elif enemyType == 4 :
        enemyImg.append(pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\enemy4.png'))
    enemyX.append(random.randint(200, 1665))
    enemyY.append(random.randint(120, 160))
    enemyX_change.append(1)
    enemyY_change.append(40) 

# Monster
happymonster = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\happymonster.png')
sadmonster = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\sadmonster.png')
monsterImg = happymonster
monsterX_change = 1.5
monsterX = 850
monsterY = -300
monster_health = 20
counter = 0

# Shot 
shot1 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\shot1.png')
shot2 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\shot2.png')
shot3 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\shot3.png')
shot4 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\shot4.png')
shot5 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\shot5.png')
shot6 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\shot6.png')
shot7 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\shot7.png')
shot8 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\shot8.png')
shot9 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\shot9.png')
laser = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\laser.png')
bullet = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\bullet.png')
shotImg = shot9
laserImg = laser
bulletImg = bullet
shotX = 0
shotY = 720
shotX_change = 0.1 
shotY_change = 3
shot_state = 'ready'
shot_items = [1]
current_item = 0

# Gift
gift1 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\gift1.png')
gift2 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\gift2.png')
gift3 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\gift3.png')
gift4 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\gift4.png')
gift5 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\gift5.png')
gift6 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\gift6.png')
gift7 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\gift7.png')
gift8 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\gift8.png')
gift9 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\gift9.png')
giftImg = gift1
witch_gift = random.randint(1,9)
giftX = random.randint(200, 1665)
giftY = 0
giftY_change = 1
gift_state = 'ready'

# Upgrade
upgradeImg = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\upgrade.png')
upgradeX = random.randint(200, 1665)
upgradeY = 0
upgradeY_change = 1
upgrade_state = 'ready'
upgrade = 1

# Virus 
virusImg = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\virus.png')
monstervirusImg = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\monster_virus.png')
virusX = 0
virusY = 0
virusX1 = 0
virusY1 = 0
virusY_change = 1.5
monster_virusX = monsterX + 200
monster_virusY = 1000
virus_state = 'ready'
witch_enemy = enemyImg.index(random.choice(enemyImg))
witch_enemy1 = enemyImg.index(random.choice(enemyImg))

# Life
lifeImg1 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\life1.png')
lifeImg2 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\life2.png')
lifeImg3 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\life3.png')
lifeImg4 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\life4.png')
lifeImg5 = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\life5.png')
lifeImg = lifeImg1
lifeX = 1555
lifeY = 135
life = 5

# Score
score_value = 0 
scoreTextX = 220
scoreTextY = 130 

# Winner
winnerY = -150
kiaY = -50
winnerY_change = 0.2
kiaY_change = 0.2

# Earth
earthImg = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\earth.png')
earthX = 600

def Player(x,y):
    screen.blit(playerImg,(x,y))

def Enemy(x,y,i):
    screen.blit(enemyImg[i] ,(x,y))

def Making_Enemy(x,y):
    enemyType = random.randint(1,4)
    if enemyType == 1 :
        enemyImg.append(pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\enemy1.png'))
    elif enemyType == 2 :
        enemyImg.append(pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\enemy2.png'))
    elif enemyType == 3 :
        enemyImg.append(pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\enemy3.png'))
    elif enemyType == 4 :
        enemyImg.append(pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\enemy4.png'))
    enemyX.append(random.randint(200, 1665))
    enemyY.append(random.randint(120, 160))
    enemyX_change.append(1)
    enemyY_change.append(40) 
    screen.blit(enemyImg[-1] ,(x,y))

def Monster(x,y):
    screen.blit(monsterImg ,(x,y))

def Shot(x,y):
    screen.blit(shotImg,(x, y+40))

def Laser_Shot(x,y):
    screen.blit(laserImg,(x, y-30))
    screen.blit(laserImg,(x+45, y-30))
    screen.blit(shotImg,(x-10, y-100))

def Bullet_Shot(x,y):
    screen.blit(bulletImg,(x, y-30))
    screen.blit(bulletImg,(x+45, y-30))
    screen.blit(shotImg,(x-10, y-100))

def Bullet_Laser_Shot(x,y):
    screen.blit(laserImg,(x-10, y-30))
    screen.blit(laserImg,(x+55, y-30))
    screen.blit(bulletImg,(x, y-30))
    screen.blit(bulletImg,(x+45, y-30))
    screen.blit(shotImg,(x-10, y-110))

def Gift(x,y,i):
    match i:
        case 1:
            giftImg = gift1
        case 2:
            giftImg = gift2
        case 3:
            giftImg = gift3
        case 4:
            giftImg = gift4
        case 5:
            giftImg = gift5
        case 6:
            giftImg = gift6
        case 7:
            giftImg = gift7
        case 8:
            giftImg = gift8
        case 9:
            giftImg = gift9
    screen.blit(giftImg,(x, y))

def Upgrade(x,y):
    screen.blit(upgradeImg, (x,y))

def Virus(x,y):
    screen.blit(virusImg,(x, y))

def Monster_Virus(x,y):
    screen.blit(monstervirusImg,(x-120, y))
    screen.blit(monstervirusImg,(x-60, y))
    screen.blit(monstervirusImg,(x, y))
    screen.blit(monstervirusImg,(x+60, y))
    screen.blit(monstervirusImg,(x+120, y))

def Collision(x1,y1,x2,y2):
    di = 30
    if x1 == monsterX:
        di = 230
    distance = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
    if distance < di :
        return True
    else :
        return False

def Score(x,y):
    score_font = pygame.font.SysFont(None, 40)
    score = score_font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

def Life(x,y,i):
    match i:
        case 5:
            lifeImg = lifeImg1
        case 4:
            lifeImg = lifeImg2
        case 3:
            lifeImg = lifeImg3
        case 2:
            lifeImg = lifeImg4
        case 1:
            lifeImg = lifeImg5
        case 0:
            Game_Over()
    screen.blit(lifeImg ,(x,y))

def Game_Over():
    mixer.music.stop()
    gameover_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\gameover.mp3')
    gameover_sound.play()
    game_over_font = pygame.font.SysFont(None, 80)
    game_over = game_over_font.render("Game Over", True, (255,0,0))
    screen.blit(game_over,(800,400))
    pygame.display.update()
    time.sleep(200)

def Earth():
    screen.blit(earthImg,(earthX, 200))

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Game Frames 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                clock = pygame.time.Clock()
                clock.tick(60)
                menu = True
                while menu:
                    screen.fill(black)
                    screen.blit(resume_text, resume_rect)
                    screen.blit(exit_text, exit_rect)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if resume_rect.collidepoint(mouse_x, mouse_y):
                                menu = False
                            elif exit_rect.collidepoint(mouse_x, mouse_y):
                                pygame.quit()
                                sys.exit()
            elif event.key == pygame.K_d:
                playerX_change = 1.5
            elif event.key == pygame.K_a:
                playerX_change = -1.5
            elif event.key == pygame.K_SPACE:
                if shot_state is 'ready':
                    shotX = playerX
                    shot_state = 'fire'
                    if playerImg == player1:
                        Shot(shotX,shotY)
                        if shotImg == shot4:
                            shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\\watersplash.wav')
                            shot_sound.play()
                        else:
                            shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\laser.wav')
                            shot_sound.play()
                    elif playerImg == player2:
                        if current_item == 0:
                            Shot(shotX,shotY)
                            if shotImg == shot4:
                                shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\\watersplash.wav')
                                shot_sound.play()
                            else:
                                shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\laser.wav')
                                shot_sound.play()
                        elif current_item == 1:
                            Laser_Shot(shotX,shotY)
                            shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\laser.wav')
                            shot_sound.play()
                    elif playerImg == player3:
                        if current_item == 0:
                            Shot(shotX,shotY)
                            if shotImg == shot4:
                                shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\\watersplash.wav')
                                shot_sound.play()
                            else:
                                shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\laser.wav')
                                shot_sound.play()
                        elif current_item == 1:
                            Laser_Shot(shotX,shotY)
                            shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\laser.wav')
                            shot_sound.play()
                        elif current_item == 2:
                            Bullet_Shot(shotX,shotY)
                            shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\\bullet.mp3')
                            shot_sound.play()
                    elif playerImg == player4:
                        if current_item == 0:
                            Shot(shotX,shotY)
                            if shotImg == shot4:
                                shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\\watersplash.wav')
                                shot_sound.play()
                            else:
                                shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\laser.wav')
                                shot_sound.play()
                        elif current_item == 1:
                            Laser_Shot(shotX,shotY)
                            shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\laser.wav')
                            shot_sound.play()
                        elif current_item == 2:
                            Bullet_Shot(shotX,shotY)
                            shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\\bullet.mp3')
                            shot_sound.play()
                        elif current_item == 3:
                            Bullet_Laser_Shot(shotX,shotY)
                            shot_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\\bullet.mp3')
                            shot_sound.play()
            elif event.key == pygame.K_LSHIFT:
                current_item = (current_item + 1) % len(shot_items)
            elif event.key == pygame.K_LCTRL:
                current_item = (current_item - 1) % len(shot_items)
                    
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_a or event.key == pygame.K_d:
               playerX_change = 0
           elif event.key == pygame.K_SPACE:
               shot_sound.stop()
           elif event.key == pygame.K_LSHIFT or event.key == pygame.K_LSHIFT:
               pass

    screen.fill((0,0,204))
    screen.blit(wallpaper,(0,0))

    # Player Movement
    playerX += playerX_change
    if playerX <= 200:
         playerX = 200 
    elif playerX >= 1665 :
        playerX = 1665

    # Enemy Movement
    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 900:
            for j in range(num_of_enemies):
                enemyY[j] = 1500
            Game_Over()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 200:
            enemyX_change[i] = 1
            enemyImg[i] = pygame.transform.flip(enemyImg[i], True, False)
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1665:
            enemyX_change[i] = -1
            enemyImg[i] = pygame.transform.flip(enemyImg[i], True, False)
            enemyY[i] += enemyY_change[i]

        # Shot Collision 
        collision = Collision(enemyX[i], enemyY[i], shotX, shotY)
        if collision:
            shot_state = 'ready'
            shotY = 720
            score_value += 1
            if score_value % 10 == 0:
                num_of_enemies = num_of_enemies + 1
                Making_Enemy(random.randint(200, 1665), random.randint(120, 160))
            del enemyY[i]
            del enemyX[i]
            del enemyImg[i]
            Making_Enemy(random.randint(200, 1665), random.randint(120, 160))
            pop_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\pop.mp3')
            pop_sound.play()
        Enemy(enemyX[i],enemyY[i],i)

    # Gift Collision 
    collision = Collision(playerX, playerY, giftX, giftY)
    if collision:
            giftY = -5000
            if witch_gift == 1:
                shotImg = shot1
            elif witch_gift == 2:
                shotImg = shot2
            elif witch_gift == 3:
                shotImg = shot3
            elif witch_gift == 4:
                shotImg = shot4
            elif witch_gift == 5:
                shotImg = shot5
            elif witch_gift == 6:
                shotImg = shot6
            elif witch_gift == 7:
                shotImg = shot7
            elif witch_gift == 8:
                shotImg = shot8
            elif witch_gift == 9:
                shotImg = shot9
    
    # Upgrade Collision 
    collision = Collision(playerX, playerY, upgradeX, upgradeY)
    if collision:
        upgrade_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\\upgrade.mp3')
        upgrade_sound.play()
        upgradeY = -1000
        if upgrade <= 4:
            upgrade += 1
            match upgrade:
                case 1:
                    playerImg = player1
                case 2:
                    playerImg = player2
                    shot_items.append(2)
                case 3:
                    playerImg = player3
                    shot_items.append(3)
                case 4:
                    playerImg = player4
                    shot_items.append(4)
        else:
            upgradeY = 2200
            
    # Virus Collision 
    collision = Collision(playerX, playerY, virusX, virusY)
    collision1 = Collision(playerX, playerY, virusX1, virusY1)
    if collision and virusY == playerY:
        virusY = 1000
        life -= 1
        Life(lifeX, lifeY, life)
    elif collision1 and virusY1 == playerY:
        virusY1 = 1000
        life -= 1
        Life(lifeX, lifeY, life)

    # Monster Virus Collision 
    collision1 = Collision(playerX, playerY, monster_virusX-120, monster_virusY)
    collision2 = Collision(playerX, playerY, monster_virusX-60, monster_virusY)
    collision3 = Collision(playerX, playerY, monster_virusX, monster_virusY)
    collision4 = Collision(playerX, playerY, monster_virusX+60, monster_virusY)
    collision5 = Collision(playerX, playerY, monster_virusX+120, monster_virusY)
    if collision1 or collision2 or collision3 or collision4 or collision5:
        monster_virusY = 1000
        life -= 1
        Life(lifeX, lifeY, life)

    # Monster Collision
    collision = Collision(monsterX, monsterY, shotX, shotY)
    if collision:
        shot_state = 'ready'
        shotY = 720
        score_value += 1
        monster_health -= 2
        explosion_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\explosion.wav')
        explosion_sound.play()

    # Shot Movement 
    if shot_state is 'fire':
        if shotY <= 0 : 
            shot_state = 'ready'
            shotY = 720
        if playerImg == player1:
            Shot(shotX, shotY)
        elif playerImg == player2:
            if current_item == 0:
                Shot(shotX, shotY)
            elif current_item == 1:
                Laser_Shot(shotX, shotY)
        elif playerImg == player3:
            if current_item == 0:
                Shot(shotX, shotY)
            elif current_item == 1:
                Laser_Shot(shotX, shotY)
            elif current_item == 2:
                Bullet_Shot(shotX, shotY)
        elif playerImg == player4:
            if current_item == 0:
                Shot(shotX, shotY)
            elif current_item == 1:
                Laser_Shot(shotX, shotY)
            elif current_item == 2:
                Bullet_Shot(shotX, shotY)
            elif current_item == 3:
                Bullet_Laser_Shot(shotX, shotY)
        shotY -= shotY_change

    # Gift Movement 
    if gift_state is 'fire':
        if giftY >= 5000 : 
            gift_state = 'ready'
            gifyY = -1000
        if giftY == -500:
            witch_gift = random.randint(1,9)
            giftX = random.randint(50, 550)
        Gift(giftX, giftY, witch_gift)
        giftY += giftY_change
    if gift_state is 'ready':
            gift_state = 'fire'
            giftY = -1000
            Gift(giftX, giftY, witch_gift)

    # Upgrade Movement 
    if upgrade_state is 'fire':
        if upgradeY == 2000 or score_value % 10 != 0 : 
            upgrade_state = 'ready'
            upgradeY = 0
        if upgradeY == -500:
            upgradeX = random.randint(50, 550)
        Upgrade(upgradeX, upgradeY)
        upgradeY += upgradeY_change
    if upgrade_state is 'ready':
        if score_value != 0 and score_value % 10 == 0:
            upgrade_state = 'fire'
            upgradeY = 0
            Upgrade(upgradeX, upgradeY)
    
    # Virus Movement 
    if virus_state is 'fire':
        if virusY == -500:
            witch_enemy = enemyImg.index(random.choice(enemyImg))
            witch_enemy1 = enemyImg.index(random.choice(enemyImg))
        if virusY >= 1000 : 
            virus_state = 'ready'
            virusX = enemyX[witch_enemy]
            virusY = enemyY[witch_enemy]
            virusX1 = enemyX[witch_enemy1]
            virusY1 = enemyY[witch_enemy1]
        Virus(virusX, virusY)
        Virus(virusX1, virusY1)
        virusY += virusY_change
        virusY1 += virusY_change
    if virus_state is 'ready':
            virus_state = 'fire'
            Virus(virusX,virusY)
            Virus(virusX1,virusY1)
    
    # Monster Movement
    if monsterY == -299.4:
        laugh_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\laugh.mp3')
        laugh_sound.play(-1)
    if score_value >= 60 and monster_health != 0:
        for i in range(num_of_enemies):
            enemyY[i] = -1000  
        Monster(monsterX, monsterY)
        if monsterY <= 160:
            monsterY_change = 0.3
            monsterY += monsterY_change
        else:
            monsterX += monsterX_change
            if monsterX <= 200:
                monsterX_change = 1.5
                monsterX += monsterX_change
            elif monsterX >= 1430:
                monsterX_change = -1.5
                monsterX += monsterX_change
        # Monster Virus
        if virus_state is 'fire':
            if monster_virusY == 1000 : 
                virus_state = 'ready'
            Monster_Virus(monster_virusX, monster_virusY)
            monster_virusY += virusY_change
        if virus_state is 'ready':
                virus_state = 'fire'
                monster_virusY = 400
                monster_virusX = monsterX + 200
                Monster_Virus(monster_virusX, monster_virusY)
    # Monster Dead
    if monster_health <= 0 and monsterY > 20:
        scream_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\\scream.mp3')
        scream_sound.play()
    if monster_health <= 0:
        laugh_sound.stop()
        monsterImg = sadmonster
        Monster(monsterX, monsterY)
        if counter != 2:
            monsterX += monsterX_change
            if monsterX <= 500:
                counter += 1
                monsterX_change = 7
            elif monsterX >= 1000:
                monsterX_change = -7
        elif counter == 2 and monsterY >= -300:
            monsterX = 850
            monsterY_change = -1
            monsterY += monsterY_change

        # Go to The Earth
        if monsterY <= 50:
            scream_sound.stop()
            winner_sound = mixer.Sound('D:\Programming\Python\Projects\Spacewar\sounds\winning.mp3')
            winner_sound.play()
        if monsterY <= -200:
            Earth()
            if playerY > 320:
                playerY_change = -1
                playerY += playerY_change
                if playerY % 30 == 0:
                    playerImg = pygame.transform.scale(playerImg, (w * 0.9, h * 0.9))
                    playerX = 700
                    w *= 0.9
                    h *= 0.9
            if playerY == 320:
                playerImg = pygame.image.load('D:\Programming\Python\Projects\Spacewar\pic\\bright.png')
                screen.blit(playerImg,(playerX, playerY))

        # Winner
        if monsterY <= -300:
            winner_sound.stop()
            winner_font = pygame.font.SysFont(None, 100)
            kia_font = pygame.font.SysFont(None, 30)
            winner = winner_font.render("Winner", True, (0,0,255))
            kia = kia_font.render("Powered by KIA", True, (255,255,255))
            screen.blit(winner,(960,winnerY))
            screen.blit(kia,(1000,kiaY))
            if winnerY <= 300:
                winnerY_change = 1
                winnerY += winnerY_change
            if kiaY <= 400:
                kiaY_change = 1
                kiaY += kiaY_change
            if winnerY == 150 and kiaY == 230:
                time.sleep(2000)    
                
    Life(lifeX, lifeY, life)
    Player(playerX, playerY)
    Score(scoreTextX, scoreTextY)
    pygame.display.update()
