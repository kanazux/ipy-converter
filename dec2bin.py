#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
"""

Convert decimal to bin.

Shows math process and output result in a table.

"""


import sys
from collections import defaultdict


def print_help():
    """Show help."""
    print ("Para usar esse conversor use um unico argumento para ip e mascara."
           " Ex: 192.168.0.1 ")
    print ("Para mascaras pode ser usada tanto notação decimal quanto binario."
           " Ex: 192.168.0.1/24 ou 192.168.0.1/255.255.255.0")


if len(sys.argv) != 2 or sys.argv[1].lower() == "-h":
    print_help()
    sys.exit(0)


def dict_values():
    """
    Return a defaultdict with eigth keys from 128 to 1 dividing the first by 2.

    Lambda: False is used to set false a key that not exists.

    """
    d_list = defaultdict(lambda: False)
    n = 256
    for i in range(8):
        n = n/2
        d_list[n] = i
    return d_list


list_values = dict_values()
ip = sys.argv[1]
mask = False

if "/" in ip:
    ip, mask = ip.split("/")


def convert_ip(dec_number):
    """Convert ip in decimal notation to binary."""
    _ip_list_bin = []

    for i in dec_number.split('.'):
        _bin = [0, 0, 0, 0, 0, 0, 0, 0]
        _i = int(i)
        if _i == 0:
            _ip_list_bin.append("00000000")
            continue
        elif _i == 255:
            _ip_list_bin.append("11111111")
            continue
        _t = [x for x in list_values if x <= _i]
        if len(_t) > 0:
            _n = max(_t)
        _v = _i - _n
        while True:
            _bin[list_values[_n]] = 1
            _t = [x for x in list_values if x <= _v]
            if len(_t) > 0:
                _n = max(_t)
            else:
                break
            _v = _v - _n
        _ip_list_bin.append("".join(map(str, _bin)))

    return _ip_list_bin


ip_list_bin = convert_ip(ip)


print(".".join(ip_list_bin))
print(".".join(["{0:08b}".format(int(x)) for x in ip.split('.')]))
