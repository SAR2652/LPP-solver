import argparse
import numpy as np
import pandas as pd
from scipy.optimize import linprog

# utility
constraint_mapping = {
    '<=': 1,
    '>=': -1,
}

parser = argparse.ArgumentParser()
parser.add_argument('filepath',
                    help='Path to the CSV file that has the following header:\n'
                    "coeff_x1,coeff_x2,...,coeff_xn,bound_type,bound_value\n"
                    'and contains data in the same format within each line',
                    type=str)
parser.add_argument('--verbose',
                    help='Display Intermediate Calculations',
                    action='store_true')


args = parser.parse_args()
file = args.filepath
verbose = args.verbose

n = int(input("Enter the number of variables: "))

coeffs = []
print("Enter their minimization coefficients: ")

for i in range(n):
    ci = int(input(f"c{i + 1}: "))
    coeffs.append(ci)

if len(coeffs) != n:
    print("Number of variables is not equal to the number of coefficients!\n"
    "Aborting further processing!")

df = pd.read_csv(file)

if n != df.shape[1] - 2:
    print('Number of variables is not equal to the number of coefficient '
    'columns within input data')
    exit(1)

if verbose:
    print(f"Total number of constraints = {df.shape[0]}")
    print(f'Preview of Data (first 5 rows):\n{df.head()}')

# Map bound types to their corresponding matrix operations
df['constraint_type'] = df['constraint_type'].replace(constraint_mapping)
if verbose:
    print(f'Preview after mapping constraint types:\n{df.head()}')

bound = df['constraint_type'].values.reshape(-1, 1)
df.drop(['constraint_type'], axis=1, inplace=True)

if verbose:
    print(f'Preview after discarding constraint types:\n{df.head()}')

Ab_raw = df.values
Ab = Ab_raw * bound
A = Ab[:, :-1]
b = Ab[:, -1].reshape(-1, 1)
c = np.array(coeffs)

if verbose:
    print(f'Minimization Coefficients (c):\n{c}')
    print(f'Inequality Constraint Matrix (A):\n{A}')
    print(f'Inequality Constraint Vector (b):\n{b}')

res = linprog(c, A_ub=A, b_ub=b, method='highs')

if not res['success']:
    print('Result failed to compute!')
    exit(1)

if verbose:
    print(f'Result in detail:\n{res}')

print('The decision variable values are:')
for i, val in enumerate(res['x']):
    print(f'x{i + 1} = {val:.2f}')

result = c @ res['x']

print(f'Minimum budget amount required is {result:.2f}.')
