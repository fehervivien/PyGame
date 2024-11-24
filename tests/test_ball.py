import unittest
from ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball()

    def test_initial_position(self):
        self.assertGreaterEqual(self.ball.rect.left, 0)
        self.assertLessEqual(self.ball.rect.right, 800)
        self.assertEqual(self.ball.rect.top, 300)

    def test_move(self):
        initial_left = self.ball.rect.left
        initial_top = self.ball.rect.top
        self.ball.move()
        self.assertNotEqual(self.ball.rect.left, initial_left)
        self.assertNotEqual(self.ball.rect.top, initial_top)

if __name__ == '__main__':
    unittest.main()