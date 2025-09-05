import numpy as np
import pandas as pd
import math

def minmax_scaling(data):
    """Apply Min-Max normalization to scale data to [0, 1]."""
    data_min, data_max = data.min(), data.max()
    return (data - data_min) / (data_max - data_min)

def zscore_scaling(data):
    """Apply Z-score normalization."""
    mu = data.mean()
    sigma = data.std(ddof=0)  # population std unless otherwise specified
    return (data - mu) / sigma

def decimal_scaling(data):
    """Apply decimal scaling so that |value| < 1."""
    max_abs = np.max(np.abs(data))
    j = int(math.ceil(math.log10(max_abs + 1e-12)))  # +tiny to avoid log10(0)
    return data / (10 ** j)
