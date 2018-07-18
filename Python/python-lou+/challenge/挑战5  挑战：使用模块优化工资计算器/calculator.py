import sys
import csv
import json
import os
from multiprocessing import Process,  Queue
from datetime import date, datetime, timedelta
import getopt
import configparser
from collections import namedtuple
#处理命令行参数类
class Args:

    def __init__(self):
        
        
 #      try:
        opts,argsothers = getopt.getopt(sys.argv[1:],'-c:-d:-o:-C:',[])
   
        cityname = 'DEFAULT'
        self.cityname = cityname

        for opt_name,opt_value in opts:
             
            
#            print(opt_name,opt_value)
            if opt_name in ('-C'):
                opt_value = opt_value.upper()
                cityname = opt_value
                self.cityname = cityname                     
            if opt_name in ('-c'):
                configfile = opt_value
                self.configfile = configfile
            if opt_name in ('-d'):
                userfile = opt_value
                self.userfile = userfile
            if opt_name in ('-o'):
                gongzifile = opt_value
                self.gongzifile = gongzifile
            
    

      # except getopt.GetoptError:
       #     print('getopt.GetoptError')
        #    sys.exit(1)


#        index = args.index('-c')
#        configfile = args[index+1]
#        index2 = args.index('-d')
#        userfile = args[index2+1]
#        index3 = args.index('-o')
#        gongzifile = args[index3+1]

 #       if os.path.isfile(configfile) and os.path.isfile(userfile) and os.path.isfile(gongzifile):
 #       self.configfile = configfile
#        self.userfile = userfile
#        self.gongzifile = gongzifile
#        self.cityname = cityname 
#        else:
#            raise ValueError
#            print('file path is wrong')


#配置文件类，得到文件中的社保参数
class Config:
    def __init__(self, configfile, cityname):
        self.configfile = configfile
        self.cityname = cityname
        self.config = self._read_config()

    def _read_config(self):
        config= {}

        cf = configparser.ConfigParser()
        cf.read(self.configfile)
        kvs = cf.items(self.cityname)
        
        for x in kvs:
            name = x[0]
            value = float(x[1])
            config[name]= value

        return config

    



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

        IncomeTaxQuickLookupItem = namedtuple(
                'IncomeTaxQuickLookupItem',
                ['start_point','tax_rate','quick_subtractor']
                )
    
        INCOME_TAX_QUICK_LOOKUP_TABLE = [
                IncomeTaxQuickLookupItem(80000, 0.45, 13505),
                IncomeTaxQuickLookupItem(55000, 0.35, 5505),
                IncomeTaxQuickLookupItem(35000, 0.30, 2755),
                IncomeTaxQuickLookupItem(9000, 0.25, 1005),
                IncomeTaxQuickLookupItem(4500, 0.2, 555),
                IncomeTaxQuickLookupItem(1500, 0.1, 105),
                IncomeTaxQuickLookupItem(0, 0.03, 0)
                ]



        for simpleusersalary in allusersalary:
            
            if simpleusersalary[1] < configshujudict['jishul']:
                insurance = configshujudict['jishul'] 
            
            elif simpleusersalary[1] > configshujudict['jishul'] and simpleusersalary[1] < configshujudict['jishuh']:
    
                jishuincome = simpleusersalary[1] 
            
            else:
                jishuincome = configshujudict['jishuh']
            
            

            insurance = jishuincome * (configshujudict['yanglao'] + configshujudict['yiliao'] + configshujudict['shiye'] + configshujudict['gongshang'] + configshujudict['shengyu'] + configshujudict['gongjijin']) 
              
            #print(insurance)
            salarypartone = simpleusersalary[1] - insurance
            #print(salarypartone)

            taxable_part = salarypartone - Initialamount
            if taxable_part <= 0:
                geshuitax = 0.00
                
            for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
                if taxable_part > item.start_point:
                    geshuitax = taxable_part * item.tax_rate - item.quick_subtractor
                    ressalary = salarypartone - geshuitax
                else:
                    ressalary = salarypartone


            shuiqiangongzi = int(simpleusersalary[1])
            insurance = ("%.2f" % insurance)
            geshuitax = ("%.2f" % geshuitax)
            ressalary = ("%.2f" % ressalary)
            nowtime = datetime.now()
            calculatortime = date.strftime(nowtime, '%Y-%m-%d %H:%M:%S')
            #print(calculatortime)
            simpleuserfanhui.append((simpleusersalary[0],shuiqiangongzi,insurance,geshuitax,ressalary,calculatortime))


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
#    print(argres.configfile,argres.cityname,argres.userfile,argres.gongzifile)
    configx = Config(argres.configfile,argres.cityname)


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
