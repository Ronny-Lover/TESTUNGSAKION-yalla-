import pygame
import random
pygame.init()

def draw_square(column, row, color):
    screen_x = column * SQUARE_SIZE
    screen_y = row * SQUARE_SIZE
    pygame.draw.rect(screen, color, (screen_x, screen_y,SQUARE_SIZE,SQUARE_SIZE))

WIN_SIZE = 1000  #konstante
SQUARE_COUNT = 20
SQUARE_SIZE = WIN_SIZE / SQUARE_COUNT
START_LENGTH = 3


screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption("Snake")

#variabeln
head_column = 5 
head_row = 5
snake_length = START_LENGTH
body_parts = []

step_x = 0
step_y = 0
#Äpfel
apple_column = random.randint(0,SQUARE_COUNT -4)
apple_row = random.randint(0,SQUARE_COUNT -4)

apple_column2 = random.randint(0,SQUARE_COUNT -4)
apple_row2 = random.randint(0,SQUARE_COUNT -4)

apple_column3 = random.randint(0,SQUARE_COUNT -4)
apple_row3 = random.randint(0,SQUARE_COUNT -4)

#Bomben
bomb_column = random.randint(0,SQUARE_COUNT -4)
bomb_row = random.randint(0,SQUARE_COUNT -4)
bomb_column2 = random.randint(0,SQUARE_COUNT -4)
bomb_row2 = random.randint(0,SQUARE_COUNT -4)
bomb_column3 = random.randint(0,SQUARE_COUNT -4)
bomb_row3 = random.randint(0,SQUARE_COUNT -4)


                  #Hauptschleife

run = True
while run:
    pygame.time.delay(120)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        if step_x !=-1:
            step_x, step_y = 1, 0
        
    elif keys[pygame.K_LEFT]:
       if step_x != 1:
           step_x, step_y = -1, 0
        
    elif keys[pygame.K_UP]:
        if step_y !=1:
            step_x, step_y = 0, -1
    elif keys[pygame.K_DOWN]:
        if step_y != -1:
            step_x, step_y = 0, 1
            
            
    if step_x != 0 or step_y != 0:
        body_parts.append((head_column, head_row))
        if len(body_parts) >= snake_length:
            body_parts.pop(0)
            
            #schlange bewegen
    head_column += step_x
    head_row += step_y
    
    #Äpfel essen
    if head_column == apple_column and head_row == apple_row:
        snake_length += 1
        apple_column = random.randint(0,SQUARE_COUNT -4)
        apple_row = random.randint(0,SQUARE_COUNT -4)
        bomb_column3 = random.randint(0,SQUARE_COUNT -4)
        bomb_row3 = random.randint(0,SQUARE_COUNT -4)
    
    if head_column == apple_column2 and head_row == apple_row2:
        snake_length += 1
        apple_column2 = random.randint(0,SQUARE_COUNT -4)
        apple_row2 = random.randint(0,SQUARE_COUNT -4)
        
        bomb_column2 = random.randint(0,SQUARE_COUNT -4)
        bomb_row2 = random.randint(0,SQUARE_COUNT -4)
        
    if head_column == apple_column3 and head_row == apple_row3:
        snake_length += 1
        apple_column3 = random.randint(0,SQUARE_COUNT -4)
        apple_row3 = random.randint(0,SQUARE_COUNT -4)
        
        bomb_column = random.randint(0,SQUARE_COUNT -4)
        bomb_row = random.randint(0,SQUARE_COUNT -4)
    #Bomben kollision
    if head_column == bomb_column and head_row == bomb_row:
        head_column = SQUARE_COUNT // 2
        head_row = SQUARE_COUNT // 2
        snake_length = START_LENGTH
        body_parts = []
        step_x = 0
        step_y = 0
        
    if head_column == bomb_column2 and head_row == bomb_row2:
        head_column = SQUARE_COUNT // 2
        head_row = SQUARE_COUNT // 2
        snake_length = START_LENGTH
        body_parts = []
        step_x = 0
        step_y = 0
        
    if head_column == bomb_column3 and head_row == bomb_row3:
        head_column = SQUARE_COUNT // 2
        head_row = SQUARE_COUNT // 2
        snake_length = START_LENGTH
        body_parts = []
        step_x = 0
        step_y = 0
    
    
        

        
    #nicht an den rand stoßen
    vertical_border_hit = head_column < 0 or head_column >= SQUARE_COUNT
    horizontal_border_hit = head_row < 0 or head_row >= SQUARE_COUNT
    
    
        
    
    #spiel neustarten
    if vertical_border_hit or horizontal_border_hit :
        head_column = SQUARE_COUNT // 2
        head_row = SQUARE_COUNT // 2
        snake_length = START_LENGTH
        body_parts = []
        step_x = 0
        step_y = 0

        
    screen.fill((250, 175, 0)) # R G B ---> max = 255
    
    #Schlangenkopf
    head_x = head_column * SQUARE_SIZE
    head_y = head_row * SQUARE_SIZE
    draw_square(head_column, head_row, ( 230,0,250))    
    
    #Schlangekörper
    for part in body_parts:
        part_column = part[0]
        part_row = part[1]
        part_x = part_column * SQUARE_SIZE
        part_y = part_row * SQUARE_SIZE
        draw_square(part_column, part_row, ( 100,0,200))
        #selbstkollsion
        if part_row == head_row and part_column == head_column:
            head_column = SQUARE_COUNT // 2
            head_row = SQUARE_COUNT // 2
            snake_length = START_LENGTH
            body_parts = []
            step_x = 0
            step_y = 0
        
    
        
        
    #Äpfel
    draw_square(apple_column, apple_row, (255,0,0))
    draw_square(apple_column2, apple_row2, (255,0,0))
    draw_square(apple_column3, apple_row3, (255,0,0))
    
    #Bomben
    draw_square(bomb_column, bomb_row, (0,0,0))
    draw_square(bomb_column2, bomb_row2, (0,0,0))
    draw_square(bomb_column3, bomb_row3, (0,0,0))
    
    
        
    
    
    
    #Gitter
    for i in range(SQUARE_COUNT):
        line_pos = SQUARE_SIZE * i
        pygame.draw.line(screen, (255,255,255), (line_pos, 0), (line_pos, WIN_SIZE), 2)
        pygame.draw.line(screen, (255,255,255), (0, line_pos), (WIN_SIZE, line_pos), 2)

    
    
    
    pygame.display.update()
    
    



pygame.display.quit()