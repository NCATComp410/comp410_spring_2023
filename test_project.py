"""Unit-test cases for class project"""
import unittest
from project import *


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

    def test_area_code_look(self):
        """""Test to verify if area_code_lookup works as it should"""
        text = '919-555-1212,212-555-1212 , 970-555-1212, 415-555-1212'
        output_dict = {212:'NY', 415:'CA', 919:'NC', 970:'CO'}
        self.assertEqual(output_dict, area_code_lookup(text))

        #test set of other valid area codes
        text1 = '336-554-3994, 603-554-3994, 207-654-3894, 208-654-3894'
        output_dict1 = {207:'ME', 208:'ID', 336:'NC', 603:'NH'}
        self.assertEqual(output_dict1, area_code_lookup(text1))

        #test set of invalid area codes
        with self.assertRaises(ValueError):
            area_code_lookup('105-554-3994, 800-554-3994, 877-554-3994, 888-554-3994')

        #test for empty list
        with self.assertRaises(ValueError):
            area_code_lookup('')
        
        # test for phone with no area code
        with self.assertRaises(ValueError):
            area_code_lookup('919-555-1212,212-555-1212 , 999-9999')
        
        #test with both wrong format and invalid area code
        with self.assertRaises(ValueError):
            area_code_lookup('921555-1212,221-555-1212 , 999-9999')
        
        #test with wrong format
        with self.assertRaises(ValueError):
            area_code_lookup('9215551212,  2215551212 , 7189999999')

    def test_area_code_look_csv(self):
        # read the csv file
        data = read_csv_file('data.csv')
        # fill in the expected values based on inspection
        expected = {203: 'CT', 211: '', 212: 'NY', 218: 'MN', 229: 'GA', 249: 'ONTARIO', 254: 'TX', 283: 'OH',
                    326: 'OH', 328: '', 337: 'LA', 341: 'CA', 348: '', 358: '', 360: 'WA', 363: 'NY', 381: '', 388: '',
                    402: 'NE', 411: '', 414: 'WI', 417: 'MO', 421: '', 434: 'VA', 448: 'FL', 482: '', 487: '', 492: '',
                    494: '', 512: 'TX', 522: 'NANP AREA', 534: 'WI', 541: 'OR', 544: 'NANP AREA', 550: 'NANP AREA',
                    551: 'NJ', 561: 'FL', 563: 'IA', 573: 'MO', 591: '', 594: '', 595: '', 596: '', 602: 'AZ',
                    610: 'PA', 612: 'MN', 626: 'CA', 627: '', 630: 'IL', 636: 'MO', 642: '', 652: '', 656: 'FL',
                    659: 'AL', 686: 'VA', 696: '', 704: 'NC', 737: 'TX', 740: 'OH', 743: 'NC', 766: '', 775: 'NV',
                    781: 'MA', 784: 'ST. VINCENT & GRENADINES', 789: '', 804: 'VA', 813: 'FL', 847: 'IL', 850: 'FL',
                    858: 'CA', 863: 'FL', 864: 'SC', 865: 'TN', 866: 'NANP AREA', 870: 'AR', 871: '', 880: '', 889: '',
                    893: '', 900: 'NANP AREA', 901: 'TN', 902: 'NOVA SCOTIA - PRINCE EDWARD ISLAND', 910: 'NC',
                    913: 'KS', 922: '', 929: 'NY', 932: '', 933: '', 937: 'OH', 969: '', 987: '', 995: ''}
        # get the actual results
        results = area_code_lookup(','.join(data['Phone']))
        # make sure they are equal
        self.assertDictEqual(expected, results)
    
    def test_area_code_prefixes(self):
        #test for none U.S. states and territories
        expected = [487, 522, 652, 642, 784, 591, 880, 348, 933, 987, 627, 893, 595, 866, 211, 627, 328, 766, 969, 544, 995, 492, 421, 381, 249, 594, 482, 494, 596, 889, 932, 411, 696, 789, 922, 900, 902, 358, 871, 388, 550]
        results = area_code_prefixes()
        self.assertListEqual(expected,results)

    def test_state_name(self):
        # Test for state_to_abb_dict
        correct_state = 'Alaska, North Carolina, New York, New Jersey, Washington'
        statesabb = {'AK': 1, 'NC': 1, 'NJ': 1, 'NY': 1, 'WA': 1}
        self.assertTrue(statesabb, get_state_abbrev_freq(correct_state))
        # Test for misspelled state names
        with self.assertRaises(ValueError):
            get_state_abbrev_freq('Alasa, North Carolina, Nue York, New Jersie, Wasinton')
        # Test for empty list
        with self.assertRaises(ValueError):
            get_state_abbrev_freq('')
    def test_email_domain_and_user_count(self):
        text = 'joe@gmail.com, joe1@gmail.com, john@outlook.com, jerry@abc.com, julie@xyz.com, tim@abc.com, joe@gmail.com'
        results = {'abc.com':2, 'gmail.com':2, 'outlook.com':1, 'xyz.com':1}
        self.assertDictEqual(results, email_domain_and_user_count(text))

    def test_email_domain_and_user_count_2(self):
        text = 'joe@gmail.com, john@outlook.com, jerry@abc.com, julie@xyz.com, tim@abc.com, joe@gmail.com'
        results = {'abc.com':2, 'gmail.com':1, 'outlook.com':1, 'xyz.com':1}
        self.assertDictEqual(results, email_domain_and_user_count(text))

    def test_email_domain_and_user_count_3(self):
        text = 'test@gmail.com'
        results = {'gmail.com':1}
        self.assertDictEqual(results, email_domain_and_user_count(text))

    def test_email_domain_and_user_count_4(self):
        text = ''
        results = {}
        self.assertDictEqual(results, email_domain_and_user_count(text))

    def test_read_csv_file(self):
        """Tests to make sure the sample csv file is read correctly"""
        data = read_csv_file('data.csv')
        # make sure headers are correct
        for header in ["First Name", "Last Name", "Email", "Phone", "Credit Card", "SSN", "DOB", "City", "State"]:
            self.assertIn(header, data)
        # length of all lists should be the same as the length of the file minus the header row
        with open('data.csv', 'r') as f:
            lines = f.readlines()
        rows = len(lines) - 1
        for key in data:
            self.assertEqual(len(data[key]), rows)

    def test_email_domain_and_user_count_csv(self):
        """Try reading email domains from the csv file"""
        # read the csv file
        data = read_csv_file('data.csv')
        # check that is was read as expected
        expected = {'abc.com': 23, 'gmail.com': 17, 'hotmail.com': 18, 'outlook.com': 15,
                    'xyz.com': 8, 'yahoo.com': 14}
        results = email_domain_and_user_count(','.join(data['Email']))
        self.assertDictEqual(expected, results)

    def test_get_credit_card_type(self):
        # load data.csv file
        data = read_csv_file('data.csv')
        expected = {'Discover': 22, 'MasterCard': 18, 'American Express': 40, 'Visa': 20}
        results = get_credit_card_type(','.join(data['Credit Card']))
        self.assertEqual(expected, results)

    def test_get_ssn_state_prefix(self):
        """Check to make sure the correct number of prefixes and assignments are returned"""
        results = get_ssn_assignment_prefix()
        self.assertEqual(len(results), 755)
        # check total assignment counts
        assigned = set(results.values())
        # 50 states plus DC, PR
        # 'Enumeration at Entry', 'Territories', 'Railroad Board**', 'Not Issued'
        # Therefore expected total is 56
        self.assertEqual(len(assigned), 56)

    
        

       
    

    


if __name__ == '__main__':
    unittest.main()
