import unittest
from bongo_solution import my_sum

class BongoSolutionTestCase(unittest.TestCase):

   def test_first_last_name(self):
       result = my_sum(4, 6)
       self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()