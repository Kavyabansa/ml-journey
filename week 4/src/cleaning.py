import pandas as pd
import numpy as np

def drop_high_missing(df, threshold=0.4):
    # drop columns where missing % > threshold
    missing_pct = df.isnull().mean()
    cols_to_drop = missing_pct[missing_pct > threshold].index
    df = df.drop(columns = cols_to_drop)
    return df

def impute_numeric(df):
    # fill numeric nulls with median
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    return df

def impute_categorical(df):
    # fill categorical nulls with mode
    cat_cols = df.select_dtypes(include='object').columns
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])
    return df

def remove_iqr_outliers(df, columns):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    return df

def parse_date(df, date_col='Date'):
    df[date_col] = pd.to_datetime(df[date_col], dayfirst=True)
    df['Year'] = df[date_col].dt.year
    df['Month'] = df[date_col].dt.month
    df = df.drop(columns=[date_col])
    return df

def clean(df):
    # call all functions in order and return cleaned df
    df = remove_iqr_outliers(df, ['Price', 'BuildingArea'])  # before dropping
    df = drop_high_missing(df)
    df = impute_numeric(df)
    df = impute_categorical(df)
    df = parse_date(df)
    return df