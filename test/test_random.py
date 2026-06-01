import random


def test_random():
    random_value = random.randint(1, 100)
    assert random_value < 100

