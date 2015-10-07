import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    start_cell = random.randrange(len(m.maze_array))
    to_visit = [start_cell]

    while len(to_visit):
        current_cell = to_visit.pop()

        all_neighbors = m.cell_neighbors(current_cell)
        if len(all_neighbors) > 0:
            neighbor, direction = random.choice(all_neighbors)
            m.connect_cells(current_cell, neighbor, direction)
            if len(all_neighbors) != 1:
                to_visit.append(current_cell)
            to_visit.append(neighbor)
        m.refresh_maze_view()
    m.state = "solve"


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
