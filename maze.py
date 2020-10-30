class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
        self.visited = False
        self.target = False
        self.examined = False

    def __str__(self):
        return "x: {}, y: {}, walls: {}, visited: {}, target: {}".format(self.x, self.y, self.walls, self.visited,
                                                                         self.target)


class Maze:

    def __init__(self, size):
        self.map = [[Cell(x, y) for x in range(size)] for y in range(size)]
        self.reset_visited_state()

    def reset_visited_state(self) -> None:
        for row in self.map:
            for cell in row:
                cell.visited = False

    def set_target(self, x: int, y: int) -> None:
        self.map[y][x].target = True

    def set_start(self, x: int, y: int) -> None:
        self.map[y][x].start = True

    def print_path(self, path: list) -> None:
        cli_representation = self._create_cli_representation()
        for coordinates in path[1:]:
            x = coordinates[0]
            y = coordinates[1]
            x_str = list(cli_representation[y * 2 + 1][x])
            x_str[1] = 'o'
            x_str[2] = 'o'
            cli_representation[y * 2 + 1][x] = ''.join(x_str)
        print('\n'.join([''.join(line) for line in cli_representation]))

    def _create_cli_representation(self) -> list:
        size = len(self.map)
        map_print = [['+--'] * size + ['+']]
        for row in self.map:
            vertical = ['|ZZ' if cell.walls.get('W') and cell.target
                        else '|  ' if cell.walls.get('W')
                        else ' ZZ' if not cell.walls.get('W') and cell.target
                        else '   ' for cell in row]
            vertical[-1] = vertical[-1] + '|'
            horizontal = ['+--' if cell.walls.get('S') else '+  ' for cell in row]
            horizontal[-1] = horizontal[-1] + '+'
            map_print.append(vertical)
            map_print.append(horizontal)
        return map_print

    def __str__(self):
        return '\n'.join([''.join(line) for line in self._create_cli_representation()])
