# 2D Site Percolation Study  
C++ simulations analyzing critical probabilities, cluster statistics, and computational efficiency in square lattices.

## **Features**  
- Depth-first search (DFS) with edge-connectivity optimization.  
- Parallelized statistical sampling (50+ seeds per configuration).  
- Integrated profiling, debugging, and CI/CD workflows.  

## **Makefile Workflow**  
| Command          | Action                                                                 |
|------------------|-----------------------------------------------------------------------|
| `make analisis`  | Full analysis: Compiles, runs simulations (all L/p/optimization levels), and generates PDF plots. |
| `make simul ARGS`| Single simulation with custom L/p/seed + visualizes percolating cluster. |
| `make test`      | Unit tests (Catch2) for edge cases: empty/full grids and horizontal/vertical percolation. |
| `make debug`     | Debug build (GDB) for error analysis.                                |
| `make valgrind ARGS` | Memory leak detection (Valgrind).                              |
| `make profile ARGS`  | Performance reports (`perf`/`gprof`) for optimized/unoptimized code. |
| `make coverage`  | Generates HTML code coverage report (gcovr).                         |
| `make report`    | Compiles LaTeX report with results.                                  |
| `make clean`     | Removes binaries, temporary files, and output data.                  |

## **Usage**  
```bash  
make analisis      # Full pipeline (simulations + plots)  
make simul L=64 p=0.59  # Quick test with visualization  
