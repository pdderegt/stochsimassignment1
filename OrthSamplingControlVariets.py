import random
import numpy as np
import time
import statistics

ITERATIONS = 1000
S = 316
SAMPLES = S**2
LEFTBOUND_X = -2; LEFTBOUND_Y = -1.5; RIGHTBOUND_X = 1; RIGHTBOUND_Y = 1.5


def LH(S):
    x_col1 = []
    for i in range(S):
        nrs = list(range(S*i, S*(i+1)))
        random.shuffle(nrs)
        x_col1 += nrs
    x_col2 = np.zeros(S*S, dtype=int)
    for i in range(S):
        nrs = list(range(S * i, S * (i + 1)))
        random.shuffle(nrs)
        for j in range(S):
            x_col2[i+j*S] = nrs[j]
    x = [np.array(x_col1), x_col2]
    return x

#
#
# lh = LH(5)
# print(lh)
# plt.plot(lh[0], lh[1], 'ro')
# plt.grid(True)
# plt.show()
#
#


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
    return points_in_set * total_area()


def generate_samples():
    x_samples, y_samples = np.zeros(SAMPLES), np.zeros(SAMPLES)
    bandwidth_x, bandwidth_y = (RIGHTBOUND_X - LEFTBOUND_X) / SAMPLES, (RIGHTBOUND_Y - LEFTBOUND_Y) / SAMPLES
    lh = LH(S)
    for i in range(SAMPLES):
        x_samples[i] = random.uniform(LEFTBOUND_X + i*bandwidth_x, LEFTBOUND_X + (i+1)*bandwidth_x)
        y_samples[i] = random.uniform(LEFTBOUND_Y + i*bandwidth_y, LEFTBOUND_Y + (i+1)*bandwidth_y)
    samples = np.zeros((SAMPLES, 2))
    for i in range(SAMPLES):
        samples[i] = np.array([x_samples[lh[0][i]], y_samples[lh[1][i]]])
    return samples



def start_experiment():
    points_in_set = 0
    samples = generate_samples()
    x_i = []
    y_i = []
    for i in samples:
        x, y = i[0], i[1]
        if is_in_set(x,y):
            points_in_set += 1
            x_i.append(1)
        else:
            x_i.append(0)
        y_i.append(x)
    cov = np.cov(x_i, y_i)[0][1]
    var = np.var(y_i)
    c_star = -cov/var
    theta = x_i + c_star*(y_i-np.full(SAMPLES, (RIGHTBOUND_X+LEFTBOUND_X)/2))
    return calculate_set_area(np.mean(theta))


def create_variance():
    steps = 50
    variance = []
    f = open('logOrthaCV.txt', 'w')

    for i in range(steps):
        x = start_experiment()
        variance.append(x)
        print(x, file=f)

    f.close()
    mean_value = statistics.mean(variance)
    variance = statistics.variance(variance, mean_value)

    print(mean_value)
    print(variance)


create_variance()