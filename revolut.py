import os
import sys
import pandas as pd
from converter import covert

# For more info
# https://docs.youneedabudget.com/article/921-formatting-csv-file

# Started Date colum contains date and time - 2022-12-25 15:20:22
# we need only date
def drop_time_from_date(x):
   return x.split()[0]

csv_file = os.path.abspath(sys.argv[1])
print('Provided budget file: {}'.format(csv_file))

df = pd.read_csv(csv_file)

columns_to_drop = ['Type', 'Product', 'Completed Date', 'Currency', 'Fee', 'State', 'Balance']
columns_to_rename = {'Started Date': 'Date', 'Descripton': 'Payee'}
column_with_amounts = 'Amount'
df['Started Date'] = df['Started Date'].apply(drop_time_from_date)
result = covert(df, columns_to_drop, columns_to_rename, column_with_amounts)

out = f'{csv_file}-ynab-ready.csv'
print(f'exporting to: {out}')
result.to_csv(out, index=False)


