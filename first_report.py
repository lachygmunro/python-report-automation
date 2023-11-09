import pandas as pd
from datetime import datetime

def generate_first_report(extract):
    data_frame = pd.read_excel(extract, sheet_name="Sheet1", header=0)
    data_frame.insert(5, "Year", pd.DatetimeIndex(data_frame['Date']).year)
    data_frame.insert(0, "Index", data_frame['Last Name'].astype(str) + data_frame['DOB'].astype(str), allow_duplicates=True)
    pivot_table = data_frame.pivot_table(values='Index', index=['Name', 'Purchase'], columns=['Year'], aggfunc="size", fill_value=0)
    date = (datetime.today()).strftime('%d%m%Y')

    with pd.ExcelWriter(date + '_First_Report') as writer:
        pivot_table.to_excel(writer, sheet_name='Pivot')
        data_frame.to_excel(writer, sheet_name="Data", index=False)
        worksheet1 = writer.sheets['Pivot']
        worksheet2 = writer.sheets['Data']
        for column in worksheet1.columns:
            length = max(len(str(cell.value)) for cell in column)
            worksheet1.column_dimensions[column[0].column_letter].width = length + 3
        for column in worksheet2.columns:
            length = max(len(str(cell.value)) for cell in column)
            worksheet2.column_dimensions[column[0].column_letter].width = length + 2
