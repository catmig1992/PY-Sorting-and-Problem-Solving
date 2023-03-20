import random

def make_random_list(size=10, min=-1000, max=1000):
    return [random.randint(min, max) for n in range(size)]