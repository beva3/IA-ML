import pandas as pd

#read file csv, ==> Data Frame
df = pd.read_csv("./data.csv")

#default data
print(df)

print('\n',
      'add new column\n')
#add new column 'total', and select : math,pc,svt
df['total'] = df[['math', 'pc', 'svt']].sum(axis=1)
print('update : \n',df,'\n')

# #ptint label : colimn
# print('\n',
#       'labels colums\n')
# print(df.columns)

#the first line
# print('\n',
#       'head():')
# print(df.head(1),'\n')

# print('describe :\n',df.describe(),'\n')

"""
result :
describe :
             math         pc       svt       total
count   5.000000   5.000000   5.00000    5.000000
mean   86.800000  84.600000  84.40000  255.800000
std     5.718391   6.580274   4.97996   15.578832
min    78.000000  75.000000  79.00000  239.000000
25%    85.000000  82.000000  80.00000  240.000000
50%    88.000000  85.000000  85.00000  260.000000
75%    90.000000  89.000000  87.00000  267.000000
max    93.000000  92.000000  91.00000  273.000000 

what it want to say?
"""

# student_name = df['name']
# print('NAME\n',student_name,'\n')

# note_math = df['math']
# print('MATH\n',note_math,'\n')

# total_ok = df[df['total'] > 250]
# print('TOTAL >250\n',total_ok,'\n')

#axixs = 1: mamafa ny mitsangana
df=df.drop('total',axis=1)
print('Drop column total\n',df,'\n')