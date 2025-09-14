import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from utils import setup_paths, save_plot, save_table, PASTEL_COLORS

def handle_missing_values():
    # Setup paths
    data_dir, _, plots_dir, tables_dir = setup_paths()
    
    # Read the dataset
    df = pd.read_csv(data_dir / 'avocado.csv')
    
    # Calculate nullity by column
    nullity = df.isnull().sum().sort_values(ascending=False)
    nullity_percent = (nullity / len(df) * 100).round(2)
    
    # Create nullity summary
    nullity_df = pd.DataFrame({
        'Missing Values': nullity,
        'Percentage': nullity_percent
    })
    save_table(nullity_df, 'q6_7_nullity_summary.csv', tables_dir)
    
    # Visualize nullity
    plt.figure(figsize=(12, 6))
    nullity_percent.plot(kind='bar', color=PASTEL_COLORS)
    plt.title('Percentage of Missing Values by Column')
    plt.xlabel('Columns')
    plt.ylabel('Percentage of Missing Values')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    save_plot(plt, 'q6_7_nullity_distribution.png', plots_dir)
    
    # Drop columns with high nullity (>50%)
    high_nullity_cols = nullity_percent[nullity_percent > 50].index
    df_cleaned = df.drop(columns=high_nullity_cols)
    
    # Remove rows with any remaining missing values
    df_no_nulls = df_cleaned.dropna()
    
    # Save processed datasets
    save_table(df_cleaned, 'q6_7_cleaned_data.csv', tables_dir)
    
    # Print summary
    print(f"Original dataset shape: {df.shape}")
    print(f"Shape after dropping high-nullity columns: {df_cleaned.shape}")
    print(f"Shape after dropping rows with missing values: {df_no_nulls.shape}")
    
    # Visualize dataset size changes
    plt.figure(figsize=(10, 6))
    sizes = [df.shape[0], df_cleaned.shape[0], df_no_nulls.shape[0]]
    labels = ['Original', 'After dropping\nhigh-nullity columns', 'After dropping\nall null values']
    plt.bar(labels, sizes, color=PASTEL_COLORS[:3])
    plt.title('Dataset Size at Different Cleaning Stages')
    plt.ylabel('Number of Records')
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_plot(plt, 'q6_7_dataset_size_changes.png', plots_dir)

if __name__ == '__main__':
    handle_missing_values()
