"""
Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

For example: remove_duplicates([1,1,2,2]) 
should return [1,2].

"""
def remove_duplicates(values):
    novo = []
    for value in values:
        if value not in novo:
            novo.append(value)
    return novo
