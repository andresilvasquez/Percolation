# 2D Site Percolation Study  

C++ simulations analyzing critical probabilities, cluster statistics, and computational efficiency in square lattices.  
This project explores how random occupation of lattice sites leads to the emergence of percolating clusters and the transition near the critical probability.  

---

## **Introduction**  
Percolation theory studies how connectivity emerges in random systems. In this project, we model 2D site percolation on square lattices, assigning each site as occupied with probability *p*. Clusters are identified via depth-first search (DFS), and we analyze whether a percolating cluster spans the lattice.  

**Example of a 128×128 lattice at p = 0.6 (seed = 15):**  
- Black: empty sites  
- White: occupied but non-percolating sites  
- Blue: percolating cluster  

![Percolation lattice example](malla.pdf)  

---

## **Main Results**  

### Probability of Percolation  
The file `Probabilidadcluster.pdf` shows the probability that a cluster percolates as a function of system size and occupation probability *p*.  
- As the lattice size increases, the data converges towards the critical probability for 2D site percolation (*p_c ≈ 0.5927*).  
- This illustrates the phase transition between non-percolating and percolating regimes.  

![Percolation probability](Probabilidadcluster.pdf)  

### Largest Cluster Size  
The file `Tamanocluster.pdf` presents the mean relative size (normalized by grid size) of the largest percolating cluster as a function of lattice size and occupation probability *p*.  
- Near *p_c*, the largest cluster grows rapidly and dominates the system.  
- Results match theoretical expectations of scaling behaviour in percolation.  

![Largest cluster size](Tamanocluster.pdf)  

---

## **Features**  
- Depth-first search (DFS) with edge-connectivity optimization.  
- Parallelized statistical sampling (50+ seeds per configuration).  
- Integrated profiling, debugging, and CI/CD workflows.  

---

## **Makefile Workflow**  
| Command             | Action                                                                 |
|---------------------|------------------------------------------------------------------------|
| `make analisis`     | Full analysis: Compiles, runs simulations (all L/p/optimization levels), and generates PDF plots. |
| `make simul ARGS`   | Single simulation with custom L/p/seed + visualizes percolating cluster. |
| `make test`         | Unit tests (Catch2) for edge cases: empty/full grids and horizontal/vertical percolation. |
| `make debug`        | Debug build (GDB) for error analysis.                                  |
| `make valgrind ARGS`| Memory leak detection (Valgrind).                                      |
| `make profile ARGS` | Performance reports (`perf`/`gprof`) for optimized/unoptimized code.   |
| `make coverage`     | Generates HTML code coverage report (gcovr).                           |
| `make report`       | Compiles LaTeX report with results.                                    |
| `make clean`        | Removes binaries, temporary files, and output data.                    |

---

## **Usage**  
```bash
make analisis             # Full pipeline (simulations + plots)  
make simul L=64 p=0.59    # Quick test with visualization  
