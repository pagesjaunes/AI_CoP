

import numpy as np


def gaussian(mean, cov, n):
    return np.random.multivariate_normal(mean, cov, n)

