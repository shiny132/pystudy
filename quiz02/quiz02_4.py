s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""

# 데이터 정제
s = s.replace(",", "").replace(".","").replace("\n","").upper()
print(s)

summary = {}
# 문자열을 자르겠습니다.
splits = s.split(" ")
print(splits)

for split in splits:
    if split in summary.keys(): # split한 단어가 summary의 키에 없으면 summary 키와 값을 설정하고, 있으면 1씩 증가시킴
        summary[split] += 1
    else:
        summary[split] = 1

for key, value in summary.items():
    print("{}: {}".format(key, value))
