TEST_CASES = [
    [[3, 4, 8, 2, 7, 1, 6, 5], [4, 2, 5, 1, 6, 8, 3, 7]],
    [[1, 2, 3, 4, 5, 6, 7, 8], [2, 7, 5, 8, 4, 1, 6, 3]],
    [[4, 1, 2, 3, 0], [3, 4, 0, 2, 1]],
    [[4, 1, 2, 3, 0], [3, 4, 0, 1, 2]],
    [[1, 2, 3, 4, 5, 6], [2, 6, 4, 1, 3, 5]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 7, 5, 8, 4, 1, 6, 3, 14, 13, 10, 11, 12, 9]]
]
TEST_ANS = [
    [[4, 1, 5, 6, 2, 8, 7, 3], [2, 8, 7, 3, 1, 5, 6, 4]],
    [[2, 1, 6, 7, 5, 3, 8, 4], [6, 7, 2, 1, 8, 4, 5, 3]],
    [[3, 0, 4, 2, 1], [2, 1, 3, 0, 4]],
    [[3, 4, 1, 0, 2], [1, 3, 4, 2, 0]],
]


def cx2_crossover(parrent_one: list, parrent_two: list) -> list:
    length = len(parrent_one)
    assert len(parrent_one) == len(parrent_two)
    child_one = [None] * length
    child_two = [None] * length
    value_index = 0

    def get_next(parrent_one, parrent_two, value_index):
        return parrent_one.index(parrent_two[value_index])
    for index in range(length):
        if parrent_two[value_index] in child_one:
            if sorted(child_one[:index]) == sorted(child_one[:index]):
                for index_two in range(length):
                    if parrent_two[index_two] not in child_one:
                        value_index = index_two
                        break
            else:
                while parrent_two[value_index] in child_one:
                    value_index = get_next(parrent_one, parrent_two, value_index)
        # assign child one
        child_one[index] = parrent_two[value_index]
        # find next value index for child two
        value_index = get_next(parrent_one, parrent_two, value_index)
        # assign child two
        child_two[index] = parrent_two[value_index]
        # update value index
        value_index = get_next(parrent_one, parrent_two, value_index)

    return child_one, child_two


def run_test():
    for index in range(len(TEST_CASES)):
        case = TEST_CASES[index]
        ans = TEST_ANS[index]
        assert ans == case


if __name__ == "__main__":
    for case in TEST_CASES:
        child_one, child_two = cx2_crossover(case[0], case[1])
        assert sorted(child_one) == sorted(child_two)
        print(child_one, child_two)
