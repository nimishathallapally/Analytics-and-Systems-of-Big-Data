#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q2: Avocado dataset processing

Input:
  data/q2/avocado.csv

Tasks:
  a) Sort "Total Volume" and bin into equal-frequency (250 bins). Smooth by:
     (i) bin-means, (ii) bin-medians, (iii) bin-boundaries.
  b) Reduce weekly data to monthly and yearly totals (Total Volume).
  c) Summarize missing values per attribute.
  d) Impute missing "AveragePrice" by region-wise mean.
  e) Discretize "Date" via concept hierarchy into {Old, New, Recent}.
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

from src.utils.config import (Q2_IN_CSV, Q2_OUT_TABLES, Q2_OUT_PLOTS,
                            COLORS, GRID_KW)
from src.data_processing.binning import (equal_frequency_bins,
                                       smooth_by_mean,
                                       smooth_by_median,
                                       smooth_by_boundaries)
from src.data_processing.avocado_processing import (load_and_preprocess_avocado,
                                                   get_time_aggregations,
                                                   impute_by_region_mean,
                                                   map_date_to_category)
from src.visualization.plotting import (save_bar, save_line, save_hist,
                                      save_smoothing_plot)

def process_equal_frequency_binning(df):
    """Process equal-frequency binning and smoothing."""
    # Get Total Volume data
    tv = df["total_volume"].astype(float).dropna().values
    nbins = min(250, max(1, len(tv)))
    
    # Create equal frequency bins
    bins = equal_frequency_bins(tv, nbins)
    
    # Get the sorted version for visualization
    tv_sorted = np.sort(tv)
    
    # Apply smoothing methods
    smooth_means = smooth_by_mean(tv, bins)
    smooth_medians = smooth_by_median(tv, bins)
    smooth_bounds = smooth_by_boundaries(tv, bins)
    
    # Sort smoothed results in same order as original for visualization
    sort_idx = np.argsort(tv)
    smooth_means_sorted = smooth_means[sort_idx]
    smooth_medians_sorted = smooth_medians[sort_idx]
    smooth_bounds_sorted = smooth_bounds[sort_idx]
    
    # Save results
    df_smooth = pd.DataFrame({
        "total_volume": tv,
        "total_volume_sorted": tv_sorted,
        "smooth_bin_mean": smooth_means_sorted,
        "smooth_bin_median": smooth_medians_sorted,
        "smooth_bin_boundaries": smooth_bounds_sorted
    })
    df_smooth.to_csv(os.path.join(Q2_OUT_TABLES, "q2a_total_volume_binning_and_smoothing.csv"), index=False)

    # Create plots
    # Plot original data distribution
    plt.figure(figsize=(9.5, 5.3), dpi=140)
    plt.hist(tv_sorted, bins=40, edgecolor="#333333", alpha=0.9, color=COLORS["alt2"])
    plt.title("Distribution of Total Volume (Original Data)", pad=12)
    plt.xlabel("Total Volume")
    plt.ylabel("Frequency")
    plt.grid(**GRID_KW)
    plt.tight_layout()
    plt.savefig(os.path.join(Q2_OUT_PLOTS, "q2a_total_volume_hist.png"))
    plt.close()
    
    # Create line plots to show the smoothing effects
    save_smoothing_plot(tv_sorted, smooth_means_sorted,
                       "Smoothed by Bin Means", COLORS["alt1"],
                       os.path.join(Q2_OUT_PLOTS, "q2a_smoothing_bin_means.png"))
    
    save_smoothing_plot(tv_sorted, smooth_medians_sorted,
                       "Smoothed by Bin Medians", COLORS["alt2"],
                       os.path.join(Q2_OUT_PLOTS, "q2a_smoothing_bin_medians.png"))
    
    save_smoothing_plot(tv_sorted, smooth_bounds_sorted,
                       "Smoothed by Bin Boundaries", COLORS["alt3"],
                       os.path.join(Q2_OUT_PLOTS, "q2a_smoothing_bin_boundaries.png"))

def process_time_aggregations(df):
    """Process and save time-based aggregations."""
    annual_total, monthly_total, annual_by_region, monthly_by_region = get_time_aggregations(df)

    # Save results
    annual_total.to_csv(os.path.join(Q2_OUT_TABLES, "q2b_annual_total_volume_overall.csv"))
    monthly_total.to_csv(os.path.join(Q2_OUT_TABLES, "q2b_monthly_total_volume_overall.csv"))
    annual_by_region.to_csv(os.path.join(Q2_OUT_TABLES, "q2b_annual_total_volume_by_region.csv"), index=False)
    monthly_by_region.to_csv(os.path.join(Q2_OUT_TABLES, "q2b_monthly_total_volume_by_region.csv"), index=False)

    # Create plots
    save_bar(annual_total,
            "Annual Total Volume (overall)",
            "Year", "Total Volume",
            os.path.join(Q2_OUT_PLOTS, "q2b_annual_total_overall.png"))
    
    # For monthly, plot as line by chronological order
    monthly_total_indexed = monthly_total.copy()
    monthly_total_indexed.index = pd.to_datetime(monthly_total_indexed.index)
    monthly_total_indexed = monthly_total_indexed.sort_index()
    save_line(monthly_total_indexed,
             "Monthly Total Volume (overall)",
             "Month", "Total Volume",
             os.path.join(Q2_OUT_PLOTS, "q2b_monthly_total_overall.png"))

def process_missing_values(df):
    """Analyze and visualize missing values."""
    na_counts = df.isna().sum().sort_values(ascending=False)
    na_counts.to_csv(os.path.join(Q2_OUT_TABLES, "q2c_missing_values_summary.csv"),
                     header=["missing_count"])
    
    save_bar(na_counts,
            "Missing Values per Attribute",
            "Attribute", "Missing count",
            os.path.join(Q2_OUT_PLOTS, "q2c_missing_values_bar.png"),
            rotate=60)

def process_price_imputation(df):
    """Impute missing prices and visualize results."""
    df_before_imp = df.copy()
    df_imputed = impute_by_region_mean(df)
    
    # Save imputed dataset
    df_imputed.to_csv(os.path.join(Q2_OUT_TABLES, "q2d_dataset_imputed_averageprice_by_region.csv"),
                      index=False)

    # Visualize pre vs post imputation
    plt.figure(figsize=(10, 5.2), dpi=140)
    plt.hist(df_before_imp["averageprice"].dropna(), bins=40, alpha=0.75,
            label="Before (non-missing)", edgecolor="#333333", color=COLORS["base"])
    plt.hist(df_imputed["averageprice"].dropna(), bins=40, alpha=0.55,
            label="After Imputation", edgecolor="#333333", color=COLORS["alt1"])
    plt.title("AveragePrice – Before vs After Region-Mean Imputation", pad=12)
    plt.xlabel("AveragePrice")
    plt.ylabel("Frequency")
    plt.legend(frameon=True)
    plt.grid(alpha=0.3, linestyle="--", linewidth=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(Q2_OUT_PLOTS, "q2d_averageprice_imputation_hist.png"))
    plt.close()
    
    return df_imputed

def process_date_categorization(df):
    """Categorize dates and visualize results."""
    df_categorized = map_date_to_category(df)
    
    # Save categorized dataset
    df_categorized.to_csv(os.path.join(Q2_OUT_TABLES, "q2e_dataset_with_date_category.csv"),
                         index=False)

    # Plot category counts
    cat_counts = df_categorized["date_category"].value_counts(dropna=False)
    save_bar(cat_counts,
            "Date Category Counts",
            "Date Category", "Count",
            os.path.join(Q2_OUT_PLOTS, "q2e_date_category_counts.png"))

def main():
    # Load and preprocess data
    df = load_and_preprocess_avocado(Q2_IN_CSV)
    
    # Process each task
    process_equal_frequency_binning(df)
    process_time_aggregations(df)
    process_missing_values(df)
    df_imputed = process_price_imputation(df)
    process_date_categorization(df_imputed)
    
    print("Q2 done. Outputs saved under:", Q2_OUT_PLOTS)

if __name__ == "__main__":
    main()
