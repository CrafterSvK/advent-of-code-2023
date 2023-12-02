def part1():
    maxes = dict(red=12, green=13, blue=14)
    possible_games = []

    with open('2.in', 'r') as f:
        for i, line in enumerate(f, start=1):
            sets = line.split(':')[1].strip()

            possible = True
            for single_set in sets.split(';'):
                for comb in single_set.strip().split(','):
                    count, color = comb.strip().split(' ')
                    if int(count) > maxes[color]:
                        possible = False
                        break

            if possible:
                possible_games.append(i)

    return sum(possible_games)


def part2():
    powers = []
    with open('2.in', 'r') as f:
        for i, line in enumerate(f, start=1):
            mins = dict(red=0, blue=0, green=0)
            sets = line.split(':')[1].strip()

            for single_set in sets.split(';'):
                for comb in single_set.strip().split(','):
                    count, color = comb.strip().split(' ')

                    if int(count) > mins[color]:
                        mins[color] = int(count)

            powers.append(mins['red'] * mins['blue'] * mins['green'])

    return sum(powers)


if __name__ == '__main__':
    print(part1())
    print(part2())
