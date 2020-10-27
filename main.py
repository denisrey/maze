import sys

from maze import Maze
from maze_creator import MazeCreatorDfs
from maze_solver import MazeSolverDfs

sys.setrecursionlimit(500000000)

if __name__ == '__main__':
    maze = Maze(70)
    creator = MazeCreatorDfs(maze)
    print(maze)
    solver = MazeSolverDfs(maze)
    solver.solve(0, 0, 9, 69)
    maze.print_path(solver.get_path())
    print(solver.get_path())
