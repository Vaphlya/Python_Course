import math
import time
def add(a,b) :
    return a + b

def subtract(a,b) :
    return a - b

def multiply(a,b) :
    return a * b

def divide(a,b) :
    if a or b == 0 :
        print('На нуль ділити не можна')
        time.sleep(2)
        exit
    return a / b
