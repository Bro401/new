import pygame
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((601, 343))
pygame.display.set_caption('My first Game')
icon = pygame.image.load('image/8747474.png')
pygame.display.set_icon(icon)
#square = pygame.Surface((50, 170))
#square.fill('Blue')
#myfont = pygame.font.Font('font/NotoSerifAhom-Regular.ttf', 40)
#text_surface = myfont.render('Among Us', True, 'Yellow')
bg = pygame.image.load('image/SeekPng.com_grass-cartoon-png_1225665.png')

walk_left = [
    pygame.image.load('image/0.png'),
    pygame.image.load('image/00.png'),
    pygame.image.load('image/000.png'),
    pygame.image.load('image/0.png')
]
walk_right = [
    pygame.image.load('image/13 (1).png'),
    pygame.image.load('image/144.png'),
    pygame.image.load('image/145.png'),
    pygame.image.load('image/13 (1).png')
]

ghost = pygame.image.load('image/девочка1.png')
#ghost_x = 603
ghost_list_in_game = []

player_anim_count = 0
bg_x = 0
player_speed = 5
player_x = 150
player_y = 250
is_jump = False
jump_count = 8

bg_sound = pygame.mixer.Sound('image/Sembari - Among us (radio.lol) (1).mp3')
bg_sound.play( )

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 5000)

label = pygame.font.Font('font/ofont.ru_Skellyman.ttf', 40)
lose_label = label.render('Вы проиграли!', False, (193, 196, 199))
restart_label = label.render('Играть заново', False, (0, 100, 0))
restart_label_rect = restart_label.get_rect(topleft=(180, 200))
gameplay = True
bullet = pygame.image.load('image/lovs.png').convert_alpha()
bullets = []
running = True
while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 601, 0))
    #screen.blit(ghost, (ghost_x, 250))
    if gameplay:


        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        #ghost_rect = ghost.get_rect(topleft=(ghost_x, 250))
        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -=10
                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    #print('Вы проиграли!')
                    gameplay = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 200:
            player_x += player_speed
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 8


        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1
        bg_x -=2
        if bg_x == -618:
            bg_x = 0


        if keys[pygame.K_b]:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4
                if el.x > 630:
                    bullets.pop(i)
                if ghost_list_in_game:
                    for (index, ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)
    else:

        screen.fill((123, 150, 53))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()
            bullets.clear()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(603, 250)))
        #elif event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_a:
                #screen.fill((252, 186, 3))
    clock.tick(7)