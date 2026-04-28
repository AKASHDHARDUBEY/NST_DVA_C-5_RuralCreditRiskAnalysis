import pandas as pd
import numpy as np
import os

def extract_data(file_path):
    """Step 1: Extract - Load the raw CSV file"""
    print("Extracting data...")
    return pd.read_csv(file_path)

def transform_data(df):
    """Step 2: Transform - Clean, Standardize, and Engineer Features"""
    print("Transforming data...")
    

    df.rename(columns={'water_availabity': 'water_availability'}, inplace=True)

    if 'Id' in df.columns:
        df.drop(columns=['Id'], inplace=True)
    
   
    df['social_class'] = df['social_class'].replace('Mouchi', 'Mochi')
    # Standardize Sex
    df['sex'] = df['sex'].str.upper().str.strip()
    

    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    
    cat_cols = df.select_dtypes(include=['object']).columns
    df[cat_cols] = df[cat_cols].fillna('Unknown')
    
    q_limit = df['annual_income'].quantile(0.95)
    df['annual_income'] = np.where(df['annual_income'] > q_limit, q_limit, df['annual_income'])
    
    df['disposable_income'] = df['annual_income'] - (df['monthly_expenses'] * 12)
    df['loan_to_income_ratio'] = (df['loan_amount'] / df['annual_income']) * 100
    df['total_dependents'] = df['old_dependents'] + df['young_dependents']
    
    df_sampled = df.sample(n=10000, random_state=42)
    
    return df_sampled

def load_data(df, output_path):
    """Step 3: Load - Save the processed data to a CSV file"""
    print(f"Loading data to {output_path}...")
    df.to_csv(output_path, index=False)
    print("ETL Pipeline completed successfully!")

if __name__ == "__main__":
    RAW_DATA_PATH = 'data/raw/RuralCreditData.csv'
    PROCESSED_DATA_PATH = 'data/processed/RuralCreditData_processed.csv'
    
    os.makedirs('data/processed', exist_ok=True)
    
    try:
       
        raw_df = extract_data(RAW_DATA_PATH)
        processed_df = transform_data(raw_df)
        load_data(processed_df, PROCESSED_DATA_PATH)
        
    except Exception as e:
        print(f"Pipeline failed: {e}")