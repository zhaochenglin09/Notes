#!/usr/bin/python3
import sys
import math



  
def main():
    
    if len(sys.argv) != 2:
        print("Parameter Error")
        exit()
    
    try:
        salary = int(sys.argv[1])

    except ValueError:
        print("Parameter Error")
        exit()
    
    

    insurance = 0.00
    Initialamount = 3500.00
    salarypart1 = salary - insurance - Initialamount

     
    if salarypart1 <= 0.00:
        taxrate = 0.00
        kouchushu = 0.00

    elif 0.00 < salarypart1 <= 1500.00:
        taxrate = 0.03
        kouchushu = 0.00


    elif 1500.00 < salarypart1 <= 4500.00:
        taxrate = 0.1
        kouchushu = 105.00
    elif 4500.00 < salarypart1 <= 9000.00:
        taxrate = 0.2
        kouchushu = 555.00    

    elif 9000.00 < salarypart1 <= 35000.00:
        taxrate = 0.25
        kouchushu = 1005.00

    elif 35000.00 < salarypart1 <= 55000.00:
        taxrate = 0.3
        kouchushu = 2755.00

    elif 55000.00 < salarypart1 <= 80000.00:
        taxrate = 0.35
        kouchushu = 5505.00

    else:
        taxrate = 0.45
        kouchushu = 13505.00

 
    salarypart2 = salarypart1 * taxrate - kouchushu

    if salarypart2 == -0.00:
        salarypart2 = 0.00

    print('{:.2f}'.format(salarypart2))

if __name__ == '__main__':
    main()
