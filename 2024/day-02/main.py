# %%


def parse_input(file: str) -> list[list[int]]:
    with open(file, "r") as f:
        content = [list(map(int, line.split())) for line in f]
    return content


def is_safe(report: list[int]) -> bool:
    if report == sorted(report) or report == sorted(report, reverse=True):
        if all(
            1 <= abs(report[k] - report[k + 1]) <= 3 for k in range(len(report) - 1)
        ):
            return True
    return False


def is_safe_with_dampener(report: list[int]) -> bool:
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True
    return False


def part_one() -> int:
    reports = parse_input("input.txt")
    return sum(map(is_safe, reports))


def part_two() -> int:
    reports = parse_input("input.txt")
    return sum(map(is_safe_with_dampener, reports))


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
