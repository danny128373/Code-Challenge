import io
import unittest
import unittest.mock

from play_trivia import play_trivia


class TestPlayTriva(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        play_trivia(8)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_only_numbers(self):
        self.assert_stdout(
            2, f'Perfect, best trivia player to ever roam this world! Score: {correct}/10')
