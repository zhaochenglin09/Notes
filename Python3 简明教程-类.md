
 **实验安排如下**：
```
1. 定义简单的类
2. __init__ 方法
3. Python 中的继承
4. 多继承
5. 删除对象
6. 属性读取方法
7. @property 装饰器
```

# 1. 定义类

```python
 class nameoftheclass(parent_class):
     statment1
     statment2
     statment3
```
在类的声明中，你可以定义函数（方法）。

```python
class MyClass(object):
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

```

# 2. \_\_init\_\_ 方法





类的实例化使用函数符号。只要将类对象看作是一个返回新的类实例的无参函数即可。例如：

    x = MyClass()

这个实例化操作创建一个空的对象。很多类希望创建有初始状态的类对象，故定义一个名为 __init__() 的特殊方法，如下：

    def __init__(self):
        self.data = []

类定义类 __init__() 方法，类的实例化操作会自动为新创建的类实例调用 __init__() 方法。所以在下例中：

```python
class Complex:
    def __init__(self,realpart,imagpart)
        self.r = realpart
        self.i = imagpart



>>> x = Complex(3.0,-4.5)
>>> x.r, x.i
    (3.0,-4.5)

```

# 3. 继承
  当一个类继承另一个类的时候，它将继承父类所有的功能（变量和方法）。有助于重用代码。在下面这个例子中，我们首先创建Person类，然后创建派生类Student和Teacher。当两个类都从Person类继承时，它们除了会有Person类的所有方法，还会有自身用途的信方法和新变量。

  **Student_teacher.py**

```python
#!/usr/bin/env python3

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """
    def __init__(self, name):
        self.name = name
    def get_details(self):
        """
        返回包含任命的字符串
        """
        return self.name

class Student(object):
    def __init__(self,name,branch,year):


class Teacher(object):
    """
     返回Teacher 对象，采用字符串列表作为参数    
    """
    def __init__(self,name,papers):    Person.__init__(self,name)
    self.papers = papers
    def get_details(self):
        return "{} teacher {}".format(self.name,','.join(self.papers))       

```  

























# 4. 多继承
# 5. 删除对象
# 6. 属性读取方法
# 7. 装饰器
