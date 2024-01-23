from typing import Iterable


class FixedPolyomino:
    def __init__(self, squares: Iterable):
        self._squares = tuple(set(sorted(squares)))

    @property
    def length(self):
        return len(self._squares)

    @property
    def id(self):
        return hash(self._squares)

    def is_monomino(self):
        return self.length == 1

    def rotate(self):
        """ Creates a new polyomino rotated by 90 degrees """
        return FixedPolyomino(squares=((square[1], -square[0]) for square in self._squares))

    def translate(self):
        """ Creates a new Polyomino translated to the origin (0, 0) """
        ox, oy = self._get_canonical_representation()
        return FixedPolyomino(squares=((square[0] - ox, square[1] - oy) for square in self._squares))

    def increase_order(self):
        """ Increases order by adding one square to a new Polyomino and returns a set with all of them """
        return {FixedPolyomino(squares=self._squares + (sq,))
                for cluster in self._get_square_cluster()
                for sq in cluster}

    def _get_square_cluster(self):
        """ Gets possible movements from a square with (x,y) coordinates"""
        adjacent_square = lambda x, y: ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        return {adjacent_square(square[0], square[1]) for square in self._squares}

    def _get_canonical_representation(self):
        """ Gets minimum values for x and y """
        ox, oy = float("+inf"), float("+inf")
        for square in self._squares:
            x, y = square
            if x < ox:
                ox = x

            if y < oy:
                oy = y
        return ox, oy

    def __hash__(self):
        current = self.translate()
        current_key = current.id

        if self.is_monomino():
            return current_key

        for i in range(3):
            current = current.rotate().translate()
            if current.id < current_key:
                current_key = current.id

        return current_key

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return hash(self) == hash(other)

    def __repr__(self):
        matrix = [["*" for _ in range(self.length)] for _ in range(self.length)]
        at_origin = self.translate()
        for square in at_origin._squares:
            x, y = square
            matrix[x][y] = "X"

        result = (str(matrix).replace("[", "").replace("]", "\n").
                  replace(",", "").replace("\'", "").replace(" ", ""))
        return result
