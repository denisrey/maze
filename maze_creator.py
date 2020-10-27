import random
from abc import ABC, abstractmethod

from maze import Maze


class AbstractMazeCreator(ABC):

    @abstractmethod
    def __init__(self, maze: Maze):
        self.maze = maze


class MazeCreatorDfs(AbstractMazeCreator):

    def __init__(self, maze: Maze):
        self.maze = maze
        self._create(0, 0)
        self.maze.reset_visited_state()

    def _create(self, x, y) -> bool:
        if not self.maze.map[y][x].target:
            if self.maze.map[y][x].visited:
                return False
            else:
                self.maze.map[y][x].visited = True
                random_destinations = [('S', 'N', (x, y + 1)),
                                       ('E', 'W', (x + 1, y)),
                                       ('N', 'S', (x, y - 1)),
                                       ('W', 'E', (x - 1, y))]
                random.shuffle(random_destinations)
                for item in random_destinations:
                    if self._is_valid_target_cell(*item[2]):
                        self.maze.map[y][x].walls[item[0]] = False
                        self.maze.map[item[2][1]][item[2][0]].walls[item[1]] = False
                        val = self._create(*item[2])
                        if val is True:
                            return val
                return False
        else:
            return True

    def _is_valid_target_cell(self, t_x, t_y):
        return 0 <= t_x < len(self.maze.map) and 0 <= t_y < len(self.maze.map) \
               and not self.maze.map[t_y][t_x].visited
