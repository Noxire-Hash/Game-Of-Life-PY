import unittest
from main import calc_state


class TestGameOfLife(unittest.TestCase):
    def test_alive_with_fewer_than_two_neighbors(self):
        grid = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(calc_state(grid, 1, 1), 0)

    def test_alive_with_two_or_three_neighbors(self):
        grid = [
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(calc_state(grid, 1, 1), 1)

        grid = [
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0]
        ]
        self.assertEqual(calc_state(grid, 1, 1), 1)

    def test_alive_with_more_than_three_neighbors(self):
        grid = [
            [1, 1, 1],
            [1, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(calc_state(grid, 1, 1), 0)

    def test_dead_with_exactly_three_neighbors(self):
        grid = [
            [1, 1, 0],
            [0, 0, 1],
            [0, 0, 0]
        ]
        self.assertEqual(calc_state(grid, 1, 1), 1)


if __name__ == '__main__':
    unittest.main()
