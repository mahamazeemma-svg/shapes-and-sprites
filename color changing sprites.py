import pygame

def main():
    pygame.init()
    screenwidth, screenheight = 400, 400
    screen = pygame.display.set_mode((screenwidth, screenheight))
    pygame.display.set_caption("Color Changing Sprites")

    colours = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "white": (255, 255, 255),}

    current_colour =  colours["white"]
    x,y = 30,30
    sprite_width, sprite_height = 60, 60
    clock = pygame.time.Clock()

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            x -= 3
        if pressed_keys[pygame.K_RIGHT]:
            x += 3
        if pressed_keys[pygame.K_UP]:
            y -= 3
        if pressed_keys[pygame.K_DOWN]:
            y += 3

        x = min(max(x, 0), screenwidth - sprite_width)
        y = min(max(y, 0), screenheight - sprite_height)

        if x== 0:
            current_colour = colours["blue"]
        elif x == screenwidth - sprite_width:
            current_colour = colours["yellow"]
        elif y == 0:
            current_colour = colours["red"]
        elif y == screenheight - sprite_height:
            current_colour = colours["green"]
        else:
            current_colour = colours["white"]
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_colour, pygame.Rect(x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__ == "__main__":
    main()