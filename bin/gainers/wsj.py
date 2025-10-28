import os
import re
import pandas as pd
from base import GainerBase

class GainerWSJ(GainerBase):
    def __init__(self):
        pass

    def download_html(self):
        """download html from Wall Street Hournal"""
        print("WSJ html download")
        os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html")

    def extract_csv(self):
        """Convert WSJ html to CSV."""
        print("WSJ csv create")
        raw = pd.read_html('wsjgainers.html')
        raw[0].to_csv('wsjgainers.csv')

    def normalize_data(self):
        """Normalize WSJ CSV into wsjgainers_normalized.csv."""
        print("WSJ normalize csv")
        df = pd.read_csv('wsjgainers.csv')

        # Extract symbol from "Company (TICKER)"
        rex = r'\(([A-Z]+)\)$'
        df['symbol'] = df['Unnamed: 0'].apply(lambda x: re.findall(rex, x)[0])
        df['company_name'] = df['Unnamed: 0'].apply(lambda x: re.sub(rex, '', str(x)).strip())
        df['price'] = pd.to_numeric(df['Last'].astype(str))
        df['change'] = pd.to_numeric(df['Chg'].astype(str))
        df['perc_change'] = pd.to_numeric(df['% Chg'].astype(str))
        df['volume'] = df['Volume']
        df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']].to_csv('wsjgainers_normalized.csv', index=False)

if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"

    gainer = GainerWSJ()

    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()
