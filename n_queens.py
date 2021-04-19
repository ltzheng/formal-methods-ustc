from z3 import *
import time


def smt(n):
    Q = [Int('Q_%i' % (i + 1)) for i in range(n)]
    val_c = [And(1 <= Q[i], Q[i] <= n) for i in range(n)]
    col_c = [Distinct(Q)]
    diag_c = [If(i == j, True, And(i+Q[i]!=j+Q[j], i+Q[j]!=j+Q[i])) for i in range(n) for j in range(i)]

    smt_start = time.time()
    solve(val_c + col_c + diag_c)
    smt_end = time.time()
    print('elapsed time of SMT (ms): %s' % ((smt_end - smt_start) * 1000))

def row_con(n):
    # at least one queen on row i
    con1 = And([Or([Bool(str(i) + str(j)) for j in range(n)]) for i in range(n)])

    # at most one queen on row i
    con2 = And([And([Or(Not(Bool(str(i) + str(j))), Not(Bool(str(i) + str(k)))) for j in range(n) for k in range(j)]) for i in range(n)])

    return And(con1, con2)

def col_con(n):
    # at least one queen on column i
    con1 = And([Or([Bool(str(i) + str(j)) for i in range(n)]) for j in range(n)])

    # at most one queen on column i
    con2 = And([And([Or(Not(Bool(str(i) + str(j))), Not(Bool(str(k) + str(j)))) for i in range(n) for k in range(i)]) for j in range(n)])
    
    return And(con1, con2)

def diag_con(n):
    # at most one queen on main diagonal
    con1 = And([And([Or(Not(Bool(str(i) + str(j))), Not(Bool(str(i_prime) + str(i_prime - i + j)))) for j in range(n) if i_prime - i + j >= 0 and i_prime - i + j < n]) for i_prime in range(n) for i in range(i_prime)])

    # at most one queen on counter diagonal
    con2 = And([And([Or(Not(Bool(str(i) + str(j))), Not(Bool(str(i_prime) + str(i + j - i_prime)))) for j in range(n) if i + j - i_prime >= 0 and i + j - i_prime < n]) for i_prime in range(n) for i in range(i_prime)])

    return And(con1, con2)

def pure_sat(n):
    con1, con2, con3 = row_con(n), col_con(n), diag_con(n)
    sat_start = time.time()
    solve(con1, con2, con3)
    sat_end = time.time()
    print('elapsed time of pure SAT (ms): %s' % ((sat_end - sat_start) * 1000))

if __name__ == '__main__':
    n = 20
    print('smt solution:\n')
    smt(n)
    print('\npure sat solution:\n')
    pure_sat(n)