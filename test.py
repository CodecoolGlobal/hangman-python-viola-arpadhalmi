import unittest
import hangman

class BasicTestCase(unittest.TestCase):
    def test_ask_level_negative(self):
        level = -1
        expected_result = "The chosen -1 level is not available!"
        actual_result = hangman.ask_level(level)
        self.assertEqual(expected_result, actual_result)

    def test_ask_level_notnumber(self):
        level = 'asd'
        expected_result = "The chosen asd level is not available!"
        actual_result = hangman.ask_level(level)
        self.assertEqual(expected_result, actual_result)
    
    def test_ask_level_toohigh(self):
        level = 100
        expected_result = "The chosen 100 level is not available!"
        actual_result = hangman.ask_level(level)
        self.assertEqual(expected_result, actual_result)
    
    def test_ask_level_correct(self):
        level = 1
        expected_result = 1
        actual_result = hangman.ask_level(level)
        self.assertEqual(expected_result, actual_result)

    def test_set_difficulty(self):
        level = 1
        expected_result = ("Cairo", 10)
        actual_result = hangman.set_difficulty(level)
        self.assertEqual(expected_result, actual_result)

    def test_underlines(self):
        word = 'alma'
        expected_result = '_ _ _ _'
        actual_result = hangman.underlines('alma')
        self.assertEqual(expected_result, actual_result)

    def test_ask_a_letter(self):
        pass
    def test_tried_letters(self):
        pass
    def test_present_letters(self):
        pass
