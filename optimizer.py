import math


def _nu(gamma: float) -> float:
    g = min(max(gamma, 1e-6), 0.999999)
    return 1.0 / math.sqrt(1.0 - g)


def c_tau(tau: float, gamma: float) -> float:
    nu = _nu(gamma)
    return math.cosh(nu * tau) + nu * math.sinh(nu * tau)


def c_prime_tau(tau: float, gamma: float) -> float:
    nu = _nu(gamma)
    return nu * math.sinh(nu * tau) + (nu**2) * math.cosh(nu * tau)


def d_tau(tau: float, gamma: float) -> float:
    c = c_tau(tau, gamma)
    cp = c_prime_tau(tau, gamma)
    return cp / c if c != 0 else 0.0


def alpha_star(w_t: float, x_t: float, tau: float, gamma: float) -> float:
    return -w_t * x_t * d_tau(tau, gamma)
