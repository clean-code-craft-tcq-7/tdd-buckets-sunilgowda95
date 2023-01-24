from current_range import get_range

# test range : `4,5`. assert output to be `4-5, 2`
assert get_range([4,5]) == "Range, Readings\n4-5, 2"

assert get_range([4,5,5,6]) == "Range, Readings\n4-6, 4"

assert get_range([4,5,5,6,9,10]) == "Range, Readings\n4-6, 4\n9-10, 2"
