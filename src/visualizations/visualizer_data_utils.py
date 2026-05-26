import pandas as pd
import numpy as np

def extract_histogram_data(series: pd.Series, z_thresh: float = 3.0):
    """
    Separates normal data from extreme outliers to prevent KDE/Histogram distortion.
    Returns:
        clean_data (pd.Series): Data within Z-score threshold.
        outliers (pd.Series): Data outside Z-score threshold.
    """
    if len(series) == 0:
        return pd.Series(dtype=float), pd.Series(dtype=float)
        
    mean = series.mean()
    std = series.std()
    if std == 0 or np.isnan(std):
        return series, pd.Series(dtype=float)
        
    z_scores = np.abs((series - mean) / std)
    clean_data = series[z_scores <= z_thresh]
    outliers = series[z_scores > z_thresh]
    
    return clean_data, outliers

def extract_rolling_quantiles(df_node: pd.DataFrame, window: int = 12):
    """
    Calculates rolling quantiles to draw a continuous 'Box Plot' (Bollinger Band style).
    Returns a DataFrame with t_idx, median, q25, q75, min_val, max_val.
    """
    if df_node.empty:
        return pd.DataFrame()
        
    df_sorted = df_node.sort_values('t_idx').copy()
    
    # Calculate rolling metrics
    df_sorted['q25'] = df_sorted['velocity_v'].rolling(window=window, min_periods=min(3, window)).quantile(0.25)
    df_sorted['median'] = df_sorted['velocity_v'].rolling(window=window, min_periods=min(3, window)).quantile(0.50)
    df_sorted['q75'] = df_sorted['velocity_v'].rolling(window=window, min_periods=min(3, window)).quantile(0.75)
    
    # Calculate IQR for standard whiskers
    iqr = df_sorted['q75'] - df_sorted['q25']
    whisker_low = df_sorted['q25'] - 1.5 * iqr
    whisker_high = df_sorted['q75'] + 1.5 * iqr
    
    # Actual min/max within rolling window to clip whiskers
    roll_min = df_sorted['velocity_v'].rolling(window=window, min_periods=min(3, window)).min()
    roll_max = df_sorted['velocity_v'].rolling(window=window, min_periods=min(3, window)).max()
    
    df_sorted['whisker_low'] = np.maximum(whisker_low, roll_min)
    df_sorted['whisker_high'] = np.minimum(whisker_high, roll_max)
    
    return df_sorted[['t_idx', 'velocity_v', 'q25', 'median', 'q75', 'whisker_low', 'whisker_high']].dropna()

def extract_stacked_bar_data(df_dyn: pd.DataFrame):
    """
    Normalizes the absolute velocity_v of all nodes at each t_idx to sum to 1.0 (100%).
    Returns:
        pd.DataFrame: Contains ['t_idx', 'node_label', 'normalized_share']
    """
    if df_dyn.empty:
        return pd.DataFrame()
        
    # We use absolute velocity to represent the magnitude of activity
    df_abs = df_dyn.copy()
    df_abs['abs_v'] = df_abs['velocity_v'].abs()
    
    # Calculate sum of absolute velocities per t_idx
    sum_per_time = df_abs.groupby('t_idx')['abs_v'].sum().reset_index()
    sum_per_time.rename(columns={'abs_v': 'total_v'}, inplace=True)
    
    df_merged = pd.merge(df_abs, sum_per_time, on='t_idx')
    
    # Avoid division by zero
    df_merged['normalized_share'] = np.where(
        df_merged['total_v'] > 0, 
        df_merged['abs_v'] / df_merged['total_v'], 
        0.0
    )
    
    return df_merged[['t_idx', 'node_label', 'normalized_share']]
