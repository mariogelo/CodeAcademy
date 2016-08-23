def is_prime(x):
    if x<2: return False
    elif x==2: return True
    else:
        print "Tu si"
        for n in range (2,x-1):
            if x%n == 0:
                print "Nije prime"
                return False
        return True """Ovdje sam ja htio staviti else, pa return True, ali  nije radilo
Izgleda da mora biti u razini sa for petljom - trebam projeriti zašto"""
