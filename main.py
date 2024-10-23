import pygame
import random

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
WALKER_COLOR = (0, 0, 0)
TARGET_FPS = 200  # Set the desired FPS

# Classes
class Walker:
    def __init__(self, width, height, color):
        self.x = width / 2
        self.y = height / 2
        self.color = color

    def move(self):
        # Generate step sizes from a normal distribution with mean 0 and standard deviation 1
        step_x = random.gauss(0, 1)
        step_y = random.gauss(0, 1)
        
        # Update position
        self.x += step_x
        self.y += step_y
        
        # Keep the walker within window boundaries
        self.x = max(0, min(self.x, WINDOW_WIDTH))
        self.y = max(0, min(self.y, WINDOW_HEIGHT))

    def display(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), 1)

# Functions
def setup(window_width, window_height, background_color):
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    window.fill(background_color)
    pygame.display.set_caption("Walker Simulation")
    return window

def main():
    window = setup(WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR)
    walker = Walker(WINDOW_WIDTH, WINDOW_HEIGHT, WALKER_COLOR)
    clock = pygame.time.Clock()  # Create a clock object to control FPS
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        walker.move()
        walker.display(window)

        pygame.display.flip()
        clock.tick(TARGET_FPS)  # Limit the frame rate to TARGET_FPS

    pygame.quit()

if __name__ == "__main__":
    main()
