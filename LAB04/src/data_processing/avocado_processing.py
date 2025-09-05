import pandas as pd
import numpy as np

def load_and_preprocess_avocado(file_path):
    """Load and preprocess avocado dataset."""
    # Date in input is day-first like "27-12-2015"
    parse_date = lambda s: pd.to_datetime(s, format="%d-%m-%Y", errors="coerce")
    
    # Read data
    df = pd.read_csv(file_path)
    
    # Normalize column names
    df.columns = [c.strip().replace(" ", "_").replace("-", "_").lower() for c in df.columns]
    
    # Parse date
    if "date" in df.columns:
        df["date"] = df["date"].apply(parse_date)
    
    # Ensure numeric
    if "averageprice" in df.columns:
        df["averageprice"] = pd.to_numeric(df["averageprice"], errors="coerce")
    if "total_volume" in df.columns:
        df["total_volume"] = pd.to_numeric(df["total_volume"], errors="coerce")
    
    return df

def get_time_aggregations(df):
    """Compute monthly and annual aggregations of total volume."""
    df_valid_dates = df.dropna(subset=["date"])
    df_valid_dates["year"] = df_valid_dates["date"].dt.year
    df_valid_dates["month"] = df_valid_dates["date"].dt.to_period("M").astype(str)

    # Overall annual total
    annual_total = df_valid_dates.groupby("year")["total_volume"].sum().sort_index()
    
    # Overall monthly total (year-month)
    monthly_total = df_valid_dates.groupby("month")["total_volume"].sum().sort_index()
    
    # Per-region annual total
    annual_by_region = df_valid_dates.groupby(["region", "year"])["total_volume"].sum().reset_index()
    
    # Per-region monthly total
    monthly_by_region = df_valid_dates.groupby(["region", "month"])["total_volume"].sum().reset_index()
    
    return annual_total, monthly_total, annual_by_region, monthly_by_region

def impute_by_region_mean(df, column="averageprice"):
    """Impute missing values using region-wise mean."""
    df_copy = df.copy()
    region_means = df_copy.groupby("region")[column].transform("mean")
    df_copy[column] = df_copy[column].fillna(region_means)
    return df_copy

def map_date_to_category(df):
    """Map dates to categorical values {Old, New, Recent}."""
    def map_year_to_category(y):
        if pd.isna(y):
            return np.nan
        if y in (2015, 2016):
            return "Old"
        elif y == 2017:
            return "New"
        elif y == 2018:
            return "Recent"
        else:
            return np.nan

    df = df.copy()
    df["date_year"] = df["date"].dt.year
    df["date_category"] = df["date_year"].apply(map_year_to_category)
    return df
