# %%


def parse_input(file: str) -> list[str]:
    with open(file, "r") as f:
        content = f.read().splitlines()
    return content


def find_coordinates(grid: list[str], character: str) -> list[tuple[int, int]]:
    coordinates = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == character:
                coordinates.append((x, y))
    return coordinates


def search_along(
    grid: list[str], start: tuple[int, int], along: tuple[int, int], length: int
) -> str:
    length_x = len(grid[0])
    length_y = len(grid)
    x, y = start
    dx, dy = along
    if not (
        0 <= x + (length - 1) * dx < length_x and 0 <= y + (length - 1) * dy < length_y
    ):
        return None
    # Remember, you traverse the grid as grid[y][x]
    return "".join([grid[y + i * dy][x + i * dx] for i in range(length)])


def part_one() -> int:
    grid = parse_input("input.txt")
    starting_coordinates = find_coordinates(grid, "X")
    # fmt: off
    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1,  0),          (1,  0), 
        (-1,  1), (0,  1), (1,  1),
    ]
    # fmt: on
    results = [
        search_along(grid, start, along, 4)
        for start in starting_coordinates
        for along in directions
    ]
    return results.count("XMAS")


def part_two() -> int:
    grid = parse_input("input.txt")
    starting_coordinates = find_coordinates(grid, "A")
    # directions = [
    #    (-1, -1),          (1, -1),
    #
    #    (-1,  1),          (1,  1),
    # ]
    count = 0
    for start in starting_coordinates:
        back_start = (start[0] - 1, start[1] - 1)
        if back_start[0] < 0 or back_start[1] < 0:
            continue
        if search_along(grid, back_start, (1, 1), 3) in ["MAS", "SAM"]:
            forward_start = (start[0] + 1, start[1] - 1)
            if search_along(grid, forward_start, (-1, 1), 3) in [
                "MAS",
                "SAM",
            ]:
                count += 1
    return count


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
