import ulab.numpy as np

print('Numpy example')

# matrix inversion example
a = np.array([[1., 2.], [3., 4.]])
print(f'a:\n{a}')
a_inv = np.linalg.inv(a)
print(f'a_inv:\n{a_inv}')

# sanity check
print(f'a * a_inv:\n{np.dot(a, a_inv)}')

print('Done')
