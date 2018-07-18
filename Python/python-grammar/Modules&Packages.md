# 模块和包(Modules and Packages)

## Modules
### 为什么使用模块？
类似于C语言的include和Java的import功能.模块提供的功能在于代码重用、命名空间划分、跨平台等。

### 模块的搜索路径
#### 为什么要谈寻找路径？

因为使用import语句时,会执行三个步骤:
1. 找到模块文件
2. 编译成位码(需要时)
3. 执行模块的代码来创建定义的对象

**如果想要添加自定义模块,则需要修改寻找路径，让系统找到模块文件完成引用**

#### 搜索路径由sys.path记录管理

```
sys.path是模块搜索的路径的总列表
   Python在启动时将PYTHONPATH和.pth文件的设置值合并到这个列表，并设置第一项为顶层文件的主目录
   可以修改sys.path添加搜索路径，但只在脚本的存在期间有效,长久还是修改PYTHONPATH和.pth文件

搜索模块的路径主要有四个部分
1.程序的主目录
        当前代码工作的目录，这个目录最先被搜索

    2.PYTHONPATH目录
        Python从左到右搜索PYTHONPATH环境变量列出的目录(取决你是否设置该环境变量)

    3.标准链接库目录
        自动搜索标准库模块安装的目录

    4.任何.pth文件的内容
        Python允许用户有效的目录文件.pth添加到模块搜索路径中
```

#### 模块文件的类型

```
  使用内置函数__import__可以定制导入工具,使用import hook实现对多种对象的导入

    import导入的文件可能存在多种格式：
    - 源代码文件 x.py
    - 字节码文件 x.pyc
    - 目录 x
    - 编译扩展模块,使用动态链接 (Linux下的.so文件 Windows下的.dll文件)
    - zip文件组件
    - .net组件,java类等

```

#### 模块存放位置建议
- 模块文件存放于主目录下
- 因为distutils工具包,自定义模模块文件可以存放在 安装位置\Lib\site-packages目录下

### 模块的基本用法
1. 定义一组模块,模块名即文件名(trans.py)

```
#文件名：trans.py

def first2da(value):
    return value.capitalize()

def all2xiao(value):
    return str.lower(value)

def all2da(value):
    return str.upper(value)
```
2. 同文件夹下另一个文件中(main.py)，使用该模块功能,导入->引用即可

```
#文件名: main.py

import trans

print trans.first2da('bushiHAOde')
print trans.all2da('buSHIHUAIde')
print trans.all2xiao('BUhaobuHAI')


#output

Bushihaode
BUSHIHUAIDE
buhaobuhai
```


### 导入模块的多种形式
- import 模块名
- import 模块名 as 模块别名
- from 模块名 import 属性 (属性为*代表导入all列表指定的所有属性)
- Note:

```
import和from是可执行语句,不是编译期间声明，是可以在程序内部嵌套的.
  - import语句是将整个模块对象赋值给一个变量名(模块名或为别名)
  - from是将一个(或多个)变量名赋值给另一个模块的同名的对象


#案例-使用别名
import trans as t

print t.first2da('bushiHAOde')
print t.all2da('buSHIHUAIde')
print t.all2xiao('BUhaobuHAI')


#案例-使用from语句
from trans import *

print first2da('bushiHAOde')
print all2da('buSHIHUAIde')
print all2xiao('BUhaobuHAI')

```

### 模块的命名空间
我们可以理解模块为变量属性名的封装,在使用import语句后，生成的模块对象就是模块的命名空间。

```
- 模块语句会在首次导入时执行
- 模块文件顶层的每一个赋值的变量名都是模块的属性
- 模块的属性可以通过M.__dict__.keys()或者dir(M)获取
- M.__file__指明模块文件位置,M.__name__指明导入者的名称
```

### Modules的Reload函数
#### 为什么使用reload？
有些系统重启应用代价会比较大，例如网络服务器、数据库服务系统等。
为了增添代码的灵活性，使用reload函数可以强制让模块代码重新导入,可用于模块代码新版本导入,系统动态定制场景等

### 基本用法

- 在sys.path包含目录下创建一个demo.py模块

```
#Python2.7 IDEL环境下 demo.py 代码

x = 1   #顶层属性
y = [1,2,3]

def myPrint(value):
    print 'my:',value

class myPhone:
    def call(self,num):
        print 'call:',num

s6 = myPhone()  #类对象

```

- 交互环境中使用demo.py模块

```
>>> import demo
>>> print(demo.x)
1
>>> demo.myPrint('apple')
my: apple
>>> demo.s6.call('110')
call: 110

```

- 修改demo.py代码，再次使用模块属性（属性不变）

```

#修改后的demo.py代码

x = 4
y = [1,2,3]

def myPrint(value):
    print 'your:',value

class myPhone:
    def call(self,num):
        print 'write:',num


s6 = myPhone()


>>> print(demo.x)
1
>>> demo.myPrint('apple')
my: apple
>>> demo.s6.call('110')
call: 110

```

- 使用reload函数重载模块,再使用新的模块属性,可以看到reload后，使用的是新的模块代码。

```
>>> reload(demo)
<module 'demo' from 'E:\software\lib\site-packages\demo.py'>
>>> print(demo.x)
4
>>> demo.myPrint('apple')
your: apple
>>> demo.s6.call('110')
write: 110

```


### 注意事项

- reload函数在Python2.x是BIF(内建函数).在Python3.x是属于imp模块,需要导入imp模块
- reload参数必须为模块名,否则会抛出TypeError
- reload导入的模块必须先前导入成功的模块，否则抛出NameError
- 如果旧版本模块有定义的新版本模块没有的属性，reload后依旧引用旧版本(新版本是对旧版本同名属性重新引用)

### Python3.6手册关于reload的描述（截取）

```
imp.reload(module)

Reload a previously imported module. The argument must be a module object, so it must have been successfully imported before.
The return value is the module object (the same as the module argument).

When reload(module) is executed:

Python modules’ code is recompiled and the module-level code reexecuted, defining a new set of objects which are bound to names in the module’s dictionary. The init function of extension modules is not called a second time.
    - As with all other objects in Python the old objects are only reclaimed after their reference counts drop to zero.
    - The names in the module namespace are updated to point to any new or changed objects.
    - Other references to the old objects (such as names external to the module) are not rebound to refer to the new objects and must be updated in each namespace where they occur if that is desired.

There are a number of other caveats:

- When a module is reloaded,  If the new version of a module does not define a name that was defined by the old version, the old definition remains.
- It is legal though generally not very useful to reload built-in or dynamically loaded modules, except for sys, __main__ and builtins. In many cases, however, extension modules are not designed to be initialized more than once, and may fail in arbitrary ways when reloaded
- If a module imports objects from another module using from ... import ..., calling reload() for the other module does not redefine the objects imported from it — one way around this is to re-execute the from statement, another is to use import and qualified names (module.*name*) instead.
- If a module instantiates instances of a class, reloading the module that defines the class does not affect the method definitions of the instances — they continue to use the old class definition. The same is true for derived classes.
```

## Packages
### 什么是包?
   说白了包就是目录.目录作为包使用需要有模块代码，满足\__init__.py包文件配置条件即可.

### 为什么使用包?
包让模块代码更具信息性，代码可读性更强，可以通过设置根目录来减少搜索路径的设置.

```
例如:A开发了一个sys模块，B也开发了一个sys模块
    如果同时使用:
        import A.sys   #A为目录,A目录下配置了__init__.py文件
        import B.sys   #B为目录,B目录下配置了__init__.py文件
因为目录名的不同让模块的引用具有唯一性.
```

### 包的基本用法
在sys.path包含的目录下,创建一个目录dir1，子目录dir2内含有模块文件pac.py

```
# dir1/dir2/pac.py 代码 dir2目录下同时配置一个空的__init__.py文件

x=3

def myPrint(value):
    print ('my:',value)

class myPhone:
    def call(self,num):
        print ('me:',num)
```

其他代码要使用pac.py模块，导入需要带入目录信息

```
#交互环境中

>>> import dir1.dir2.pac
>>> dir1.dir2.pac.x
3
```

### 文件\_init_.py的作用
我们注意到上述举例中，在目录下配置了一个\_init_.py文件，那是因为Python规定了如果选择使用包导入，必须遵循:包导入语句的路径内每个目录都必须有init.py文件,该配置文件的作用有:

- 声明作用,这些文件可以防止有相同名称的目录被搜索
- 包的初始化作用,Python首次导入某个目录时,会自动执行目录下的init.py的代码
- 模块命名空间初始化作用,即dir1为一个模块对象，为pac.py的所有属性提供命名空间
- from 语句的行为，可以在init.py中使用all列表来定义以from 语句导入的子模块的名称清单, 即如果没有设定all，from \*语句不会自动加载嵌套于该目录内的子模块,只加载该目录的init.py文件中赋值语句定义的变量名、代码明确导入的子模块
- Note:属性_all_与_X介绍

```
在使用from * (from dir.xxx import modx) 语句情况下:
    1. 模块中变量使用_X下划线形式来修饰，可以避免被导出
    2. 在模块顶层中使用__all__属性来对外指出要复制的变量名
    3. 规范的做法是对面提供的方法属性等存放在__all__中
    4. 当然可以通过import或者from 属性来直接导入定义的属性
```

```
#__all__举例  dir1/pac.py代码
__all__=['myPrint','myPhone']

_x=3  #前面带下划线不对外提供

def myPrint(value):
    print ('my:',value)

class myPhone:
    def call(self,num):
        print ('me:',num)
```
```
#交互环境
>>> from dir1.pac import *
i am dir1 init   #__init__初始化代码
>>> x   #访问不到x属性
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> myPrint('apple')
my: apple
```

#### 注意事项

- 包导入需要配置init.py包文件
- 包的主容器目录需要在sys.path配置目录下

## 模块应用技巧
### name属性
在模块的命名空间中注意到模块的导入者属性可用通过name属性获取.

```
_name_属性的设置规律:

    - 如果文件是以顶层程序文件(主程序)执行，__name__设置为__main__
    - 如果文件是被导入，__name__就会设置导入者的名称

_name_属性的应用:

#使用 if __name__ == '__main__'实现单元测试或者主程序执行
from trans import *

if __name__ == '__main__':
    print first2da('bushiHAOde')
    print all2da('buSHIHUAIde')
    print all2xiao('BUhaobuHAI')
```

### 相对导入
当脚本在导入的模块文件出现同名文件,且都在模块搜索路径上，解决这类问题的模糊性

系统的默认寻找路径是按照sys.path寻找

```
    使用from语句实现相对导入
        例如存在文件目录如下
           |-A
              |-B
                |--__init__.py
                |--main.py
                |--str.py
              |-C
                |--__init__.py
                |--num.py

        顶层程序运行在main.py中，假设str.py与num.py在其他搜索路径中也有定义
        使用from语句导入模块
            1.如果main.py要导入B目录下的str.py
                使用 from . import str

            2.如果main.py要导入C目录下的num.py
                使用 from .. import num

        当然，能使用import最佳
            import A.B.str
            import A.C.num
```

### 注意事项
#### 模块代码的语句次序

- 在导入时，运行前面的代码会立即执行，无法引用文件后面的变量名
- 函数内的代码，会在函数调用时执行

#### 通过变量名字符串导入模块

- 使用exec函数导入，exec语句会编译一段字符串代码传给系统解释器

```
>>> modname = 'dir1.pac'
>>> exec ('import ' + modname)
i am dir1 init
>>> dir1.pac
<module 'dir1.pac' from 'C:\\Python\\Python36\\lib\\site-packages\\dir1\\pac.py'>

    Python3.6关于exec的介绍(截取)
    exec(object[, globals[, locals]])
        This function supports dynamic execution of Python code.
        object must be either a string or a code object.
        If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs).
```

- 使用import函数导入

```
>>> modname = 'dir1.pac'  #搜索路径下有dir1文件夹内pac.py
>>> modobj = __import__(modname)
i am dir1 init
>>> modobj
<module 'dir1' from 'C:\\Python\\Python36\\lib\\site-packages\\dir1\\__init__.py'>
```
