from datetime import datetime
start_time = datetime.now()

#importing input excel file
import openpyxl
wb = openpyxl.load_workbook(r'octant_input.xlsx')
sheet = wb.active

#finding the number of rows
row_count=sheet.max_row
entire_count=row_count-1


# creating a list to store octants sign
Octant_Sign_List = [1, -1, 2, -2, 3, -3, 4, -4]

#Code
def octant_ranking(mod):
    if mod>30000:
        raise Exception('Mod value needs to be less or equal to 30000.')

    octant_id = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
    variable_row = (30000//mod)+8
    for i, label in enumerate(Octant_Sign_List):
        try:
            sheet.cell(row=1, column=i+22).value = label
            sheet.cell(row=2, column=i+22).value = 'Rank of ' + str(label)
            sheet.cell(row=variable_row+i+1,column=14).value=label
            sheet.cell(row=variable_row+i+1,column=15).value=octant_id[str(label)]
        except FileNotFoundError:
            print("File not found")
            exit()
    try:
        sheet.cell(row=2, column=30).value = 'Rank1 Octant ID'
        sheet.cell(row=2, column=31).value = 'Rank1 Octant Name'
        sheet.cell(row=variable_row, column=14).value = 'Octant ID'
        sheet.cell(row=variable_row, column=15).value = 'Octant Name'
        sheet.cell(row=variable_row, column=16).value = 'Count of Rank1 Mod values'
    except FileNotFoundError:
        print("File not found")
        exit()
    # code for ranking the octants
    for i in range(3,5+(30000//mod)):
        try:
            if i==4:
                continue
            list_tuple_rank=[]
            for j in range(14,22):
                count = int(sheet.cell(row=i,column=j).value)
                column_no = j
                list_tuple_rank.append((column_no,count))
            # sorting in descending order on the basis of count values
            list_tuple_rank.sort(key=lambda x:x[1], reverse=True)
            # storing the rank in the sheet
            rank=1
            for pair in list_tuple_rank:
                sheet.cell(row = i, column = pair[0]+8).value = rank
                rank+=1
            # finding and storing rank1 for each mod value and overall count as well
            for j in range(22,30):
                if int(sheet.cell(row = i, column = j).value) == 1:
                    octant_sign_rank1 = sheet.cell(row = 1, column = j).value
                    sheet.cell(row = i, column = 30).value = octant_sign_rank1
                    sheet.cell(row = i, column = 31).value = octant_id[str(octant_sign_rank1)]
                    break
        except FileNotFoundError:
            print("File not found")
            exit()
    # calculate the number of rank1 for each octant_sign per mod
    begin = variable_row+1
    for j in range(22,30):
        try:
            rank1_count = 0
            for i in range(5,5+(30000//mod)):
                if int(sheet.cell(row = i,column = j).value)==1:
                    rank1_count+=1
            sheet.cell(row = begin,column = 16).value = rank1_count
            begin+=1
        except FileNotFoundError:
            print ("File missing")
            exit()

def count_in_range(mod):
    if mod>30000:
        raise Exception('mod value should be less than or equal to 30000')
    begin=2
    add=5
    while begin<entire_count:
        # loop to initialize the cell value as 0
        try:
            for j in range(14,22):
                sheet.cell(row=add,column=j).value=0

            # loop to add the count of octant in appropriate cell
            for i in range(begin,min(row_count+1,mod+begin)):
                region = sheet.cell(row=i,column=11).value
                if region==1:
                    sheet.cell(row=add,column=14).value += 1
                elif region==-1:
                    sheet.cell(row=add,column=15).value+=1
                elif region==2:
                    sheet.cell(row=add,column=16).value+=1
                elif region==-2:
                    sheet.cell(row=add,column=17).value+=1
                elif region==3:
                    sheet.cell(row=add,column=18).value+=1
                elif region==-3:
                    sheet.cell(row=add,column=19).value+=1
                elif region==4:
                    sheet.cell(row=add,column=20).value+=1
                else:
                    sheet.cell(row=add,column=21).value+=1
            # adding range value in appropriate cell
            x1=str(begin-2)
            y1=str(min(entire_count-1,mod+begin-3))
            sheet.cell(row=add,column=13).value=x1+'-'+y1

            # changed the value of for by increasing it by mod
            begin+=mod
            #increasing adding row by 1
            add+=1
        except FileNotFoundError:
            print('File Missing!')
            exit()