import re


digit_regex = re.compile('[0-9]')


def get_calibration_value(line):
    """
    Given a line of text from our calibration document, find the calibration value.
    """
    # findall() gives us a list of matches, which will be a list of
    # digit strings. We want the first and last matches.
    digits = digit_regex.findall(line)
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)


if __name__ == '__main__':
    with open('../calibration-document.txt') as calibration_doc:
        calibration_sum = 0
        for line in calibration_doc:
            calibration_value = get_calibration_value(line)
            calibration_sum += calibration_value
        print(f'Done! Calibration sum: {calibration_sum}')
