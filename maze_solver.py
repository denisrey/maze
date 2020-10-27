from abc import ABC, abstractmethod

from maze import Maze


class AbstractMazeSolver(ABC):

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
