import sys

from maze import Maze
from maze_creator import MazeCreatorBlank
from maze_solver import MazeSolverDfs

sys.setrecursionlimit(500000000)

if __name__ == '__main__':
    maze = Maze(30)
    creator = MazeCreatorBlank(maze)
    print(maze)
    solver = MazeSolverDfs(maze)
    solver.solve(0, 0, 29, 29)

    maze.print_path(solver.get_path())
