#!/usr/bin/python3
"""

Convert decimal to bin.

Shows math process and output result in a table.

"""


from collections import defaultdict


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


def convert_ip(dec_number):
    """Convert ip in decimal notation to binary."""
    _ip_list_bin = []

    for i in dec_number.split('.'):
        _bin = [0, 0, 0, 0, 0, 0, 0, 0]
        _i = int(i)
        if _i == 0:
            _ip_list_bin.append("00000000")
        elif _i == 255:
            _ip_list_bin.append("11111111")
        else:
            _t = [x for x in dict_values() if x <= _i]
            if len(_t) > 0:
                _n = max(_t)
            _v = _i - _n
            while True:
                _bin[dict_values()[_n]] = 1
                _t = [x for x in dict_values() if x <= _v]
                if len(_t) > 0:
                    _n = max(_t)
                else:
                    break
                _v = _v - _n
        _ip_list_bin.append("".join(map(str, _bin)))

    return ".".join(_ip_list_bin)
