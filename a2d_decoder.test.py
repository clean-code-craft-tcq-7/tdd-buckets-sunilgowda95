import unittest
import sys
import os

class TypewiseTest(unittest.TestCase):
    def test_decoder(self):
        from test_code.t_decoder_12_bit import test
        test()
            
if __name__ == '__main__':
    unittest.main()