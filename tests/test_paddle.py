import unittest
from paddle import Paddle

class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddle()

    def test_initial_position(self):
        self.assertEqual(self.paddle.rect.left, 400 - self.paddle.width // 2)
        self.assertEqual(self.paddle.rect.top, 570)

    def test_move_left(self):
        initial_left = self.paddle.rect.left
        self.paddle.move("left")
        self.assertLess(self.paddle.rect.left, initial_left)

    def test_move_right(self):
        initial_left = self.paddle.rect.left
        self.paddle.move("right")
        self.assertGreater(self.paddle.rect.left, initial_left)

if __name__ == '__main__':
    unittest.main()