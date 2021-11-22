import multiprocessing
from tqdm import tqdm
import time

import numpy as np
import random
import statistics

RIGHT_X = 1; LEFT_X = -2; UPPER_i = 1.5; LOWER_i = -1.5
GUESSES = 100000
DEPTH = 1000

def set_value_step(upper,lower):
    random_lh_list = []

    distance = abs(upper - lower)
    steps_size = distance / GUESSES

    for i in range(GUESSES):
        random_lh_list.append(random.uniform(i*steps_size+lower, i*steps_size+lower+steps_size))

    return random_lh_list

def latin_hypercube():
    x_axis = set_value_step(RIGHT_X, LEFT_X)
    i_axis = [complex(0, number) for number in set_value_step(UPPER_i, LOWER_i)] ##*1j does not seem to work

    x_shuffled = random.sample(x_axis, len(x_axis))
    i_shuffled = random.sample(i_axis, len(i_axis))

    latin_set = np.add(x_shuffled,i_shuffled)
    return latin_set

def total_area():
    return abs(LEFT_X-RIGHT_X)*abs(LOWER_i-UPPER_i)

def number_stay_in(c):
    z = c
    for i in range(DEPTH):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    return True

def calculate_inside():
    random_points = latin_hypercube()
    numbers_in = 0

    for point in random_points:
        if number_stay_in(point):
            numbers_in+=1
    return numbers_in

def calculate_surface():
    ratio_inside = calculate_inside()/GUESSES
    return total_area()*ratio_inside

print(calculate_surface())











