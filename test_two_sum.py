from two_sum import two_sum

def test_exists():
    two_sum

def test_empty_list():
    assert two_sum([], 9) == "No solution"

def test_one_value():
    assert two_sum([1], 9) == "No solution"

def test_cannot_equal_target():
    assert two_sum([1, 2, 3], 20) == "No solution"

def test_correct_sum_first_two_idx():
    assert two_sum([1, 2], 3) == [0, 1]

def test_correct_sum_0th_and_random_idx():
    assert two_sum([1, 2, 3], 4) == [0, 2]

def test_correct_sum_misc_idx():
    assert two_sum([1, 2, 3, 4, 5, 6], 8) == [2, 4]