import pandas as pd
import re

def normalize_yahoo(path):
    df = pd.read_csv(path)

    # Separate string into 3 columns  with the price, change, and perc_change 
    parts = df['Price'].str.extract(
        r'^\s*([\d.,]+)\s+([+\-]?\d+(?:\.\d+)?)\s*\(\s*([+\-]?\d+(?:\.\d+)?)%\s*\)\s*$'
    )
    price = pd.to_numeric(parts[0])
    change = pd.to_numeric(parts[1])
    perc  = pd.to_numeric(parts[2])

    df['symbol'] = df['Symbol'].astype(str).str.strip()
    df['company_name'] = df['Name'].astype(str).str.strip()
    df['price'] = price
    df['change'] = change
    df['perc_change'] = perc
    df['volume'] = df['Volume']
    return [
        f"{row['symbol']},{row['company_name']},{row['price']},{row['change']},{row['perc_change']},{row['volume']}"
        for _, row in df.iterrows()
    ]

def normalize_wsj(path):
    df = pd.read_csv(path)

    # Extract symbol from "Company (TICKER)"
    rex = r'\(([A-Z]+)\)$'
    df['symbol'] = df['Unnamed: 0'].apply(lambda x: re.findall(rex, x)[0])
    df['company_name'] = df['Unnamed: 0'].apply(lambda x: re.sub(rex, '', str(x)).strip())
    df['price'] = pd.to_numeric(df['Last'].astype(str))
    df['change'] = pd.to_numeric(df['Chg'].astype(str))
    df['perc_change'] = pd.to_numeric(df['% Chg'].astype(str))
    df['volume'] = df['Volume']

    rows = [
        f"{row['symbol']},{row['company_name']},{row['price']},{row['change']},{row['perc_change']},{row['volume']}"
        for _, row in df.iterrows()
    ]
    return rows

