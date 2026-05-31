import pygame
import random

from maze import generate_maze
from solver import astar

pygame.init()

# WINDOW
WIDTH = 900
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEURAL LOCKDOWN")

clock = pygame.time.Clock()

# COLORS
BACKGROUND = (5, 6, 12)

PLAYER = (0, 255, 200)
ENEMY = (255, 60, 60)

TEXT = (220, 220, 220)

KEYCARD = (80, 180, 255)

# FONT
font = pygame.font.SysFont("consolas", 32)

# GAME STATES
MENU = 0
PLAYING = 1
GAME_OVER = 2

game_state = MENU

win = False

# INTRO TIMER
intro_timer = 0

# MAZE
maze = generate_maze()

ROWS = len(maze)
COLS = len(maze[0])

CELL_SIZE = WIDTH // COLS

# PLAYER
player_pos = [0, 0]

# SECURITY DRONES
enemies = [
    [ROWS // 2, COLS // 2],
    [ROWS // 2, COLS // 2 - 3],
    [ROWS // 2 - 3, COLS // 2]
]

# EXIT
exit_pos = [ROWS - 2, COLS - 2]

# Ensure exit open
maze[exit_pos[0]][exit_pos[1]] = 0

# KEYCARD
has_key = False

while True:

    key_row = random.randint(2, ROWS - 3)
    key_col = random.randint(2, COLS - 3)

    if maze[key_row][key_col] == 0:
        key_pos = [key_row, key_col]
        break

# TIMERS
move_counter = 0
player_move_delay = 0
glow_timer = 0


def reset_game():

    global maze
    global player_pos
    global enemies
    global has_key
    global key_pos
    global win

    maze = generate_maze()

    maze[exit_pos[0]][exit_pos[1]] = 0

    player_pos = [0, 0]

    enemies = [
        [ROWS // 2, COLS // 2],
        [ROWS // 2, COLS // 2 - 3],
        [ROWS // 2 - 3, COLS // 2]
    ]

    has_key = False

    while True:

        key_row = random.randint(2, ROWS - 3)
        key_col = random.randint(2, COLS - 3)

        if maze[key_row][key_col] == 0:
            key_pos = [key_row, key_col]
            break

    win = False


def draw_text(text, y, color=TEXT):

    render = font.render(text, True, color)

    rect = render.get_rect(center=(WIDTH // 2, y))

    screen.blit(render, rect)


def draw_maze():

    for row in range(ROWS):

        for col in range(COLS):

            x = col * CELL_SIZE
            y = row * CELL_SIZE

            # FLOOR
            color = (8, 10, 15)

            if maze[row][col] == 1:

                # AI MACHINE BASE
                pygame.draw.rect(
                    screen,
                    (35, 35, 45),
                    (x, y, CELL_SIZE, CELL_SIZE)
                )

                # MACHINE BODY
                pygame.draw.rect(
                    screen,
                    (90, 95, 110),
                    (
                        x + 3,
                        y + 3,
                        CELL_SIZE - 6,
                        CELL_SIZE - 6
                    ),
                    border_radius=5
                )

                # SCREEN PANEL
                pygame.draw.rect(
                    screen,
                    (10, 20, 30),
                    (
                        x + 8,
                        y + 8,
                        CELL_SIZE - 16,
                        CELL_SIZE // 3
                    ),
                    border_radius=3
                )

                # BLUE LIGHT
                pygame.draw.circle(
                    screen,
                    (0, 255, 255),
                    (
                        x + CELL_SIZE // 2,
                        y + CELL_SIZE // 2
                    ),
                    4
                )

                # RED LIGHT
                pygame.draw.circle(
                    screen,
                    (255, 60, 60),
                    (
                        x + CELL_SIZE - 10,
                        y + 10
                    ),
                    3
                )

                # WIRES
                pygame.draw.line(
                    screen,
                    (50, 200, 255),
                    (x + 10, y + CELL_SIZE - 10),
                    (x + CELL_SIZE - 10, y + CELL_SIZE - 10),
                    2
                )

            else:

                pygame.draw.rect(
                    screen,
                    color,
                    (x, y, CELL_SIZE, CELL_SIZE)
                )

                pygame.draw.rect(
                    screen,
                    (18, 22, 32),
                    (
                        x + 2,
                        y + 2,
                        CELL_SIZE - 4,
                        CELL_SIZE - 4
                    ),
                    1
                )

            # GRID
            pygame.draw.rect(
                screen,
                (25, 30, 40),
                (x, y, CELL_SIZE, CELL_SIZE),
                1
            )

    # KEYCARD
    if not has_key:

        pygame.draw.circle(
            screen,
            KEYCARD,
            (
                key_pos[1] * CELL_SIZE + CELL_SIZE // 2,
                key_pos[0] * CELL_SIZE + CELL_SIZE // 2
            ),
            CELL_SIZE // 3
        )

    # EXIT
    pulse = abs((glow_timer % 60) - 30)

    center_x = (
        exit_pos[1] * CELL_SIZE
        + CELL_SIZE // 2
    )

    center_y = (
        exit_pos[0] * CELL_SIZE
        + CELL_SIZE // 2
    )

    pygame.draw.circle(
        screen,
        (0, 255, 120),
        (center_x, center_y),
        CELL_SIZE + 15 + pulse // 2
    )

    pygame.draw.circle(
        screen,
        (120, 255, 180),
        (center_x, center_y),
        CELL_SIZE
    )

    pygame.draw.rect(
        screen,
        (0, 255, 120),
        (
            exit_pos[1] * CELL_SIZE,
            exit_pos[0] * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
    )

    pygame.draw.rect(
        screen,
        (180, 255, 200),
        (
            exit_pos[1] * CELL_SIZE + 6,
            exit_pos[0] * CELL_SIZE + 6,
            CELL_SIZE - 12,
            CELL_SIZE - 12
        )
    )

    # PLAYER
    pygame.draw.circle(
        screen,
        PLAYER,
        (
            player_pos[1] * CELL_SIZE + CELL_SIZE // 2,
            player_pos[0] * CELL_SIZE + CELL_SIZE // 2
        ),
        CELL_SIZE // 2 - 2
    )

    # ENEMIES
    for enemy_pos in enemies:

        center_enemy_x = (
            enemy_pos[1] * CELL_SIZE
            + CELL_SIZE // 2
        )

        center_enemy_y = (
            enemy_pos[0] * CELL_SIZE
            + CELL_SIZE // 2
        )

        pygame.draw.circle(
            screen,
            ENEMY,
            (center_enemy_x, center_enemy_y),
            CELL_SIZE // 2 - 2
        )

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (center_enemy_x, center_enemy_y),
            CELL_SIZE // 7
        )


running = True

while running:

    clock.tick(30)

    glow_timer += 1

    screen.fill(BACKGROUND)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # MENU
        if game_state == MENU:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    intro_timer = 180
                    game_state = PLAYING

        # GAME OVER
        elif game_state == GAME_OVER:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:

                    reset_game()

                    intro_timer = 180
                    game_state = PLAYING

    # MENU
    if game_state == MENU:

        draw_text(
            "NEURAL LOCKDOWN",
            HEIGHT // 2 - 50,
            (0, 255, 200)
        )

        draw_text(
            "Find the Keycard. Escape the Facility.",
            HEIGHT // 2 + 10
        )

        draw_text(
            "Press SPACE to Start",
            HEIGHT // 2 + 70
        )

    # GAMEPLAY
    elif game_state == PLAYING:

        draw_maze()

        # INTRO SCREEN
        if intro_timer > 0:

            intro_timer -= 1

            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(120)
            overlay.fill((0, 0, 0))

            screen.blit(overlay, (0, 0))

            draw_text(
                "MISSION STARTING...",
                HEIGHT // 2 - 60,
                (0, 255, 200)
            )

            draw_text(
                "COLLECT THE KEYCARD",
                HEIGHT // 2,
                (80, 180, 255)
            )

            draw_text(
                "AVOID SECURITY DRONES",
                HEIGHT // 2 + 60,
                (255, 60, 60)
            )

            pygame.display.update()
            continue

        objective = "GET KEYCARD"

        if has_key:
            objective = "REACH EXIT"

        hud_text = font.render(
            f"OBJECTIVE: {objective}",
            True,
            PLAYER
        )

        screen.blit(hud_text, (20, 20))

        # MOVEMENT
        keys = pygame.key.get_pressed()

        player_move_delay += 1

        if player_move_delay >= 4:

            player_move_delay = 0

            new_row = player_pos[0]
            new_col = player_pos[1]

            if keys[pygame.K_UP]:
                new_row -= 1

            elif keys[pygame.K_DOWN]:
                new_row += 1

            elif keys[pygame.K_LEFT]:
                new_col -= 1

            elif keys[pygame.K_RIGHT]:
                new_col += 1

            if (
                0 <= new_row < ROWS and
                0 <= new_col < COLS and
                maze[new_row][new_col] == 0
            ):
                player_pos = [new_row, new_col]

        # KEYCARD
        if player_pos == key_pos:
            has_key = True

        # AI MOVEMENT
        move_counter += 1

        if move_counter >= 10:

            move_counter = 0

            for i in range(len(enemies)):

                enemy_pos = enemies[i]

                distance = abs(
                    enemy_pos[0] - player_pos[0]
                ) + abs(
                    enemy_pos[1] - player_pos[1]
                )

                if distance < 20:

                    path = astar(
                        maze,
                        tuple(enemy_pos),
                        tuple(player_pos)
                    )

                    if len(path) > 1:
                        enemies[i] = list(path[1])

        # WIN
        if player_pos == exit_pos and has_key:

            win = True
            game_state = GAME_OVER

        # LOSE
        for enemy_pos in enemies:

            if player_pos == enemy_pos:

                win = False
                game_state = GAME_OVER

    # GAME OVER
    elif game_state == GAME_OVER:

        if win:

            draw_text(
                "ESCAPE SUCCESSFUL",
                HEIGHT // 2 - 40,
                (0, 255, 120)
            )

        else:

            draw_text(
                "CAPTURED BY SECURITY",
                HEIGHT // 2 - 40,
                (255, 60, 60)
            )

        draw_text(
            "Press R to Restart",
            HEIGHT // 2 + 40
        )

    pygame.display.update()

pygame.quit()
