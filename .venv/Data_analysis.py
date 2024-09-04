import pandas as pd
import Data_ingestion 


df= Data_ingestion.ingestion()
# Load the data


print(df.head())
print(df)
print(df.info())
df=df.drop(df.columns[[2]],axis=1)
print(df.head())