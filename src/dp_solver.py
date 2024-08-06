import numpy as np
from utility import utility


class DPSolver:
    def __init__(self, incomes, probs, beta, w_grid, tau_grid):
        self.incomes = incomes
        self.probs = probs
        self.beta = beta
        self.w_grid = w_grid
        self.tau_grid = tau_grid
        self.V = np.zeros(len(w_grid))  # Initial value function

    def iterate_value_function(self, max_iter=1000, epsilon=1e-6):
        for iter in range(max_iter):
            V_new = np.zeros_like(self.V)
            for i, w in enumerate(self.w_grid):
                max_val = -np.inf
                for y, pi in zip(self.incomes, self.probs):
                    for tau in self.tau_grid:
                        c = y + tau
                        if c > 0:
                            phi = w + tau  # Example state transition
                            if phi >= 0 and phi <= self.w_grid[-1]:
                                val = pi * (utility(c) + self.beta *
                                            np.interp(phi, self.w_grid, self.V))
                                if val > max_val:
                                    max_val = val
                V_new[i] = max_val
            if np.max(np.abs(V_new - self.V)) < epsilon:
                break
            self.V = V_new
        return self.V

    def extract_policy_functions(self):
        tau_opt = np.zeros_like(self.w_grid)
        phi_opt = np.zeros_like(self.w_grid)
        for i, w in enumerate(self.w_grid):
            max_val = -np.inf
            best_tau = 0
            best_phi = 0
            for y, pi in zip(self.incomes, self.probs):
                for tau in self.tau_grid:
                    c = y + tau
                    if c > 0:
                        phi = w + tau
                        if phi >= 0 and phi <= self.w_grid[-1]:
                            val = pi * (utility(c) + self.beta *
                                        np.interp(phi, self.w_grid, self.V))
                            if val > max_val:
                                max_val = val
                                best_tau = tau
                                best_phi = phi
            tau_opt[i] = best_tau
            phi_opt[i] = best_phi
        return tau_opt, phi_opt
