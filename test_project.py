"""Unit-test cases for class project"""
from typing import Self
import unittest
from project import show_aggie_pride, reverse_list, get_area_codes, convert_text_numbers_to_integers, convert_text_to_digits_example, get_state_abbrev_freq


class ProjectTestCase(unittest.TestCase):
    """Unit Tests"""
    def test_show_aggie_pride(self):
        """Tests to make sure show_aggie_pride() returns the correct value"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_reverse_list(self):
        """Test to make sure reverse_list works as expected"""
        # make sure an empty list works
        self.assertFalse(reverse_list([]))

        # try numbers
        reverse = [5, 4, 3, 2, 1]
        self.assertListEqual(reverse, reverse_list([1, 2, 3, 4, 5]))

        # try letters
        reverse = ['e', 'd', 'c', 'b', 'a']
        self.assertListEqual(reverse, reverse_list(['a', 'b', 'c', 'd', 'e']))

    def test_get_area_codes(self):
        """Test to make sure we can get area codes OK"""
        ac_dict = get_area_codes()

        # Try a few known area codes
        self.assertEqual(ac_dict['516'], 'NY')
        self.assertEqual(ac_dict['919'], 'NC')
        self.assertEqual(ac_dict['212'], 'NY')
        self.assertEqual(ac_dict['970'], 'CO')

    def test_convert_text_numbers_to_integers(self):
        """Test to make sure we can convert text numbers to integers"""
        text = 'zero, one, two ,three , four,five,six,seven,eight,nine'
        results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(results, convert_text_numbers_to_integers(text))

        # test an ivnalid input
        with self.assertRaises(ValueError):
            convert_text_numbers_to_integers('zero, one, two ,three , four,five,six,seven,eight,nine,ten')

        # Empty list
        with self.assertRaises(ValueError):
            convert_text_numbers_to_integers(')')

    def test_convert_text_to_digits_example(self):
        """Test to make sure convert_text_to_digits_example works as expected"""
        text = 'zero, one, two ,three , four,five,six,seven,eight,nine'
        results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(results, convert_text_to_digits_example(text))

        with self.assertRaises(ValueError):
            convert_text_to_digits_example('ten')

        with self.assertRaises(ValueError):
            convert_text_to_digits_example('')

    def test_state_name(self):
        #Test for state_to_abb_dict    
            correct_state = 'Alaska, North Carolina, New York, New Jersey, Washington'
            statesabb = ['AK', 'NC', 'NJ', 'NY', 'WA']
            self.assertEqual(statesabb, get_state_abbrev_freq(correct_state))
        #Test for misspelled state names    
            with self.assertRaises(ValueError):  
                get_state_abbrev_freq('Alasa, North Carolina, Nue York, New Jersie, Wasinton')
        #Test for empty list
            with self.assertRaises(ValueError): 
                get_state_abbrev_freq('')


if __name__ == '__main__':
    unittest.main()

