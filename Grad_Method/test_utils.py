import unittest
import numpy as np

from utils import RED, ORTH

class TestUtils(unittest.TestCase):

    def test_RED(self):
        test_cases = [(np.array([[1,1,1],[-1,0,2],[3,5,6]]), np.array([[0,1,0],[1,0,1],[-1,0,2]])),
                     ]
        for B, expected in test_cases:
            with self.subTest(B=B, expected=expected):
                self.assertTrue(np.allclose(RED(B), expected))

    # def test_ORTH(self):
    #     test_cases = [(np.array([[4,12,-16], [12,37,-43], [-16,-43,98]]), np.array([[2,0,0],[6,1,0],[-8,5,3]]))]
    #     for B, expected in test_cases:
    #         with self.subTest(B=B, expected=expected):
    #             self.assertTrue(np.allclose(ORTH(B), expected))


if __name__ == '__main__':
    unittest.main()