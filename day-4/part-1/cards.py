def get_win_count(scratchcard):
    """
    Determine how many of our scratchcard numbers are winning numbers.
    """
    winning_numbers, our_numbers = scratchcard.strip().split("|")
    _, numbers = winning_numbers.strip().split(":")
    # Create a lookup table for the winning numbers
    # so we can figure out which of our numbers won
    winning_number_lookup = {
        number: True
        for number in winning_numbers.strip().split(" ")
        if number != ""
    }
    win_count = 0
    for number in our_numbers.strip().split(" "):
        if winning_number_lookup.get(number.strip(), False):
            win_count += 1
    return win_count


if __name__ == "__main__":
    with open("../scratchcards.txt") as scratchcards:
        point_total = 0
        for card in scratchcards:
            win_count = get_win_count(card)
            if win_count > 0:
                point_total += 2**(win_count - 1)
        print(f"Done! The point total is: {point_total}")