import unittest
from play_trivia import PlayTrivia


class TestPlayTriva(unittest.TestCase):
    def test_score_rating(self):
        '''Tests when score is between 0 and 10'''
        trivia = PlayTrivia()
        self.assertEqual(trivia.score_rating(
            8), f'You did great! Score: 8/10')
        self.assertEqual(trivia.score_rating(
            5), f'Were you even trying? Score: 5/10')
        self.assertEqual(trivia.score_rating(
            10), f'Perfect, best trivia player to ever roam this world! Score: 10/10')

    def test_score_rating_values(self):
        '''Tests to make sure errors are raise when necessary'''
        trivia = PlayTrivia()
        self.assertRaises(ValueError, trivia.score_rating, -1)
        self.assertRaises(ValueError, trivia.score_rating, 11)
        self.assertRaises(TypeError, trivia.score_rating, 'hello')
        self.assertRaises(TypeError, trivia.score_rating, 5.5)
