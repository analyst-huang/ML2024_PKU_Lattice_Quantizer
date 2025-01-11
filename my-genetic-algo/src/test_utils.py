import unittest
import numpy as np

from lattice_utils import *

class TestUtils(unittest.TestCase):

    def test_RED(self):
        test_cases = [(np.array([[1,1,1],[-1,0,2],[3,5,6]]), np.array([[0,1,0],[1,0,1],[-1,0,2]])),
                     ]
        for B, expected in test_cases:
            with self.subTest(B=B, expected=expected):
                self.assertTrue(np.allclose(RED(B), expected))

    def test_ORTH(self):
        t = 100
        for i in range(t):
            B = np.random.randint(-100, 100, (3, 3))
            A = B@B.T
            expected = np.linalg.cholesky(A)
            self.assertTrue(np.allclose(ORTH(B), expected))

    # def test_new_CLP(self):
    #     t = 100
    #     n = 6
    #     for i in range(t):
    #         B = ORTH(RED(GRAN(n,n)))
    #         u = URAN(n)
    #         answer = CLP(B, u@B)
    #         my_answer = new_CLP(B, u@B)
    #         print(answer)
    #         print(my_answer)
    #         my_answer[1:] += 1
    #         self.assertTrue(np.allclose(answer, my_answer))



if __name__ == '__main__':
    unittest.main()