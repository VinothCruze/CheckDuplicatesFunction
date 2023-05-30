import unittest
import pandas as pd
from check_duplicate import check_duplicates

class TestDuplicate(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(data=[
            ['A', 'a', 'x', 1],
            ['A', 'b', 'x', 1],
            ['A', 'c', 'x', 1],
            ['B', 'a', 'x', 1],
            ['B', 'b', 'x', 1],
            ['B', 'c', 'x', 1],
            ['A', 'a', 'y', 1],
        ],
        columns=['col_1', 'col_2', 'col_3', 'col_4'])

    def test_duplicate_1(self):
        result = check_duplicates(self.df, ['col_1', 'col_2'])
        self.assertEqual(result['count'], 1)

    def test_duplicate_2(self):
        result = check_duplicates(self.df, ['col_1'])
        self.assertEqual(result['count'], 5)

    def test_duplicate_3(self):
        result = check_duplicates(self.df, ['col_1', 'col_2', 'col_3'])
        self.assertEqual(result['count'], 0)
        
    def test_error_case(self):
        with self.assertRaises(ValueError):
            # Call the function with invalid column name
            check_duplicates(self.df, ['col_1', 'col_5'])


if __name__ == '__main__':
  unittest.main(argv=[''], defaultTest='TestDuplicate')
  
  
    
