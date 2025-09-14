import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from utils import setup_paths, save_plot, save_table, PASTEL_COLORS

def process_organic_avocados():
    # Setup paths
    data_dir, output_dir, plots_dir, tables_dir = setup_paths()
    
    # Create calculations directory
    calculations_dir = output_dir / 'calculations'
    calculations_dir.mkdir(exist_ok=True)
    
    # Read the dataset
    df = pd.read_csv(data_dir / 'avocado.csv')
    
    # Select organic avocados and relevant columns
    organic_df = df[df['type'] == 'organic']
    relevant_columns = ['Date', 'region', '4046', '4225', '4770', 'Total Volume']
    organic_subset = organic_df[relevant_columns]
    
    # Save the subset as both CSV and PNG
    # save_table(organic_subset, 'q1_organic_avocados.csv', tables_dir, plots_dir)
    
    # Calculate PLU volumes
    plu_volumes = organic_subset[['4046', '4225', '4770']].sum()
    plu_volumes_df = pd.DataFrame({
        'PLU_Code': plu_volumes.index,
        'Total_Volume': plu_volumes.values
    })
    
    # Save PLU volumes as both CSV and PNG
    # save_table(plu_volumes_df, 'q1_plu_volumes.csv', tables_dir, plots_dir)
    
    # Create visualization of PLU volumes
    plt.figure(figsize=(12, 6))
    plt.bar(plu_volumes.index, plu_volumes.values, color=PASTEL_COLORS[:3])
    plt.title('Total Volume by PLU Code (Organic Avocados)')
    plt.xlabel('PLU Code')
    plt.ylabel('Total Volume')
    save_plot(plt, 'q1_plu_volumes_bar.png', plots_dir)
    
    # Save detailed calculations and summary
    with open(calculations_dir / 'q1_analysis_details.txt', 'w') as f:
        f.write("Analysis of Organic Avocados - Detailed Calculations\n")
        f.write("=" * 50 + "\n\n")
        
        # Dataset statistics
        f.write("Dataset Statistics:\n")
        f.write("-" * 20 + "\n")
        f.write(f"Total number of records: {len(df)}\n")
        f.write(f"Number of organic records: {len(organic_subset)}\n")
        f.write(f"Percentage of organic records: {(len(organic_subset)/len(df))*100:.2f}%\n\n")
        
        # PLU volumes analysis
        f.write("PLU Volumes Analysis:\n")
        f.write("-" * 20 + "\n")
        for plu in ['4046', '4225', '4770']:
            total_vol = organic_subset[plu].sum()
            avg_vol = organic_subset[plu].mean()
            max_vol = organic_subset[plu].max()
            min_vol = organic_subset[plu].min()
            
            f.write(f"\nPLU {plu}:\n")
            f.write(f"Total Volume: {total_vol:,.2f}\n")
            f.write(f"Average Volume: {avg_vol:,.2f}\n")
            f.write(f"Maximum Volume: {max_vol:,.2f}\n")
            f.write(f"Minimum Volume: {min_vol:,.2f}\n")
            f.write(f"Percentage of Total: {(total_vol/plu_volumes.sum())*100:.2f}%\n")
        
        # Regional distribution
        f.write("\nRegional Distribution:\n")
        f.write("-" * 20 + "\n")
        region_counts = organic_subset['region'].value_counts()
        for region, count in region_counts.items():
            f.write(f"{region}: {count} records ({(count/len(organic_subset))*100:.2f}%)\n")

if __name__ == '__main__':
    process_organic_avocados()
