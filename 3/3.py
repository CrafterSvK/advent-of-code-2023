def check_around(data: list[str], row: int, col: int, width: int):
    if width < 1:
        return False

    for l in range(row - 1, row + 2):
        if 0 > l:
            continue
        if l > 139:
            break

        for c in range(col - 1, col + width + 1):
            if 0 > c:
                continue
            if c > 139:
                break

            if not data[l][c].isdigit() and data[l][c] != '.':
                return True

    return False


def part1():
    parts = []
    data: list[str] = []
    with open('3.in', 'r') as f:
        for line in f:
            data.append(line)

        for row, line in enumerate(data):
            line = line.strip()
            col = 0
            number_start_col = None

            while col < 140:
                if data[row][col].isdigit() and number_start_col is None:
                    number_start_col = col

                if data[row][col + 1].isdigit():
                    col += 1
                else:
                    if line[col].isdigit() and check_around(data, row, number_start_col, col - number_start_col + 1):
                        part = data[row][number_start_col:col + 1]
                        parts.append(int(part))

                    col += 1
                    number_start_col = None

    return sum(parts)


def find_number_here(data: list[str], row: int, col: int) -> int:
    if not (0 <= row < len(data)) or not (0 <= col < len(data[row])):
        raise Exception()

    start = None

    while col >= 0 and data[row][col].isdigit():
        start = col
        col -= 1

    col = start

    while col < len(data[row]) and data[row][col].isdigit():
        col += 1

    if start is not None:
        return int(data[row][start:col])


def get_numbers_around(data: list[str], row: int, col: int) -> int | None:
    numbers = []
    for r in range(row - 1, row + 2):
        if 0 > r:
            continue
        if r > 139:
            break

        found = False
        for c in range(col - 1, col + 2):
            if c < 0:
                continue
            if c > 139:
                break

            if found:
                if not data[r][c].isdigit():
                    found = False
                continue

            if data[r][c].isdigit():
                numbers.append(find_number_here(data, r, c))
                found = True

    if len(numbers) == 2:
        first, second = numbers
        return first * second


def part2():
    gears = []
    data: list[str] = []
    with open('3.in', 'r') as f:
        for line in f:
            data.append(line)

        for row, line in enumerate(data):
            line = line.strip()
            for col, c in enumerate(line):
                if c == '*':
                    if gear := get_numbers_around(data, row, col):
                        gears.append(gear)

    return sum(gears)


if __name__ == "__main__":
    print(part1())
    print(part2())
