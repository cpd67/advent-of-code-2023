if __name__ == "__main__":
    with open("../scratchcards.txt") as scratchcards:
        point_total = 0
        for card in scratchcards:
            winning_numbers, our_numbers = card.strip().split("|")
            _, numbers = winning_numbers.strip().split(":")
            # Create a lookup table for the winning numbers
            # so we can figure out which of our numbers won
            winning_number_lookup = {
                number: True
                for number in numbers.strip().split(" ")
                if number != ""
            }
            win_count = 0
            for number in our_numbers.strip().split(" "):
                if winning_number_lookup.get(number.strip(), False):
                    win_count += 1
            if win_count > 0:
                point_total += 2**(win_count - 1)
        print(f"Done! The point total is: {point_total}")