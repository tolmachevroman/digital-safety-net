# Dynamic Programming Solver for Digital Safety Net Blueprint Paper

This project demonstrates how to solve a dynamic programming functional equation mentioned in the **Digital Safety Net** paper for multiple participants and simulate their state variable evolution over time using Python. The project includes:

- Initialization and iteration of a value function.
- Extraction of optimal policy functions.
- Simulation of state variable evolution for multiple participants.
- Visualization of results.

## Features

- **Dynamic Programming Solver**: Solves for the optimal policy functions and value function using value function iteration.
- **Multi-Participant Simulation**: Simulates the evolution of the state variable for multiple participants over a specified number of periods.
- **Visualization**: Plots the evolution of the value function, state variable trajectories, and optimal policy functions.

## Getting Started

### Prerequisites

- Python 3.x
- NumPy
- Matplotlib

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tolmachevroman/digital-safety-net.git
    cd digital-safety-net
    ```

2. Install the required packages:
    ```bash
    pip install numpy matplotlib
    ```

### Usage

1. Navigate to the project directory:
    ```bash
    cd digital-safety-net/src
    ```

2. Run the main script to perform the simulation and generate plots:
    ```bash
    python main.py
    ```

### Project Structure

- `dp_solver.py`: Contains the `DPSolver` class which implements the dynamic programming solver, policy function extraction, and state variable simulation.
- `main.py`: The main script that initializes the solver, runs the simulation for multiple participants, and generates plots.
  
### Example

After running the `main.py` script, you will see the following plot:

1. **State Variable Trajectories**: Displays the state variable evolution over time for each participant.

<p align="center">
  <img src="https://github.com/user-attachments/assets/bba7f55d-6972-4f71-96f0-29e7a5d25b36" width="1200" title="hover text">
</p>

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

This project is inspired by dynamic programming and optimal control theories. Special thanks to all the contributors and the open-source community.
