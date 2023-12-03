import re


# Note that we may have overlapping matches with this regex, so we use
# a lookahead to deal with them
digit_regex = re.compile('(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))')


# Lookup dict that maps the digit name to the actual digit
name_to_digit_lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
                        }


def get_calibration_value(line):
    """
    Given a line of text from our calibration document, find the calibration value.
    """
    digits = digit_regex.findall(line)
    # findall() gives us a list of matches, which will be a list of
    # either digit strings, or the name of the digit.
    # We need to get the first & last matches and process them accordingly.
    first_digit = digits[0]
    last_digit = digits[-1]
    if not first_digit.isdigit():
        first_digit = name_to_digit_lookup[first_digit]
    if not last_digit.isdigit():
        last_digit = name_to_digit_lookup[last_digit]
    return int(first_digit + last_digit)


if __name__ == '__main__':
    with open('../calibration-document.txt') as calibration_doc:
        calibration_sum = 0
        for line in calibration_doc:
            calibration_value = get_calibration_value(line)
            calibration_sum += calibration_value
        print(f'Done! Calibration sum: {calibration_sum}')
