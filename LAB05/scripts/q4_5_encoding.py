import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from utils import setup_paths, save_plot, save_table, PASTEL_COLORS
from sklearn.preprocessing import LabelEncoder

def encode_categories():
    # Setup paths
    data_dir, _, plots_dir, tables_dir = setup_paths()
    
    # Read the dataset
    df = pd.read_csv(data_dir / 'avocado.csv')
    
    # Integer Encoding for all categorical attributes
    categorical_cols = df.select_dtypes(include=['object']).columns
    label_encoders = {}
    
    for col in categorical_cols:
        le = LabelEncoder()
        df[f'{col}_encoded'] = le.fit_transform(df[col])
        label_encoders[col] = le
    
    # One-Hot Encoding for Region
    region_encoded = pd.get_dummies(df['region'], prefix='region')
    df = pd.concat([df, region_encoded], axis=1)
    
    # Save processed dataset
    save_table(df, 'q4_5_encoded_data.csv', tables_dir)
    
    # Visualize integer encoding
    plt.figure(figsize=(12, 6))
    for i, col in enumerate(categorical_cols):
        plt.subplot(1, len(categorical_cols), i+1)
        sns.boxplot(data=df, y=f'{col}_encoded', color=PASTEL_COLORS[i])
        plt.title(f'{col} Encoding')
    plt.tight_layout()
    save_plot(plt, 'q4_integer_encoding.png', plots_dir)
    
    # Visualize one-hot encoding distribution
    plt.figure(figsize=(15, 6))
    region_encoded.sum().sort_values(ascending=True).plot(kind='bar', color=PASTEL_COLORS[0])
    plt.title('Distribution of Regions (One-Hot Encoded)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    save_plot(plt, 'q5_onehot_encoding.png', plots_dir)
    
    # Create mapping table
    mapping_df = pd.DataFrame()
    for col in categorical_cols:
        mapping = pd.DataFrame({
            'Original': label_encoders[col].classes_,
            'Encoded': range(len(label_encoders[col].classes_))
        })
        mapping['Attribute'] = col
        mapping_df = pd.concat([mapping_df, mapping])
    
    save_table(mapping_df, 'q4_encoding_mapping.csv', tables_dir)

if __name__ == '__main__':
    encode_categories()
