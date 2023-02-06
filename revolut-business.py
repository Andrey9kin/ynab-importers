from converter import covert

# For more info
# https://docs.youneedabudget.com/article/921-formatting-csv-file

csv_file = os.path.abspath(sys.argv[1])
print('Provided budget file: {}'.format(csv_file))

df = pd.read_csv(csv_file)

columns_to_drop = [
   'Date completed (UTC)',
   'ID',
   'Type',
   'Payer',
   'Card number',
   'Orig currency',
   'Orig amount',
   'Payment currency',
   'Fee',
   'Balance',
   'Account',
   'Beneficiary account number',
   'Beneficiary sort code or routing number',
   'Beneficiary IBAN',
   'Beneficiary BIC'
]
columns_to_rename = {'Date started (UTC)': 'Date', 'Descripton': 'Payee', 'Reference': 'Memo'}
column_with_amounts = 'Amount'
result = covert(df, columns_to_drop, columns_to_rename, column_with_amounts)

out = f'{csv_file}-ynab-ready.csv'
print(f'exporting to: {out}')
result.to_csv(out, index=False)
