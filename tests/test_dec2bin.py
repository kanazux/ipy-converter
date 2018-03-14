#!/usr/bin/python3
"""Tests for dec2bin files"""


import re
from unittest import TestCase, main
from collections import defaultdict
from ipy_converter.dec2bin import dict_values, convert_ip


pattern = re.compile(r"([0|1]{8}\.){3}[0|1]{8}")


class testDictValues(TestCase):
    def test_dict_values(self):
        self.assertIsInstance(dict_values(), defaultdict)


class testConvertIp(TestCase):
    def test_convert_ip(self):
        self.assertTrue(pattern.match(convert_ip('192.168.0.255')))


if __name__ == "__main__":
    main()
