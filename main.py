import json
import coursemaker

coursemaker.coursemaker()

JSONfile = 'courses.json'

with open(JSONfile, 'r') as file:
    courseList = json.load(file)


while True:
    rollnumber = str(input("Enter your rollnumber: "))
    try:
        batch = int(rollnumber[:4])
        fDegree = rollnumber[4:6]
        sDegree = rollnumber[6:8]
        code = int(rollnumber[8:12])
        campus = rollnumber[12]
        break
    except:
        print('please input correct roll num in the form of yyyyXXXXzzzzG')
