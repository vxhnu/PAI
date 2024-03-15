import heapq

def astar(start, goal, grid):
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, (0, start, None))
    while open_set:
        _, current, parent = heapq.heappop(open_set)
        if current == goal:
            path = []
            while parent:
                path.append(parent)
                _, parent, _ = closed_set[parent]
            return path[::-1] + [current]
        
        if current in closed_set:
            continue
        
        closed_set[current] = (_, parent, None)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (current[0] + dx, current[1] + dy)
            if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]) and grid[new_pos[0]][new_pos[1]] == 0:
                heapq.heappush(open_set, (abs(goal[0] - new_pos[0]) + abs(goal[1] - new_pos[1]), new_pos, current))
                
    return None

if __name__ == "_main_":
    grid = [[0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]

    start = (0, 0)
    goal = (4, 4)

    path = astar(start, goal, grid)

    if path:
        print("Path found:")
        for step in path:
            print(step)
    else:
        print("No path found")