import pygame
import math


# (((x0,y0), (x1, y1)), ((x2, y2), (x3, y3)))
def draw_dragon(initial_lines_coordinates: tuple, line_color: tuple, generations: int, screen):
    lines = [initial_lines_coordinates]
    for i in range(generations):
        lines = get_next_generation(lines)
    for line in lines:
        pygame.draw.line(screen, line_color, line[1], line[0])
    pygame.display.flip()


def get_next_generation(lines):
    next_gen = []
    clockwise = True
    for line in lines:
        new_lines = get_new_lines(line, clockwise)
        for new_line in new_lines:
            next_gen.append(new_line)
        clockwise = not clockwise
    return next_gen


def get_new_lines(line, clockwise):
    beginning = line[0]
    end = line[1]
    angle = get_angle(beginning, end)
    size = math.sqrt(((beginning[0] - end[0])**2) + ((beginning[1] - end[1])**2))
    point = calculate_point_for_new_lines(beginning, angle, size, clockwise)
    return (beginning, point), (point, end)


def get_angle(beginning, end):
    opposite = beginning[1] - end[1]        # lower on canvas == higher values
    adjacent = end[0] - beginning[0]
    angle = math.degrees(math.atan2(opposite, adjacent))
    if angle < 0:
        angle += 360
    return angle


def calculate_point_for_new_lines(beginning, angle, size, clockwise):
    new_size = size/math.sqrt(2)
    k = 0
    if clockwise:
        k = -1
    else:
        k = 1
    new_angle = angle + k*45
    x = math.cos(math.radians(new_angle)) * new_size
    y = math.sin(math.radians(new_angle)) * new_size
    # adjust from coordinates to canvas
    x += beginning[0]
    y = beginning[1] - y     # lower on canvas == higher values

    return x, y


width = 500
height = 500
color_screen = (255, 255, 255)
color_line = (0, 0, 0)
# draw canvas
screen = pygame.display.set_mode([width, height])
screen.fill(color_screen)
pygame.display.flip()

draw_dragon(((250, 400), (250, 100)), color_line, 20, screen)
# doesn't let it close automatically, must be at the end
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
