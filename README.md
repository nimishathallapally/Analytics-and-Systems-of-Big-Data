# Analytics and Systems of Big Data (ASBD) Course Labs

This repository contains comprehensive lab assignments for the Analytics and Systems of Big Data course, focusing on data preprocessing, analysis, and visualization techniques using Python.

## Structure

The repository is organized into progressive lab assignments:

### LAB02 - Data Visualization
Comprehensive visualization techniques using the Iris dataset:
- Area Charts with Tables
- Bar Charts with Statistical Analysis
- Doughnut Charts with Percentage Distribution
- Histograms with Frequency Analysis
- Line Charts with Trend Analysis
- Pareto Charts with Cumulative Distribution
- Pie Charts with Legend
- Radar Charts with Multiple Variables
- Scatter Plots with Correlation Analysis

### LAB03 - Advanced Statistical Visualization
In-depth statistical analysis and visualization:
1. Histogram Analysis with Variable Bin Sizes
2. Stem-and-Leaf Plots with Data Distribution
3. Density Estimation with Kernel Functions
4. Scatter Plot Analysis with Regression
5. Box and Swarm Plots for Distribution Analysis
6. Violin Plots for Probability Density
7. Radar Charts for Multivariate Data
8. Funnel Charts for Process Analysis
9. Correlation Analysis with Heatmaps

### LAB04 - Data Processing and Analysis
Advanced data processing techniques:
- Data Normalization Methods
  - Min-Max Scaling
  - Standard Scaling
  - Robust Scaling
- Avocado Price Analysis
  - Time Series Analysis
  - Price Prediction
  - Market Trend Analysis

### LAB05 - Comprehensive Data Preprocessing
Advanced data preprocessing and feature selection:
1. Attribute Selection with Statistical Analysis
2. Duplicate Entry Detection and Handling
3. Year Binarization Techniques
4. Categorical Data Transformation
5. One-Hot Encoding Implementation
6. Missing Value Analysis and Treatment
7. Nullity Analysis for Feature Selection
8. Complete Statistical Summary
9. Feature Selection Measures
   - Entropy Calculation
   - Gini Index Analysis
   - Information Gain Assessment
10. End-to-End Data Preprocessing Pipeline

## Setup and Requirements

### Prerequisites
- Python 3.x
- pip package manager

### Required Libraries
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## Project Structure

```
LAB0X/
├── scripts/
│   ├── utils.py            # Common utilities
│   ├── q1_analysis.py      # Question-specific scripts
│   ├── q2_analysis.py
│   └── ...
├── data/
│   ├── Iris.csv
│   ├── avocado.csv
│   └── Trail.csv
├── outputs/
│   ├── plots/             # Generated visualizations
│   ├── tables/            # Analysis results
│   └── calculations/      # Detailed computation logs
└── README.md
```

## Running the Code

### Individual Scripts
Each lab contains modular Python scripts that can be run independently:

```bash
cd LAB05/scripts
python q1_attribute_selection.py
```

### Full Lab Execution
To run all questions in a lab:

```bash
cd LAB05
python run_all.py
```

## Output and Documentation

### Generated Files
- Visualizations (PNG format)
- Data tables (CSV format)
- Detailed calculations (TXT format)
- Statistical analysis reports

### Documentation
Each script includes:
- Comprehensive comments
- Function documentation
- Implementation details
- Analysis methodology

## Features

### Data Processing
- Robust error handling
- Missing value treatment
- Data type validation
- Outlier detection

### Visualization
- Publication-ready plots
- Multiple chart types
- Customizable styles
- Statistical annotations

### Analysis
- Feature selection metrics
- Statistical measures
- Data quality assessment
- Correlation analysis

## Author
Nimisha Thallapally

## License
This project is licensed under the MIT License
