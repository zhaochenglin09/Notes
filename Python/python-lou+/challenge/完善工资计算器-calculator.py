#!/usr/bin/python3
import sys
import math

def calculator(salary):
    Initialamount = 3500.00
    insurance = salary * (0.08 + 0.02 + 0.005 + 0 + 0 + 0.06)
    #print(insurance)
    salarypartone = salary - insurance
    #print(salarypartone)

    if salarypartone <= Initialamount:
        ressalary = salarypartone
    else:
        salaryparttwo = salary - insurance - Initialamount
        #print(salaryparttwo)
        if salaryparttwo <= 0.00:
            taxrate = 0.00
            kouchushu = 0.00

        elif salaryparttwo <= 1500.00 and salaryparttwo >  0.00:
            taxrate = 0.03
            kouchushu = 0.00

        elif salaryparttwo > 1500.00 and salaryparttwo <= 4500.00:
            taxrate = 0.1
            kouchushu = 105.00
        elif salaryparttwo > 4500.00 and salaryparttwo <= 9000.00:
            taxrate = 0.2
            kouchushu = 555.00    

        elif salaryparttwo > 9000.00 and salaryparttwo <= 35000.00:
            taxrate = 0.25
            kouchushu = 1005.00

        elif salaryparttwo > 35000.00 and salaryparttwo <= 55000.00:
            taxrate = 0.3
            kouchushu = 2755.00

        elif salaryparttwo > 55000.00 and salaryparttwo <= 80000.00:
            taxrate = 0.35
            kouchushu = 5505.00

        else:
            taxrate = 0.45
            kouchushu = 13505.00
        #print (taxrate)
        #print (kouchushu) 
        #print(salaryparttwo * taxrate - kouchushu)
        #print(salary)
        ressalary = salarypartone - (salaryparttwo * taxrate - kouchushu)
        #print(ressalary)
    return ressalary



if __name__ == '__main__':

    try:

        keylist = list()
        valuelist = list()

        for arg in sys.argv[1:]:
            temp = arg.split(':') 
            keylist.append(int(temp[0]))
            valuelist.append(int(temp[1]))
        resprint = dict(zip(keylist,valuelist))     

        for key,value in resprint.items():
            resvalue = calculator(value)
            print('{}:{:.2f}'.format(key,resvalue))


    except ValueError:
        print("Parameter Error")

