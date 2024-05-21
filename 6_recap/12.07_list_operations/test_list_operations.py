import unittest
from list_operations import list_operations

class TesListOperations(unittest.TestCase):
    def test_result(self):
        result = list_operations([2,3])
        self.assertEqual(result[0], 5)
        
    def test_Larger_number(self):
        result = list_operations([5, 9, 15])
        self.assertTrue(result[0], 15)
        
    def test_even(self):
        list_to_test = [2, 4, 6, 8, 10]
        result = list_operations(list_to_test)
        self.assertTrue(result[-1],2)
    
        
if __name__ ==  "__main__":
    unittest.main()    
    
    """
import unittest
from list_operations import list_operations

class TestListOperations(unittest.TestCase):
    def test_result(self):
        result = list_operations([2, 3])
        self.assertEqual(result[0], 5)
        
    def test_largest_number(self):
        result = list_operations([5, 9, 15])
        self.assertEqual(result[1], 15)
        
    def test_even(self):
        result = list_operations([2, 4, 6, 8])
        self.assertEqual(result[2][0], 4)
    
        
if __name__ == "__main__":
    unittest.main()
        """