import os
import pandas as pd
from base import GainerBase
class GainerYahoo(GainerBase):
    def __init__(self):
        pass

    def download_html(self):
        """Download the raw HTML from Yahoo."""
        print("Yahoo html download")
        os.system(
        	"sudo google-chrome-stable --headless --disable-gpu --dump-dom "
        	"--no-sandbox --timeout=5000 "
        	"'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html"
        )

    def extract_csv(self):
        """Convert Table from Html to Cs.v"""
        print("Yahoo csv create")
        raw = pd.read_html('ygainers.html')
        raw[0].to_csv('ygainers.csv')

    def normalize_data(self):
        """Normalize Yahoo csv."""
        print("Yahoo normalize csv")
        df = pd.read_csv('ygainers.csv')

        # Separate string into 3 columns with the price, change, and perc_change
        parts = df['Price'].str.extract(
        	r'^\s*([\d.,]+)\s+([+\-]?\d+(?:\.\d+)?)\s*\(\s*([+\-]?\d+(?:\.\d+)?)%\s*\)\s*$'
        )
        price = pd.to_numeric(parts[0].astype(str).str.replace(',', '', regex=False), errors='coerce')
        change = pd.to_numeric(parts[1])
        perc  = pd.to_numeric(parts[2])

        df['symbol'] = df['Symbol'].astype(str).str.strip()
        df['company_name'] = df['Name'].astype(str).str.strip()
        df['price'] = price
        df['change'] = change
        df['perc_change'] = perc
        df['volume'] = df['Volume']
        out = df[["symbol", "company_name", "price", "change", "perc_change", "volume"]]
        out.to_csv('ygainers_normalized.csv', index=False)

if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"

    gainer = GainerYahoo()

    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()
