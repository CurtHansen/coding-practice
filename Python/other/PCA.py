import numpy as np
from sklearn.decomposition import PCA


# Create some data.
np.random.seed(42)
n, p = 10, 4
X = np.random.random((n, p), )
col_means = np.reshape(np.mean(X, axis=0), (1, p))
X_c = X - np.ones((n, 1)).dot(col_means)

# Compute sample covariance matrix two ways, using function and by hand.
Sigma = np.cov(X, rowvar=False)
Sigma_alt = (1/(n-1)) * X_c.T.dot(X_c)
assert (Sigma - Sigma_alt < 1e-15).all()

# Perform SVD on X_c.
U, S, VT = np.linalg.svd(X_c)
V = VT.T

# Perform eigen decompositions.
eye_sigma, v_sigma = np.linalg.eig(Sigma)
eye_Xc, v_Xc = np.linalg.eig(X_c.T.dot(X_c))
eye_Xc_ordering = np.argsort(eye_Xc)[::-1]

'''Checks'''
# Check that singular values are the square roots of the ordered eigenvalues.
assert all(abs(S**2 - eye_Xc[eye_Xc_ordering]) < 1e-14)

# Check that the V matrix from the SVD of X_c is the same as the eigenvectors of X_c'X_c.
def check_cols(x, y): return all(abs(x-y) < 1e-14) or all(abs(x+y) < 1e-14)
for col_idx in range(V.shape[1]):
    assert check_cols(V[:, col_idx], v_Xc[:, eye_Xc_ordering[col_idx]])

# Check that eigenvectors of X_c'X_c are orthonormal, meaning that the V is orthogonal.
assert (VT.dot(V) - np.identity(p) < 1e-14).all()

# Check reconstruction using increasing number of principal components.
# Compare against PCs using PC function.
for num_pc in range(1, p+1):
    approx = X.dot(V[:, :num_pc])
    recons = approx.dot(VT[:num_pc, :])
    print("Using {} pcs, Frobenius norm of error is {}".format(num_pc, np.linalg.norm(X-recons)))
    pc = PCA(n_components=num_pc)
    pc.fit(X)
    print("Frobenius norm of difference between PCA-generated 'components' and V: {}".
          format(np.linalg.norm(V[:, :num_pc] - pc.components_.T[:])))
    print(pc.explained_variance_ratio_)
    print(eye_sigma[eye_Xc_ordering][:num_pc]/eye_sigma.sum())
