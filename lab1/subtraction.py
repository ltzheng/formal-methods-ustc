from z3 import *


def str2bools(bin_str, var_name):
    bools = []
    for i, s in enumerate(reversed(bin_str)):  # from right to left
        if s == '1':
            bools.append(Bool(var_name + str(i)))
        else:
            bools.append(Not(Bool(var_name + str(i))))

    return And(bools)

def requirements(n):
    con1 = And(Not(Bool('c0')), Not(Bool('c' + str(n + 1))))
    con2 = []
    con3 = []
    for i in range(n):
        str_i = str(i)
        ai, bi, ci, di, ciplus1 = Bool('a' + str_i), Bool('b' + str_i), Bool('c' + str_i), Bool('d' + str_i), Bool('c' + str(i + 1))
        con2.append(And([di == (ai == (bi == ci))]))
        con3.append(And([ciplus1 == (Or(And(bi, ci), And(Not(ai), bi, Not(ci)), And(Not(ai), Not(bi), ci)))]))
    
    return And(con1, And(con2), And(con3))

def subtract(str_a, str_b):
    print('a:', str_a)
    print('b:', str_b)

    s = Solver()
    a = str2bools(str_a, 'a')  # operand a
    b = str2bools(str_b, 'b')  # operand b
    constraints = requirements(len(str_a))
    s.add(And(a, b, constraints))
    s.check()
    m = s.model()

    # only print assignments for the result, namely, d
    res = sorted([(d, m[d]) for d in m if 'd' in str(d)], key=lambda x: str(x[0]), reverse=True)
    print(res)

    # return result in binary format
    result = ''
    for digit in res:
        result += '1' if digit[1] else '0'

    return result


if __name__ == '__main__':
    a = 1000
    b = 100

    # convert to binary string format
    a = bin(a)[2:]
    b = bin(b)[2:]

    # fill leading zero to align 2 numbers
    max_len = max(len(a), len(b))
    result = subtract(a.zfill(max_len), b.zfill(max_len))  
    print('a - b:', result)