join_set = A.union(B)
print(join_set)

intersected_set = A.intersection(B)
print(intersected_set)

print(A.issubset(B))

print(A.isdisjoint(B))

ab_join = A.union(B)
ba_join = B.union(A)
print(ab_join)
print(ba_join)

print(A.symmetric_difference(B))

del A
del B

age_set = set(age)
print(age_set)
if len(age_set) > len(age):
    print("Length of set is bigger")
else:
    print("Length of list is bigger")

sentence = "I am a teacher and I love to inspire and teach people"
lst = sentence.strip().split()
words = set(lst)
print(len(words))