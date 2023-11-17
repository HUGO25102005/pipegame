import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Background")

# Colors
white = (255, 255, 255)

# Load background images or create surfaces for animation
background_images = [
    pygame.image.load("assets/image-1.png"),
    pygame.image.load("assets/image.png"),
    # Add more images as needed
]

# Set initial background
current_background = 0

# Set up clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update background or animation properties
    # Here, we'll just cycle through the background images
    current_background = (current_background + 1) % len(background_images)

    # Draw background
    screen.fill(white)
    screen.blit(background_images[current_background], (0, 0))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)  # Adjust the value to control the frame rate

# Quit Pygame
pygame.quit()
sys.exit()

