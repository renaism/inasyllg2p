import unittest
import numpy as np

from syllg2p import utility as util

class UtilityTestCase(unittest.TestCase):
    def test_log_prob(self):
        self.assertEqual(util.log_prob(1), 0)
        self.assertEqual(util.log_prob(0), -np.inf)
        self.assertEqual(util.log_prob(-1), -np.inf)


if __name__ == "__main__":
    unittest.main()