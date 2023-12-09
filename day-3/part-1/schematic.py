def is_special_char_adjacent(adjacent_chars):
    """
    Determine if there are any special characters adjacent to a 
    possible part number.
    """
    for adj_char in adjacent_chars:
        if not adj_char.isdigit() and adj_char != '.':
            return True
    return False


with open('../engine-schematic.txt') as schematic:
    schematic_lines = list(schematic)
    total_line_count = len(schematic_lines)
    part_number_sum = 0
    for line_idx, schematic_line in enumerate(schematic_lines):
        # Strip whitespace from the line, keep track of the length of the line
        # and the previous & next line indexes, as well as the part number digits
        # and adjacent chars.
        schematic_line = schematic_line.strip()
        schematic_line_length = len(schematic_line)
        prev_line_idx = line_idx - 1
        next_line_idx = line_idx + 1
        possible_part_number = ''
        adjacent_chars = ''
        for char_idx, char in enumerate(schematic_line):
            if char.isdigit():
                # Append the char to our current possible part number
                possible_part_number += char
            if (not char.isdigit() or char == '.' or char_idx == (schematic_line_length - 1)) and possible_part_number:
                # We've found a full possible part number.
                # Check adjacent characters and see if any of them
                # are special characters.
                prev_char_idx = (char_idx - len(possible_part_number)) - 1
                next_char_idx = char_idx + 1
                if prev_char_idx < 0:
                    prev_char_idx = 0
                if prev_line_idx >= 0:
                    adj_prev_line_chars = schematic_lines[prev_line_idx][prev_char_idx:next_char_idx] 
                    adjacent_chars += adj_prev_line_chars
                if prev_char_idx >= 0:
                    prev_char = schematic_line[prev_char_idx]
                    adjacent_chars += prev_char
                adjacent_chars += char
                if next_line_idx <= total_line_count - 1:
                    adj_next_line_chars = schematic_lines[next_line_idx][prev_char_idx:next_char_idx]
                    adjacent_chars += adj_next_line_chars

                if is_special_char_adjacent(adjacent_chars):
                    part_number_sum += int(possible_part_number)

                possible_part_number = ''
                adjacent_chars = ''
    print(f'Done! The part number sum is: {part_number_sum}')