def test():
    from current_range import get_range, sort_samples
    # sort_samples
    assert sort_samples([3,2,1]) == [1,2,3]
    assert sort_samples([4,5]) == [4,5]
    assert sort_samples([415]) == [415]

    # get_range
    assert get_range([4,5]) == "Range, Readings\n4-5, 2"
    assert get_range([4,5,5,6]) == "Range, Readings\n4-6, 4"
    assert get_range([4,5,5,6,9,10]) == "Range, Readings\n4-6, 4\n9-10, 2"
    assert get_range([]) == "Range, Readings"
    assert get_range([1, 5, 9]) == "Range, Readings\n1-1, 1\n5-5, 1\n9-9, 1"
    assert get_range([1, 5, 11,12]) == "Range, Readings\n1-1, 1\n5-5, 1\n11-12, 2"
    assert get_range([5,4,5,35,85,6,10,9]) == "Range, Readings\n4-6, 4\n9-10, 2\n35-35, 1\n85-85, 1"