# %%


def parse_input(file: str) -> list[str]:
    with open(file, "r") as f:
        content = f.read()
    return [int(x) for x in content]


def as_blocks(disk_map: list[int]) -> list[int | str]:
    blocks = []
    for idx, size in enumerate(disk_map):
        if idx % 2 == 0:
            blocks.extend([idx // 2] * size)
        else:
            blocks.extend(["."] * size)
    return blocks


def rearrange_blocks(blocks: list[int | str]) -> list[int | str]:
    file_ids = [b for b in blocks if b != "."]
    dots = [b for b in blocks if b == "."]
    return file_ids + dots


def checksum(blocks: list[int | str]) -> list[int | str]:
    return sum([x * y for x, y in enumerate(blocks) if y != "."])


def rearrange_blocks_as_whole_files(blocks: list[int | str]) -> list[int | str]:
    max_id = max([x for x in blocks if x != "."])

    for file_id in range(max_id, -1, -1):
        file_start = blocks.index(file_id)
        file_end = file_start
        while file_end < len(blocks) and blocks[file_end] == file_id:
            file_end += 1

        length = file_end - file_start

        dot_index = blocks.index(".")
        while dot_index < file_start:
            if (
                blocks[dot_index] == "."
                and dot_index + length <= file_start
                and all(b == "." for b in blocks[dot_index : dot_index + length])
            ):
                for k in range(length):
                    blocks[dot_index + k] = file_id
                for k in range(file_start, file_end):
                    blocks[k] = "."
                break
            dot_index += 1

    return blocks


def part_one() -> int:
    disk_map = parse_input("input.txt")
    blocks = rearrange_blocks(as_blocks(disk_map))
    return checksum(blocks)


def part_two() -> int:
    disk_map = parse_input("input.txt")
    blocks = rearrange_blocks_as_whole_files(as_blocks(disk_map))
    return checksum(blocks)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
