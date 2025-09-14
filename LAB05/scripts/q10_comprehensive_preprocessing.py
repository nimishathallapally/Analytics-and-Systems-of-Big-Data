import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from utils import setup_paths, save_plot, save_table, PASTEL_COLORS

def comprehensive_preprocessing():
    # Setup paths
    data_dir, _, plots_dir, tables_dir = setup_paths()
    
    # Read only the avocado dataset
    avocado_df = pd.read_csv(data_dir / 'avocado.csv')
    
    # 1. Data Cleaning
    def clean_dataset(df, name):
        # Create a copy of the DataFrame
        df_cleaned = df.copy()
        
        # Remove duplicates
        df_cleaned = df_cleaned.drop_duplicates()
        
        # Handle missing values
        numerical_cols = df_cleaned.select_dtypes(include=[np.number]).columns
        categorical_cols = df_cleaned.select_dtypes(include=['object']).columns
        
        # Numerical imputation
        if len(numerical_cols) > 0:
            num_imputer = SimpleImputer(strategy='mean')
            df_cleaned.loc[:, numerical_cols] = num_imputer.fit_transform(df_cleaned[numerical_cols])
        
        # Categorical imputation
        if len(categorical_cols) > 0:
            cat_imputer = SimpleImputer(strategy='most_frequent')
            df_cleaned.loc[:, categorical_cols] = cat_imputer.fit_transform(df_cleaned[categorical_cols])
        
        # Save cleaned dataset
        save_table(df_cleaned, f'q10_cleaned_{name}.csv', tables_dir)
        return df_cleaned
    
    avocado_cleaned = clean_dataset(avocado_df, 'avocado')
    
    # 2. Data Transformation
    def transform_dataset(df, name):
        # Standardization
        scaler = StandardScaler()
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        df_scaled = df.copy()
        df_scaled[numerical_cols] = scaler.fit_transform(df[numerical_cols])
        
        # Categorical encoding
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            le = LabelEncoder()
            df_scaled[col] = le.fit_transform(df[col])
        
        # Save transformed dataset
        save_table(df_scaled, f'q10_transformed_{name}.csv', tables_dir)
        return df_scaled
    
    avocado_transformed = transform_dataset(avocado_cleaned, 'avocado')
    
    # 3. Feature Selection
    def select_features(df, target_col, name):
        # Separate features and target
        X = df.drop(columns=[target_col])
        y = df[target_col]
        
        # Select top k features
        k = 5  # Number of features to select
        selector = SelectKBest(score_func=f_classif, k=k)
        X_selected = selector.fit_transform(X, y)
        
        # Get selected feature names
        selected_features = X.columns[selector.get_support()].tolist()
        
        # Visualize feature scores
        plt.figure(figsize=(10, 6))
        scores = pd.DataFrame({
            'Feature': X.columns,
            'Score': selector.scores_
        }).sort_values('Score', ascending=True)
        
        scores.plot(kind='barh', x='Feature', y='Score', color=PASTEL_COLORS[0])
        plt.title(f'Feature Selection Scores ({name})')
        plt.xlabel('F-score')
        plt.tight_layout()
        save_plot(plt, f'q10_feature_scores_{name}.png', plots_dir)
        
        return selected_features
    
    # Use 'type' as target for avocado dataset
    avocado_features = select_features(avocado_transformed, 'type', 'avocado')
    
    # Create preprocessing summary
    summary = {
        'Original Shape': avocado_df.shape,
        'Cleaned Shape': avocado_cleaned.shape,
        'Selected Features (Avocado)': avocado_features
    }
    with open(tables_dir / 'q10_preprocessing_summary.txt', 'w') as f:
        for category, details in summary.items():
            f.write(f"{category}:\n")
            f.write(f"{details}\n\n")

if __name__ == '__main__':
    comprehensive_preprocessing()
