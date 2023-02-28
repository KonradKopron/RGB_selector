import sys
import pygame


# init and set up screen
pygame.init()
background_color = [125,125,125]
width, height = 1200,800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Python RGB Pygame')
screen.fill(background_color)
screen_rect = screen.get_rect()
screen_center = screen_rect.center

# creating boxes

class Box:
    def __init__(self, x=10,y=10,a=10,b=10, color=[255,255,255]):
        self.rect = pygame.Rect(x,y,a,b)
        self.color = color
        
    def display(self):
        pygame.draw.rect(screen,self.color,self.rect)
    

# one instance of the Box:  

# my_box = Box()

# creating multiple instances:

my_boxes = []
my_buttons = []

for i in range(3):
    my_boxes.append(Box(x=i*300+300,b=510,color=[100,100,100]))
    my_buttons.append(Box(x=i*300+300,y=i*(-50)+500, a=50,b=20,color=[255,255,255]))
    
for box, button in zip(my_boxes,my_buttons):
    box.rect.centery = button.rect.centery = screen_rect.centery
    button.rect.centerx = box.rect.centerx
    box.display()
    button.display()
    
    
#creating buttons:

box_rect = pygame.Rect(10,10,585,300)

running = True
#mouse_on = False
button_zero = False
button_one = False
button_two = False

while running:
    
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in my_buttons:
                if my_buttons[0].rect.collidepoint(mouse_pos):
                    button_zero = True
                elif my_buttons[1].rect.collidepoint(mouse_pos):
                    button_one = True
                elif my_buttons[2].rect.collidepoint(mouse_pos):
                    button_two = True
            
        elif event.type == pygame.MOUSEBUTTONUP:
            button_zero = button_one = button_two = False
            print('r: ',(background_color[0]))
            print('g: ',(background_color[1]))
            print('b: ',(background_color[2]))
            print('\n')

    # drawing area
    
    screen.fill(background_color)

    for box, button in zip(my_boxes,my_buttons):
        box.rect.centery = screen_rect.centery
        button.rect.centerx = box.rect.centerx
        if button_zero:
                if button == my_buttons[0] and int((-mouse_pos[1]+655)/2) <=255 and int((-mouse_pos[1]+655)/2) >= 0:
                    background_color[0] = int((-mouse_pos[1]+655)/2)
                    my_buttons[0].rect.centery = mouse_pos[1]
        elif button_one:   
                if button == my_buttons[1] and int((-mouse_pos[1]+655)/2) <=255 and int((-mouse_pos[1]+655)/2) >= 0:
                    background_color[1] = int((-mouse_pos[1]+655)/2)
                    my_buttons[1].rect.centery = mouse_pos[1]
        elif button_two: 
                if button == my_buttons[2] and int((-mouse_pos[1]+655)/2) <=255 and int((-mouse_pos[1]+655)/2) >= 0:
                    background_color[2] = int((-mouse_pos[1]+655)/2)
                    my_buttons[2].rect.centery = mouse_pos[1]
 
        box.display()
        button.display()


    pygame.display.flip()

    # end of drawing area
    

pygame.quit()
