#!/usr/bin/python3
import sys
import math

try:
    salary = int(sys.argv[1])
    insurance = 0.00
    Initialamount = 3500.00
    salarypart1 = salary - insurance - Initialamount

     
    if salarypart1 <= 0.00:
        taxrate = 0.00
        kouchushu = 0.00

    elif salarypart1 <= 1500.00 and salarypart1 > 0.00:
        taxrate = 0.03
        kouchushu = 0.00


    elif salarypart1 > 1500.00 and salarypart1 <= 4500.00:
        taxrate = 0.1
        kouchushu = 105.00
    elif salarypart1 > 4500.00 and salarypart1 <= 9000.00:
        taxrate = 0.2
        kouchushu = 555.00    

    elif salarypart1 > 9000.00 and salarypart1 <= 35000.00:
        taxrate = 0.25
        kouchushu = 1005.00

    elif salarypart1 > 35000.00 and salarypart1 <= 55000.00:
        taxrate = 0.3
        kouchushu = 2755.00

    elif salarypart1 > 55000.00 and salarypart1 <= 80000.00:
        taxrate = 0.35
        kouchushu = 5505.00

    else:
        taxrate = 0.45
        kouchushu = 13505.00

 
    salarypart2 = salarypart1 * taxrate - kouchushu
    if salarypart2 == -0.00:
        salarypart2 = 0.00

    print('{:.2f}'.format(salarypart2))

except:
    print("Parameter Error")
