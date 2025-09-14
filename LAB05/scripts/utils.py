import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# Set style for all plots
plt.style.use('default')  # Using default style instead of seaborn
# Set figure aesthetics for better visualization
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3

PASTEL_COLORS = ['#FFB3BA', '#BAFFC9', '#BAE1FF', '#FFFFBA', '#FFB3F7', '#B3F7FF']

def setup_paths():
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'
    output_dir = base_dir / 'outputs'
    plots_dir = output_dir / 'plots'
    tables_dir = output_dir / 'tables'
    
    # Create directories if they don't exist
    for dir_path in [output_dir, plots_dir, tables_dir]:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    return data_dir, output_dir, plots_dir, tables_dir

def save_plot(plt, filename, plots_dir):
    plt.savefig(plots_dir / filename, dpi=300, bbox_inches='tight')
    plt.close()

def save_table(df, filename, tables_dir, plots_dir=None):
    # Save as CSV
    df.to_csv(tables_dir / filename, index=False)
    
    # If plots_dir is provided, also save as image
    if plots_dir is not None:
        # Create figure with no margins
        plt.figure(figsize=(max(8, len(df.columns) * 2), max(6, len(df) * 0.3)))
        plt.axis('off')
        
        # Create table with clean style
        table = plt.table(
            cellText=df.values,
            colLabels=df.columns,
            cellLoc='center',
            loc='center',
            edges='closed'
        )
        
        # Style the table
        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1.2, 1.5)
        
        # Add alternating row colors for better readability
        for idx, cell in table._cells.items():
            if idx[0] == 0:  # Header
                cell.set_facecolor('#E6E6E6')
                cell.set_text_props(weight='bold')
            elif idx[0] % 2 == 0:  # Even rows
                cell.set_facecolor('#F5F5F5')
            else:  # Odd rows
                cell.set_facecolor('white')
        
        # Save table as image
        img_filename = filename.replace('.csv', '.png')
        plt.savefig(plots_dir / img_filename, dpi=300, bbox_inches='tight', pad_inches=0.5)
        plt.close()
