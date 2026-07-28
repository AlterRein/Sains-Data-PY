import pandas as pd

df = pd.read_csv('customers-100.csv')
df.head(3)
df
Out = df.to_csv('customers-100.csv')

print(Out)