import heapq

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def find_path_with_astar(start, goal, obstacles, snake_body, width, height, cell_size):
    grid_width = width // cell_size
    grid_height = height // cell_size
    start_grid = (start[0] // cell_size, start[1] // cell_size)
    goal = (goal[0] // cell_size, goal[1] // cell_size)
    obstacles = {(x // cell_size, y // cell_size) for x, y in obstacles}
    snake_body = {(x // cell_size, y // cell_size) for x, y in snake_body if (x, y) != start}

    open_set = [(0, start_grid)]
    came_from = {}
    g_score = {start_grid: 0}
    f_score = {start_grid: manhattan_distance(start_grid, goal)}

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < grid_width and 0 <= neighbor[1] < grid_height and
                neighbor not in obstacles and neighbor not in snake_body):
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None
