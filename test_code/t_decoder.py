def test():
    from a2d_12_bit_decoder.decoder_12_bit import decode_12bit
    assert decode_12bit([]) == []
    assert decode_12bit([999]) == [2]
    assert decode_12bit([0,4094]) == [0,10]
    assert decode_12bit([409,409,1228,1637,2047,3684,3275,2865,1556,1555,1554,2998,3000,2999,3001]) \
        == [1,1,3,4,5,9,8,7,4,4,4,7,7,7,7]
    assert decode_12bit([0,9,99,999,1999,2999,3999,4094]) == [0,0,0,2,5,7,10,10]
    assert decode_12bit([-1,0,4094,4095]) == [0,10]