import numpy as np
import statistics
import random
import time

ITERATIONS = 100
SAMPLES = 10000
LEFTBOUND_X = -2; LEFTBOUND_Y = -2; RIGHTBOUND_X = 1.5; RIGHTBOUND_Y = 2


def total_area():
    return (RIGHTBOUND_X-LEFTBOUND_X)*(RIGHTBOUND_Y-LEFTBOUND_Y)


def is_in_set(a,b):
    c = complex(a,b)
    z = 0
    for i in range(ITERATIONS):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    return True


def calculate_set_area(points_in_set):
    return (points_in_set/SAMPLES) * total_area()


def start_experiment():
    points_in_set = 0
    for i in range(SAMPLES):
        x, y = random.uniform(LEFTBOUND_X, RIGHTBOUND_X), random.uniform(LEFTBOUND_Y, RIGHTBOUND_Y)
        if is_in_set(x,y):
            points_in_set += 1
    return calculate_set_area(points_in_set)


def create_variance():
    steps = 1000
    variance = []
    for i in range(steps):
        variance.append(start_experiment())

    mean_value = statistics.mean(variance)
    variance = statistics.variance(variance, mean_value)

    print(mean_value)
    print(variance)

create_variance()