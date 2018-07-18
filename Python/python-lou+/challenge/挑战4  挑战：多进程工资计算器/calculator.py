import sys
import csv
import json
import os
from multiprocessing import Process,  Queue
from datetime import date, datetime, timedelta



#处理命令行参数类
class Args:

    def __init__(self):
        try:
            
            args = sys.argv[1:]

            if len(args) == 6:

                index = args.index('-c')
                configfile = args[index+1]
                index2 = args.index('-d')
                userfile = args[index2+1]
                index3 = args.index('-o')
                gongzifile = args[index3+1]
     
                if os.path.isfile(configfile) and os.path.isfile(userfile) and os.path.isfile(gongzifile):
                    self.configfile = configfile
                    self.userfile = userfile
                    self.gongzifile = gongzifile
                else:
                    raise ValueError
                    print('file path is wrong')


            else:
                raise ValueError
                print('Not right input')

        except:              
            print('Please input again')
            exit(-1)

#配置文件类，得到文件中的社保参数
class Config:
    def __init__(self, configfile):
        self.configfile = configfile
        self.config = self._read_config()

    def _read_config(self):
        config = {}

        with open(self.configfile, 'r') as file1:
            for data1 in file1.readlines():
      
                data22 = data1.replace(' ','')
                data2 = data22.strip()
                data3 = data2.split('=')
                dictvalue = float(data3[1])                
                dictkey = data3[0]
                #print(type(dictvalue))
                config[dictkey]= dictvalue
        return config     

    

    def get_config(self, dictkey):
#       for key,value in self.config.items():
#           print('{}={}'.format(key,value))
        return self.config[dictkey]  


#得到输入的员工工资数据

class UserData:

#    def __init__(self, userfile):
#        self.userfile = userfile
#        self.userdata = self._read_user_data()  

    def _read_user_data(self, userfile, queue):
        userdata = list()
        

        with open(userfile) as file2:
#           count = 0
            for userda1 in file2.readlines():
                userda11 = userda1.strip()
                userda2 = userda11.replace(' ','')
                userda3 = userda2.split(',')
                userdata.append((userda3[0],float(userda3[1])))
           
#                print(userdata[count])
#                count+=1
#        return userdata        
        queue.put(userdata)



#计算工资类
class IncomeTaxCalculator:


    #def __name__(self,allusersalary, configshujudict):


    #计算每个员工的税后工资函数
    def calc_for_all_userdata(self, configshujudict, queue, queue2):

        allusersalary = queue.get() 


        Initialamount = 3500.00

        simpleuserfanhui = list()
    
        for simpleusersalary in allusersalary:
            
            if simpleusersalary[1] < configshujudict['JiShuL']:
                insurance = configshujudict['JiShuL'] * (configshujudict['YangLao'] + configshujudict['YiLiao'] + configshujudict['ShiYe'] + configshujudict['GongShang'] + configshujudict['ShengYu'] + configshujudict['GongJiJin'])
            
            elif simpleusersalary[1] > configshujudict['JiShuL'] and simpleusersalary[1] < configshujudict['JiShuH']:
    
                insurance = simpleusersalary[1] * (configshujudict['YangLao'] + configshujudict['YiLiao'] + configshujudict['ShiYe'] + configshujudict['GongShang'] + configshujudict['ShengYu'] + configshujudict['GongJiJin'])
            
            else:
                insurance = configshujudict['JiShuH'] * (configshujudict['YangLao'] + configshujudict['YiLiao'] + configshujudict['ShiYe'] + configshujudict['GongShang'] + configshujudict['ShengYu'] + configshujudict['GongJiJin'])
            
            
            #print(insurance)
            salarypartone = simpleusersalary[1] - insurance
            #print(salarypartone)
        
            if salarypartone <= Initialamount:
                ressalary = salarypartone
                geshuitax = 0.00
            else:
                salaryparttwo = salarypartone - Initialamount
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
                geshuitax = salaryparttwo * taxrate - kouchushu
                #print(geshuitax)
            
                ressalary = salarypartone - geshuitax
                #print(ressalary)


            shuiqiangongzi = int(simpleusersalary[1])
            insurance = ("%.2f" % insurance)
            geshuitax = ("%.2f" % geshuitax)
            ressalary = ("%.2f" % ressalary)
            simpleuserfanhui.append((simpleusersalary[0],shuiqiangongzi,insurance,geshuitax,ressalary))


#        return simpleuserfanhui
        queue2.put(simpleuserfanhui)
        
        
    
    
    
    
    

    def export(self, exportfile, queue2):
        result = queue2.get()
#        result = self.calc_for_all_userdata(allusersalary, configshujudict)
        with open(exportfile, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)
            print('over')







if __name__ == '__main__':


    a = datetime.now()
    argres = Args()
    configx = Config(argres.configfile)
#    res = configx.get_config('JiShuH')
#    print(res)


    queue = Queue()
    queue2 = Queue()

    userdata = UserData()

    userdataprocess = Process(target=userdata._read_user_data, args=(argres.userfile,queue,))

#    userdata = UserData(argres.userfile)
#    for x in userdata.userdata:
#        print(x)

    userdataprocess.start()
    userdataprocess.join()

    fanhui = IncomeTaxCalculator()

    calculatorprocess = Process(target=fanhui.calc_for_all_userdata, args=(configx.config, queue, queue2,))

    calculatorprocess.start() 
    calculatorprocess.join()


    exportprocess = Process(target=fanhui.export, args=(argres.gongzifile,queue2,))

    exportprocess.start() 
    exportprocess.join()

    b = datetime.now()

    c = b - a
    d = c.total_seconds()
    print('{} .s.'.format(d))
