# %%
from collections import deque


def parse_input(file: str) -> list[list[int]]:
    with open(file, "r") as f:
        content = f.read().splitlines()
    return [[int(x) for x in line] for line in content]


def find_coordinates(grid: list[list[int]], value: int) -> list[tuple[int, int]]:
    coordinates = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == value:
                coordinates.append((x, y))
    return coordinates


def get_neighbours(grid: list[list[int]], x: int, y: int) -> list[tuple[int, int]]:
    length_y = len(grid)
    length_x = len(grid[0])
    for nx, ny in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
        if 0 <= nx < length_x and 0 <= ny < length_y:
            yield nx, ny


def nines_from_trailhead(grid: list[list[int]], start: tuple[int, int]) -> int:
    queue = deque([start])
    visited = set([start])
    nines = set()

    while queue:
        x, y = queue.popleft()
        current_height = grid[y][x]
        if current_height == 9:
            nines.add((x, y))
            continue

        for nx, ny in get_neighbours(grid, x, y):
            if (nx, ny) not in visited:
                if grid[ny][nx] == current_height + 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return len(nines)


def compute_trail_ratings(grid: list[list[int]]) -> dict[tuple[int, int], int]:
    rows, cols = len(grid), len(grid[0])
    ratings = {}

    nines = find_coordinates(grid, 9)
    for nine in nines:
        ratings[nine] = 1

    for height in range(8, -1, -1):
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == height:
                    ratings[(x, y)] = sum(
                        ratings.get((nx, ny), 0)
                        for nx, ny in get_neighbours(grid, x, y)
                        if grid[ny][nx] == height + 1
                    )

    return ratings


def part_one() -> int:
    grid = parse_input("input.txt")
    trailheads = find_coordinates(grid, 0)

    total_score = 0
    for head in trailheads:
        score = nines_from_trailhead(grid, head)
        total_score += score

    return total_score


def part_two() -> int:
    grid = parse_input("input.txt")
    trailheads = find_coordinates(grid, 0)

    ratings = compute_trail_ratings(grid)

    return sum(ratings.get(head, 0) for head in trailheads)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
