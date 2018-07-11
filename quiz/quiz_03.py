#두 학생의 kor, eng, math 합계 점수와 평균을 사전 데이터에 "total", "average" 키값으로 넣어 봅시다.

students = [
    {   
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {   
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]
for student in students:
    total = student.get('kor') + student.get('eng') + student.get('math')
    average = total / 3
    student['total'] = total
    student['average'] = average
print(students)

'''
kim = dict(students[0])
lee = dict(students[1])
lst = list(kim.values())
lst2 = list(lee.values())
kor = lst[1] + lst2[1]
eng = lst[2] + lst2[2]
math = lst[3] + lst2[3]

dic = dict({"kortotal": kor, "engtotal": eng, "mathtotal":math, "koraverage" : kor/2, "engeverage":eng/2, "mathaverage":math/2, "total":kor+eng+math, "average":(kor+eng+math)/6})
print(dic)
'''