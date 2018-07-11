import math
room_num = input()
split = list(room_num)
summary = {}
for split in split:
    if split in summary.keys():
        summary[split] += 1
    else:
        summary[split] = 1
if "6" in summary and "9" in summary:
    summary["6"] = math.ceil((summary["6"]+summary["9"])/2)
    summary["9"] = 0
elif "6" in summary and "9" not in summary:
    summary["6"] = math.ceil(summary["6"]/2)
elif "9" in summary and "6" not in summary:
    summary["9"] = math.ceil(summary["9"]/2)
print(max(summary.values()))