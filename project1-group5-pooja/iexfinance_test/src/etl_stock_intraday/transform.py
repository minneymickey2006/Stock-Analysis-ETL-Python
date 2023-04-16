import pandas as pd 
class Transform():
    
    @staticmethod
    def transform(
            df:pd.DataFrame
        )->pd.DataFrame:
        """
        Transform the raw dataframes. 
        - df: the dataframe produced from extract_stocks(). 
        """
        # renaming columns
        df = df.rename(columns={
            "numberOfTrades": "numberoftrades"
            })

        #Adding column datetime that includes date and time both. Conversion of minutes into 24-hours format.
        df["datetime"] = pd.to_datetime(df["minute"])
        #Droping columns "date", "minutes" and labels, added datetime in prior step
        df = df.drop(df.columns[[0,1,2]],axis=1)
        #Difference between open and close value across rows.
        df["difference"] = (df["close"]-df["open"])
        #Creation of new dataframe to analyse the raw dataframe for per day stock vlues.
        df1 = pd.DataFrame()
        #MAX AND MINOF OPEN , CLOSE, HIGH, LOW VALUE GROUPING ON PER STOCK BASIS and APPLYING LAMBDA FUNCTION
        df1["max_open_value_per_day"] = df.groupby('stock_code').apply(lambda df: df["open"].max())
        df1["min_open_value_per_day"] = df.groupby('stock_code').apply(lambda df: df["open"].min())
        df1["max_close_value_per_day"] = df.groupby('stock_code').apply(lambda df: df["close"].max())
        df1["min_close_value_per_day"] = df.groupby('stock_code').apply(lambda df: df["close"].min())
        df1["max_high_per_day"] = df.groupby('stock_code').apply(lambda df: df["high"].max())
        df1["min_high_per_day"] = df.groupby("stock_code").apply(lambda df: df["high"].min())
        df1["max_low_per_day"] = df.groupby('stock_code').apply(lambda df: df["low"].max())
        df1["min_low_per_day"] = df.groupby("stock_code").apply(lambda df: df["low"].min())
        # Difference sum for per stock
        df1["status_difference"] = df.groupby("stock_code").apply(lambda df: df["difference"].sum())

        #MEAN VALUE FOR trades and volume PER DAY PER STOCK THROUGH GROUPING BY STOCK CODE AND LAMBDA FUNCTION APPLYING.
        df1["trades_mean"] = df.groupby("stock_code").apply(lambda df: df["numberoftrades"].mean())
        df1["volume_mean"] = df.groupby("stock_code").apply(lambda df: df["volume"].mean())
        
        return df1