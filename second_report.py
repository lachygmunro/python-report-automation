import pandas as pd
from datetime import datetime

def generate_second_report(extract):
    data_frame = pd.red_excel(extract, sheet_name="Sheet1", header=0)
    over_18 = data_frame[(data_frame['DOB'] >= '01/01/2005')]
    over_18_pivot = over_18.pivot_table(values='Last Name', index=['First Name'], columns=['DOB'], affunc="size", fill_value=0)
    under_18 = data_frame[(data_frame['DOB'] <= '01/01/2005')]
    date = (datetime.today()).strftime('%d%m%Y')

    with pd.ExcelWriter(date + '_Over18_Second_Report.xlsx', engine='openpyxl') as writer:
        over_18_pivot.to_excel(writer, sheet_name='Over 18 Pivot')
        over_18.to_excel(writer, sheet_name='Over 18 Data')
        worksheet1 = writer.sheets['Over 18 Pivot']
        worksheet2 = writer.sheets['Over 18 Data']
        for column in worksheet1.columns:
            length = max(len(str(cell.value)) for cell in column)
            worksheet1.column_dimensions[column[0].column_letter].width = length + 2
        for column in worksheet2.columns:
            length = max(len(str(cell.value)) for cell in column)
            worksheet2.column_dimensions[column[0].column_letter].width = length + 2

    with pd.ExcelWriter(date + '_Under18_Second_Report.xlsx', engine='openpyxl') as writer:
        under_18.to_excel(writer, sheet_name='Under 18 Data')
        worksheet1 = writer.sheets['Under 18 Data']
        for idx, col_cell in enumerate(worksheet1.columns, 1):
            worksheet1.column_dimensions[col_cell[0].column_letter].width = 20
