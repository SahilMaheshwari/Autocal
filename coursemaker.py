import json
import csv
import datetime

TTfile = "Timetable.csv"
JSONfile = "courses.json"

def datedefiner(Times):

    Times = str(Times)
    Times.split()
    
    days = ['M', 'T', 'W', 'TH', 'F', 'S']
    slots = [str(i+1) for i in range(11)]

    defined = []
    temp = []
    wasDate = True
    
    for i in Times:
        i = i[0]

        if i in days and wasDate:
            temp.append([i])
            wasDate = True

        elif i in days and not wasDate:
            temp = []
            temp.append([i])
            wasDate = True

        elif i in slots and wasDate:
            for j in range(len(temp)):
                temp[j].append(i)
                defined.append(temp[j])
            wasDate = False

        elif i in slots and not wasDate:
            for j in range(len(temp)):
                temp[j].append(i)
            wasDate = False
        
    return defined

def coursemaker():
    global TTfile
    courseDict = {}

    with open(TTfile, 'r') as file:
        line = csv.reader(file)
        for i in line:
            courseDict[i[1]] = {
                'ID'     : i[0],
                'Code'   : i[1],
                'Title'  : i[2],
                'LorT'   : i[4],
                'Section': i[5],
                'Times'  : datedefiner(i[6]),
                'Room'   : i[7],
                'Midsem' : [i[8]] 
            }

    courseDict = {k: v for k, v in courseDict.items() if v}

    with open(JSONfile, 'w') as file:
        json.dump({}, file)

    with open(JSONfile, 'w') as file:
        json.dump(courseDict, file, indent=2)

coursemaker()
