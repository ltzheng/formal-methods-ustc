import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
n = [4, 8, 16, 20, 32, 40]
smt_time = [45.1522, 105.8621, 279.2518, 732.4312, 2338.5613, 25855.8326]
sat_time = [37.2417, 51.8267, 188.3368, 195.6971, 439.6229, 849.2498]
plt.plot(n, smt_time, label='SMT')
plt.plot(n, sat_time, label='pure SAT')

plt.legend(loc='upper left')
plt.xlabel('N')
plt.ylabel('Elapsed Time (ms)')
plt.title('Comparison between SMT and pure SAT')

plt.savefig("n_queens.png")
plt.show()