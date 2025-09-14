import pandas as pd
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import setup_paths, save_plot, save_table, PASTEL_COLORS

def statistical_summary():
    # Setup paths
    data_dir, _, plots_dir, tables_dir = setup_paths()
    
    # Read the dataset
    df = pd.read_csv(data_dir / 'avocado.csv')
    
    # Basic dataset information
    dataset_info = {
        'Dimensions': df.shape,
        'Datatypes': df.dtypes,
        'Most Frequent Values': {col: df[col].mode()[0] for col in df.columns}
    }
    
    # Save dataset info
    with open(tables_dir / 'q8_dataset_info.txt', 'w') as f:
        f.write(f"Dataset Dimensions: {dataset_info['Dimensions']}\n\n")
        f.write("Datatypes:\n")
        for col, dtype in dataset_info['Datatypes'].items():
            f.write(f"{col}: {dtype}\n")
        f.write("\nMost Frequent Values:\n")
        for col, value in dataset_info['Most Frequent Values'].items():
            f.write(f"{col}: {value}\n")
    
    # Statistical summary
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    stats_summary = df[numerical_cols].describe()
    stats_summary.loc['skew'] = df[numerical_cols].skew()
    save_table(stats_summary, 'q8_statistical_summary.csv', tables_dir)
    
    # Class distribution (Type)
    class_dist = df['type'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(class_dist.values, labels=class_dist.index, autopct='%1.1f%%', colors=PASTEL_COLORS)
    plt.title('Class Distribution (Type)')
    save_plot(plt, 'q8_class_distribution.png', plots_dir)
    
    # Correlation matrix
    plt.figure(figsize=(12, 10))
    correlation_matrix = df[numerical_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu', center=0)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    save_plot(plt, 'q8_correlation_matrix.png', plots_dir)
    
    # Skewness visualization
    plt.figure(figsize=(12, 6))
    skewness = df[numerical_cols].skew().sort_values()
    skewness.plot(kind='bar', color=PASTEL_COLORS)
    plt.title('Skewness by Attribute')
    plt.xlabel('Attributes')
    plt.ylabel('Skewness')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    save_plot(plt, 'q8_skewness.png', plots_dir)
    
    # Box plots for numerical attributes
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(numerical_cols):
        plt.subplot(1, len(numerical_cols), i+1)
        sns.boxplot(y=df[col], color=PASTEL_COLORS[i % len(PASTEL_COLORS)])
        plt.title(col)
    plt.tight_layout()
    save_plot(plt, 'q8_distributions.png', plots_dir)

if __name__ == '__main__':
    statistical_summary()
