import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_int(self):
        a = {1,1,1,1,2,2,2,3,3,3,3}
        self.assertEqual(a, {1,2,3})
            
    def test_str(self):
        a = {"a", "a", "A", "b", "b"}
        self.assertEqual(a, {"a","A","b"})
                    
    def test_str_int(self):
        a = {"a", "a", 1, 1}
        self.assertEqual(a, {"a",1})

    def test_len(self):
        a = {1,1,2,2,3,3}
        self.assertEqual(len(a), 3)

    def test_remove(self):
        a = {1,2,3,4}
        a.remove(2)
        self.assertEqual(a, {1,3,4})

if __name__ == '__main__':
    unittest.main()
