import numpy as np

from formulas import ou_step, power_utility
from optimizer import alpha_star


def run_simulation(k: float, sigma: float, gamma: float, w0: float, horizon: float, steps: int = 250):
    dt = horizon / steps
    x = 0.0
    w = w0

    rows = []
    for i in range(steps + 1):
        t = i * dt
        tau = max(horizon - t, 1e-9)
        alpha = alpha_star(w, x, tau, gamma)

        rows.append({
            "t": t,
            "x": x,
            "w": w,
            "alpha": alpha,
            "utility": power_utility(max(w, 1e-9), gamma),
        })

        if i < steps:
            x_next, d_x = ou_step(x, k, sigma, dt)
            w = w + alpha * d_x
            x = x_next

    return rows
