import csv
import pandas as pd
from datetime import datetime
import openpyxl
from tkinter import N
import os
os.system("cls")
import numpy as np
import calendar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
start_time = datetime.now()

def attendance_report():
                                ##file reading is done here
    inp_file = pd.read_csv('input_attendance.csv')
    inp = inp_file.fillna("2001CCXX Random") ##filling the empty cells with garbage value
    
    
    try:
        rollno_inp=pd.read_csv('input_registered_students.csv')          ##reading the registered student file
    except:
        print('File containing name of all students is missing!')
    mc=sum(1 for row in open("input_registered_students.csv"))         ##getting the size of dataframe
    mc_consolidated=sum(1 for row in open("input_attendance.csv"))
    total_dates=list()
    for j in range(0,mc_consolidated-1):
        day=inp.at[j,'Timestamp'].split()[0].split('-')[0]
        month=inp.at[j,'Timestamp'].split()[0].split('-')[1]
        year=inp.at[j,'Timestamp'].split()[0].split('-')[2]
        date=datetime.strptime(f'{year}-{month}-{day}', "%Y-%m-%d").date()
        day_name=date.strftime("%A")
        if day_name=="Monday" or day_name=="Thursday":
            if inp.at[j,'Timestamp'].split()[0] not in total_dates:
                total_dates.append(inp.at[j,'Timestamp'].split()[0]) ##getting the total dates on which lectures were held
    
                                                                    
    fileName_consolidated=".\output\\attendance_report_consolidated.xlsx"
    try:
        output_file=openpyxl.Workbook()
        output=output_file.active
        output_file.save(fileName_consolidated)
    
    except:
        print("Code is not working")