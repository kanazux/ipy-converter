#!/usr/bin/python3
"""Tests for ipy_data files"""


import re
from unittest import TestCase, main
from collections import defaultdict
from ipy_show.ipy_data import (dict_values, convert_ip, convert_mask,
                               return_mask, return_network, hosts_number,
                               networks_number, return_broadcast, return_class,
                               return_ip_data)


b_pattern = re.compile(r"([0|1]{8}\.){3}[0|1]{8}")
f_pattern = re.compile(r"([0-9]{1,3}\.){3}[0-9]{1,3}")


class testDictValues(TestCase):
    def test_dict_values(self):
        self.assertIsInstance(dict_values(), defaultdict)


class testConvertIp(TestCase):
    def test_convert_ip(self):
        self.assertTrue(b_pattern.match(convert_ip('192.168.0.255')))


class testConvertMask(TestCase):
    def test_convert_mask(self):
        self.assertTrue(b_pattern.match(convert_mask('24')))


class returnMask(TestCase):
    def test_return_mask(self):
        self.assertTrue(f_pattern.match(return_mask('24')))


class returnNetwork(TestCase):
    def test_return_network(self):
        self.assertTrue(f_pattern.match(return_network('192.168.0.1', '24')))


class hostNumber(TestCase):
    def test_hosts_number(self):
        self.assertIsInstance(hosts_number('24'), int)


class networksNumber(TestCase):
    def test_networks_number(self):
        self.assertIsInstance(networks_number('24'), int)


class returnBroadcast(TestCase):
    def test_return_broadcast(self):
        self.assertTrue(f_pattern.match(return_broadcast('192.168.0.1', '24')))


class returnClass(TestCase):
    def test_return_class(self):
        self.assertIsInstance(return_class('192.168.8.0'), str)


class returnIpData(TestCase):
    def test_return_ip_data(self):
        self.assertIsInstance(return_ip_data('192.168.8.0', '24'), defaultdict)


if __name__ == "__main__":
    main()
