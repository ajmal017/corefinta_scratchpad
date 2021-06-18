import pandas as pd

df = pd.read_csv('mailing_list_sorted.csv')

# print(df)

df.drop_duplicates(subset = 'Email Address', keep = False, inplace = True)

print(df)
df.to_csv('new_mailing_list.csv')
