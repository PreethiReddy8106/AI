import random
from solver import astar

ROWS = 25
COLS = 25

def generate_maze():

    while True:

        maze = []

        for r in range(ROWS):

            row = []

            for c in range(COLS):

                # Keep start/end open
                if (
                    (r == 0 and c == 0)
                    or
                    (r == ROWS - 1 and c == COLS - 1)
                ):

                    row.append(0)

                else:

                    row.append(
                        1 if random.random() < 0.30 else 0
                    )

            maze.append(row)

        # CHECK IF PATH EXISTS
        path = astar(
            maze,
            (ROWS - 1, COLS - 1),
            (0, 0)
        )

        if path:
            return maze
