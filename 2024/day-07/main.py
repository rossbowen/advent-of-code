# %%
from functools import reduce
from itertools import product


def parse_input(file: str) -> list[tuple[int, list[int]]]:
    with open(file, "r") as f:
        result = [
            (
                int(line.split(":")[0].strip()),
                [int(v) for v in line.split(":")[1].strip().split()],
            )
            for line in f
            if line.strip()
        ]

    return result


def can_produce_target(target: int, nums: list[int]) -> bool:
    for ops in product([0, 1], repeat=len(nums) - 1):
        ops_iter = iter(ops)

        def apply_op(acc, x):
            op = next(ops_iter)
            return acc + x if op == 0 else acc * x

        result = reduce(apply_op, nums[1:], nums[0])
        if result == target:
            return True
    return False


def can_produce_target_with_concatenation(target: int, nums: list[int]) -> bool:
    for ops in product([0, 1, 2], repeat=len(nums) - 1):
        ops_iter = iter(ops)

        def apply_op(acc, x):
            op = next(ops_iter)
            if op == 0:
                return acc + x
            elif op == 1:
                return acc * x
            else:
                return int(str(acc) + str(x))

        result = reduce(apply_op, nums[1:], nums[0])
        if result == target:
            return True
    return False


def part_one() -> int:
    lines = parse_input("input.txt")
    result = [target for target, nums in lines if can_produce_target(target, nums)]
    return sum(result)


def part_two() -> int:
    lines = parse_input("input.txt")
    result = [
        target
        for target, nums in lines
        if can_produce_target_with_concatenation(target, nums)
    ]
    return sum(result)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
