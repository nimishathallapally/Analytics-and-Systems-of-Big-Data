# Avocado Data Preprocessing and Analysis

This repository contains scripts and resources for comprehensive data preprocessing and analysis using the Avocado dataset. The workflow covers data cleaning, selection, transformation, and feature selection, along with statistical analysis and handling of missing values.

## Directory Structure

```
├── data/
│   ├── avocado.csv
│   └── Trail.csv
├── outputs/
│   ├── calculations/
│   ├── plots/
│   └── tables/
├── scripts/
│   ├── q1_attribute_selection.py
│   ├── q2_duplicate_handling.py
│   ├── q3_year_binarization.py
│   ├── q4_5_encoding.py
│   ├── q6_7_missing_values.py
│   ├── q8_statistical_analysis.py
│   ├── q9_feature_selection.py
│   ├── q10_comprehensive_preprocessing.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Main Scripts

- **q10_comprehensive_preprocessing.py**: Performs cleaning, transformation, and feature selection on the Avocado dataset.
- **q6_7_missing_values.py**: Handles missing values in the dataset.
- **q8_statistical_analysis.py**: Provides statistical summaries and visualizations.
- **Other scripts**: Address specific preprocessing and analysis tasks as per lab requirements.

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run preprocessing:**
   ```bash
   cd scripts
   python3 q10_comprehensive_preprocessing.py
   ```
3. **Run other analyses as needed:**
   ```bash
   python3 q6_7_missing_values.py
   python3 q8_statistical_analysis.py
   # ...and so on
   ```

## Outputs
- Processed data, tables, and plots are saved in the `outputs/` directory under `tables/`, `plots/`, and `calculations/`.

## Notes
- Only the Avocado dataset is used for comprehensive preprocessing.
- Integration step is skipped to avoid memory issues.
- See each script for detailed documentation and comments.

---

*Prepared for ASBD LAB05.*
