import pandas as pd
from pathlib import Path
paths = [
    Path(r'D:\Jayanth\Headers.xlsx'),
    Path(r'D:\Jayanth\POB.xlsx'),
    Path(r'D:\Jayanth\sales_summ.xlsx'),
    Path(r'D:\Jayanth\Buying_groups.xlsx'),
]
for path in paths:
    print(f'FILE: {path.name}')
    try:
        xls = pd.ExcelFile(path)
    except Exception as exc:
        print(f'ERROR: {exc}')
        continue
    print('SHEETS:', xls.sheet_names)
    for sheet in xls.sheet_names:
        try:
            df = pd.read_excel(path, sheet_name=sheet, header=None)
        except Exception as exc:
            print(f'SHEET ERROR {sheet}: {exc}')
            continue
        print(f'SHEET: {sheet}')
        print(df.head(12).to_string(index=True, header=False))
    print('---')
