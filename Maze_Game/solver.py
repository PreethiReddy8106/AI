import heapq

def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end):

    rows = len(maze)
    cols = len(maze[0])

    open_set = []

    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {
        start: 0
    }

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == end:

            path = []

            while current in came_from:

                path.append(current)

                current = came_from[current]

            path.append(start)

            path.reverse()

            return path

        row, col = current

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            neighbor = (nr, nc)

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                maze[nr][nc] == 0
            ):

                temp_g = g_score[current] + 1

                if (
                    neighbor not in g_score or
                    temp_g < g_score[neighbor]
                ):

                    came_from[neighbor] = current

                    g_score[neighbor] = temp_g

                    f_score = temp_g + heuristic(neighbor, end)

                    heapq.heappush(
                        open_set,
                        (f_score, neighbor)
                    )

    return []
