import unittest

class TypewiseTest(unittest.TestCase):
    def test_current_range(self):
        from test_code.a2d_decoder.decoder import test
        test()
        
if __name__ == '__main__':
    unittest.main()