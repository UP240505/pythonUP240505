def same_type(lst):
    for i in lst:
        for j in range(i, len(lst)):
            if type(i) != type(lst[j]):
                return "Not Same"
    return "Same"


print(same_type([1, 2, 3, 4]))