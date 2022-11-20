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

    attend_consolidated=pd.read_excel(fileName_consolidated)
    for i in range(0,mc-1):  ##looping the registered students name
        total_Present=0
        date_index=1
        rollno=rollno_inp.at[i,'Roll No']
        fileName=".\output\\"+rollno+'.xlsx'
        output_file=openpyxl.Workbook()
        output=output_file.active
        output_file.save(fileName)
        out=pd.read_excel(fileName)
        for sp_date in total_dates: ##looping through the dates on which lectures were held
            duplicated_attendance=0
            t_lec,t_lec_act,t_lec_fake,t_lec_abs,percent=len(total_dates),0,0,0,0
            t_lec_count=0
            for j in range(0,mc_consolidated-1):
                if inp.at[j,'Attendance'].split()[0]==rollno:  ##if the roll no. matches
                    if inp.at[j,'Timestamp'].split()[0] == sp_date:
                        t_lec_count+=1
                        time=inp.at[j,'Timestamp'].split()[1]
                        hour=time.split(':')[0]
                        minutes=time.split(':')[1]
                        if ((hour=='14') or (hour=='15' and minutes=='00')):  ##if the timing is within the lecture timings
                            if t_lec_act==0:
                                t_lec_act+=1
                            else:
                                duplicated_attendance+=1
                        else:
                            t_lec_fake+=1
        
        ##setting the data begins here
            out.at[0,'Roll']=rollno
            out.at[0,'Name']=rollno_inp.at[i,'Name']
            out.at[date_index,'Dates']=sp_date
            attend_consolidated.at[i+1,'Roll']=rollno
            attend_consolidated.at[i+1,'Name']=rollno_inp.at[i,'Name']
            out.at[date_index,'Total Attendance Count']=t_lec_count
            attend_consolidated.at[i+1,f'{sp_date}']='P' if t_lec_act>0 else 'A'
            if t_lec_act>0: total_Present+=1 
            out.at[date_index,'Real']=t_lec_act
            out.at[date_index,'Duplicate']=duplicated_attendance
            out.at[date_index,'Invalid']= t_lec_fake
            out.at[date_index,'Absent']=1 if t_lec_act==0 else 0
            date_index+=1

        ##setting the data into the consolidated file
        attend_consolidated.at[i+1,'Actual Lecture Taken']=len(total_dates)
        attend_consolidated.at[i+1,'Total Real']=total_Present
        attend_consolidated.at[i+1,'% Attendance']=round(total_Present/len(total_dates)*100,2)
        out.to_excel(fileName,index=False)

    attend_consolidated.to_excel(fileName_consolidated,index=False)

    send_mail()
    ## Writing code for the mail purpose        
def send_mail():
    path = os.getcwd().replace("\\","/") + "/output/attendance_report_consolidated.xlsx"

    fromaddr = input("Enter Mail Id: ")
    toaddr = "cs3842022@gmail.com"
    Password_ = input("Enter Password: ")

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Attendance Report Consolidated"

    # string to store the body of the mail
    body = "Dear Sir,\n\nPlease find below attached file.\n\nWarm Regards\nShantanu singh\n2001MM32"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = 'attendance_report_consolidated.xlsx'

    attachment = open(path, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, Password_)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

from platform import python_version
ver = python_version()
##version checking of the python
if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))