"""COMP-410 Spring 2023 Class Project"""
import requests
import re
import csv


def add_two_numbers(num1, num2):
    """Adds two numbers together"""
    return num1 + num2

def convert_text_numbers_to_integers(text_numbers:str) -> list:
    """Convert comma separated list of numbhers zero, one, two, three, four, five, six, 
    seven, eight, nine to integers"""
    text_numbers = text_numbers.split(',')
    numbers = []
    for number in text_numbers:
        number = number.strip()
        if number == 'zero':
            numbers.append(0)
        elif number == 'one':
            numbers.append(1)
        elif number == 'two':
            numbers.append(2)
        elif number == 'three':
            numbers.append(3)
        elif number == 'four':
            numbers.append(4)
        elif number == 'five':
            numbers.append(5)
        elif number == 'six':
            numbers.append(6)
        elif number == 'seven':
            numbers.append(7)
        elif number == 'eight':
            numbers.append(8)
        elif number == 'nine':
            numbers.append(9)
        else:
            raise ValueError(f'Unknown number {number}')
    return numbers


def convert_text_to_digits_example(text: str) -> list:
    """Converts a comma seperated list of text digits to integers"""
    text_digits = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                   'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    results = []
    for digit in text.split(','):
        digit = digit.strip()
        if digit in text_digits:
            results.append(text_digits[digit])
        else:
            raise ValueError('Invalid digit: ' + digit)

    return results


def email_domain_and_user_count(string_of_emails):
    dict_of_emails_and_users_count = {}
    seen_emails = set()
    if not string_of_emails:
        return dict_of_emails_and_users_count
    email_list = re.findall(r'[\w\.-]+@[\w\.-]+', string_of_emails)
    for email in email_list:
        if not re.match(r'[\w\.-]+@[\w\.-]+', email):
            raise ValueError(f"{email} is not a valid email address")
        email_domain = email.split('@')[1]
        if email not in seen_emails:
            seen_emails.add(email)
            if email_domain not in dict_of_emails_and_users_count:
                dict_of_emails_and_users_count[email_domain] = 1
            else:
                dict_of_emails_and_users_count[email_domain] += 1
    
    return dict(sorted(dict_of_emails_and_users_count.items()))

def show_aggie_pride():
    """Show Aggie Pride"""
    return 'Aggie Pride - Worldwide'


def reverse_list(input_list) -> list:
    """Returns a list in reverse order"""
    return input_list[::-1]

def get_area_codes() -> dict:
    """Returns a dict of known area codes"""
    # Get the area code information from NANPA
    url = requests.get('https://nationalnanpa.com/nanp1/npa_report.csv', timeout=10)
    area_codes = {}
    for line in url.text.split('\n'):
        # skip the header lines
        if line.startswith('NPA') or line.startswith('File Date') or not line:
            continue
        ac_info = line.split(',')
        area_codes[ac_info[0]] = ac_info[8]
    return area_codes


def area_code_lookup(phone_nums:str) -> dict:
    """Returns a dict of area codes and corresponding state"""
    # optimize for speed by getting the area codes once instead of calling for each num in phone_list
    ac_dict = get_area_codes()
    phone_list = sorted(phone_nums.replace(" ", "").split(","))
    output_dict = {}
    for num in phone_list:
        area_code = num[0:3]
        if bool(re.match(r"(\d{3}-\d{3}-\d{4})",num)) & (int(area_code) > 200):
            output_dict[int(area_code)] = ac_dict[area_code]
        else:
            raise ValueError('Invalid phone number: ' + num)
    return output_dict


def get_state_abbrev() -> dict:
    """Returns a dict of state abbreviations and corresponding states"""
    return {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "District of Columbia": "DC",
        "American Samoa": "AS",
        "Guam": "GU",
        "Northern Mariana Islands": "MP",
        "Puerto Rico": "PR",
        "United States Minor Outlying Islands": "UM",
        "U.S. Virgin Islands": "VI"
    }


def get_state_abbrev_freq(text_states: str) -> dict:
    state_to_abb_dict = get_state_abbrev()
    states = [x.strip() for x in text_states.split(",")]
    state_freq_dict = {}
    
    for state in states:
        #check for valid state names
        if state in state_to_abb_dict:
            #check if state has already been added to abbreviation frequency dict
            if state_to_abb_dict[state] in state_freq_dict:
                state_freq_dict[state_to_abb_dict[state]] += 1
            #if not, add it
            else:
                state_freq_dict[state_to_abb_dict[state]] = 1
        #If invalid state name, raise ValueError
        else:
            raise ValueError('Invalid State: ' + state) 
    return dict(sorted(state_freq_dict.items()))


def read_csv_file(csv_file: str) -> dict:
    """Reads a csv file and returns a dict of lists for each row
       For example:
            {'First Name': ['John', 'Jane', 'Joe'], 'Last Name': ['Smith', 'Doe', 'Rogers']}
    """
    if not csv_file:
        return {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # get the header row
        header = next(reader)
        # get the rest of the rows
        rows = [row for row in reader]
    # return a dict of lists with key equal to the header and value equal to the list of values
    return {header[i]: [row[i] for row in rows] for i in range(len(header))}


def get_ssn_assignment_prefix():
    """Returns a dict of SSN prefixes and their corresponding states.  If a state has multiple prefixes
       assigned, there will be multiple entries.

       For example:
          {4: 'Maine', 5: 'Maine', ..., 232: 'North Carolina', 233: 'West Virginia', 234: 'West Virginia', ...}
    """
    ssn_prefix = {}
    with open('ssn.txt') as f:
        for line in f:
            # treat a # as a comment
            if line.startswith('#'):
                continue
            # if there is a dash in the line, split it and add the range to the dict
            elif '-' in line:
                ls = line.strip().split('\t')
                # find the start and end of the range such as 4-7
                start, end = ls[0].split('-')
                # add an entry for each assignment in the range
                for i in range(int(start), int(end) + 1):
                    ssn_prefix[i] = ls[1]
            # handle multiple ssn values comma separated
            elif ',' in line:
                ls = line.strip().split('\t')
                # handle multiple individual values such as 525,585
                for i in ls[0].split(','):
                    ssn_prefix[int(i)] = ls[1]
            # single ssn prefix such as 232
            else:
                ls = line.strip().split('\t')
                ssn_prefix[int(ls[0])] = ls[1]
    return ssn_prefix


def get_credit_card_type(text: str) -> dict:
    """Returns a dict of credit card types and their counts"""
    # If text is empty, nothing to do
    if not text:
        return {}

    # Create a conversion dictionary
    conversion = {'4': 'Visa', '5': 'MasterCard', '3': 'American Express', '6': 'Discover'}

    results = {}
    for t in text.split(','):
        if t.strip()[0] in conversion:
            card_type = conversion[t.strip()[0]]
            if card_type in results:
                results[card_type] += 1
            else:
                results[card_type] = 1
        else:
            raise ValueError(f'Invalid credit card number: {t.strip()}')
    return results


def area_code_prefixes() -> list:
    """Returns a list of area code prefixes that do not belong to the US and its territories"""

    state_abbrev = get_state_abbrev() # get a dict of abbreviations
    ac_dict = get_area_codes() # get a dict of area codes and their abbreviations
    data = read_csv_file('data.csv') # read the data from the data.csv file
    phone_nums_dict = data['Phone'] # get a list of phone numbers
    phone_nums_list = phone_nums_dict # does not really make any difference, I could have kept 'phone_nums_dict', I did it just for name sake
    output_list = [] # create an empty list
    for num in phone_nums_list:
        m = re.match(r"(\d{3})-\d{3}-\d{4}", num)
        # if a valid phone number is found, get the area code prefix
        if m:
            area_code = m.group(1) # get the area code prefix from the phone numbers in phone_nums_list
            if int(area_code) > 200 and ac_dict[area_code] not in state_abbrev.values():
                output_list.append(int(area_code))

    return output_list


if __name__ == '__main__':
    print(show_aggie_pride(), end='\n\n')

    print(area_code_prefixes())

    # read the data file
    csv_data = read_csv_file('data.csv')

    # Summarize the credit card types
    print('Credit Card Types')
    print(get_credit_card_type(','.join(csv_data['Credit Card'])))
    print()

    # Summarize the email domains
    print('Email Domains')
    print(email_domain_and_user_count(','.join(csv_data['Email'])))
    print()
