import re

if __name__ == '__main__':
    calibration_doc = open('../calibration-document.txt')
    digit_regex = re.compile('[0-9]')
    calibration_sum = 0
    for line in calibration_doc:
        digits = digit_regex.findall(line)
        # findall() gives us a list of matches, which will be a list of 
        # digit strings. We want the first and last matches.
        first_digit = digits[0]
        last_digit = digits[-1]
        calibration_value = int(first_digit + last_digit)
        calibration_sum += calibration_value
    print(f'Done! Calibration sum: {calibration_sum}')
