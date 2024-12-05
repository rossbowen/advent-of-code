# %%
import re


def parse_input(file: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    with open(file, "r") as f:
        rules, updates = f.read().split("\n\n")
    rules = [
        (int(rule[0]), int(rule[1])) for rule in re.findall(r"(\d+)\|(\d+)", rules)
    ]
    updates = [list(map(int, x.split(","))) for x in updates.split()]
    return rules, updates


def get_applicable_rules(
    rules: list[tuple[int, int]], pages: list[int]
) -> list[tuple[int, int]]:
    return [rule for rule in rules if rule[0] in pages and rule[1] in pages]


def has_correct_order(rules: list[tuple[int, int]], pages: list[int]) -> bool:
    return all([pages.index(rule[0]) < pages.index(rule[1]) for rule in rules])


def fix_order(rules: list[tuple[int, int]], pages: list[int]) -> list[int]:
    pages = pages.copy()
    for rule in rules:
        if pages.index(rule[0]) > pages.index(rule[1]):
            pages[pages.index(rule[0])] = rule[1]
            pages[pages.index(rule[1])] = rule[0]
    return pages


def get_middle_number(pages: list[int]) -> int:
    return pages[int((len(pages) - 1) / 2)]


def part_one() -> int:
    rules, updates = parse_input("input.txt")
    middle_numbers = []
    for update in updates:
        applicable_rules = get_applicable_rules(rules, update)
        if has_correct_order(applicable_rules, update):
            middle_numbers.append(get_middle_number(update))
    return sum(middle_numbers)


def part_two() -> int:
    rules, updates = parse_input("input.txt")
    middle_numbers = []
    for update in updates:
        applicable_rules = get_applicable_rules(rules, update)
        while not has_correct_order(applicable_rules, update):
            update = fix_order(applicable_rules, update)
            if has_correct_order(applicable_rules, update):
                middle_numbers.append(get_middle_number(update))
    return sum(middle_numbers)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
