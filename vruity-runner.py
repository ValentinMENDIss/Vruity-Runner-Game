### VRUITY-RUNNER-GAME
### MADE BY VALENTIN VIRSTIUC AS A SCHOOL PROJECT. HAVE FUN :)
### LAST EDIT: Tue, 11 Jun 2024; 09:49:10 PM
##
#

######## QUESTIONS THAT MIGHT COME UP BY READING THE CODE:
'''

Why Have you used .convert()?:
    Well, you might not need it, but I had a problem with performance of the game(code) at the end. So .convert() is just sort of compiling your textures. (++improved Performance (usually :>) )






DO NOT FORGET!!!!:
    .convert() can make some new problem appear. Example: By converting Jump picture it won't run. CONSIDER THIS!!!!


'''
########


import pygame
import os
import random


pygame.font.init()
pygame.init # Initializing pygame engine

# SCREEN SETTINGS

SCREEN_WIDTH = 1100     # Width of the screen
SCREEN_HEIGHT = 550     # Height of the screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create screen with screen width(SCREEN_WIDTH= 1100px) and screen height(SCREEN_HEIGHT = 550px)

# SPRITES (WITH ACTIONS (ex.: running, jumping, ...))

RUNNING = [pygame.image.load(os.path.join("graphics", "dino_run1.png")),
           pygame.image.load(os.path.join("graphics", "dino_run2.png"))]    # Sprite of Dinosaur (in action: running)

JUMPING = pygame.image.load(os.path.join("graphics", "dino_jump.png"))   # Sprite of Dinosaur (in action: jumping)



# OTHER SPRITES (FOR CLASSES):

CLOUD = pygame.image.load(os.path.join("graphics", "Cloud.png")).convert_alpha()    

BACKGROUND = pygame.image.load(os.path.join("graphics", "Background.png")).convert_alpha()

CACTUS = pygame.image.load(os.path.join("graphics", "Cactus.png")).convert_alpha()

## CLASSES ##

class Dinosaur:
    # Coordinates of player(dino)
    X_POS = 80                      # X-Coordinates of dinosaur (by initialization)         
    Y_POS = 310                     # Y-Coordinates of dinosaur (by initialization)
    JUMP_VEL = 8.5
               
    def __init__(self):                                 # Initialize the dinosaur whenever an object of this class is created
        #self.duck_img = DUCKING
        self.run_img = RUNNING                          # giving action (sprite of action) to variable self.run_img
        self.jump_img = JUMPING
        
        #self.dino_duck = False
        self.dino_run = True                            # by default make dino run (as an action)
        self.dino_jump = False  
        
        self.step_index = 0                             # Start of sprite/action (starts at first image of running action)
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()          # Convert image to rectangle (needed for collision (in the future...))
        self.dino_rect.x = self.X_POS   
        self.dino_rect.y = self.Y_POS
        
    def update(self, userInput):                        # Function (def) updating / Refreshing ( For each Frame )
        #if self.dino_duck:
            #self.duck()
        if self.dino_run:                               # If dino run set to True: than        
            self.run()                                  # run (def run() )
        if self.dino_jump:                              # If dino jump set to True: than
            self.jump()                                 # run (def jump() )
        
        
        if self.step_index >= 10:                       # helps to animate in the future
            self.step_index = 0
            
        
        if userInput [pygame.K_UP] and not self.dino_jump:      # if Key Up is pressed and/but dino_jump isn't set to True: than
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True                               # Set dino_jump to True
        
        elif userInput [pygame.K_DOWN] and not self.dino_jump:  # if Key Down is pressed and/but dino jump isn't set to True: than
            self.dino_duck = True                               # Make Dino Duck (TEST: MAY NOT BE IN THIS VERSION YET!!!... )
            self.dino_run = False
            self.dino_jump = False                          
        
        
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):  # if Key Down isn't pressed or dino_jump isn't set to True: than 
            self.dino_duck = False
            self.dino_run = True                                # Make dino run (default animation)
            self.dino_jump = False    
            
            
    def duck(self):                                             # Ducking (TEST: MAY NOT BE IN THIS VERSION!!!... )
        pass
    
    def run(self):                                              # Def for Running
        self.image = self.run_img[self.step_index // 5]         # Image of dino is set to (pictures from list) and being changed to make an animation
        self.dino_rect = self.image.get_rect()                  # Get Rectangle, AKA. Collision from dino (used for Collision, and other things.)
        self.dino_rect.x = self.X_POS                           # Dino's position of rectangle (made by previous line) on X-Coordinates is set to his position on X-Coordinates  
        self.dino_rect.y = self.Y_POS                           # Dino's position of rectangle (made by previous line) on Y-Coordinates is set to his position on Y-Coordinates
        self.step_index += 1                                    # 'self.step_index' (is needed for animation to change sprites...)
        
    def jump(self):                                             # Def for jumping
        self.image = self.jump_img                              # Image for dino in action (jumping) is set to images of list[] called 'JUMPING'
        if self.dino_jump:                                      # if dino is jumping (AKA. if dino_jump is set to True: than... )
            self.dino_rect.y -= self.jump_vel * 4               # Setting height of the jump
            self.jump_vel -= 0.6                                # Setting Speed/Velocity of the jump
        if self.jump_vel < - self.JUMP_VEL:                     # if Dino is on the ground: than...
            self.dino_jump = False                              # Set jump to False
            self.jump_vel = self.JUMP_VEL                       # Reset Jump_Velocity
            
    def draw(self, SCREEN):                                     # draw function (def)
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))   # Draw image of dino on the screen (coordinates are: coordinates of dino's rectangle )

class Cloud:                                                # New Class (for cloud)
    def __init__(self):                                     # When the code is being initialized, than...
        self.x = SCREEN_WIDTH + random.randint(875, 1200)   # X-Coordinates for drawing cactus, which would be given when code is being initialized (Width of the screen + random number in range of 875 and 1200)
        self.y = random.randint(20, 50)                     # Y-Coodinates for drawing cactus (by init.)  ( random numbers in range of 20 and 50 )
        self.image = CLOUD                                  # Image of cloud is set to image ( with variable: ) Cloud
        self.width = self.image.get_width()                 # Get the Width of the Image 
        
    def update(self):                                           # Function (def) updating / Refreshing ( For each Frame )
        self.x -= game_speed                                    # Cloud is being moved on X-Coordinates by the speed of the variable ( game_speed )                               
        if self.x < -self.width:                                # if Cloud is off of the screen
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)  # if image is out of view, than place it at the start
            self.y = random.randint(20,50)                      # Y-Coordinates of the cloud are set to random numbers in range of 20 and 50 ( for small difference by each cloud )
    def draw(self, SCREEN):                                     # Function for Drawing a cloud
        SCREEN.blit(self.image, (self.x, self.y))               # Draw an image on his coordinates which are variables (self.x / self.y)    ( variable self. image is giving an image for cloud )
    
class Cactus:                                               # Creating new Class called 'Cactus'
    
    def __init__(self):                                     # Function (def) init. ( by initializing  do this: )
        self.x = SCREEN_WIDTH + random.randint(650, 1100)   # X-Coordinates for drawing cactus, which stars when code is being initialized
        self.y = 310                                        # Y-Coordinates of Cactus
        self.image = CACTUS                                 # Giving an Image for class (Cactus)    
        self.width = self.image.get_width()                 # Get the Width of the Image ( Needed to know when Cactus is off of the screen and move it to the start )
        self.cactus_rect = self.image.get_rect()            # Create rectangle ( Needed for Collision ) for Cactus
           
    def update(self):                                                       # Function (def) updating / Refreshing ( For each Frame )
        self.cactus_rect.x -= game_speed                                    # Cactus is being moved on X-Coordinates by the speed of the variable ( game_speed )
        if self.cactus_rect.x < -self.width:                                # if cactus is off of the screen than: ... 
            self.cactus_rect.x = SCREEN_WIDTH + random.randint(50, 1250)    # place the Image at the start ( Right Side of the Screen )
            self.cactus_rect.y = 310                                        # image should be placed at ... Y-Coordinates 
    def draw(self, SCREEN):                                                 # Function (def) to draw a Cactus
        SCREEN.blit(self.image, (self.cactus_rect.x, self.cactus_rect.y))   # Draw an image on his coordinates
        
        


        
def main():                                                                 # Main loop (Game/Loop)
    # GLOBAL VARIABLES:
    
    global coins, game_speed, x_pos_background, y_pos_background            # Take variables ( global )
    
    # VARIABLES:
    
    run = True                                                              # set run to True ( needed for while loop )
    clock = pygame.time.Clock()                                             # Make a Clock / Timer ( needed to set up ingame fps )
    coins = 0                                                               # Variable for ingame Coins / Points / Score ( set to 0 )
    font = pygame.font.Font('font/Pixeltype.ttf', 50)                       # Make a new variable for Font ( used for Text )
    game_speed = 14                                                         # Variable for Game Speed ( Default: 14 )
    death_count = 0                                                         # Variable to Count Deaths ( Needed to show right menu ( Example: Start Menu; Retry Menu ) )

    
    # ACTORS/OBJECTS:
    
    player = Dinosaur()                                                     # Create New Variable ( to set up a Player, AKA. Dinosaur ) which is class of Dinosaur
    cloud = Cloud()                                                         # Create New Variable ( to set up a cloud ) which is class of Cloud 
    cactus = Cactus()                                                       # Create New Variable ( to set up a Cactus ) which is class of Cactus
    
    
    # CODE (MAIN LOOP):
    
    def score():                                                                                        # Function (def) for score ( Getting Points / Score for the run )
        global coins, game_speed                                                                        # Take Global Varibles ... ( which are located at main loop )
        coins += 1                                                                                      # Add 1 Coin when each Frame bypasses

        text_surface = font.render('Coins: ' + str(coins), False, (0, 0, 0)).convert_alpha()            # Render a Text for Coins / Score
        text_rect = text_surface.get_rect()                                                             # Create a Rectangle for Text ( to be able to place text precisely )
        text_rect.center = (1000, 40)                                                                   # Place Rectangle ( Text ) in the center of the screen
        SCREEN.blit(text_surface, text_rect)                                                            # Draw a Text on ( Text Rectangle ) coordinates
        if coins % 100 == 0:                                                          # if Coins % by 100 is divideable, than: ...  ;  (example: 25 / 5 = 5.0 = TRUE;   22 / 5 = 4.4 = FALSE) 
            game_speed += 1                                                           # make game_speed faster
    
    
    while run:  # While Loop for game
        for event in pygame.event.get():                                                # For every Event in Pygame: 
            if event.type == pygame.QUIT:                                               # If event QUIT was used(if button quit was pressed):
                run = False                                                             # Quit Loop 
    
    
        SCREEN.fill((255, 255, 255))                        # Fill SCREEN with white color, also refreshes it
        
        userInput = pygame.key.get_pressed()                # Gets user Inputs ( such as Keyboard Inputs/events)
        
        SCREEN.blit(BACKGROUND, (0, 0))
           
        # DRAW OBJECTS:
            
        player.draw(SCREEN)                                 # Drawing a Dinosaur/Player on the Screen
        player.update(userInput)                            # Updating Motion of the Dinosaur/Player by the Input of the Player himself

        cloud.draw(SCREEN)                                  # Drawing a Cloud on the Screen
        cloud.update()                                      # Refreshing Frames / Updating Motion of the Cloud

        cactus.draw(SCREEN)                                 # Drawing a Cactus on the Screen
        cactus.update()                                     # Refreshing Frames / Updating Motion of the Cloud
        #####################       

        
        score()                                             # Run Score Function (def)


        # COLIDING
        
        if player.dino_rect.colliderect(cactus.cactus_rect):       # IF PLAYER COLIDES WITH CACTUS THAN:
            death_count += 1                                       # 1 is added to the Death Count
            menu(death_count)                                      # Open Menu() with number of deaths, is needed to say if the menu started on the game bootup or is it because of collision with an object
                                                                   # Which would start ( Main Menu ) or ( Retry Menu )       

        
        
        
        clock.tick(60)                      # Setting FPS to 60
        pygame.display.update()             # Updating the Screen / Refreshing the screen
        
        
def menu(death_count):                      # Function (def) Menu
    global coins                            # Take a Global Variable Coins which is located in the Main Loop
    run = True                              # Set Variable Run to True ( needed for while Loop )
    while run:                              # While Run is set to True: ...
        
        SCREEN.fill((255, 255, 255))                                                                                                    # Draw a White coloured Screen
        smallText = pygame.font.Font('font/Pixeltype.ttf', 20)                                                                          # Set Font and Size for the Small Text
        text = pygame.font.Font('font/Pixeltype.ttf', 50)                                                                               # Set Font and Size for the Normal Text
        heading = pygame.font.Font('font/Pixeltype.ttf', 100)                                                                           # Set Font and Size for the ( Heading ) Text


        if death_count == 0:                                                                                                            # If Death Count is 0 ( If you loaded Menu by the bootup of the game run Main Menu ): than ...
        
            # SMALL TEXT
        
            smallText = smallText.render("Made by Valentin.V as a school project, Have fun :)", True, (0, 0, 0)).convert_alpha()        # Render a Small Text 
            smallTextRect = smallText.get_rect()                                                                                        # Get a Rectangle of the small Text ( needed, to be able to place the Text precisely )
            smallTextRect.center = (SCREEN_WIDTH // 2, + 500)                                                                           # Place a Text in the Center of the screen ( X-Coordinates ) and Bottom of the screen ( Y-Coordinates ) 
            SCREEN.blit(smallText, smallTextRect)                                                                                       # Draw a Text on the Screen 
        
            # TEXT
        
            text = text.render("Press any Key to Start", True, (0, 0, 0)).convert_alpha()                                               # Render a Normal Text
            textRect = text.get_rect()                                                                                                  # Get a Rectangle of the Normal Text ( needed, to be able to place the Text precisely )
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)                                                              # Place Rectangle of Text in The middle of Display on X-Coordinates / Y-Coordinates and 100 from middle of y-coordinates
            SCREEN.blit(text, textRect)                                                                                                 # Blit the text on textRect (Center of the screen) Coordinates

            # HEADING TEXT

            headingText = heading.render("Vruity Runner Game", True, (0, 0, 0)).convert_alpha()                                         # Render a Normal Text
            headingTextRect = headingText.get_rect()                                                                                    # Get a Rectangle of the Normal Text ( needed, to be able to place the Text precisely )
            headingTextRect.center = (SCREEN_WIDTH // 2, 100)                                                                           # Place Rectangle of Heading Text in The middle of Display on X-Coordinates and 100 pixel from top (Y-Coordinates)
            SCREEN.blit(headingText, headingTextRect)                                                                                   # Blit the text on textRect (Center of the screen) Coordinates

        elif death_count >= 0:                                                                                                          # If your Death Count is bigger than 0 ( If you have opened menu not by the bootup of the game, but by dying ): Open ( Retry Menu )
            
            # HEADING TEXT
            
            headingText = heading.render("RETRY", True, (0, 0, 0)).convert_alpha()
            headingTextRect = headingText.get_rect()
            headingTextRect.center = (SCREEN_WIDTH // 2, 100)
            SCREEN.blit(headingText, headingTextRect)
            
            # TEXT
        
            text = text.render("Press any Key to Start", True, (0, 0, 0)).convert_alpha()
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)     # Place Rectangle of Text in The middle of Display on X-Coordinates / Y-Coordinates and 100 from middle of y-coordinates
            SCREEN.blit(text, textRect)     # Blit the text on textRect (Center of the screen) Coordinates            
           


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()

        

menu(death_count=0)   






#main()                         # Calling Main loop
