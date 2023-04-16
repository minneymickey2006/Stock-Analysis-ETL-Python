class Extract():
    @staticmethod
    def extract_per_stock(
            iex_api_key:str,
            stock_ticker:str=None,
        )->pd.DataFrame:
        headers = {
            "token" : iex_api_key
        }
        """
        Extracting data from the intraday stock API. 
        - iex_api_key: api key 
        - stock_tickere: code of the stock e.g. AAPL for APPLE stock
        """
        params = {
            "token" : iex_api_key
        }
        base_url = f"https://cloud.iexapis.com/stable/stock/{stock_ticker}/intraday-prices"
        response = requests.get(base_url, params=params)
        if response.status_code == 200: 
            stock_data = response.json()
        else: 
            raise Exception("Extracting weather api data failed. Please check if API limits have been reached.")
        df_stock_codes = pd.json_normalize(stock_data)
        return df_stock_codes
    
    @staticmethod
    def extract_stocks(
            iex_api_key:str, 
        )->pd.DataFrame:
     # read list of stock_codes
    df_stock_codes = pd.read_csv("src\data\stock_codes.csv")
    # request data for each stock_code (json) and push to a list 
    df_concat = pd.DataFrame()
    for exchange_code in df_stock_codes["exchange_code"]:
        df_extracted = extract_per_stock(stock_ticker=exchange_code, iex_api_key= iex_api_key)
        df_extracted["stock_code"] = exchange_code
        df_concat = pd.concat([df_concat,df_extracted])
    return df_concat
    
        