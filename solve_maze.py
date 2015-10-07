import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    start_cell = 0
    to_visit = [start_cell]
    while len(to_visit):
        current_cell = to_visit.pop()

        x, y = m.x_y(current_cell)
        if x == m.w_cells - 1 and y == m.h_cells - 1:
            return

        all_neighbors = m.cell_neighbors(current_cell)
        if len(all_neighbors) > 0:
            neighbor, direction = random.choice(all_neighbors)
            m.visit_cell(current_cell, neighbor, direction)
            to_visit.append(current_cell)
            to_visit.append(neighbor)
        else:
            m.backtrack(current_cell)
        m.refresh_maze_view()
    m.state = "idle"


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # TODO: Implement solve_bfs
    pass


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
