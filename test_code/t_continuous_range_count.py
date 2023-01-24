def test_get_continuous_range_and_count():
    from continuous_range_count import get_continuous_range_and_count
    assert get_continuous_range_and_count([5,4,5,35,85,6,10,9]) == \
        {'5-5': 2, '4-5': 3, '35-35': 1, '85-85': 1, '6-6': 1, '10-10': 1, '9-9': 1}
    assert get_continuous_range_and_count([0]) == {'0-0': 1}
    assert get_continuous_range_and_count([0,1]) == {'0-1': 2}
    assert get_continuous_range_and_count([0,0,0]) == {'0-0': 3}

def test_get_continuous_count():
    from continuous_range_count import get_continuous_count
    assert get_continuous_count([11,12], [[11,12]]) == {'11-12': 2}
    assert get_continuous_count([111], [[111,111]]) == {'111-111': 1}
    assert get_continuous_count([15,16,18,26,27], [[15,16],[18,18],[26,27]]) == \
        {'15-16': 2,'18-18':1,'26-27':2}

def test_get_count_for_range():
    from continuous_range_count import get_count_for_range
    assert get_count_for_range([2,5,8,9],6,2) == 2
    assert get_count_for_range([2,5,8,9],16,10) == 0
    assert get_count_for_range([2],16,0) == 1
    
def test_in_limits():
    from continuous_range_count import in_limits
    assert in_limits(2,3,1) == True
    assert in_limits(515,63,48) == False
    assert in_limits(12,26,14) == False

def test_get_key():    
    from continuous_range_count import get_key
    assert get_key([0,0]) == "0-0"
    assert get_key([5,60]) == "5-60"

def test_get_continuous_range():
    from continuous_range_count import get_continuous_range
    assert get_continuous_range([2,5,6,8]) == [[2,2],[5,6],[8,8]]
    assert get_continuous_range([8]) == [[8,8]]
    assert get_continuous_range([14,14,14]) == [[14,14]]

def test_value_is_continuous():
    from continuous_range_count import value_is_continuous
    assert value_is_continuous(4,5) == True
    assert value_is_continuous(5,5) == True
    assert value_is_continuous(9,15) == False
        
def test():
    test_get_continuous_range_and_count()
    test_get_continuous_count()
    test_get_count_for_range()
    test_in_limits()
    test_get_key()
    test_get_continuous_range()
    test_value_is_continuous()