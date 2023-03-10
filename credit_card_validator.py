"""
ou and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with 4,5,6
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.
"""

import re

#method for validating credit card number
def is_valid_credit_card_number(cc_number):
    pattern = r'^[4-6][.,]?\d{3}(?:-?\d{4}){2}(?:-?\d{3,4})?$'
    if not re.match(pattern, cc_number):
        return False
    if re.search(r'(\d)\1{3,}', cc_number.replace('-', '')):
        return False
    return True

valid_data = ["4253625879615786","4424424424442444","5122-2368-7954-3214"]
invalid_data = ["42536258796157867","4424444424442444","44244x4424442444","5122-2368-7954 - 3214","0525362587961578"]

def test_is_valid_credit_card_number():
    for cc in valid_data:
        assert is_valid_credit_card_number(cc)
    for cc in invalid_data:
        assert not is_valid_credit_card_number(cc)

test_is_valid_credit_card_number()
print("All Test cases passed")