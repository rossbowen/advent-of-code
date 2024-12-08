# %%


def parse_input(file: str) -> list[str]:
    with open(file, "r") as f:
        content = f.read().splitlines()
    return content


def find_antennas_by_frequency(grid: list[str]) -> dict[str, list[tuple[int, int]]]:
    frequency_map = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != ".":
                if char not in frequency_map:
                    frequency_map[char] = []
                frequency_map[char].append((x, y))
    return frequency_map


def calculate_antinodes(
    p1: tuple[int, int], p2: tuple[int, int]
) -> list[tuple[int, int]]:
    x1, y1 = p1
    x2, y2 = p2
    antinode1 = (2 * x1 - x2, 2 * y1 - y2)
    antinode2 = (2 * x2 - x1, 2 * y2 - y1)
    return [antinode1, antinode2]


def calculate_resonant_antinodes(
    grid: list[str], p1: tuple[int, int], p2: tuple[int, int]
) -> set[tuple[int, int]]:
    length_y = len(grid)
    length_x = len(grid[0])
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    antinodes = set()

    nx, ny = x1, y1
    while 0 <= nx < length_x and 0 <= ny < length_y:
        antinodes.add((nx, ny))
        nx -= dx
        ny -= dy

    nx, ny = x1, y1
    while 0 <= nx < length_x and 0 <= ny < length_y:
        antinodes.add((nx, ny))
        nx += dx
        ny += dy

    return antinodes


def part_one() -> int:
    grid = parse_input("input.txt")
    frequency_map = find_antennas_by_frequency(grid)
    antinodes = set()

    for freq, coords in frequency_map.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                p1 = coords[i]
                p2 = coords[j]
                for antinode in calculate_antinodes(p1, p2):
                    if 0 <= antinode[0] < len(grid[0]) and 0 <= antinode[1] < len(grid):
                        antinodes.add(antinode)

    return len(antinodes)


def part_two() -> int:
    grid = parse_input("input.txt")
    frequency_map = find_antennas_by_frequency(grid)
    antinodes = set()

    for freq, coords in frequency_map.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                p1 = coords[i]
                p2 = coords[j]
                new_antinodes = calculate_resonant_antinodes(grid, p1, p2)
                antinodes.update(new_antinodes)

        for coord in coords:
            antinodes.add(coord)

    return len(antinodes)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
