import numpy as np
import random
import time
import statistics

ITERATIONS = 100
SAMPLES = 10000
LEFTBOUND_X = -2; LEFTBOUND_Y = -2; RIGHTBOUND_X = 2; RIGHTBOUND_Y = 2


def total_area():
    return (RIGHTBOUND_X-LEFTBOUND_X) * (RIGHTBOUND_Y-LEFTBOUND_Y)


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


def generate_samples():
    x_samples, y_samples = np.zeros(SAMPLES), np.zeros(SAMPLES)
    bandwidth_x, bandwidth_y = (RIGHTBOUND_X - LEFTBOUND_X) / SAMPLES, (RIGHTBOUND_Y - LEFTBOUND_Y) / SAMPLES
    for i in range(SAMPLES):
        x_samples[i] = random.uniform(LEFTBOUND_X + i*bandwidth_x, LEFTBOUND_X + (i+1)*bandwidth_x)
        y_samples[i] = random.uniform(LEFTBOUND_Y + i*bandwidth_y, LEFTBOUND_Y + (i+1)*bandwidth_y)
    random.shuffle(x_samples), random.shuffle(y_samples)
    return zip(x_samples, y_samples)


def start_experiment():
    points_in_set = 0
    samples = generate_samples()
    for i in samples:
        x, y = i[0], i[1]
        if is_in_set(x,y):
            points_in_set += 1
    return calculate_set_area(points_in_set)

def create_variance():
    steps = 500
    variance = []
    for i in range(steps):
        variance.append(start_experiment())

    mean_value = statistics.mean(variance)
    variance = statistics.variance(variance, mean_value)

    print(mean_value)
    print(variance)

create_variance()