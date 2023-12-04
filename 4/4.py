import re


def part1():
    points: list[int] = []
    with open('4.in', 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()
            line = line[9:].strip()
            winning, card = line.split('|')
            win_nums = re.split(r'\s+', winning.strip())
            card_nums = re.split(r'\s+', card.strip())

            for c in card_nums:
                points.append(0)
                for w in win_nums:
                    if w == c:
                        points[i] = 1 if points[i] == 0 else points[i] * 2

        return sum(points)


def part2():
    cards: list[int] = [1] * 220
    total = 220
    with open('4.in', 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()
            line = line[9:].strip()
            winning, card = line.split('|')
            win_nums = re.split(r'\s+', winning.strip())
            card_nums = re.split(r'\s+', card.strip())

            for copy in range(0, cards[i]):
                c_total = 0
                for c in card_nums:
                    if c in win_nums:
                        c_total += 1

                        if i + c_total >= 220:
                            break
                        cards[i + c_total] += 1
                total += c_total

        return total


if __name__ == '__main__':
    print(part1())
    print(part2())
