import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_int(self):
        a = {1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3}
        self.assertEqual(a, {1,2,3})
            
    def test_str(self):
        a = {"a", "a", "A", "b", "b"}
        self.assertEqual(a, {"a","A","b"})
                    
    def test_str_int(self):
        a = {"a", "a", 1, 1}
        self.assertEqual(a, {"a",1})

    def test_len(self):
        a = {1, 1, 2, 2, 3, 3}
        self.assertEqual(len(a), 3)

    def test_remove(self):
        a = {1, 2, 3, 4}
        a.remove(2)
        self.assertEqual(a, {1,3,4})

    # Негативные проверки!
    
    def test_not_in_set(self):
        a = {1, 2, 3, 4}
        self.assertFalse(5 in a)

    def test_not_in_set_str(self):
        a = {"a", "b"}
        self.assertFalse(False, "c" in a)

    # Еще тесты свойств
    
    def test_union(self):
        a = {1, 2, 3}
        b = {4, 5, 6}
        self.assertEqual(a.union(b), {1, 2, 3, 4, 5, 6})

    def test_isdisjoint(self): # проверка, что пересечение пустое
        a = {1, 2, 3}
        b = {4, 5, 6}
        self.assertTrue(a.isdisjoint(b))

    def test_pop(self):
        a = {1, 2, 3}
        len_a = len(a)
        a.pop()
        self.assertFalse(len_a == len(a)) # какой-то элемент должен удалиться, мы не знаем какой

    def test_add(self):
        a = {1, 2}
        a.add(3)
        self.assertTrue(3 in a)


if __name__ == '__main__':
    unittest.main()
