import pygame
import math
import numdifftools as nd
import numpy as np
from random import randint


# Define the dimensions of the screen
screen_width = 800
screen_height = 600

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define the parameters of the arm
base_x = 400
base_y = 300
arm_length = 150
arm_length2 = 100
arm_length3 = 50

joint_radius = 10
joint_color = red
arm_color = blue

# Define the angles of the joints
theta1 = math.pi/2
theta2 = math.pi/4
theta3 = math.pi/4

dot=[400,300]

# Define the update function
def update():
    #base
    pygame.draw.line(screen, arm_color, (base_x-50, base_y), (base_x+50, base_y), 15)
    
    #adjut the position of the first jointure in fonction of the first angle
    arm_x = base_x + arm_length * math.cos(theta1)
    arm_y = base_y - arm_length * math.sin(theta1)
    
    pygame.draw.line(screen, arm_color, (base_x, base_y), (arm_x, arm_y), 5)
    
    
    arm2_x = arm_x + arm_length2 * math.cos(theta1 + theta2)
    arm2_y = arm_y - arm_length2 * math.sin(theta1 + theta2)
    
    pygame.draw.line(screen, arm_color, (arm_x, arm_y), (arm2_x, arm2_y), 5)
    

    arm3_x = arm2_x + arm_length3 * math.cos(theta1 + theta2 + theta3)
    arm3_y = arm2_y - arm_length3 * math.sin(theta1 + theta2 + theta3)

    pygame.draw.line(screen, arm_color, (arm2_x, arm2_y), (arm3_x, arm3_y), 5)

    pygame.draw.circle(screen, joint_color, (int(base_x), int(base_y)), joint_radius)
    pygame.draw.circle(screen, joint_color, (int(arm_x), int(arm_y)), joint_radius)
    pygame.draw.circle(screen, joint_color, (int(arm2_x), int(arm2_y)), joint_radius)
    pygame.draw.circle(screen, joint_color, (int(arm3_x), int(arm3_y)), joint_radius, 3)
    pygame.draw.circle(screen, white, (int(arm3_x), int(arm3_y)), joint_radius - 3)

    if dot!=None:
        pygame.draw.circle(screen, red, dot, 5)
    return arm3_x,arm3_y


def distance(x):
    theta1 = x[0]
    theta2 = x[1]
    theta3 = x[2]
    return math.sqrt(((base_x + arm_length * math.cos(theta1) + arm_length2 * math.cos(theta1 + theta2) + arm_length3 * math.cos(theta1 + theta2 + theta3))-dot[0])**2+((base_y - arm_length * math.sin(theta1) - arm_length2 * math.sin(theta1 + theta2) - arm_length3 * math.sin(theta1 + theta2 + theta3))-dot[1])**2)

# Define the Armijo rule
def armijo_rule(f, grad_f, x, alpha, c=0.5):
    while f(x - alpha * grad_f(x)) > f(x) - c * alpha * np.linalg.norm(grad_f(x))**2:
        alpha *= 0.5
    return alpha

# Define the main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN or dot!=None:
            # Get the mouse position when the button is clicked
            #mouse_pos = pygame.mouse.get_pos()
            #dot = mouse_pos
            dot=[randint(100,700),randint(100,500)]
            print(distance([theta1,theta2,theta3]))
            n=0
            
            x = [theta1,theta2,theta3]
            while distance(x)>2.5 and n<600:
                #Armijo rule
                """
                grad = nd.Gradient(distance)(x)
                alpha = armijo_rule(distance, nd.Gradient(distance), x, 1)
                x = x - alpha * grad
                """
                #Fixed step size
                x = x - 0.0001 * nd.Gradient(distance)(x)
                print(distance(x))
                screen.fill(white)
                theta1 = x[0]
                theta2 = x[1]
                theta3 = x[2]
                update()
                pygame.display.flip()
                n+=1
                    
    
    # Clear the screen
    screen.fill(white)
    
    # Update the arm

    
    update()
    
    # Flip the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
