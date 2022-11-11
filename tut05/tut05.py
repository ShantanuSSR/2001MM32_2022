from datetime import datetime
start_time = datetime.now()

#importing input excel file
import openpyxl
wb = openpyxl.load_workbook(r'octant_input.xlsx')
sheet = wb.active