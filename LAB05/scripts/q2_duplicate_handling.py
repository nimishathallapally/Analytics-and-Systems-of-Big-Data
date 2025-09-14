import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from utils import setup_paths, save_plot, save_table, PASTEL_COLORS

def process_duplicates():
    # Setup paths
    data_dir, output_dir, plots_dir, tables_dir = setup_paths()
    
    # Create calculations directory
    calculations_dir = output_dir / 'calculations'
    calculations_dir.mkdir(exist_ok=True)
    
    # Read the Trail dataset
    df = pd.read_csv(data_dir / 'Trail.csv', na_values=['NA', 'NaN', 'na', 'n/a', ''])
    
    # Print original size
    original_size = len(df)
    print(f"Original dataset size: {original_size}")
    
    # Convert AveragePrice to numeric, coercing errors to NaN
    df['AveragePrice'] = pd.to_numeric(df['AveragePrice'], errors='coerce')
    
    # Get original missing values count and statistics before filling
    original_missing = df['AveragePrice'].isna().sum()
    original_mean = df['AveragePrice'].mean()
    
    # Fill missing values in AveragePrice
    df['AveragePrice'] = df['AveragePrice'].fillna(1.25)
    
    # Remove duplicates
    df_no_duplicates = df.drop_duplicates()
    final_size = len(df_no_duplicates)
    print(f"Dataset size after removing duplicates: {final_size}")
    
    # Save processed dataset as both CSV and PNG
    save_table(df_no_duplicates, 'q2_processed_trail.csv', tables_dir, plots_dir)
    
    # Create summary DataFrame
    summary_df = pd.DataFrame({
        'Stage': ['Original', 'After removing duplicates'],
        'Number of Records': [original_size, final_size],
        'Average Price': [original_mean, df_no_duplicates['AveragePrice'].mean()],
        'Missing Values': [original_missing, 0]  # 0 after filling with 1.25
    })
    
    # Save summary as both CSV and PNG
    save_table(summary_df, 'q2_processing_summary.csv', tables_dir, plots_dir)
    
    # Visualize the change in dataset size
    plt.figure(figsize=(8, 6))
    plt.bar(['Original', 'After removing duplicates'], [original_size, final_size], color=PASTEL_COLORS[:2])
    plt.title('Dataset Size Comparison')
    plt.ylabel('Number of Records')
    save_plot(plt, 'q2_size_comparison.png', plots_dir)
    
    # Save detailed calculations and analysis
    with open(calculations_dir / 'q2_processing_details.txt', 'w') as f:
        f.write("Trail Dataset Processing - Detailed Analysis\n")
        f.write("=" * 50 + "\n\n")
        
        # Dataset statistics
        f.write("Dataset Statistics:\n")
        f.write("-" * 20 + "\n")
        f.write(f"Original number of records: {original_size}\n")
        f.write(f"Number of duplicates found: {original_size - final_size}\n")
        f.write(f"Final number of records: {final_size}\n")
        f.write(f"Percentage of duplicates: {((original_size - final_size)/original_size)*100:.2f}%\n\n")
        
        # Missing values analysis
        f.write("Missing Values Analysis:\n")
        f.write("-" * 20 + "\n")
        f.write(f"Original missing values in AveragePrice: {original_missing}\n")
        f.write(f"Missing values after filling with 1.25: 0\n\n")
        
        # Price statistics
        f.write("Price Statistics:\n")
        f.write("-" * 20 + "\n")
        f.write("Before processing:\n")
        f.write(f"Mean price: {df['AveragePrice'].mean():.2f}\n")
        f.write(f"Median price: {df['AveragePrice'].median():.2f}\n")
        f.write(f"Standard deviation: {df['AveragePrice'].std():.2f}\n\n")
        
        f.write("After processing:\n")
        f.write(f"Mean price: {df_no_duplicates['AveragePrice'].mean():.2f}\n")
        f.write(f"Median price: {df_no_duplicates['AveragePrice'].median():.2f}\n")
        f.write(f"Standard deviation: {df_no_duplicates['AveragePrice'].std():.2f}\n")

if __name__ == '__main__':
    process_duplicates()
