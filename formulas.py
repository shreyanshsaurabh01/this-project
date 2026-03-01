import math
import numpy as np


def ou_step(x: float, k: float, sigma: float, dt: float):
    d_b = np.random.normal(0.0, math.sqrt(dt))
    d_x = -k * x * dt + sigma * d_b
    return x + d_x, d_x


def power_utility(w_t: float, gamma: float):
    w_t = max(w_t, 1e-12)
    if abs(gamma) < 1e-12:
        return math.log(w_t)
    return (w_t ** gamma) / gamma
