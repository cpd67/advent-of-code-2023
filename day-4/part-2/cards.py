# TODO clean this up & improve it
if __name__ == "__main__":
    with open("../scratchcards.txt") as scratchcards:
        copy_totals = {}
        for card_id, card in enumerate(scratchcards, start=1):
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
                if copy_totals.get(card_id) is None:
                    copy_totals[card_id] = 0
                copy_totals[card_id] += 1
                for _ in range(copy_totals[card_id]):
                    for i in range(card_id + 1, card_id + win_count + 1):
                        if copy_totals.get(i) is None:
                            copy_totals[i] = 0
                        copy_totals[i] += 1
            else:
                if copy_totals.get(card_id) is None:
                    copy_totals[card_id] = 1
                else:
                    copy_totals[card_id] += 1
            print(card_id, copy_totals[card_id])
        print(f"Done! The copy total is: {sum(copy_totals.values())}")