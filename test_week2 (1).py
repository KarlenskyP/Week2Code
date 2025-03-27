import unittest
from week2 import most_frequent_item, most_frequent_count, find_repeat_number, unique_array, only_unique_items, exclude_product, are_all_items_unique, list_cycle, three_sum, is_anagram, count


class TestCount(unittest.TestCase):
    def test_count(self):
        self.assertDictEqual(count(['a', 'b', 'a']), {'a': 2, 'b': 1})

class TestMostFrequentItem(unittest.TestCase):
    def test_most_frequent_item(self):
        self.assertEqual(most_frequent_item([1, 3, 1, 3, 2, 1]), 1)


class TestMostFrequentCount(unittest.TestCase):
    def test_most_frequent_count(self):
        self.assertEqual(most_frequent_count([1, 1, 2, 2, 2, 7, 7, 7]), 3)
        self.assertEqual(most_frequent_count([1, 2, 3, 4, 5, 8, 8]), 1)


class TestFindRepeatNumber(unittest.TestCase):
    def test_find_repeat_number(self):
        self.assertEqual(find_repeat_number([1, 2, 3, 4, 2]), 2)


class TestUniqueArray(unittest.TestCase):
    def test_unique_array(self):
        self.assertEqual(unique_array([1, 2, 3, 2, 4, 3, 5]), [1, 2, 3, 4, 5])


class TestOnlyUniqueItems(unittest.TestCase):
    def test_only_unique_items(self):
        self.assertEqual(only_unique_items([1, 2, 3, 2, 4, 3, 5]), [1, 4, 5])


class TestAreAllItemsUnique(unittest.TestCase):
    def test_are_all_items_unique(self):
        self.assertTrue(are_all_items_unique([1, 2, 3, 4, 5]))
        self.assertFalse(are_all_items_unique([1, 2, 3, 2, 4]))


class TestListCycle(unittest.TestCase):
    def test_list_cycle(self):
        self.assertTrue(list_cycle([2, 0, 1]))
        self.assertFalse(list_cycle([1, 2, 0, 2]))


class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        self.assertEqual(three_sum([1, 2, 3, 4, 5], 9), [0, 2, 4])


class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))


class TestExcludeProduct(unittest.TestCase):
    def test_exclude_product(self):
        self.assertEqual(exclude_product([1, 2, 3, 4]), [24, 12, 8, 6])


if __name__ == '__main__':
    unittest.main()