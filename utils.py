from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SimulationConfig:
    k: float
    sigma: float
    gamma: float
    initial_wealth: float
    horizon: float
    steps: int = 250


def clamp_gamma(gamma: float) -> float:
    return min(max(gamma, 1e-6), 0.999999)
