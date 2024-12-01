# %%


def parse_input(file: str) -> tuple[list[int], list[int]]:
    with open(file, "r") as f:
        content = f.read()

    digits = [int(x) for x in content.split()]
    first_list = digits[::2]
    second_list = digits[1::2]

    return first_list, second_list


def part_one() -> int:
    first_list, second_list = parse_input("input.txt")
    first_sorted = sorted(first_list)
    second_sorted = sorted(second_list)
    result = [abs(a - b) for a, b in zip(first_sorted, second_sorted)]
    return sum(result)


def part_two() -> int:
    first_list, second_list = parse_input("input.txt")
    result = [x * second_list.count(x) for x in first_list]
    return sum(result)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
