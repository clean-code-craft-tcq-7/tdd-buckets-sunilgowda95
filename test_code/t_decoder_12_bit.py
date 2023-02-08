def test():
    from a2d_12_bit_decoder.decoder_12_bit import decode_12_bit, decode_12_bit_continous_range
    
    # decoding
    assert decode_12_bit([]) == []
    assert decode_12_bit([999]) == [2]
    assert decode_12_bit([0,4094]) == [0,10]
    assert decode_12_bit([409,409,1228,1637,2047,3684,3275,2865,1556,1555,1554,2998,3000,2999,3001]) \
        == [1,1,3,4,5,9,8,7,4,4,4,7,7,7,7]
    assert decode_12_bit([0,9,99,999,1999,2999,3999,4094]) == [0,0,0,2,5,7,10,10]
    assert decode_12_bit([-1,0,4094,4095]) == [0,10]
    
    # finding continuous range
    assert decode_12_bit_continous_range([]) == 'Range, Readings'
    assert decode_12_bit_continous_range([999]) == 'Range, Readings\n2-2, 1'
    assert decode_12_bit_continous_range([0,4094]) == 'Range, Readings\n0-0, 1\n10-10, 1'
    assert decode_12_bit_continous_range([409,409,1228,1637,2047,3684,3275,\
    2865,1556,1555,1554,2998,3000,2999,3001]) == 'Range, Readings\n1-1, 2\n3-5, 6\n7-9, 7'
    assert decode_12_bit_continous_range([0,9,99,999,1999,2999,3999,4094]) == \
        'Range, Readings\n0-0, 3\n2-2, 1\n5-5, 1\n7-7, 1\n10-10, 2'
    assert decode_12_bit_continous_range([-1,0,4094,4095]) == 'Range, Readings\n0-0, 1\n10-10, 1'
