
def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]

lst = [(1, 2), (5, 7), (3, 6), (1, 2)]
print(removeDuplicates(lst))