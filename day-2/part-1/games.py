max_cube_values = {'red': 12, 'green': 13, 'blue': 14}

class InvalidCubeConfiguration(Exception):
    pass


def check_cube_constraint(cube_str):
    """
    Check that a cube value is at or below the max value for that cube.
    """
    cube_value, cube_name = cube_str.split(' ')
    if int(cube_value) > max_cube_values[cube_name]:
        raise InvalidCubeConfiguration()


if __name__ == "__main__":
    with open("../list-of-games.txt") as games:
        id_sum = 0
        for game in games:
            game_id, cube_subsets = game.split(":")
            try:
                for cube_subset in cube_subsets.split(';'):
                    for cube in cube_subset.split(','):
                        check_cube_constraint(cube.strip())
                # All games are good, this is one of the IDs to sum
                id_sum += int(game_id.split(' ')[1])
            except InvalidCubeConfiguration:
                pass
        print(f"Done! The sum is: {id_sum}")
