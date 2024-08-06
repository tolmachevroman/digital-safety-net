from dp_solver import DPSolver
import numpy as np


def main():
    incomes = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
    probs = [1/9] * len(incomes)
    beta = 0.95
    w_grid = np.linspace(0, 1000, 100)
    tau_grid = np.linspace(-200, 200, 50)

    dp_solver = DPSolver(incomes, probs, beta, w_grid, tau_grid)
    Π = dp_solver.iterate_value_function()
    tau_opt, phi_opt = dp_solver.extract_policy_functions()

    print("\nOptimal Value Function Π:", Π)
    print("\nOptimal Transfer Function τ:", tau_opt)
    print("\nOptimal State Transition Function φ:", phi_opt)


if __name__ == "__main__":
    main()
