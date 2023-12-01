def get_first_last_number(line: str):
    line = ''.join(filter(lambda i: i.isdigit(), line))
    return int(f'{line[0]}{line[-1]}')


num_dict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

test_lines = [
    "xtwone3four"
]


def part1():
    num = []
    with open('./1/1.in', 'r') as f:
        for line in f:
            num.append(get_first_last_number(line))

    return sum(num)


def part2():
    num = []
    with open('./1/1.in', 'r') as f:
        for i, line in enumerate(f):
            num.append("")
            for j, c in enumerate(line):
                if c.isdigit():
                    num[i] += c

                for k, num_str in enumerate(num_dict, start=1):
                    if line[j:].startswith(num_str):
                        num[i] += str(k)

            num[i] = int(f'{num[i][0]}{num[i][-1]}')

    return sum(num)


if __name__ == '__main__':
    print(part1())
    print(part2())