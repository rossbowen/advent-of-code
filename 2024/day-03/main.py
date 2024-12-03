# %%
import re


def parse_input(file: str) -> str:
    with open(file, "r") as f:
        content = f.read()
    return content


def part_one() -> int:
    lines = parse_input("input.txt")
    matches = re.findall(r"mul\((\d+),(\d+)\)", lines)
    return sum(int(x) * int(y) for x, y in matches)


def part_two() -> int:
    lines = parse_input("input.txt")
    matches = re.finditer(r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)", lines)
    is_enabled = True
    result = []
    for match in matches:
        command = match.group(0)
        if command == "do()":
            is_enabled = True
        elif command == "don't()":
            is_enabled = False
        elif is_enabled:
            x, y = match.groups()
            result.append(int(x) * int(y))
    return sum(result)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
