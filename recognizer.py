# Ju Pan

import re

def is_phone_number(input_string):
    num_regex = re.compile(r"(^[(]?\d{3}[)]?[-]?\d{3}[-]?\d{4}$)")
    if not num_regex.match(input_string):
        return False
    return True

def is_email_address(input_string):
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not email_regex.match(input_string):
        return False
    return True
