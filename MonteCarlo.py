import numpy as np
import random

from tqdm import tqdm
import matplotlib.pyplot as plt

RIGHT_X = 1; LEFT_X = -2; UPPER_i = 1.5; LOWER_i = -1.5
GUESSES = 100000
DEPTH = 1000

def random_coordinates():
    random_i = 1j*random.uniform(UPPER_i, LOWER_i)
    random_x = random.uniform(LEFT_X, RIGHT_X)
    return random_x+random_i

def random_list():
    coordinate_list = [];

    for i in range(GUESSES):
        coordinate_list.append(random_coordinates())

    return coordinate_list

def total_area():
    return abs(LEFT_X-RIGHT_X)*abs(LOWER_i-UPPER_i)

def amount_stay_in(z):
    return len([i for i in [abs(ele) for ele in z] if i <= 2])

def calculate_inside():
    random_points = random_list()

    z = random_points
    for j in range(DEPTH):
        z = np.add([i**2 for i in z], random_points)

    return amount_stay_in(z)

def calculate_surface():
    ratio_inside = calculate_inside()/GUESSES
    return total_area()*ratio_inside

print(calculate_surface())