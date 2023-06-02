import ulab.numpy as np

# matrix inversion example
a = np.array([[1., 2.], [3., 4.]])
a_inv = np.linalg.inv(a)

# sanity check
assert np.allclose(np.dot(a, a_inv), np.eye(2))
assert np.allclose(np.dot(a_inv, a), np.eye(2))
