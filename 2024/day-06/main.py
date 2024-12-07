# %%


def parse_input(file: str) -> list[str]:
    with open(file, "r") as f:
        content = f.read().splitlines()
    return content


def find_start_coordinates(grid: list[str]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "^":
                return (x, y)


def is_in_bounds(grid: list[str], x: int, y: int) -> bool:
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def place_obstruction(grid: list[str], x: int, y: int) -> list[str]:
    modified = [list(row) for row in grid]
    modified[y][x] = "#"
    return ["".join(row) for row in modified]


def guard_stuck_in_loop(grid: list[str], directions: list[tuple[int, int]]) -> bool:
    x, y = find_start_coordinates(grid)
    direction = 0

    visited_states = set()
    visited_states.add((x, y, direction))

    while True:
        dx, dy = directions[direction]
        nx = x + dx
        ny = y + dy

        if not is_in_bounds(grid, nx, ny):
            return False

        if grid[ny][nx] == "#":
            direction = (direction + 1) % 4
        else:
            x, y = nx, ny

        state = (x, y, direction)
        if state in visited_states:
            return True
        visited_states.add(state)


def part_one() -> int:
    grid = parse_input("input.txt")
    x, y = find_start_coordinates(grid)
    direction = 0
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    visited = set()
    visited.add((x, y))

    while True:
        dx, dy = directions[direction]
        nx = x + dx
        ny = y + dy

        if not is_in_bounds(grid, nx, ny):
            break

        if grid[ny][nx] == "#":
            direction = (direction + 1) % 4
        else:
            x, y = nx, ny
            visited.add((x, y))

    return len(visited)


def part_two() -> int:
    grid = parse_input("input.txt")
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    start = find_start_coordinates(grid)

    candidates = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "." and (x, y) != start:
                candidates.append((x, y))

    loops = 0
    for cx, cy in candidates:
        modified_grid = place_obstruction(grid, cx, cy)

        if guard_stuck_in_loop(modified_grid, directions):
            loops += 1

    return loops


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
