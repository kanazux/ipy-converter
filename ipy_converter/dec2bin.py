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
            continue
        elif _i == 255:
            _ip_list_bin.append("11111111")
            continue
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


def convert_mask(mask):
    """Convert mask in slash notation to binary."""
    return ".".join(['{:032}'.format(int('1'*int(mask)))[::-1][i:i+8]
                     for i in range(0, 32, 8)])


def return_network(ip, mask):
    """Return network with an and operation."""
    b_ip = convert_ip(ip).replace('.', '')
    b_mask = convert_mask(mask).replace('.', '')
    b_network = [
        "".join(map(str, [int(x[0]) & int(x[1]) for x in list(
            zip(b_ip, b_mask))]))[i:i+8] for i in range(0, 32, 8)]
    return ".".join(
        map(str, [int(sum([list(dict_values().keys())[x[0]] for x in list(
            enumerate(map(int, list(i)))) if x[1] == 1])) for i in b_network]))


def hosts_number(mask):
    """Return number of hosts based on network mask."""
    return int(2**(32-int(mask))-2)


def networks_number(mask):
    """Return number of sub nets based on network mask."""
    return int(2**(32-24-2))


def return_broadcast(ip, mask):
    """Return broadcast."""
    rev = ['1', '0']
    b_network = convert_ip(return_network(ip, mask)).replace('.', '')
    r_mask = "".join([rev[x] for x in map(int, list(
        convert_mask(mask).replace('.', '')))])
    b_mask = ["".join(map(str, [int(x[0]) | int(x[1]) for x in list(zip(
        b_network, r_mask))]))[i:i+8] for i in range(0, 32, 8)]
    return ".".join(
        map(str, [int(sum([list(dict_values().keys())[x[0]] for x in list(
            enumerate(map(int, list(i)))) if x[1] == 1])) for i in b_mask]))
