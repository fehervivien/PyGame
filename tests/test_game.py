# FILE: test_game.py
import unittest
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_score(self):
        self.assertEqual(self.game.score, 0)

    def test_paddle_initialization(self):
        self.assertIsNotNone(self.game.paddle)

    def test_ball_initialization(self):
        self.assertIsNotNone(self.game.ball)

if __name__ == '__main__':
    unittest.main()