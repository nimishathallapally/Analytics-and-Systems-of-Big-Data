#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q1: Normalization of 'age' values
- (a) Min-Max normalization to [0, 1]
- (b) Z-score normalization
- (c) Decimal scaling so that |value| < 1
"""

import os
import sys

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from src.utils.config import (Q1_OUT_TABLES, Q1_OUT_PLOTS, 
                            COLORS)
from src.data_processing.normalization import (minmax_scaling,
                                             zscore_scaling,
                                             decimal_scaling)
from src.visualization.plotting import save_hist

def main():
    # Given ages (sorted)
    ages = [
        13, 15, 16, 16, 19, 20, 20, 21, 22, 22,
        25, 25, 25, 25, 30, 33, 33, 35, 35, 35,
        35, 36, 40, 45, 46, 52, 70
    ]
    ages = np.array(ages, dtype=float)

    # Apply normalizations
    minmax = minmax_scaling(ages)
    zscore = zscore_scaling(ages)
    dec_scaled = decimal_scaling(ages)

    # Save results to CSV
    df_out = pd.DataFrame({
        "age": ages,
        "minmax_[0,1]": minmax,
        "zscore": zscore,
        "decimal_scaled": dec_scaled
    })
    df_out.to_csv(os.path.join(Q1_OUT_TABLES, "q1_normalizations.csv"), index=False)

    # Create comparison scatter plot
    x = np.arange(len(ages))
    plt.figure(figsize=(10, 5.5), dpi=140)
    plt.scatter(x, ages, label="Original age", s=36, edgecolor="none", c=COLORS["base"])
    plt.scatter(x, minmax, label="Min-Max [0,1]", s=30, edgecolor="none", c=COLORS["alt1"])
    plt.scatter(x, zscore, label="Z-score", s=30, edgecolor="none", c=COLORS["alt2"])
    plt.scatter(x, dec_scaled, label="Decimal scaled", s=30, edgecolor="none", c=COLORS["alt3"])
    plt.title("Age – Original vs. Normalized", pad=12)
    plt.xlabel("Tuple index (sorted by age)")
    plt.ylabel("Value")
    plt.grid(alpha=0.3, linestyle="--", linewidth=0.7)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(os.path.join(Q1_OUT_PLOTS, "q1_scatter_comparison.png"))
    plt.close()

    # Save histograms
    save_hist(pd.Series(ages, name="Age"), 
             "Original Age Distribution",
             os.path.join(Q1_OUT_PLOTS, "q1_hist_original.png"), 
             bins=10, 
             color=COLORS["base"])
    
    save_hist(pd.Series(minmax, name="Min-Max [0,1]"),
             "Min-Max [0,1] Distribution",
             os.path.join(Q1_OUT_PLOTS, "q1_hist_minmax.png"),
             bins=10,
             color=COLORS["alt1"])
    
    save_hist(pd.Series(zscore, name="Z-score"),
             "Z-score Distribution",
             os.path.join(Q1_OUT_PLOTS, "q1_hist_zscore.png"),
             bins=10,
             color=COLORS["alt2"])
    
    save_hist(pd.Series(dec_scaled, name="Decimal-Scaled"),
             "Decimal-Scaled Distribution",
             os.path.join(Q1_OUT_PLOTS, "q1_hist_decimal_scaled.png"),
             bins=10,
             color=COLORS["alt3"])

    print("Q1 done.")

if __name__ == "__main__":
    main()
