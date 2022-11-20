from datetime import datetime
start_time = datetime.now()
import os
os.system("cls")

import openpyxl
import glob

from openpyxl.styles import Color, PatternFill, Font, Border, Side

octant_sign = [1,-1,2,-2,3,-3,4,-4]
octant_name_id_mapping = {1:"Internal outward interaction", -1:"External outward interaction", 2:"External Ejection", -2:"Internal Ejection", 3:"External inward interaction", -3:"Internal inward interaction", 4:"Internal sweep", -4:"External sweep"}
yellow = "00FFFF00"
yellow_bg = PatternFill(start_color=yellow, end_color= yellow, fill_type='solid')
black = "00000000"
double = Side(border_style="thin", color=black)
black_border = Border(top=double, left=double, right=double, bottom=double)

#Code starts here
def reset_count(count):
    for item in octant_sign:
        count[item] = 0

# Method to initialise dictionary with 0 for "octant_sign" except 'left'
def reset_count_except(count, left):
    for item in octant_sign:
        if(item!=left):
            count[item] = 0

def set_frequency(longest, frequency, outputSheet):
    # Iterating "octant_sign" and updating sheet
    for i in range(9):
        for j in range(3):
            outputSheet.cell(row = 3+i, column = 45+j).border = black_border

    outputSheet.cell(row=3, column=45).value= "Octant ##"
    outputSheet.cell(row=3, column=46).value= "Longest Subsquence Length"
    outputSheet.cell(row=3, column=47).value= "Count"

    for i, label in enumerate(octant_sign):
        currRow = i+3
        outputSheet.cell(row=currRow+1, column=45).value = label	
        outputSheet.cell(column=46, row=currRow+1).value = longest[label]
        outputSheet.cell(column=47, row=currRow+1).value = frequency[label]

# Function to set time range for longest subsequence
def longest_subsequence_time(longest, frequency, timeRange, outputSheet):
    # Naming columns number
    lengthCol = 50
    freqCol = 51
    
    # Initial row, just after the header row
    row = 4

    outputSheet.cell(row=3, column = 49).value = "Octant ###"
    outputSheet.cell(row=3, column = 50).value = "Longest Subsquence Length"
    outputSheet.cell(row=3, column = 51).value = "Count"

    # Iterating all octants 
    for octant in octant_sign:
        try:
            # Setting octant's longest subsequence and frequency data
            outputSheet.cell(column=49, row=row).value = octant
            outputSheet.cell(column=lengthCol, row=row).value = longest[octant]
            outputSheet.cell(column=freqCol, row=row).value = frequency[octant]
        except FileNotFoundError:
            print("File not found!!")
            exit()

        row+=1

        try:
            # Setting default labels
            outputSheet.cell(column=49, row=row).value = "Time"
            outputSheet.cell(column=lengthCol, row=row).value = "From"
            outputSheet.cell(column=freqCol, row=row).value = "To"
        except FileNotFoundError:
            print("File not found!!")
            exit()

        row+=1

        # Iterating time range values for each octants
        for timeData in timeRange[octant]:
            try:
                # Setting time interval value
                outputSheet.cell(row=row, column=lengthCol).value = timeData[0]
                outputSheet.cell(row=row, column=freqCol).value = timeData[1]
            except FileNotFoundError:
                print("File not found!!")
                exit()
            row += 1

    for i in range(3, row):
        for j in range(49, 52):
            outputSheet.cell(row=i, column = j).border = black_border

def count_longest_subsequence_freq_func(longest, outputSheet, total_count):
    # Dictionary to store consecutive sequence count
    count = {}

    # Dictionary to store frequency count
    frequency = {}

    # Dictionary to store time range
    timeRange = {}

    for label in octant_sign:
        timeRange[label] = []

    # Initialing dictionary to 0 for all labels
    reset_count(count)
    reset_count(frequency)

    # Variable to check last value
    last = -10

    # Iterating complete excel sheet
    for i in range(0, total_count):
        currRow = i+3
        try:
            curr = int(outputSheet.cell(column=11, row=currRow).value)
            
            # Comparing current and last value
            if(curr==last):
                count[curr]+=1
            else:
                count[curr]=1        
                reset_count_except(count, curr)

            # Updating frequency
            if(count[curr]==longest[curr]):
                frequency[curr]+=1

                # Counting starting and ending time of longest subsequence
                end = float(outputSheet.cell(row=currRow, column=1).value)
                start = 100*end - longest[curr]+1
                start/=100

                # Inserting time interval into map
                timeRange[curr].append([start, end])

                # Resetting count dictionary
                reset_count(count)
            else:
                reset_count_except(count, curr)
        except FileNotFoundError:
            print("File not found!!")
            exit()
        except ValueError:
            print("File content is invalid!!")
            exit()

        # Updating 'last' variable
        last = curr

    # Setting frequency table into sheet
    set_frequency(longest, frequency, outputSheet)

    # Setting time range for longest subsequence
    longest_subsequence_time(longest, frequency, timeRange, outputSheet)

# Function to set frequency count to sheet
			
def find_longest_subsequence(outputSheet, total_count):
	# Dictionary to store consecutive sequence count
    count = {}

    # Dictionary to store longest count
    longest = {}

    # Initialing dictionary to 0 for all labels
    reset_count(count)
    reset_count(longest)

    # Variable to check last value
    last = -10

    # Iterating complete excel sheet
    for i in range(0, total_count):
        currRow = i+3
        try:
            curr = int(outputSheet.cell(column=11, row=currRow).value)

            # Comparing current and last value
            if(curr==last):
                count[curr]+=1
                longest[curr] = max(longest[curr], count[curr])
                reset_count_except(count, curr)
            else:
                count[curr]=1
                longest[curr] = max(longest[curr], count[curr])
                reset_count_except(count, curr)
        except FileNotFoundError:
            print("File not found!!")
            exit()

        # Updating "last" variable
        last = curr

    # Method to Count longest subsequence frequency
    count_longest_subsequence_freq_func(longest, outputSheet, total_count)

def transition_count_func(row, transition_count, outputSheet):
    # Setting hard coded inputs
    try:
        outputSheet.cell(row=row, column=36).value = "To"
        outputSheet.cell(row=row+1, column=35).value = "Octant #"
        outputSheet.cell(row=row+2, column=34).value = "From"

        for i in range(35, 44):
            for j in range(row+1, row+1+9):
                outputSheet.cell(row=j, column = i).border = black_border

    except FileNotFoundError:
        print("Output file not found!!")
        exit()
    except ValueError:
        print("Row or column values must be at least 1 ")
        exit()

    # Setting Labels
    for i, label in enumerate(octant_sign):
        try:
            outputSheet.cell(row=row+1, column=i+36).value=label
            outputSheet.cell(row=row+i+2, column=35).value=label
        except FileNotFoundError:
            print("Output file not found!!")
            exit()
        except ValueError:
            print("Row or column values must be at least 1 ")
            exit()

    # Setting data
    for i, l1 in enumerate(octant_sign):
        maxi = -1

        for j, l2 in enumerate(octant_sign):
            val = transition_count[str(l1)+str(l2)]
            maxi = max(maxi, val)

        for j, l2 in enumerate(octant_sign):
            try:
                outputSheet.cell(row=row+i+2, column=36+j).value = transition_count[str(l1)+str(l2)]
                if transition_count[str(l1)+str(l2)] == maxi:
                    maxi = -1
                    outputSheet.cell(row=row+i+2, column=36+j).fill = yellow_bg
            except FileNotFoundError:
                print("Output file not found!!")
                exit()
            except ValueError:
                print("Row or column values must be at least 1 ")
                exit()

def set_mod_overall_transition_count(outputSheet, mod, total_count):
	# Counting partitions w.r.t. mod
    try:
        totalPartition = total_count//mod
    except ZeroDivisionError:
        print("Mod can't have 0 value")
        exit()

    # Checking mod value range
    if(mod<0):
        raise Exception("Mod value should be in range of 1-30000")

    if(total_count%mod!=0):
        totalPartition +=1

    # Initializing row start for data filling
    rowStart = 16

    # Iterating all partitions 
    for i in range (0,totalPartition):
        # Initializing start and end values
        start = i*mod
        end = min((i+1)*mod-1, total_count-1)

        # Setting start-end values
        try:
            outputSheet.cell(column=35, row=rowStart-1 + 13*i).value = "Mod Transition Count"
            outputSheet.cell(column=35, row=rowStart + 13*i).value = str(start) + "-" + str(end)
        except FileNotFoundError:
            print("Output file not found!!")
            exit()
        except ValueError:
            print("Row or column values must be at least 1 ")
            exit()

        # Initializing empty dictionary
        transCount = {}
        for a in range (1,5):
            for b in range(1,5):
                transCount[str(a)+str(b)]=0
                transCount[str(a)+str(-b)]=0
                transCount[str(-a)+str(b)]=0
                transCount[str(-a)+str(-b)]=0
                
        # Counting transition for range [start, end)
        for a in range(start, end+1):
            try:
                curr = outputSheet.cell(column=11, row=a+3).value
                next = outputSheet.cell(column=11, row=a+4).value
            except FileNotFoundError:
                print("Output file not found!!")
                exit()
            except ValueError:
                print("Row or column values must be at least 1 ")
                exit()

            # Incrementing count for within range value
            if(next!=None):
                transCount[str(curr) + str(next)]+=1

        # Setting transition counts
        transition_count_func(rowStart + 13*i, transCount, outputSheet)