#1_______________________________________
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
#2_______________________________________
def seven_random():
    s = set()
    lst = []
    while True:
        if len(s) == 7:
            lst = s
            return lst
        n = random.randint(0, 10)
        s.add(n)