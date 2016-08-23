"""
Define a function called count that has two arguments called sequence and item.
Return the number of times the item occurs in the list.
For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).

Moj kod:

def count(sequence, item):
    times = 0
    i = 0
    for i in range(len(sequence)):
        if sequence[i] == item:
            times = times + 1
    return times

"""
    
def count(sequence, item):
    found=0
    for a in sequence:
        if a==item:
            found = found +1
    return found
