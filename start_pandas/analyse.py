import pandas as pd

#read file csv, ==> Data Frame
df = pd.read_csv("./data.csv")

#default data
print(df)

print('\n',
      'add new column\n')
#add new column 'total', and select : math,pc,svt
df['total'] = df[['math', 'pc', 'svt']].sum(axis=1)
print(df)

#ptint label : colimn
print('\n',
      'labels colums\n')
print(df.columns)