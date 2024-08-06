from dp_solver import DPSolver
import numpy as np
import matplotlib.pyplot as plt


def main():
    incomes = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
    probs = [1/9] * len(incomes)
    beta = 0.05
    w_grid = np.linspace(0, 1000, 100)
    tau_grid = np.linspace(-200, 200, 50)

    dp_solver = DPSolver(incomes, probs, beta, w_grid, tau_grid)

    tau_opt, phi_opt = dp_solver.extract_policy_functions()
    # Simulate the state variable evolution over 100 periods

    # Number of participants
    num_participants = 10
    initial_states = np.linspace(0, 1000, num_participants)
    periods = 100

    all_trajectories = []

    # Simulate for each participant
    for i in range(num_participants):
        w0 = initial_states[i]
        w_trajectory = dp_solver.simulate(w0, periods)
        all_trajectories.append(w_trajectory)

    # Plot the state variable trajectories for all participants
    plt.figure(figsize=(10, 6))
    for i, trajectory in enumerate(all_trajectories):
        plt.plot(range(periods + 1), trajectory,
                 marker='o', label=f'Participant {i+1}')
    plt.xlabel('Period')
    plt.ylabel('State Variable w')
    plt.title('State Variable Evolution Over Time for Multiple Participants')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
