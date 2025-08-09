# Stanford Algorithms Specialization - Python Implementations

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Complete Python implementations of algorithms from Stanford University's 4-course Algorithms Specialization, including automated testing framework and custom data structures.

## 📚 Course Coverage

### Course 1: Divide and Conquer, Sorting and Searching, and Randomized Algorithms

- **[Karatsuba Multiplication](course-1/1/karatsuba.py)** - Fast integer multiplication using divide-and-conquer
- **[Inversion Counting](course-1/2/inversions.py)** - Count inversions in an array using merge sort
- **[Quicksort](course-1/3/quicksort.py)** - Multiple pivot selection strategies with comparison counting
- **[Minimum Cut](course-1/4/mincut.py)** - Randomized contraction algorithm for finding minimum cuts
- **[Theory Problems](course-1/Q/ex1.py)** - Second maximum finding with optimal comparisons

### Course 2: Graph Search, Shortest Paths, and Data Structures

- **[Strongly Connected Components](course-2/1/scc.py)** - Kosaraju's two-pass algorithm
- **[Dijkstra's Algorithm](course-2/2/dijkstra.py)** - Single-source shortest paths with binary heap
- **[Median Maintenance](course-2/3/median.py)** - Dynamic median using two heaps
- **[Two-Sum Problem](course-2/4/two-sum.py)** - Hash table implementation for target sum counting

### Course 3: Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming

- **[Job Scheduling](course-3/1/scheduling.py)** - Weighted completion time optimization
- **[Minimum Spanning Tree](course-3/1/MST.py)** - Prim's algorithm implementation
- **[Clustering](course-3/2/clustering.py)** - Single-link clustering using Kruskal's algorithm
- **[Hamming Distance Clustering](course-3/2/hamming.py)** - Clustering with Union-Find data structure
- **[Huffman Coding](course-3/3/huffman.py)** - Optimal prefix-free codes
- **[Maximum Weight Independent Set](course-3/3/mwis.py)** - Dynamic programming on paths
- **[Knapsack Problem](course-3/4/knapsack.py)** - Space-optimized dynamic programming

### Course 4: Shortest Paths Revisited, NP-Complete Problems and What To Do About Them

- **[All-Pairs Shortest Path](course-4/1/all-pairs-shortest-path.py)** - Johnson's algorithm
- **[Traveling Salesman Problem](course-4/2/tsp.py)** - Exact solution using dynamic programming
- **[TSP Heuristic](course-4/3/tsp-heuristic.py)** - Nearest neighbor approximation
- **[2-SAT](course-4/4/two-sat.py)** - Polynomial-time satisfiability using SCC

## Project Structure

```
algorithms-specialization/
├── course-1/                          # Divide & Conquer Algorithms
│   ├── 1/karatsuba.py                 # Fast multiplication
│   ├── 2/inversions.py                # Inversion counting
│   ├── 3/quicksort.py                 # Quicksort variants
│   ├── 4/mincut.py                    # Minimum cut algorithm
│   └── Q/ex1.py                       # Theory problems
├── course-2/                          # Graph & Data Structure Algorithms
│   ├── 1/scc.py                       # Strongly connected components
│   ├── 2/dijkstra.py                  # Shortest paths
│   ├── 3/median.py                    # Median maintenance
│   └── 4/two-sum.py                   # Hash table problems
├── course-3/                          # Greedy & Dynamic Programming
│   ├── 1/scheduling.py, MST.py        # Scheduling & MST
│   ├── 2/clustering.py, hamming.py    # Clustering algorithms
│   ├── 3/huffman.py, mwis.py          # Huffman & MWIS
│   └── 4/knapsack.py                  # Knapsack problem
├── course-4/                          # Advanced Algorithms
│   ├── 1/all-pairs-shortest-path.py   # Johnson's algorithm
│   ├── 2/tsp.py                       # Exact TSP
│   ├── 3/tsp-heuristic.py             # TSP approximation
│   └── 4/two-sat.py                   # 2-SAT solver
├── utils/                              # Custom Data Structure Library
│   ├── Graph/                          # Graph implementations
│   ├── Heap/                           # Heap data structures
│   ├── HashTable/                      # Hash table variants
│   ├── List/                           # List implementations
│   ├── Stack/                          # Stack implementations
│   ├── Tree/                           # Tree structures
│   └── UnionFind/                      # Union-Find implementation
├── run-tests.py                        # Automated test runner
├── shell-commands.txt                  # Usage instructions
└── README.md                          # This file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

