# code quantum sorting algorithm to sort a list of numbers

# import libraries
import random
import time

import matplotlib.pyplot as plt
import qiskit as qk

style = {'ggplot', 'seaborn', 'dark_background', 'grayscale', 'bmh', 'fivethirtyeight', 'seaborn-dark-palette', }


# create a class for the quantum sorting algorithm
def get_sorted_values(counts):
    return [int(x[0], 2) for x in sorted(counts.items(), key=lambda x: int(x[0], 2))]


def get_sorted_keys(counts):
    return [x[0] for x in sorted(counts.items(), key=lambda x: int(x[0], 2))]


def get_sorted(counts):
    return sorted(counts.items(), key=lambda x: int(x[0], 2))


def get_counts(counts):
    return counts


def plot(counts):
    plt.bar(counts.keys(), counts.values())
    plt.show()


def quantum_circuit(n, m):
    qc = qk.QuantumCircuit(2 * n * m, 2 * n * m)
    qc.h(range(n * m))
    qc.barrier()
    qc.measure(range(n * m), range(n * m))
    qc.barrier()
    qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
    qc.barrier()
    qc.measure(range(n * m), range(n * m))
    qc.barrier()
    qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
    qc.barrier()
    qc.measure(range(n * m), range(n * m))
    qc.barrier()
    qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
    qc.barrier()
    qc.measure(range(n * m), range(n * m))
    qc.barrier()
    qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
    qc.barrier()
    qc.measure(range(n * m), range(n * m))
    qc.barrier()
    qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
    qc.barrier()
    return qc


class Quantum_Sorter:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.qc = qk.QuantumCircuit(2 * n * m, 2 * n * m)
        self.qc.h(range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m), range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m), range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m), range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m), range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m), range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m), range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m), range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m), range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m), range(n * m))
        self.qc.barrier()
        self.qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))


def run(self, backend, shots):
    job = qk.execute(self.qc, backend=backend, shots=shots)
    return job.get_counts()


def get_circuit(self):
    return self.qc


def quantum_sorter(n, m):
    qc = qk.QuantumCircuit(2 * n * m, 2 * n * m)
    qc.h(range(n * m))
    qc.barrier()
    qc.measure(range(n * m), range(n * m))
    qc.barrier()
    qc.measure(range(n * m, 2 * n * m), range(n * m, 2 * n * m))
    qc.barrier()
    return qc


# generate a random list of numbers
def generate_random_list(n):
    return [random.randint(0, 2 ** 8 - 1) for _ in range(n)]


# plot the time taken for the quantum sorting algorithm
def plot_time(n, m):
    times = []
    for i in range(1, n + 1):
        start = time.time()
        quantum_sorter(i, m)
        end = time.time()
        times.append(end - start)
    plt.plot(range(1, n + 1), times)
    plt.show()


# main function
def main():
    # create a random list of numbers
    n = 4
    m = 2
    qk.Aer.get_backend('qasm_simulator')
    1000
    qc = quantum_sorter(n, m)
    counts = qc
    print(counts)
    # plot the time taken for the quantum sorting algorithm
    plot_time(10, 2)


# run the main function
if __name__ == "__main__":
    main()
