#!/usr/bin/python3

import random
def generate_random_integers():
    tuple1 = tuple(random.randint(0, 100) for _ in range(5))
    print(tuple1)
    return
generate_random_integers()
