from current_range import get_range

# test range : `4,5`. assert output to be `4-5, 2`
assert get_range([4,5]) == "4-5, 2"

assert get_range([4,5,5,6]) == "4-6, 4"