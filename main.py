import pygame
import sys

# Αρχικοποίηση του  - starting Pygame
pygame.init()

# Ρυθμίσεις παραθύρου - window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Pygame Example")

# Χρώματα - colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ρυθμίσεις κύκλου - cicle settings
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
circle_radius = 30
circle_speed = 5

# Ρυθμίσεις του clock για να ελέγξουμε το FPS - fps settings for clock 
clock = pygame.time.Clock()

# Βρόχος κύριου παιχνιδιού - main body
while True:
    # Διαχείριση γεγονότων
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ελέγχουμε ποιο πλήκτρο έχει πατηθεί - check which button clicked 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed

    # Γέμισμα της οθόνης με λευκό - white blank page
    screen.fill(WHITE)

    # Σχεδίαση του κύκλου -draw circle 
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    # Ενημέρωση της οθόνης - screen update 
    pygame.display.flip()

    # Οριοθέτηση του FPS - fps limmit
    clock.tick(30)
