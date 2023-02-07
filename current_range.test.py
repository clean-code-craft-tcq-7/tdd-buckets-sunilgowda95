import unittest

class TypewiseTest(unittest.TestCase):
    def test_current_range(self):
        from test_code.continuous_range.t_current_range import test
        test()
        
    def test_continuous_range_count(self):
        from test_code.continuous_range.t_continuous_range_count import test
        test()
        
if __name__ == '__main__':
    unittest.main()