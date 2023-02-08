import unittest
import sys
import os

class TypewiseTest(unittest.TestCase):
    def test_current_range(self):
        from test_code.t_current_range import test
        test()
        
    def test_continuous_range_count(self):
        from test_code.t_continuous_range_count import test
        test()

    def test_decoder_12_bit_a2d(self):
        from test_code.t_decoder_12_bit import test
        test()

    def test_decoder_10_bit_a2d(self):
        from test_code.t_decoder_10_bit import test
        test()

            
if __name__ == '__main__':
    unittest.main()