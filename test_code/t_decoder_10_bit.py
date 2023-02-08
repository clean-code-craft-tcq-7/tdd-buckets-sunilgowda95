def test():
    from a2d_10_bit_decoder.decoder_10_bit import decode_10_bit, decode_10_bit_continous_range
    
    # decoding
    assert decode_10_bit([]) == []
    assert decode_10_bit([155]) == [-11]
    assert decode_10_bit([-1,0,510,511,512,1011,1022,1023]) == [-15, -1, 1, 1, 15, 15]
    assert decode_10_bit([0,9,99,999]) == [-15, -15, -13, 15]
    assert decode_10_bit([0,34,817,681,647,136,953,919,545,511]) == [-15, -14, 9, 5, 4, -11, 13, 11, 1, 1]

    # finding continuous range
    assert decode_10_bit_continous_range([]) == 'Range, Readings'
    assert decode_10_bit_continous_range([155]) == 'Range, Readings\n11-11, 1'
    assert decode_10_bit_continous_range([-1,0,510,511,512,1011,1022,1023]) == 'Range, Readings\n1-1, 3\n15-15, 3'
    assert decode_10_bit_continous_range([0,9,99,999]) == 'Range, Readings\n13-13, 1\n15-15, 3'
    assert decode_10_bit_continous_range([0,34,817,681,647,136,953,919,545,511]) == 'Range, Readings\n1-1, 2\n4-5, 2\n9-9, 1\n11-11, 2\n13-15, 3'
