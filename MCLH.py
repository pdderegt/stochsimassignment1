import numpy as np
import random

RIGHT_X = 1; LEFT_X = -2; UPPER_i = 1.5; LOWER_i = -1.5
GUESSES = 100000
DEPTH = 100

def set_value_step(upper,lower):
    random_lh_list = []

    distance = abs(upper - lower)
    steps_size = distance / GUESSES

    for i in range(GUESSES):
        random_lh_list.append(random.uniform(i*steps_size+lower, i*steps_size+lower+steps_size))

    return random_lh_list

def latin_hypercube():
    x_axis = set_value_step(RIGHT_X, LEFT_X)
    i_axis = [complex(0, number) for number in set_value_step(UPPER_i, LOWER_i)]

    x_shuffled = random.sample(x_axis, len(x_axis))
    i_shuffled = random.sample(i_axis, len(i_axis))

    latin_set = np.add(x_shuffled,i_shuffled)
    print(latin_set)
    return latin_set

def total_area():
    return abs(LEFT_X-RIGHT_X)*abs(LOWER_i-UPPER_i)

def amount_stay_in(z):
    return len([i for i in [abs(ele) for ele in z] if i <= 2])

def calculate_inside():
    random_points = latin_hypercube()

    z = random_points
    for j in range(DEPTH):
        z = np.add([i**2 for i in z], random_points)

    return amount_stay_in(z)

def calculate_surface():
    ratio_inside = calculate_inside()/GUESSES
    return total_area()*ratio_inside

print (calculate_surface())





