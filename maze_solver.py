from abc import ABC, abstractmethod
from queue import Queue

from maze import Maze


class AbstractMazeSolver(ABC):

    @abstractmethod
    def __init__(self, maze):
        self.maze = maze

    @abstractmethod
    def get_path(self) -> list:
        raise NotImplementedError

    @abstractmethod
    def solve(self, start_x: int, start_y: int, target_x: int, target_y: int) -> None:
        raise NotImplementedError


class MazeSolverDfs(AbstractMazeSolver):

    def __init__(self, maze: Maze):
        self.maze = maze
        self.has_solution = False
        self.path = []

    def get_path(self) -> list:
        return self.path

    def solve(self, start_x: int, start_y: int, target_x: int, target_y: int) -> None:
        self.maze.set_target(target_x, target_y)
        self.has_solution, self.path = self._solve(start_x, start_y)

    def _solve(self, x: int, y: int) -> (bool, list):
        if not self.maze.map[y][x].target:
            if self.maze.map[y][x].visited:
                return False, []
            else:
                self.maze.map[y][x].visited = True
                for item in (('S', (x, y + 1)),
                             ('E', (x + 1, y)),
                             ('N', (x, y - 1)),
                             ('W', (x - 1, y))):
                    if not self.maze.map[y][x].walls.get(item[0]):
                        val, coord = self._solve(*item[1])
                        if val is True:
                            coord.append((x, y))
                            return val, coord
                return False, coord
        else:
            return True, [(x, y)]


class MazeSolverBfs(AbstractMazeSolver):

    def __init__(self, maze):
        self.maze = maze
        self.path = []

    def solve(self, start_x: int, start_y: int, target_x: int, target_y: int) -> None:
        self.maze.set_target(target_x, target_y)
        q = Queue()
        q.put([self.maze.map[start_y][start_x]])
        while not q.empty():
            path = q.get()
            current_cell = path[-1]
            if current_cell.target:
                self.path = [(cell.x, cell.y) for cell in path]
                return
            else:
                for item in (('S', (current_cell.x, current_cell.y + 1)),
                             ('E', (current_cell.x + 1, current_cell.y)),
                             ('N', (current_cell.x, current_cell.y - 1)),
                             ('W', (current_cell.x - 1, current_cell.y))):
                    if not self.maze.map[current_cell.y][current_cell.x].walls.get(item[0]):
                        neighbor_cell = self.maze.map[item[1][1]][item[1][0]]
                        if not neighbor_cell.visited:
                            neighbor_cell.visited = True
                            new_path = list(path)
                            new_path.append(neighbor_cell)
                            q.put(new_path)
                current_cell.examined = True
        self.path = []

    def get_path(self) -> list:
        return self.path[0:-1]
