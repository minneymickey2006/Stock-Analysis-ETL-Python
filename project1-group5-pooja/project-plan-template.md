# Project plan 

## Objective 
Stock Market Investing is a tough job for retail investors. You can either rely on Fund Managers or do your own analysis to find the right stocks.
With this project we want to provide insights to investors to make better investing/trading decisions.

## Consumers 
What users would find your data useful? How do they want to access the data?
Retail Investors and Data analysts are able to pull the data from AWS Services like RDS and S3.

## Questions 
What questions are you trying to answer with your data? How will your data support your users?

1. Most stable stocks from each sector for each day. This would help retail investors in planning their intraday shortterm trades.
2. Best stocks for Intraday swing trading, based on most variance/swing. This would help retail investors in planning their intraday and swing trades.
3. Upward momentum stocks for monthly Calls. This would help retail investors in Option trading for Calls.
4. Downward momentum for monthly Puts. This would help retail investors in Option trading for Puts.

The dataset provides 56 columns, ranging from calculationPrice, changePercent, to lastTradeTime. If these 56 columns from different stocks are not aggregated together, it will be challenging to get an overall comparison of different stocks by parameters. Providing a transformed data for the consumers of this aplication.

## Source datasets 
What datasets are you sourcing from? How frequently are the source datasets updating?

The source of dataset is sourced from IEX Cloud Legacy API.
IEX Cloud provides real time prices, volume, and quotes for all NMS US securities
Methods:
GET /stock/{symbol}/intraday-prices

Datasets are updating every minute. The data set is delayed by 15 minutes for free accounts.

## Solution architecture
How are we going to get data flowing from source to serving? What components and services will we combine to implement the solution? How do we automate the entire running of the solution? 

Process Flow
EXTRACT
1. Get the Symbol data from IEX using a web service. Store it in a DataFrame.
<URL+API>
2. Loop through the Symbol DataFrame to fetch incremental data from the intraday-prices API. The data returned from this web service will be in JSON format. We will convert this into a Pandas Dataframe for transformations.
When we will be running the intraday-prices API for the first time we will fetch FULL data and in the incremental runs we will use MERGE to upsert the incremental data.

Response Attributes from the IEX intraday-prices API:
date
minute
marketAverage
marketNotional
marketNumberOfTrades
marketOpen
marketClose
marketHigh
marketLow
marketVolume
marketChangeOverTime
simplifyFactor
changeOverTime
label
average
notional
numberOfTrades
high
low
volume
open
close

TRANSFORM
1. Remove datasets which have NULL/NaN values.
2. Rename the columns to give them useful names.
3. Apply aggregations to get insights from data.
4. Apply aggregation hourly on each symbol.
5. Compare the aggregated data across symbols to find the right stocks.

LOAD
1. Use SQLAlchemy to connect with Postgres database in AWS and upload the final datasets.
2. Use Python BOTO Library to connect and upload the inital and final datasets to S3.

Solution Architecture
1. Use Github to host project code and documentation.
2. Build the local project as a docker file.
3. Host the project as a Docker file in ECR.
4. Create private S3 Bucket to place the .env file which will store runtime variables and secrets.
5. Create S3 bucket to store the inital and final datasets to S3
6. Create Postgres Database in Cloud using AWS RDS Web Service.
7. Create appropriate inline IAM policy that would be required by the ECS service.
8. Create appropriate IAM policy for the users to run the ECS tasks.


## Breakdown of tasks 
How is your project broken down? Who is doing what?

- Create Github Repository - Ajay
- Create Draft Project Plan - Sukarno, Pooja, Ajay
- Extract - Pooja
- Transform - Perform transformations using Pandas DF APIs - Pooja
- Pipeline - Ajay
- Load - Sukarno
- Logging - Pooja
- Testing - Ajay 
- Generating the Docker File - Sukarno, Pooja, Ajay
- Create private S3 Bucket to place the .env file - Sukarno
- Create S3 bucket to store the inital and final datasets to S3 - Sukarno
- Create Postgres Database in Cloud using AWS RDS Web Service - Sukarno
- Create appropriate inline IAM policy that would be required by the ECS service - Sukarno
- Create appropriate IAM policy for the users to run the ECS tasks - Sukarno
- ECS - Sukarno, Pooja, Ajay
- EKS - Sukarno, Pooja, Ajay
- Documentation - Sukarno, Pooja, Ajay


