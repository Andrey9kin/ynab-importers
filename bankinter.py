import os
import sys
import pandas as pd
from converter import covert

# For more info
# https://docs.youneedabudget.com/article/921-formatting-csv-file

excel_files = []

if len(sys.argv) > 1:
    for file_path in sys.argv[1:]:
        if os.path.isfile(file_path):
            excel_files.append(file_path)
        else:
            print(f'File {file_path} does not exist')
else:
    # Search for files that start from Movimientos and end with .xls
    for file_path in os.listdir():
        if file_path.startswith('Movimientos') and file_path.endswith('.xls'):
            excel_files.append(file_path)

print('Provided transaction files: {}'.format(excel_files))

for excel_file in excel_files:
    print('Processing: {}'.format(excel_file))
    # read the file and skip first 3 rows since they contain the header
    df = pd.read_excel(excel_file, skiprows=[0,1,2])

    columns_to_drop = ['SALDO', 'IMPORTE', 'FECHA CONTABLE']
    columns_to_rename = {'FECHA VALOR': 'Date', 'DESCRIPCION': 'Payee'}
    column_with_amounts = 'IMPORTE'
    result = covert(df, columns_to_drop, columns_to_rename, column_with_amounts)

    out = f'{excel_file}.csv'
    print(f'exporting to: {out}')
    result.to_csv(out, index=False)


