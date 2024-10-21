import pandas as pd

df = pd.read_csv('./data_.csv')

print("data frame classic")
print(df,'\n')

print("data frame to_string")
print(df.to_string(),'\n')