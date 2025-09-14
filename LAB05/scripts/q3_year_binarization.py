import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Must be before importing pyplot
import numpy as np
import matplotlib.pyplot as plt
from utils import setup_paths, save_plot, save_table, PASTEL_COLORS

def binarize_year():
    try:
        # Setup paths
        data_dir, output_dir, plots_dir, tables_dir = setup_paths()
        
        # Create calculations directory
        calculations_dir = output_dir / 'calculations'
        calculations_dir.mkdir(exist_ok=True)
        
        # Read the dataset
        df = pd.read_csv(data_dir / 'avocado.csv')
        # Ensure year column is numeric
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
        
        # Binarize the Year attribute
        df['Year_binary'] = (df['year'] > 2016).astype(int)
        
        # Create a subset for visualization
        year_data = df[['year', 'Year_binary']].copy()
        
        # Save processed dataset
        save_table(year_data.head(20), 'q3_binarized_year.csv', tables_dir, plots_dir)
        
        # Create visualization
        plt.figure(figsize=(10, 6))
        year_counts = df['Year_binary'].value_counts().sort_index()
        plt.bar(['2016 and earlier', 'After 2016'], 
                year_counts.values, 
                color=PASTEL_COLORS[:2])
        plt.title('Distribution of Binarized Year')
        plt.ylabel('Count')
    
        # Add count labels
        for i, v in enumerate(year_counts.values):
            plt.text(i, v, str(v), ha='center', va='bottom')
        
        # Save plot and close figure
        save_plot(plt, 'q3_year_distribution.png', plots_dir)
        plt.close()
        
        # Save analysis to text file
        with open(calculations_dir / 'q3_binarization_details.txt', 'w') as f:
            f.write("Year Binarization Analysis\n")
            f.write("=" * 50 + "\n\n")
            
            f.write("Overall Statistics:\n")
            f.write("-" * 20 + "\n")
            f.write(f"Total records: {len(df)}\n")
            f.write(f"Year range: {df['year'].min()} to {df['year'].max()}\n")
            f.write(f"Threshold: 2016\n\n")
            
            f.write("Distribution:\n")
            f.write("-" * 20 + "\n")
            for binary_val, count in year_counts.items():
                label = "After 2016" if binary_val == 1 else "2016 and earlier"
                f.write(f"{label}: {count} records ({(count/len(df))*100:.2f}%)\n")
    
        # Display results
        print("\nFirst 20 records of binarized data:")
        print(year_data.head(20).to_string())
        print("\nResults saved in output directory.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    binarize_year()

if __name__ == '__main__':
    binarize_year()
