
if __name__ == "__main__":
    with open("../list-of-games.txt") as games:
        max_red = 12
        max_green = 13
        max_blue = 14
        for game in games:
            if game != "":
                print(game)