if __name__ == '__main__':
    with open('../list-of-games.txt') as games:
        power_sum = 0
        for game in games:
            fewest_cube_values = {'red': 0, 'blue': 0, 'green': 0}
            _, cube_subsets = game.split(':')
            for cube_subset in cube_subsets.split(';'):
                for cube in cube_subset.split(','):
                    cube_val, cube_name = cube.strip().split(' ')
                    # cube_val is a str, but we want to compare and store it as an
                    # int. We use the walrus operator to store the typecasted value
                    # and compare in one step.
                    if fewest_cube_values[cube_name] < (cube_val := int(cube_val)):
                        fewest_cube_values[cube_name] = cube_val
            # At this point, we should have the fewest number of cubes needed in order
            # to play this game. Anything lower and we'd have an invalid game.
            # Increment the power sum.
            power_sum += (fewest_cube_values['red'] * fewest_cube_values['blue'] * fewest_cube_values['green'])
        print(f"Done! The sum is: {power_sum}")
