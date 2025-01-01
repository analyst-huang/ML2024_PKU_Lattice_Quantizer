# Genetic Algorithm Implementation

This project implements a genetic algorithm to optimize the Normalized Spectral Measure (NSM) of a generator matrix. The algorithm is encapsulated in the `Gene` class, which is designed to initialize and evolve a population of matrices through selection, crossover, and mutation processes.

## Project Structure

- **src/**
  - **gene.py**: Contains the `Gene` class with methods to run the genetic algorithm.
  - **gene_utils.py**: Includes utility functions such as the `GRAN` function for matrix initialization and other helper functions.
  - **__init__.py**: Marks the directory as a Python package and may include import statements.

- **requirements.txt**: Lists the dependencies required for the project, primarily `numpy`.

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the genetic algorithm, create an instance of the `Gene` class with the desired matrix dimension and call the `run` method:

```python
from src.gene import Gene

# Initialize with matrix dimension n
gene_algorithm = Gene(n)
# Run the genetic algorithm
gene_algorithm.run()
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.