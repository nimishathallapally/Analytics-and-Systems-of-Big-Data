import numpy as np
import pandas as pd

def equal_frequency_bins(values: np.ndarray, nbins: int):
    """
    Create equal-frequency bins from the data.
    
    Args:
        values: Input array of values
        nbins: Number of bins to create
    
    Returns:
        bins: List of arrays containing indices for each bin
        bin_edges: Array of bin boundary values
    """
    n = len(values)
    # Calculate target size for each bin
    bin_size = n // nbins
    remainder = n % nbins
    
    # Sort indices based on values
    sorted_indices = np.argsort(values)
    
    bins = []
    current_idx = 0
    
    # Create bins with equal number of elements
    for i in range(nbins):
        # Add one extra element to some bins if n is not perfectly divisible by nbins
        current_bin_size = bin_size + (1 if i < remainder else 0)
        bin_indices = sorted_indices[current_idx:current_idx + current_bin_size]
        bins.append(bin_indices)
        current_idx += current_bin_size
    
    return bins

def smooth_by_mean(values: np.ndarray, bins):
    """
    Replace values in each bin with the bin mean.
    
    Args:
        values: Original array of values
        bins: List of arrays containing indices for each bin
    
    Returns:
        Array with values replaced by bin means
    """
    out = values.copy()
    for bin_indices in bins:
        if len(bin_indices) == 0:
            continue
        bin_values = values[bin_indices]
        mean_val = np.mean(bin_values)
        out[bin_indices] = mean_val
    return out

def smooth_by_median(values: np.ndarray, bins):
    """
    Replace values in each bin with the bin median.
    
    Args:
        values: Original array of values
        bins: List of arrays containing indices for each bin
    
    Returns:
        Array with values replaced by bin medians
    """
    out = values.copy()
    for bin_indices in bins:
        if len(bin_indices) == 0:
            continue
        bin_values = values[bin_indices]
        median_val = np.median(bin_values)
        out[bin_indices] = median_val
    return out

def smooth_by_boundaries(values: np.ndarray, bins):
    """
    Replace values in each bin with the nearest boundary (min or max) of that bin.
    
    Args:
        values: Original array of values
        bins: List of arrays containing indices for each bin
    
    Returns:
        Array with values replaced by nearest bin boundaries
    """
    out = values.copy()
    for bin_indices in bins:
        if len(bin_indices) == 0:
            continue
        bin_values = values[bin_indices]
        lo, hi = np.min(bin_values), np.max(bin_values)
        # For each value in the bin, replace with the nearest boundary
        for idx in bin_indices:
            val = values[idx]
            out[idx] = lo if abs(val - lo) <= abs(val - hi) else hi
    return out
