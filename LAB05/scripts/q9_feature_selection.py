import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from utils import setup_paths, save_plot, save_table, PASTEL_COLORS

def calculate_entropy(y):
    """Calculate entropy of a target variable."""
    classes = np.unique(y)
    entropy = 0
    for cls in classes:
        p = len(y[y == cls]) / len(y)
        entropy -= p * np.log2(p)
    return entropy

def calculate_gini(y):
    """Calculate Gini index of a target variable."""
    classes = np.unique(y)
    gini = 1
    for cls in classes:
        p = len(y[y == cls]) / len(y)
        gini -= p**2
    return gini

def calculate_information_gain(X, y, feature):
    """Calculate information gain for a feature."""
    entropy_parent = calculate_entropy(y)
    values = np.unique(X[feature])
    weighted_entropy = 0
    
    for value in values:
        subset_indices = X[feature] == value
        entropy_child = calculate_entropy(y[subset_indices])
        weight = len(y[subset_indices]) / len(y)
        weighted_entropy += weight * entropy_child
    
    return entropy_parent - weighted_entropy

def feature_selection_measures():
    # Setup paths
    data_dir, output_dir, plots_dir, tables_dir = setup_paths()
    
    # Create calculations directory
    calculations_dir = output_dir / 'calculations'
    calculations_dir.mkdir(exist_ok=True)
    
    # Read the dataset
    df = pd.read_csv(data_dir / 'avocado.csv')
    
    # Prepare the data
    # Using 'type' as target variable and numerical features for analysis
    numerical_features = ['Total Volume', 'AveragePrice', '4046', '4225', '4770']
    
    # Convert features to numeric type and handle any invalid values
    X = df[numerical_features].apply(pd.to_numeric, errors='coerce')
    
    # Encode the target variable
    le = LabelEncoder()
    y = le.fit_transform(df['type'])
    
    # Calculate measures for each feature
    results = []
    for feature in numerical_features:
        try:
            # Remove NaN values and bin the continuous values for entropy and gini calculations
            feature_data = X[feature].dropna()
            X_binned = pd.qcut(feature_data, q=5, labels=['q1', 'q2', 'q3', 'q4', 'q5'],duplicates='drop')
            
            result = {
                'Feature': feature,
                'Entropy': calculate_entropy(X_binned),
                'Gini': calculate_gini(X_binned),
                'Information_Gain': calculate_information_gain(pd.DataFrame({feature: X_binned}), y[feature_data.index], feature)
            }
            results.append(result)
        except Exception as e:
            print(f"Warning: Could not process feature {feature}: {str(e)}")
            results.append({
                'Feature': feature,
                'Entropy': np.nan,
                'Gini': np.nan,
                'Information_Gain': np.nan
            })
    
    # Create results dataframe
    results_df = pd.DataFrame(results)
    save_table(results_df, 'q9_feature_selection_measures.csv', tables_dir, plots_dir)
    
    # Save detailed calculations to text file
    with open(calculations_dir / 'q9_detailed_calculations.txt', 'w') as f:
        f.write("Feature Selection Measures - Detailed Calculations\n")
        f.write("=" * 50 + "\n\n")
        
        for feature in numerical_features:
            try:
                f.write(f"Feature: {feature}\n")
                f.write("-" * 30 + "\n")
                
                # Get feature data and handle missing values
                feature_data = X[feature].dropna()
                f.write(f"Data Summary:\n")
                f.write(f"Total samples: {len(X[feature])}\n")
                f.write(f"Valid samples: {len(feature_data)}\n")
                f.write(f"Missing values: {X[feature].isna().sum()}\n")
                f.write(f"Value range: {feature_data.min():.2f} to {feature_data.max():.2f}\n\n")
                
                # Get binned data with handling for duplicate bin edges
                try:
                    X_binned = pd.qcut(feature_data, q=5, labels=['q1', 'q2', 'q3', 'q4', 'q5'], duplicates='drop')
                except ValueError as ve:
                    # If we can't create 5 bins due to too many duplicates, try with fewer bins
                    unique_values = len(feature_data.unique())
                    if unique_values < 5:
                        n_bins = max(2, unique_values - 1)  # At least 2 bins, but no more than unique values - 1
                        try:
                            X_binned = pd.qcut(feature_data, q=n_bins, labels=[f'q{i+1}' for i in range(n_bins)], duplicates='drop')
                            f.write(f"Note: Reduced to {n_bins} bins due to duplicate values\n\n")
                        except ValueError:
                            # If qcut fails, try cut instead which creates equal-width bins
                            X_binned = pd.cut(feature_data, bins=n_bins, labels=[f'q{i+1}' for i in range(n_bins)],duplicates='drop')
                            f.write(f"Note: Using equal-width bins instead of equal-frequency bins\n\n")
                
                # Calculate and write entropy details
                entropy = calculate_entropy(X_binned)
                f.write(f"Entropy Calculation:\n")
                for cls in np.unique(X_binned):
                    p = len(X_binned[X_binned == cls]) / len(X_binned)
                    f.write(f"  Class {cls}: p={p:.4f}, -p*log2(p)={-p * np.log2(p):.4f}\n")
                f.write(f"Total Entropy: {entropy:.4f}\n\n")
                
                # Calculate and write gini details
                gini = calculate_gini(X_binned)
                f.write(f"Gini Index Calculation:\n")
                for cls in np.unique(X_binned):
                    p = len(X_binned[X_binned == cls]) / len(X_binned)
                    f.write(f"  Class {cls}: p={p:.4f}, p^2={p**2:.4f}\n")
                f.write(f"Total Gini Index: {gini:.4f}\n\n")
                
                # Calculate and write information gain details
                
            except Exception as e:
                f.write(f"Error processing feature {feature}: {str(e)}\n\n")
                continue
                
            # Calculate and write information gain details
            info_gain = calculate_information_gain(pd.DataFrame({feature: X_binned}), y[feature_data.index], feature)
            f.write(f"Information Gain Calculation:\n")
            f.write(f"Parent Entropy: {calculate_entropy(y[feature_data.index]):.4f}\n")
            f.write(f"Weighted Child Entropy: {calculate_entropy(y[feature_data.index]) - info_gain:.4f}\n")
            f.write(f"Information Gain: {info_gain:.4f}\n\n")
    
    # Visualize the measures
    measures = ['Entropy', 'Gini', 'Information_Gain']
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for i, measure in enumerate(measures):
        ax = axes[i]
        results_df.plot(kind='bar', x='Feature', y=measure, ax=ax, color=PASTEL_COLORS[i])
        ax.set_title(f'{measure} by Feature')
        ax.set_xticklabels(results_df['Feature'], rotation=45, ha='right')
    
    plt.tight_layout()
    save_plot(plt, 'q9_feature_selection_measures.png', plots_dir)
    
    # Using sklearn's DecisionTreeClassifier for feature importance
    dt = DecisionTreeClassifier(random_state=42)
    # Fill missing values with mean for decision tree
    X_filled = X.fillna(X.mean())
    dt.fit(X_filled, y)
    
    # Plot feature importance
    plt.figure(figsize=(10, 6))
    importance = pd.DataFrame({
        'Feature': numerical_features,
        'Importance': dt.feature_importances_
    }).sort_values('Importance', ascending=True)
    
    # Save feature importance to CSV and PNG
    save_table(importance, 'q9_feature_importance.csv', tables_dir, plots_dir)
    
    # Save decision tree parameters and feature importance to text file
    with open(calculations_dir / 'q9_decision_tree_details.txt', 'w') as f:
        try:
            f.write("Decision Tree Feature Importance Analysis\n")
            f.write("=" * 50 + "\n\n")
            
            f.write("Tree Parameters:\n")
            for param, value in dt.get_params().items():
                f.write(f"{param}: {value}\n")
            
            f.write("\nFeature Importance Scores:\n")
            for idx, row in importance.iterrows():
                f.write(f"{row['Feature']}: {row['Importance']:.4f}\n")
            
            f.write("\nTree Properties:\n")
            f.write(f"Number of nodes: {dt.tree_.node_count}\n")
            f.write(f"Tree depth: {dt.tree_.max_depth}\n")
            f.write(f"\nData Properties:\n")
            f.write(f"Training samples: {len(X_filled)}\n")
            f.write(f"Features: {len(numerical_features)}\n")
            f.write(f"Missing values (before filling):\n")
            for feature in numerical_features:
                missing = X[feature].isna().sum()
                if missing > 0:
                    f.write(f"  {feature}: {missing} ({missing/len(X)*100:.1f}%)\n")
                    
        except Exception as e:
            f.write(f"\nError while writing decision tree details: {str(e)}\n")
    
    importance.plot(kind='barh', x='Feature', y='Importance', color=PASTEL_COLORS[0])
    plt.title('Feature Importance using Decision Tree')
    plt.xlabel('Importance')
    plt.tight_layout()
    save_plot(plt, 'q9_feature_importance.png', plots_dir)

if __name__ == '__main__':
    feature_selection_measures()
