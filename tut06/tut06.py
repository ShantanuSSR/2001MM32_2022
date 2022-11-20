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