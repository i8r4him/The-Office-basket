import os.path

import pygame
import math
import random
from pygame import mixer
from os import path
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675
BODEN_Y = 645
COLOR_LINE = (0,0,0)
COLOR_PLINE = (255,255,255)
angle_i = -90
HS_bool = True
game_easy_active = False
HS_easy_FILE = "HighScore_easy.txt"
game_medium_active = False
HS_medium_FILE = "HighScore_medium.txt"
game_hard_active = False
HS_hard_FILE = "HighScore_hard.txt"
change_level = False
score = "0"
score_five=0
level = ""
easy_gross = False
medium_gross = False
hard_gross = False
music_gross = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Office basket')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)


#load high score easy
if os.path.exists(HS_easy_FILE):
    with open(HS_easy_FILE,'r') as e:
            highscore_easy = int(e.read())
else:
    highscore_easy = 0

#load high score medium
if os.path.exists(HS_medium_FILE):
    with open(HS_medium_FILE,'r') as e:
            highscore_medium = int(e.read())
else:
    highscore_medium = 0

#load high score hard
if os.path.exists(HS_hard_FILE):
    with open(HS_hard_FILE,'r') as e:
            highscore_hard = int(e.read())
else:
    highscore_hard = 0

#Background sound
mixer.music.load('Assets\hintergrund.wav')
mixer.music.play(-1)
pygame.mixer.music.set_volume(0.075)

paper_surf = pygame.image.load('Assets\papier.png').convert_alpha()     #https://www.cleanpng.com/png-paper-shredder-recycling-waste-distances-2322683/
paper_surf = pygame.transform.scale(paper_surf, (50, 50))
paper_rect = paper_surf.get_rect(bottomleft=(0, BODEN_Y))

korb_surf = pygame.image.load('Assets\Trash_Can.png').convert_alpha()        #https://www.crazypng.com/download.php?url=http://pngimg.com/download/18471
korb_surf = pygame.transform.scale(korb_surf, (125, 150))
korb_rect = korb_surf.get_rect(bottomright=(SCREEN_WIDTH,BODEN_Y ))
korb_y=korb_rect.midtop[1]



score_surf = test_font.render('Score: '+ score, False, (255,0,0))
score_rect = score_surf.get_rect(topright=(SCREEN_WIDTH, 0))

backg_surf = pygame.image.load('Assets\hinterg.png')    #https://www.cleanpng.com/png-loft-window-office-room-stock-photography-building-370018/preview.html
backg_surf = pygame.transform.scale(backg_surf, (SCREEN_WIDTH+120,SCREEN_HEIGHT+60))
backg_rect = backg_surf.get_rect(topleft=(0,0))

backg1_surf = pygame.image.load('Assets\hintergrund.jpg')       #https://unsplash.com/s/photos/office
backg1_surf = pygame.transform.scale(backg1_surf, (SCREEN_WIDTH,SCREEN_HEIGHT))
backg1_rect = backg1_surf.get_rect(topleft=(0,0))

backg2_surf = pygame.image.load('Assets\hinterg_hard.jpg')      #https://www.etsy.com/de/listing/796604190/zoom-hintergrund-home-office-kulisse
backg2_surf = pygame.transform.scale(backg2_surf, (SCREEN_WIDTH,SCREEN_HEIGHT))
backg2_rect = backg2_surf.get_rect(topleft=(0,0))

power_surf = pygame.image.load('Assets\power.png')      #https://github.com/techwithtim/Golf-Game/blob/master/img/power.png
power_surf = pygame.transform.scale(power_surf, (125,125))
power_rect = power_surf.get_rect(bottomleft=(0,SCREEN_HEIGHT+60))

start_surf = pygame.image.load('Assets\start.jpeg')
start_surf = pygame.transform.scale(start_surf,(SCREEN_WIDTH,SCREEN_HEIGHT))
start_rect = start_surf.get_rect(topleft=(0,0))

level_surf = pygame.image.load('Assets\office-waste-bin_3.png')
level_surf = pygame.transform.scale(level_surf,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_rect = level_surf.get_rect(topleft=(0,0))
paper_vel = 10

music_surf = pygame.image.load('Assets\Music.png')  #https://www.pikpng.com/pngvi/hwboRb_music-icon-white-clipart/
music_surf = pygame.transform.scale(music_surf,(25,25))
music_rect = music_surf.get_rect(topright=(SCREEN_WIDTH-25,25))

restart_message = test_font.render(f'Press Space to restart ', False, (0, 0, 0))
restart_message_rect = restart_message.get_rect(center=(550, 350))
restart_message = pygame.transform.rotozoom(restart_message, 0, 1.25)

menu_message = test_font.render(f'Press ENTER to select another level', False, (0,0,0))
menu_message = pygame.transform.rotozoom(menu_message,0,1.25)
menu_message_rect = menu_message.get_rect(center=(600, 425))

press_message = test_font.render(f'Press ENTER to start', False, (238,238,0))
press_message = pygame.transform.rotozoom(press_message,0,1)
press_message_rect = press_message.get_rect(center=(225, 400))

easy_message = test_font.render(f'Easy', False, (250, 250, 250))
easy_message = pygame.transform.rotozoom(easy_message, 0, 2)
easy_message_rect = easy_message.get_rect(center=(535, 325))

medium_message = test_font.render(f'Medium', False, (250, 250, 250))
medium_message = pygame.transform.rotozoom(medium_message, 0, 2)
medium_message_rect = medium_message.get_rect(center=(535, 460))

hard_message = test_font.render(f'Hard', False, (250, 250, 250))
hard_message = pygame.transform.rotozoom(hard_message, 0, 2)
hard_message_rect = hard_message.get_rect(center=(535, 600))


#Globale variables for the draw_line function
laenge = 100
ang = 0.01
vel_easy_ang = 0.03
vel_medhard_ang = 0.05
line_y = paper_rect.midtop[1] - math.sin(ang) * laenge
line_x = math.cos(ang) * laenge + paper_rect.midtop[0]
leertaste = True

#Globale variables for the draw_pline function
laenge_pline = 45
ang_p = math.pi-0.01
vel_easy_angp = 0.03
vel_medhard_angp = 0.05
pline_y = power_rect.center[1] - math.sin(ang) * laenge_pline
pline_x = math.cos(ang) * laenge_pline + power_rect.center[0]
leertaste_two = True

#Drawing direction line
def draw_line():
    global ang, vel_easy_ang,vel_medhard_ang, line_x, line_y, shoot
    if game_easy_active:
        if ang > 0 and ang < math.pi / 2 and leertaste == True:#the angle is between pi and pi/2 and space == not Keydown
            line_y = paper_rect.midtop[1] - math.sin(ang) * laenge
            line_x = math.cos(ang) * laenge + paper_rect.midtop[0]
            pygame.draw.line(screen, COLOR_LINE, paper_rect.midtop, (line_x, line_y), 4)
            ang = ang + vel_easy_ang

        elif leertaste == True and (ang <= 0 or ang >= math.pi / 2):
            vel_easy_ang = -vel_easy_ang
            ang += vel_easy_ang
        elif shoot == False:
            pygame.draw.line(screen, COLOR_LINE, paper_rect.midtop, (line_x, line_y), 4)

    elif game_medium_active or game_hard_active:
        if ang > 0 and ang < math.pi / 2 and leertaste == True:  # the angle is between pi and pi/2 and space == not Keydown
            line_y = paper_rect.midtop[1] - math.sin(ang) * laenge
            line_x = math.cos(ang) * laenge + paper_rect.midtop[0]
            pygame.draw.line(screen, COLOR_LINE, paper_rect.midtop, (line_x, line_y), 4)
            ang = ang + vel_medhard_ang

        elif leertaste == True and (ang <= 0 or ang >= math.pi / 2):
            vel_medhard_ang = -vel_medhard_ang
            ang += vel_medhard_ang
        elif shoot == False:
            pygame.draw.line(screen, COLOR_LINE, paper_rect.midtop, (line_x, line_y), 4)

#Drawing power line
def draw_pline():
    global ang_p, vel_easy_angp,vel_medhard_angp, pline_x,pline_y
    if game_easy_active:
        if ang_p > 0 and ang_p < math.pi and leertaste_two == True:
            pline_y = power_rect.center[1] - math.sin(ang_p) * laenge_pline
            pline_x = math.cos(ang_p) * laenge_pline + power_rect.center[0]
            pygame.draw.line(screen, COLOR_PLINE, power_rect.center, (pline_x, pline_y), 3)
            ang_p = ang_p + vel_easy_angp

        elif leertaste_two == True and (ang_p <= 0 or ang_p >= math.pi):
            vel_easy_angp = -vel_easy_angp
            ang_p += vel_easy_angp
        else:
            pygame.draw.line(screen, COLOR_PLINE, power_rect.center, (pline_x, pline_y), 3)

    elif game_medium_active or game_hard_active:
        if ang_p > 0 and ang_p < math.pi and leertaste_two == True:
            pline_y = power_rect.center[1] - math.sin(ang_p) * laenge_pline
            pline_x = math.cos(ang_p) * laenge_pline + power_rect.center[0]
            pygame.draw.line(screen, COLOR_PLINE, power_rect.center, (pline_x, pline_y), 3)
            ang_p = ang_p + vel_medhard_angp

        elif leertaste_two == True and (ang_p <= 0 or ang_p >= math.pi):
            vel_medhard_angp = -vel_medhard_angp
            ang_p += vel_medhard_angp
        else:
            pygame.draw.line(screen, COLOR_PLINE, power_rect.center, (pline_x, pline_y), 3)

def ballPath(startx, starty, power, ang, time):     #https://github.com/techwithtim/Golf-Game/blob/master/physics.py
    angle = ang
    velx = math.cos(angle) * power#(y-math.sin(angle)*power*(time-0.15))>=korb_rect.midtop[1]
    vely = math.sin(angle) * power

    distX = velx * time
    distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

    newx = round(distX + startx)
    newy = round(starty - distY)

    return (newx, newy)

def reset_score():
    global score,score_rect,score_surf
    score = 0
    score = str(int(score))
    score_surf = test_font.render('Score: ' + score, False, (255, 0, 0))
    score_rect = score_surf.get_rect(topright=(SCREEN_WIDTH, 0))

#paper mouvement variables
x=0
y=0
time=0
power=0
angle=0
shoot=False
collide=False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #updating high score
            if level == "e":
                if int(score)> highscore_easy:
                    highscore_easy = int(score)
                    with open(HS_easy_FILE,'w') as e:
                        e.write(score)
            elif level == "m":
                if int(score)> highscore_medium:
                    highscore_medium = int(score)
                    with open(HS_medium_FILE,'w') as e:
                        e.write(score)
            elif level == "h":
                if int(score)> highscore_hard:
                    highscore_hard = int(score)
                    with open(HS_hard_FILE,'w') as e:
                        e.write(score)
            pygame.quit()
            exit()
        if game_easy_active:#active easy game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and leertaste == False and shoot == False:#second space click
                leertaste_two = False
                shoot = True
                x = paper_rect.x
                y = paper_rect.y
                time = 0
                power = abs(ang_p - math.pi) * 30
                angle = ang
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # first space click ##wenn ich das vor die zweiteclick condition gemacht habe,dann halten beide Pfeile gleichzeitig
                leertaste = False


        elif game_medium_active:#active medium game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and leertaste == False and shoot == False:#second space click
                leertaste_two = False
                shoot = True
                x = paper_rect.x
                y = paper_rect.y
                time = 0
                power = abs(ang_p - math.pi) * 30
                angle = ang
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # first space click ##wenn ich das vor die zweiteclick condition gemacht habe,dann halten beide Pfeile gleichzeitig
                leertaste = False


        elif game_hard_active:#active hard game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # first space click ##wenn ich das vor die zweiteclick condition gemacht habe,dann halten beide Pfeile gleichzeitig
                leertaste = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and leertaste == False and shoot == False:#second space click
                leertaste_two = False
                shoot = True
                x = paper_rect.x
                y = paper_rect.y
                time = 0
                power = abs(ang_p - math.pi) * 30
                angle = ang


        elif change_level:

            if easy_message_rect.collidepoint(pygame.mouse.get_pos()):
                easy_gross = True
                medium_gross = False
                hard_gross = False
                music_gross = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_easy_active = True
                    change_level = False
                    level = "e"
            elif medium_message_rect.collidepoint(pygame.mouse.get_pos()):
                easy_gross = False
                medium_gross = True
                hard_gross = False
                music_gross = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_medium_active = True
                    change_level = False
                    level = "m"
            elif hard_message_rect.collidepoint(pygame.mouse.get_pos()):
                easy_gross = False
                medium_gross = False
                hard_gross = True
                music_gross = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_hard_active = True
                    change_level = False
                    level = "h"
            elif music_rect.collidepoint(pygame.mouse.get_pos()):
                easy_gross = False
                medium_gross = False
                hard_gross = False
                music_gross = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    music_volume = mixer.music.get_volume()
                    if music_volume>0:
                        mixer.music.set_volume(0)
                    else:
                        mixer.music.set_volume(0.075)
            else:
                easy_gross = False
                medium_gross = False
                hard_gross = False
                music_gross = False

        else:#game over
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:#click space to return to the game and set score=0
                change_level = True
                reset_score()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if level == "e":
                    game_easy_active = True
                    reset_score()
                elif level == "m":
                    game_medium_active = True
                    reset_score()
                elif level == "h":
                    game_hard_active = True
                    reset_score()


    if game_easy_active: #active easy game
        if shoot and collide == False:#ball in the air and not colliding
            if paper_rect.midright[0] >= SCREEN_WIDTH or (paper_rect.midright[0] >= korb_rect.midleft[0]+10 and paper_rect.midbottom[1] >= korb_rect.midtop[1]+10): #is_collision
                collide = True
                power = power/4
                time = 0
            elif  paper_rect.midbottom[1] <= BODEN_Y and paper_rect.midleft[0] < SCREEN_WIDTH and (not (paper_rect.midbottom[1]>=korb_y and  paper_rect.bottomleft[0]>=korb_rect.bottomleft[0] and paper_rect.bottomright[0]<=korb_rect.bottomright[0]and paper_rect.center[1]<korb_y)):#not in the ground#not succeeding the border#not in korb ##paper in the air
                time += 0.15
                po = ballPath(x,y,power,angle,time)
                paper_rect.x = po[0]
                paper_rect.y = po[1]

            elif paper_rect.midbottom[1]>= BODEN_Y and paper_rect.bottomright[0]< korb_rect.bottomleft[0]:#is_on_the_floor#x_paper<korb_x
                shoot = False
                leertaste = True
                leertaste_two = True
                paper_rect.x = 0
                if paper_rect.colliderect(power_rect):
                    paper_rect.x = paper_rect.x + random.randint(0, 150)

                paper_rect.bottom = BODEN_Y
                game_easy_active = False
                #game over sound effect
                game_over_sound = mixer.Sound('Assets\game_over_1.wav')     #https://mixkit.co/free-sound-effects/game-over/
                game_over_sound.play()
                game_over_sound.set_volume(0.075)

            elif paper_rect.midbottom[1]>=korb_y and  paper_rect.bottomleft[0]>=korb_rect.topleft[0] and paper_rect.bottomright[0]<=korb_rect.topright[0] and paper_rect.center[1]<korb_y:#ball in the basket
                shoot = False
                leertaste = True
                leertaste_two = True
                paper_rect.x = 0
                paper_rect.bottom = BODEN_Y
                score = str(int(score) + 1)
                score_surf = test_font.render('Score: ' + score, False, (255, 0, 0))
                score_rect = score_surf.get_rect(topright=(SCREEN_WIDTH, 0))
                goal_sound = mixer.Sound('Assets\goal.wav')  # https://mixkit.co/free-sound-effects/win/
                goal_sound.play()
                goal_sound.set_volume(0.075)
                if paper_rect.colliderect(power_rect):
                    paper_rect.x = paper_rect.x + random.randint(0, 150)

            else:
                shoot = False
                leertaste = True
                leertaste_two = True
                paper_rect.x = 0
                if paper_rect.colliderect(power_rect):
                    paper_rect.x = paper_rect.x + random.randint(0, 150)
                paper_rect.bottom = BODEN_Y
                game_easy_active = False
                change_level = False
                # game over sound effect
                game_over_sound = mixer.Sound('Assets\game_over_1.wav')  # https://mixkit.co/free-sound-effects/game-over/
                game_over_sound.play()
                game_over_sound.set_volume(0.075)

        elif collide == True:#is_collision
            angle = math.pi + angle
            #Collision sound effect
            collision_sound = mixer.Sound('Assets\collision.wav')   #https://mixkit.co/free-sound-effects/ball/
            collision_sound.play()
            collision_sound.set_volume(0.1)
            if paper_rect.midright[0] >= SCREEN_WIDTH:
                paper_rect.right=SCREEN_WIDTH-1
            elif paper_rect.midbottom[1]-10<=korb_rect.midtop[1]+10 and paper_rect.center[0]>korb_rect.midleft[0]:#ball over the basket
                paper_rect.bottom = korb_rect.midtop[1]
                angle = math.pi/4
                power *= 2
            elif paper_rect.midbottom[1]-10<=korb_rect.midtop[1]+10 and paper_rect.center[0]<=korb_rect.midleft[0]:
                paper_rect.bottom = korb_rect.midtop[1]
                angle = math.pi * 3 / 4
                power *= 2
            else:
                paper_rect.right = korb_rect.midleft[0]-1
                angle = math.pi
                power /= 2

            x=paper_rect.x
            y=paper_rect.y
            collide=False


        # No collision between the paper and the power indicator
        if paper_rect.colliderect(power_rect):
            paper_rect.x = paper_rect.x + random.randint(0,150)


        # Drawing images while game active
        screen.fill((225, 225, 225))
        screen.blit(backg_surf, backg_rect)
        screen.blit(paper_surf, paper_rect)
        screen.blit(korb_surf, korb_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(power_surf, power_rect)


        draw_line()
        draw_pline()

    elif game_medium_active:#active medium game
        if shoot and collide == False:#ball in the air and not colliding
            if paper_rect.midright[0] >= SCREEN_WIDTH or (paper_rect.midright[0] >= korb_rect.midleft[0]+10 and paper_rect.midbottom[1] >= korb_rect.midtop[1]+10): #is_collision
                collide = True
                power=power/4
                time=0
            elif  paper_rect.midbottom[1]<= BODEN_Y and paper_rect.midleft[0]<SCREEN_WIDTH and (not (paper_rect.midbottom[1]>=korb_y and  paper_rect.bottomleft[0]>=korb_rect.bottomleft[0] and paper_rect.bottomright[0]<=korb_rect.bottomright[0]and paper_rect.center[1]<korb_y)):#not in the ground#not succeeding the border#not in korb ##paper in the air
                time+=0.15
                po = ballPath(x,y,power,angle,time)
                paper_rect.x = po[0]
                paper_rect.y = po[1]

            elif paper_rect.midbottom[1]>= BODEN_Y and paper_rect.bottomright[0]< korb_rect.bottomleft[0]:#is_on_the_floor#x_paper<korb_x
                shoot = False
                leertaste = True
                leertaste_two = True
                paper_rect.x = 0
                if paper_rect.colliderect(power_rect):
                    paper_rect.x = paper_rect.x + random.randint(0, 150)

                paper_rect.bottom = BODEN_Y
                game_medium_active = False
                # game over sound effect
                game_over_sound = mixer.Sound('Assets\game_over_1.wav')  # https://mixkit.co/free-sound-effects/game-over/
                game_over_sound.play()
                game_over_sound.set_volume(0.075)

            elif paper_rect.midbottom[1]>=korb_y and  paper_rect.bottomleft[0]>=korb_rect.topleft[0] and paper_rect.bottomright[0]<=korb_rect.topright[0] and paper_rect.center[1]<korb_y:#ball in the basket
                shoot = False
                leertaste = True
                leertaste_two = True
                paper_rect.x = 0
                paper_rect.bottom = BODEN_Y
                score = str(int(score) + 1)
                score_surf = test_font.render('Score: ' + score, False, (255, 0, 0))
                score_rect = score_surf.get_rect(topright=(SCREEN_WIDTH, 0))
                goal_sound = mixer.Sound('Assets\goal.wav')  # https://mixkit.co/free-sound-effects/win/
                goal_sound.play()
                goal_sound.set_volume(0.075)
                if paper_rect.colliderect(power_rect):
                    paper_rect.x = paper_rect.x + random.randint(0, 150)

            else:
                shoot = False
                leertaste = True
                leertaste_two = True
                paper_rect.x = 0
                if paper_rect.colliderect(power_rect):
                    paper_rect.x = paper_rect.x + random.randint(0, 150)
                paper_rect.bottom = BODEN_Y
                game_medium_active = False
                change_level = False
                # game over sound effect
                game_over_sound = mixer.Sound('Assets\game_over_1.wav')  # https://mixkit.co/free-sound-effects/game-over/
                game_over_sound.play()
                game_over_sound.set_volume(0.075)

        elif collide == True:#is_collision
            angle = math.pi + angle
            # Collision sound effect
            collision_sound = mixer.Sound('Assets\collision.wav')  # https://mixkit.co/free-sound-effects/ball/
            collision_sound.play()
            collision_sound.set_volume(0.1)
            if paper_rect.midright[0] >= SCREEN_WIDTH:
                paper_rect.right=SCREEN_WIDTH-1
            elif paper_rect.midbottom[1]-10<=korb_rect.midtop[1]+10 and paper_rect.center[0]>=korb_rect.midleft[0]:#ball over the basket
                paper_rect.bottom = korb_rect.midtop[1]
                angle = math.pi/4
                power *= 2
            elif paper_rect.midbottom[1]-10<=korb_rect.midtop[1]+10 and paper_rect.center[0]<=korb_rect.midleft[0]:
                paper_rect.bottom = korb_rect.midtop[1]
                angle = math.pi * 3 / 4
                power *= 2
            else:
                paper_rect.right = korb_rect.midleft[0]-1
                angle = math.pi
                power /= 2

            x = paper_rect.x
            y = paper_rect.y
            collide = False

        # No collision between the paper and the power indicator
        if paper_rect.colliderect(power_rect):
            paper_rect.x = paper_rect.x + random.randint(0,150)


        # Drawing images while game active
        screen.fill((225, 225, 225))
        screen.blit(backg1_surf, backg1_rect)
        screen.blit(paper_surf, paper_rect)
        screen.blit(korb_surf, korb_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(power_surf, power_rect)


        draw_line()
        draw_pline()

    elif game_hard_active:  # active hard game
        if shoot and collide == False:  # ball in the air and not colliding
            if paper_rect.midright[0] >= SCREEN_WIDTH or (paper_rect.midright[0] >= korb_rect.midleft[0]+10 and paper_rect.midbottom[1] >= korb_rect.midtop[1]+10):  # is_collision
                collide = True
                power = power / 4
                time = 0
            elif paper_rect.midbottom[1] <= BODEN_Y and paper_rect.midleft[0] < SCREEN_WIDTH and (not (paper_rect.midbottom[1] >= korb_y and paper_rect.bottomleft[0] >= korb_rect.bottomleft[0] and paper_rect.bottomright[0] <= korb_rect.bottomright[0] and paper_rect.center[1] < korb_y)):  # not in the ground#not succeeding the border#not in korb ##paper in the air
                time += 0.15
                po = ballPath(x, y, power, angle, time)
                paper_rect.x = po[0]
                paper_rect.y = po[1]

            elif paper_rect.midbottom[1] >= BODEN_Y and paper_rect.bottomright[0] < korb_rect.bottomleft[0]:  # is_on_the_floor#x_paper<korb_x
                shoot = False
                leertaste = True
                leertaste_two = True
                paper_rect.x = 0
                if paper_rect.colliderect(power_rect):
                    paper_rect.x = paper_rect.x + random.randint(0, 150)

                paper_rect.bottom = BODEN_Y
                game_hard_active = False
                # game over sound effect
                game_over_sound = mixer.Sound('Assets\game_over_1.wav')  # https://mixkit.co/free-sound-effects/game-over/
                game_over_sound.play()
                game_over_sound.set_volume(0.075)

            elif paper_rect.midbottom[1] >= korb_y and paper_rect.bottomleft[0] >= korb_rect.topleft[0] and paper_rect.bottomright[0] <= korb_rect.topright[0] and paper_rect.center[1] < korb_y:  # ball in the basket
                shoot = False
                leertaste = True
                leertaste_two = True
                paper_rect.x = 0
                paper_rect.bottom = BODEN_Y
                score = str(int(score) + 1)
                score_surf = test_font.render('Score: ' + score, False, (255, 0, 0))
                score_rect = score_surf.get_rect(topright=(SCREEN_WIDTH, 0))
                goal_sound = mixer.Sound('Assets\goal.wav')  # https://mixkit.co/free-sound-effects/win/
                goal_sound.play()
                goal_sound.set_volume(0.075)
                if paper_rect.colliderect(power_rect):
                    paper_rect.x = paper_rect.x + random.randint(0, 150)

            else:
                shoot = False
                leertaste = True
                leertaste_two = True
                paper_rect.x = 0
                if paper_rect.colliderect(power_rect):
                    paper_rect.x = paper_rect.x + random.randint(0, 150)
                paper_rect.bottom = BODEN_Y
                game_hard_active = False
                change_level = False
                # game over sound effect
                game_over_sound = mixer.Sound('Assets\game_over_1.wav')  # https://mixkit.co/free-sound-effects/game-over/
                game_over_sound.play()
                game_over_sound.set_volume(0.075)

        elif collide == True:  # is_collision
            angle = math.pi + angle
            # Collision sound effect
            collision_sound = mixer.Sound('Assets\collision.wav')  # https://mixkit.co/free-sound-effects/ball/
            collision_sound.play()
            collision_sound.set_volume(0.1)
            if paper_rect.midright[0] >= SCREEN_WIDTH:
                paper_rect.right = SCREEN_WIDTH - 1
            elif paper_rect.midbottom[1] - 10 <= korb_rect.midtop[1] + 10 and paper_rect.center[0] >= korb_rect.midleft[0]:  # ball over the basket
                paper_rect.bottom = korb_rect.midtop[1]
                angle = math.pi / 4
                power *= 2
            elif paper_rect.midbottom[1]-10<=korb_rect.midtop[1]+10 and paper_rect.center[0]<=korb_rect.midleft[0]:
                paper_rect.bottom = korb_rect.midtop[1]
                angle = math.pi * 3 / 4
                power *= 2
            else:
                paper_rect.right = korb_rect.midleft[0] - 1
                angle = math.pi
                power /= 2

            x = paper_rect.x
            y = paper_rect.y
            collide = False

        # No collision between the paper and the power indicator
        if paper_rect.colliderect(power_rect):
            paper_rect.x = paper_rect.x + random.randint(0, 150)

        # Drawing images while game active
        screen.fill((225, 225, 225))
        screen.blit(backg2_surf, backg2_rect)
        screen.blit(paper_surf, paper_rect)
        screen.blit(korb_surf, korb_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(power_surf, power_rect)

        draw_line()
        draw_pline()

    else:#game over
        score_message = test_font.render(f'Your Score: {score}', False, (0, 0, 0))
        score_message_rect = score_message.get_rect(center=(550, 275))
        score_message = pygame.transform.rotozoom(score_message, 0, 1.25)

        easy_message = test_font.render(f'Easy', False, (250, 250, 250))
        easy_message = pygame.transform.rotozoom(easy_message, 0, 2)
        easy_message_rect = easy_message.get_rect(center=(535, 325))

        medium_message = test_font.render(f'Medium', False, (250, 250, 250))
        medium_message = pygame.transform.rotozoom(medium_message, 0, 2)
        medium_message_rect = medium_message.get_rect(center=(535, 460))

        hard_message = test_font.render(f'Hard', False, (250, 250, 250))
        hard_message = pygame.transform.rotozoom(hard_message, 0, 2)
        hard_message_rect = hard_message.get_rect(center=(535, 600))

        music_surf = pygame.image.load('Assets\Music.png')  #https://www.pikpng.com/pngvi/hwboRb_music-icon-white-clipart/
        music_surf = pygame.transform.scale(music_surf, (25, 25))
        music_rect = music_surf.get_rect(topright=(SCREEN_WIDTH-25, 25))

        highscore_easy_message = test_font.render(f'High Score: '+str(highscore_easy),False, (0,0,0))
        highscore_easy_message = pygame.transform.rotozoom(highscore_easy_message, 0, 1.25)
        highscore_easy_message_rect = highscore_easy_message.get_rect(center=(575, 175))

        highscore_medium_message = test_font.render(f'High Score: ' + str(highscore_medium), False, (0, 0, 0))
        highscore_medium_message = pygame.transform.rotozoom(highscore_medium_message, 0, 1.25)
        highscore_medium_message_rect = highscore_medium_message.get_rect(center=(575, 175))

        highscore_hard_message = test_font.render(f'High Score: ' + str(highscore_hard), False, (0, 0, 0))
        highscore_hard_message = pygame.transform.rotozoom(highscore_hard_message, 0, 1.25)
        highscore_hard_message_rect = highscore_hard_message.get_rect(center=(575, 175))

        if time>0 and change_level == False:
            screen.fill((225,225,225))
            screen.blit(score_message,score_message_rect)
            screen.blit(restart_message, restart_message_rect)
            screen.blit(menu_message, menu_message_rect)
            if level == "e":
                if int(score) > highscore_easy:
                    highscore_easy = int(score)
                    with open(HS_easy_FILE,'w') as e:
                        e.write(score)
                screen.blit(highscore_easy_message,highscore_easy_message_rect)
            elif level == "m":
                if int(score) > highscore_medium:
                    highscore_medium = int(score)
                    with open(HS_medium_FILE,'w') as e:
                        e.write(score)
                screen.blit(highscore_medium_message,highscore_medium_message_rect)
            elif level == "h":
                if int(score)> highscore_hard:
                    highscore_hard = int(score)
                    with open(HS_hard_FILE,'w') as e:
                        e.write(score)
                screen.blit(highscore_hard_message,highscore_hard_message_rect)


        elif change_level:
            if easy_gross:
                easy_message = pygame.transform.rotozoom(easy_message, 0, 1.25)
                easy_message_rect = easy_message.get_rect(center=(535, 325))
            elif medium_gross:
                medium_message = pygame.transform.rotozoom(medium_message, 0, 1.25)
                medium_message_rect = medium_message.get_rect(center=(535, 460))
            elif hard_gross:
                hard_message = pygame.transform.rotozoom(hard_message, 0, 1.25)
                hard_message_rect = hard_message.get_rect(center=(535, 600))
            elif music_gross:
                music_surf = pygame.transform.rotozoom(music_surf, 0, 1.25)
                music_rect = music_surf.get_rect(topright=(SCREEN_WIDTH-25, 25))
            screen.blit(level_surf, level_rect)
            screen.blit(easy_message, easy_message_rect)
            screen.blit(medium_message, medium_message_rect)
            screen.blit(hard_message,hard_message_rect)
            screen.blit(music_surf, music_rect)
            if mixer.music.get_volume() == 0:
                pygame.draw.line(screen, (255, 0, 0), music_rect.bottomleft, music_rect.topright, 3)

        else:
            screen.blit(start_surf, start_rect)
            screen.blit(press_message, press_message_rect)

    pygame.display.update()
    clock.tick(60)
