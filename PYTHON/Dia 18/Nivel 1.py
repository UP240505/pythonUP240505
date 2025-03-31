import re
#1_____________________________________________________
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
lst = paragraph.split()
lst_set = set(lst)
output = []

for word in lst_set:
    matches = re.findall(word, paragraph, re.I)
    count = len(matches)
    tup = []
    tup.append(count)
    tup.append(word)
    tup = tuple(tup)
    output.append(tup)
print(output)
#2____________________________________________________
points = [-12, -4, -3, -1, 0, 4, 8]
print(abs(points[0]) + points[len(points)-1])


def is_valid_variable(a):
    regex_pattern1 = r'^[a-z]|^[A-Z]|^_'
    if re.findall(regex_pattern1, a):
        print(True)
    else:
        print(False)