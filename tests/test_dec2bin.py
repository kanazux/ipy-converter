"""Tests for dec2bin files"""


from unittest import TestCase, main
from collections import defaultdict
from dec2bin import dict_values


class testDictValues(TestCase):
    def test_dict_values(self):
        self.assertIsInstance(dict_values(), defaultdict)


if __name__ == "__main__":
    main()
