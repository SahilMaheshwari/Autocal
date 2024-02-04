import json
import coursemaker
from ics import Calendar, Event

codeToDegree = {'B4' : 'MATH'}

coursemaker.coursemaker()

JSONfile = 'courses.json'
with open(JSONfile, 'r') as file:
    courseList = json.load(file)

cdcFile = 'cdc.json'
with open(cdcFile, 'r') as file:
    cdcList = json.load(file)

while True:
    rollnumber = str(input("Enter your rollnumber: ")).upper()
    print(rollnumber)
    try:
        batch = int(rollnumber[:4])
        fDegree = rollnumber[4:6]
        sDegree = rollnumber[6:8]
        code = int(rollnumber[8:12])
        campus = rollnumber[12]
        break
    except:
        print('please input correct roll num in the form of yyyyXXXXzzzzG')
sem = 1
year = 2024-batch
fDegree = codeToDegree[fDegree]

cdcThisSem = cdcList[fDegree]['Course List'][str(year)+'-'+str(sem)]

for i in cdcThisSem :
    try:
        courseName = courseList[i]["Title"]
        print(courseName)
    except:
        print(i, ' is not offered')