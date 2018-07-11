str = "Life is too short, You need Python"

str = str.lower()

str = str.replace(" ","").replace(",","")
lst = list(str)
print("lst: ", lst)
# str = str.lower().replace(" ","").replace(",","")

chars = set(lst)
print("chars:", chars)

lst = list(chars)
print("lst: ", lst)

list.sort(lst)
print("lst: ", lst)
print("length of lis: ", len(lst))