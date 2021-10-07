import os
import sys
import pandas as pd
from converter import convert

# For more info
# https://docs.youneedabudget.com/article/921-formatting-csv-file

excel_file = os.path.abspath(sys.argv[1])
print('Provided budget file: {}'.format(excel_file))

df = pd.read_excel(excel_file)

columns_to_drop = ['Type', 'Currency Amount', 'Currency Rate', 'Currency', 'Merchant Area', 'ValueDate', 'BookDate', 'Amount']
columns_to_rename = {'TransactionDate': 'Date', 'Text': 'Payee', 'Merchant Category': 'Memo'}
column_with_amounts = 'Amount'
result = convert(df, columns_to_drop, columns_to_rename, column_with_amounts)

out = f'{excel_file}.csv'
print(f'exporting to: {out}')
result.to_csv(out, index=False)


