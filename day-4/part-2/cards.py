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
        num_card_copies = {}
        for card_id, card in enumerate(scratchcards, start=1):
            if num_card_copies.get(card_id) is None:
                num_card_copies[card_id] = 1
            win_count = get_win_count(card)
            if win_count > 0:
                for i in range(card_id + 1, card_id + win_count + 1):
                    if num_card_copies.get(i) is None:
                        num_card_copies[i] = 1
                    num_card_copies[i] += num_card_copies[card_id]
        print(f"Done! The number of scratchcard copies is: {sum(num_card_copies.values())}")