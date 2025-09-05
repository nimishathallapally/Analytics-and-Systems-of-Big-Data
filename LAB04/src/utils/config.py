import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
OUT_BASE = os.path.join(PROJECT_ROOT, "outputs")

# Q1 specific paths
Q1_DATA_DIR = os.path.join(DATA_DIR, "q1")
Q1_OUT_TABLES = os.path.join(OUT_BASE, "q1", "tables")
Q1_OUT_PLOTS = os.path.join(OUT_BASE, "q1", "plots")

# Q2 specific paths
Q2_DATA_DIR = os.path.join(DATA_DIR, "q2")
Q2_OUT_TABLES = os.path.join(OUT_BASE, "q2", "tables")
Q2_OUT_PLOTS = os.path.join(OUT_BASE, "q2", "plots")
Q2_IN_CSV = os.path.join(Q2_DATA_DIR, "avocado.csv")

# Plot styling
COLORS = {
    "base": "#a6cee3",   # light blue
    "alt1": "#b2df8a",   # light green
    "alt2": "#fdbf6f",   # light orange
    "alt3": "#cab2d6"    # light purple
}

GRID_KW = dict(alpha=0.3, linestyle="--", linewidth=0.7)

# Create directories
for dir_path in [Q1_DATA_DIR, Q1_OUT_TABLES, Q1_OUT_PLOTS,
                 Q2_DATA_DIR, Q2_OUT_TABLES, Q2_OUT_PLOTS]:
    os.makedirs(dir_path, exist_ok=True)
