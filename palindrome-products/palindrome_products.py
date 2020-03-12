# tests pass in 11s
from collections import namedtuple
from itertools import combinations_with_replacement as cwr
from operator import gt, lt
from math import inf

Product = namedtuple('Product', 'value factors')


def largest(min_factor, max_factor):
    return _get_pproducts_extremum(min_factor, max_factor, max)


def smallest(min_factor, max_factor):
    return _get_pproducts_extremum(min_factor, max_factor, min)


def _get_pproducts_extremum(_min, _max, op):
    if _min > _max:
        raise ValueError('Min greater than max. WTF?')
    nums = range(_min, _max+1)
    p_products = []
    extremum = inf if op == min else 0
    compare = lt if op == min else gt
    for p in cwr(nums, 2):
        product = p[0]*p[1]
        if compare(product, extremum) and _is_palindrome(product):
            p_products = [Product(product, p)]
            extremum = product
        if product == extremum and _is_palindrome(product):
            p_products.append(Product(product, p))
    nothing_found = extremum == inf or extremum == 0
    return (None, []) if nothing_found else (
        extremum,
        [p.factors for p in p_products if p.value == extremum]
    )


def _is_palindrome(s):
    return str(s) == str(s)[::-1]