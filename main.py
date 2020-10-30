import sys

from maze import Maze
from maze_creator import MazeCreatorDfs
from maze_solver import MazeSolverDfs, MazeSolverBfs

sys.setrecursionlimit(500000000)

if __name__ == '__main__':
    maze = Maze(30)
    creator = MazeCreatorDfs(maze)
    print(maze)
    solver = MazeSolverBfs(maze)
    solver.solve(0, 0, 29, 29)

    maze.print_path(solver.get_path())

