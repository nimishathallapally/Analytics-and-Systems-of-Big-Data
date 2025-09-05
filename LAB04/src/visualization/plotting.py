import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ..utils.config import COLORS, GRID_KW

def save_bar(values, title, xlabel, ylabel, outpath, rotate=0):
    plt.figure(figsize=(10, 5.5), dpi=140)
    ax = plt.gca()
    values.plot(kind="bar", ax=ax, color=COLORS["base"], edgecolor="#333333")
    plt.title(title, pad=12)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if rotate:
        plt.xticks(rotation=rotate, ha="right")
    plt.grid(**GRID_KW, axis="y")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def save_line(df_xy, title, xlabel, ylabel, outpath):
    plt.figure(figsize=(10.5, 5.5), dpi=140)
    plt.plot(df_xy.index, df_xy.values, marker="o", linewidth=1.8, markersize=3.5, color=COLORS["alt1"])
    plt.title(title, pad=12)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(**GRID_KW)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def save_hist(series, title, outpath, bins=40, color=COLORS["alt2"]):
    plt.figure(figsize=(9.5, 5.3), dpi=140)
    plt.hist(series.dropna().values, bins=bins, edgecolor="#333333", alpha=0.9, color=color)
    plt.title(title, pad=12)
    plt.xlabel(series.name)
    plt.ylabel("Frequency")
    plt.grid(**GRID_KW)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def save_smoothing_plot(original, smoothed, label, color, outpath):
    x = np.arange(len(original))
    plt.figure(figsize=(11, 5.8), dpi=140)
    plt.plot(x, original, linewidth=1.2, alpha=0.7, label="Original (sorted)", color=COLORS["base"])
    plt.plot(x, smoothed, linewidth=1.8, alpha=0.95, label=label, color=color)
    plt.title(f"Total Volume – {label}", pad=12)
    plt.xlabel("Index (after sorting by Total Volume)")
    plt.ylabel("Total Volume")
    plt.grid(**GRID_KW)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
