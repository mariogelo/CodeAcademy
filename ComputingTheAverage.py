"""
Define a function grades_average(), below the grades_sum() function that does the following:

Has one argument, grades, a list
Calls grades_sum with grades
Computes the average of the grades by dividing that sum by float(len(grades)).
Returns the average.
Call the newly created grades_average() function with the list of grades and print the result.
"""
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total=0
    for score in scores:
        total += score
    print total
    return total

def grades_average(grades):
    total2=grades_sum(grades)
    """Ovo je bitan dio. ide float da se dobije decimala. Može ići i float(total2) """
    average=total2/float(len(grades))
    print average
    return average

grades_sum(grades)
grades_average(grades)
