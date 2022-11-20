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
    try:                              ##file reading
        inp_file = pd.read_csv('input_attendance.csv')
        inp = inp_file.fillna("2001CCXX Random") ##filling the empty cells with garbage value
    except:
        print("File not found")
    
    
    try:
        rollno_inp=pd.read_csv('input_registered_students.csv')          ##reading the registered student file
    except:
        print("File is not generated")
import os
import math
from datetime import datetime
start_time = datetime.now()

os.system('cls')

def get_fall(element):
    fall_at = int(element[:element.index('-')])
    return(fall_at)