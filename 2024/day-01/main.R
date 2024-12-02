# %%
library(readr)
library(stringr)
library(vctrs)

parse_input <- function(file) {
  content <- read_file(file)
  digits <- str_extract_all(content, "\\d+") |>
    unlist() |>
    vec_cast(integer())
  first_list <- digits[seq(1, length(digits), by = 2)]
  second_list <- digits[seq(2, length(digits), by = 2)]

  list(first_list = first_list, second_list = second_list)
}


# def part_one() -> int:
#     first_list, second_list = parse_input("input.txt")
#     first_sorted = sorted(first_list)
#     second_sorted = sorted(second_list)
#     result = [abs(a - b) for a, b in zip(first_sorted, second_sorted)]
#     return sum(result)


# def part_two() -> int:
#     first_list, second_list = parse_input("input.txt")
#     result = [x * second_list.count(x) for x in first_list]
#     return sum(result)


# if __name__ == "__main__":
#     print(f"Part one: {part_one()}")
#     print(f"Part two: {part_two()}")
