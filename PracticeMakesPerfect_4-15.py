"""Prvi način"""
def digit_sum(n):
    u_znak = str(n)
    suma = 0
    for number in u_znak:
        suma = suma + int(number)
    return suma

"""Drugi način"""
def digit_sum_floor(n):
    suma = 0
    while n > 0:
        suma = suma + n%10
        n = n // 10
        print "n: "
        print n
        print "Suma: "
        print suma
    

digit_sum_floor(434)
