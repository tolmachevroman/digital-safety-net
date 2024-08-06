from dp_solver import DPSolver
import numpy as np
import matplotlib.pyplot as plt


def main():
    incomes = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
    probs = [1/9] * len(incomes)
    beta = 0.95
    w_grid = np.linspace(0, 1000, 100)
    tau_grid = np.linspace(-200, 200, 50)

    dp_solver = DPSolver(incomes, probs, beta, w_grid, tau_grid)

    tau_opt, phi_opt = dp_solver.extract_policy_functions()
    # Simulate the state variable evolution over 100 periods
    w0 = 100  # Initial state
    periods = 100
    w_trajectory = dp_solver.simulate(w0, periods)

    # Plot the state variable trajectory
    plt.figure(figsize=(10, 6))
    plt.plot(range(periods + 1), w_trajectory, marker='o')
    plt.xlabel('Period')
    plt.ylabel('State Variable w')
    plt.title('State Variable Evolution Over Time')
    plt.show()

    # Plot the optimal policy functions
    plt.figure(figsize=(10, 6))
    plt.plot(dp_solver.w_grid, tau_opt, label='Optimal Transfer Function τ')
    plt.xlabel('State Variable w')
    plt.ylabel('Transfer Function τ')
    plt.title('Optimal Transfer Function τ(w)')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(dp_solver.w_grid, phi_opt,
             label='Optimal State Transition Function φ')
    plt.xlabel('State Variable w')
    plt.ylabel('State Transition Function φ')
    plt.title('Optimal State Transition Function φ(w)')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
