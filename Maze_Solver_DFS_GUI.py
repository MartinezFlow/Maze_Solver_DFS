from numpy import *
import numpy as np

import pygame, sys
import os


pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 700

INDIGO = (75, 0, 130)
YELLOW = (238,232,170)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FUCHSIA = (255, 0, 255)
LIGHTER_FUCHSIA = (249, 132, 239)
SILVER = (192, 192, 192)

FONT_MAIN = pygame.font.SysFont('gabriola', 75)
FONT_GAMEPLAY = pygame.font.SysFont('couriernew', 17)

FPS = 60
VELOCITY = 80

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill(INDIGO)
pygame.display.flip()
pygame.display.set_caption("Shinso's Mazes")

SHINSO_IMAGE = pygame.image.load(os.path.join('Maze_Solver', 'Shinso.png'))
SHINSO = pygame.transform.scale(SHINSO_IMAGE, (250, 250))
SHINSO_MAZE = pygame.transform.scale(SHINSO_IMAGE, (70, 70))

BORDER_LEFT = 20
BORDER_TOP = 140
BORDER_RIGHT = 0
BORDER_BOTTOM = 0

WALLS = []
START = []
END = []
OPEN_SPACES = []

def mazeSolver(maze):
    path_found = button(BLACK, FUCHSIA, BORDER_RIGHT / 2, BORDER_BOTTOM / 2, 300, 50, FONT_GAMEPLAY, text="Path found! ^_^")
    current_pos = START[0]

    solutionFound = False
    width, height = 80, 80

    path_found_screen = True

    for path in WALLS:
        pygame.draw.rect(WINDOW, BLACK, (path[0], path[1], width, height), 0)
    for path in OPEN_SPACES:
        pygame.draw.rect(WINDOW, WHITE, (path[0], path[1], width, height), 0)
    for path in START:
        pygame.draw.rect(WINDOW, FUCHSIA, (path[0], path[1], width, height), 0)
    for path in END:
        pygame.draw.rect(WINDOW, FUCHSIA, (path[0], path[1], width, height), 0)

    while solutionFound == False:
        obstructed = 0

        possible_pos = [
                        (current_pos[0] - 80, current_pos[1]), #up
                        (current_pos[0], current_pos[1] + 80), #right
                        (current_pos[0] + 80, current_pos[1]), #down
                        (current_pos[0], current_pos[1] - 80)  #left
                        ]

        for pos in possible_pos:
            if pos in END:
                for path in right_way:
                    pygame.draw.rect(WINDOW, LIGHTER_FUCHSIA, (path[0], path[1], width, height), 0)
                    pygame.display.update()
                print(traversed)
                print("Path Found!")
                print(right_way)
                print(maze)
                return solutionFound == True
            if pos[0] < BORDER_LEFT or pos[1] < BORDER_TOP or pos[0] > BORDER_RIGHT or pos[1] > BORDER_BOTTOM:
                print("out of bounds")
                obstructed += 1
                continue
            if pos in WALLS:
                print("blocked")
                obstructed += 1
                continue
            if pos in traversed:
                print("been here")
                obstructed += 1
                continue
            else:
                break

        if obstructed == 4:
            right_way.pop()
            current_pos = right_way[-1]
            print(current_pos)
        else:
            current_pos = pos
            traversed.append(pos)
            right_way.append(pos)
            for path in right_way:
                pygame.draw.rect(WINDOW, YELLOW, (path[0], path[1], width, height), 0)
                pygame.display.update()


class button():
    def __init__(self, color, border, x, y, width, height, font, text=''):
        self.color = color
        self.border = border
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(win, self.border, (self.x, self.y, self.width, self.height), 2)

        if self.text != '':
            if self.font == FONT_MAIN:
                text = FONT_MAIN.render(self.text, 1, (FUCHSIA))
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            if self.font == FONT_GAMEPLAY:
                text = FONT_GAMEPLAY.render(self.text, 1, (FUCHSIA))
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def mouseHover(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def draw_shinso(shinso):
    WINDOW.blit(SHINSO_MAZE, (shinso.x, shinso.y))
    pygame.display.update()

def shinso_controls(keys_pressed, shinso):
    if keys_pressed[pygame.K_UP] and (shinso.y) > BORDER_TOP:
        if (shinso.x, shinso.y - VELOCITY) not in WALLS:
            shinso.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and (shinso.y) < BORDER_BOTTOM:
        if (shinso.x, shinso.y + VELOCITY) not in WALLS:
            shinso.y += VELOCITY
    if keys_pressed[pygame.K_LEFT] and (shinso.x) > BORDER_LEFT:
        if (shinso.x - VELOCITY, shinso.y) not in WALLS:
            shinso.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and (shinso.x) < BORDER_RIGHT:
        if (shinso.x + VELOCITY, shinso.y) not in WALLS:
            shinso.x += VELOCITY

def end_game():
    end_title = button(BLACK, FUCHSIA, BORDER_RIGHT / 2, BORDER_BOTTOM / 2, 300, 50, FONT_GAMEPLAY, text="Path found! ^_^")

    end_screen = True
    click = False

    while end_screen == True:
        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                end_screen = False
                sys.exit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                if end_title.mouseHover(mouse_position):
                    end_title.color = SILVER
                else:
                    end_title.color = BLACK

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if end_title.mouseHover(mouse_position) and click:
                    main()

            end_title.draw(WINDOW)

            pygame.display.update()


def main():

    MainMenu = True
    clock = pygame.time.Clock()

    title_button = button(BLACK, FUCHSIA, 150, 25, 400, 100, FONT_MAIN, text="Shinso's Mazes")
    button_level_1 = button(BLACK, FUCHSIA, 375, 175, 300, 100, FONT_MAIN, text='Level 1')
    button_level_2 = button(BLACK, FUCHSIA, 375, 300, 300, 100, FONT_MAIN, text='Level 2')
    button_level_3 = button(BLACK, FUCHSIA, 375, 425, 300, 100, FONT_MAIN, text='Level 3')

    gamplay_text_greet = FONT_GAMEPLAY.render("Welcome to Shinso's Mazes.", 1, FUCHSIA)
    gamplay_text_1 = FONT_GAMEPLAY.render("There are three levels of mazes ranging from easy, medium, and hard,", 1, FUCHSIA)
    gamplay_text_2 = FONT_GAMEPLAY.render("or Level 1, Level 2, and Level 3. Choose at your own discretion.", 1, FUCHSIA)

    click = False

    global WALLS
    WALLS = []
    global START
    START = []
    global END
    END = []
    global OPEN_SPACES
    OPEN_SPACES = []
    global right_way
    right_way = []
    global traversed
    traversed = []

    while MainMenu == True:
        WINDOW.fill(INDIGO)

        clock.tick(FPS)
        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                MainMenu = False
                sys.exit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                if button_level_1.mouseHover(mouse_position):
                    button_level_1.color = SILVER
                else:
                    button_level_1.color = BLACK
                if button_level_2.mouseHover(mouse_position):
                    button_level_2.color = SILVER
                else:
                    button_level_2.color = BLACK
                if button_level_3.mouseHover(mouse_position):
                    button_level_3.color = SILVER
                else:
                    button_level_3.color = BLACK

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if button_level_1.mouseHover(mouse_position) and click:
                    MazeMenu(maze1)
                if button_level_2.mouseHover(mouse_position) and click:
                    MazeMenu(maze2)
                if button_level_3.mouseHover(mouse_position) and click:
                    MazeMenu(maze3)
                click = False

            title_button.draw(WINDOW)
            button_level_1.draw(WINDOW)
            button_level_2.draw(WINDOW)
            button_level_3.draw(WINDOW)

            pygame.draw.circle(WINDOW, BLACK, (170, 370), 130)
            WINDOW.blit(SHINSO, (50, 275))

            WINDOW.blit(gamplay_text_greet, (20, 600))
            WINDOW.blit(gamplay_text_1, (20, 620))
            WINDOW.blit(gamplay_text_2, (20, 640))

            pygame.display.update()


def MazeMenu(maze):
    clock = pygame.time.Clock()

    GameLoop = True
    click = False

    button_back_to_main = button(BLACK, FUCHSIA, 20, 75, 200, 30, FONT_GAMEPLAY, text='Back To Main Menu')
    button_feeling_stuck = button(BLACK, FUCHSIA, 240, 75, 200, 30, FONT_GAMEPLAY, text='Feeling Stuck?')

    width, height = 80, 80

    maze_y, maze_x = maze.shape

    global BORDER_RIGHT
    BORDER_RIGHT = BORDER_LEFT + ((maze_x - 1) * width)
    global BORDER_BOTTOM
    BORDER_BOTTOM = BORDER_TOP + ((maze_y - 1) * height)

    shinso_x = 0
    shinso_y = 0

    shinso_start = False
    feeling_stuck = False

    while GameLoop == True:
        WINDOW.fill(INDIGO)

        clock.tick(FPS)

        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                GameLoop = False
                sys.exit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                if button_back_to_main.mouseHover(mouse_position):
                    button_back_to_main.color = SILVER
                else:
                    button_back_to_main.color = BLACK
                if button_feeling_stuck.mouseHover(mouse_position):
                    button_feeling_stuck.color = SILVER
                else:
                    button_feeling_stuck.color = BLACK

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if button_back_to_main.mouseHover(mouse_position):
                    if click:
                        GameLoop = False
                if button_feeling_stuck.mouseHover(mouse_position):
                    if click:
                        mazeSolver(maze)
                        feeling_stuck = True
                        break

            x, y = 20, 140

            for row in maze:
                for col in row:
                    if col == '*':
                        pygame.draw.rect(WINDOW, BLACK, (x, y, width, height), 0)
                        WALLS.append((x, y))
                        x += width
                    if col == 'S':
                        pygame.draw.rect(WINDOW, FUCHSIA, (x, y, width, height), 0)
                        if shinso_start == False:
                            shinso_x = x
                            shinso_y = y
                            shinso = pygame.Rect(shinso_x, shinso_y, 70, 70)
                        shinso_start = True
                        START.append((x, y))
                        x += width
                    if col == 'E':
                        pygame.draw.rect(WINDOW, FUCHSIA, (x, y, width, height), 0)
                        END.append((x, y))
                        x += width
                    elif col == ' ': # and feeling_stuck == False:
                        pygame.draw.rect(WINDOW, WHITE, (x, y, width, height), 0)
                        OPEN_SPACES.append((x, y))
                        x += width
                x = 20
                y += height


            if feeling_stuck == True:
                for path in right_way:
                    pygame.draw.rect(WINDOW, LIGHTER_FUCHSIA, (path[0], path[1], width, height), 0)
                    pygame.display.update()
                    end_game()
                    break


            draw_shinso(shinso)

            if (shinso.x, shinso.y) in END:
                end_game()
                break



            keys_pressed = pygame.key.get_pressed()
            shinso_controls(keys_pressed, shinso)

            button_back_to_main.draw(WINDOW)
            button_feeling_stuck.draw(WINDOW)

            pygame.display.update()
    return


maze3 = array([
    [" ", "*", "*", " ", " ", "*", "*", "E"],
    [" ", " ", "*", " ", "*", "*", " ", " "],
    ["*", " ", "*", " ", "*", " ", " ", "*"],
    ["*", " ", " ", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", " ", " ", "*", " "],
    ["S", " ", "*", "*", "*", " ", " ", " "],

])

maze1 = array([
    [" ", "*", "*", "*", "E"],
    [" ", "*", " ", "*", " "],
    [" ", " ", " ", " ", " "],
    ["*", " ", "*", " ", "*"],
    ["S", " ", "*", "*", "*"]
])

maze2 = array([
    [" ", "*", " ", " ", "*", "*", "E"],
    [" ", " ", " ", "*", "*", " ", " "],
    ["*", " ", "*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", " ", "*", " "],
    ["S", " ", "*", "*", " ", " ", " "],
])

#maze as a matrix
matrix1 = matrix(maze1)
matrix2 = matrix(maze2)
matrix3 = matrix(maze3)

traversed = []
right_way = []


    #setting up the staring line
#start = np.where(matrix0 == 'S')
#end = np.where(matrix0 == 'E')

#main()

main()
#if __name__ == "__main__":
    #main()
