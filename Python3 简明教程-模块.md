
 **知识点**：
```
1. 模块的导入
2. 包
3. 默认/第三方模块介绍
4. 命令行参数
```
[TOC]

# 1. 模块定义

模块是包括Python定义和声明的文件，文件名=模块名+.py后缀
可以由全局变量 \_\_name\_\_得到模块的模块名，如下举例：

**bars.py**

```python
"""
Bars Module
"""

def starbar(num):
    """打印 * 分割线
    :arg num : 长度
    """
    print('*' * num)

def hashbar(num):
    """打印 # 分割线
    :arg num : 长度
    """
    print('#' * num)

def simplebar(num):
    """打印 - 分割线
    :arg num : 长度
    """
    print('-' * num)

```
模块导入方式：

    >>> import bars
    >>> bars.hashbar(10)
    >>> bars.simplebar(10)
    >>> bars.starbar(10)

或

    >>> from bars import hashbar.simplebar
    >>> simplebar(20)


# 2. 包

含有\_\_init\_\_.py 文件的目录可以用来作为一个包，目录里所有的.py文件都是包的子模块。


```
tree mymudule
mymudule
|___bars.py
|___ __init__
|___others.py
```

**\_\_init\_\_.py**
如果\_\_init\_\_.py文件内有一个名为\_\_all\_\_的列表，那么只有在列表内列出的名字将会被公开。因此，如果在\_\_init\_\_.py文件中含有一下内容：

    from baomodulename.bars import simplebar
    __all__ = [simplebar,]

那么导入以后只有simplebar可用。



# 3. 默认模块

 - os 模块
 - Requests 模块

   **Requests是一个第三方Python模块**  

    第三方模块非默认安装，使用pip3 安装。  

    >sudo pip3 install requests

    Requests 模块

    获取一个简单的网页：
```python
        >>> import requests  
        >>> req = requests.get('https://github.com')
        >>> req.status_code
        200
```
    req 的 text 属性存有服务器返回的HTML网页。

    **从指定URL中下载文件程序：**

```python
import os
import os.path
import requests

def download(url):
    '''从指定URL中下载文件并储存到当前目录
    :arg url:要下载的文件URL
    '''
    if req.status_code == 404:
        print("No such file found at %s "% url)
        return
    filename = url.split('/')[-1]
    with open(filename,'wb') as fobj:
        fobj.write(req.content)
    print("Download over.")

if __name__ == '__main__':
    url = input('Enter a URL:')
    download(url)


```

- argparse命令行参数处理模块

    sys.argv

---

#### 异常处理小知识：

原始代码：


```python

set things up
try:
    do something
finally:
    tear things down

#以下举例：
try:
    f = open('xxx')
except:
    print 'fail to open'
    exit(-1)
try:
    do something
except:
    do something
finally:
    f.close()
```

**封装**

```python
def controlled_execution(callback):
    set things up
    try:
        callback(thing)
    finally:
        tear things down

def my_function(thing):
    do something

controlled_execution(my_function)

```
**生成器**

```python
def controlled_execution():
    set things up
    try:
        yield thing
    finally:
        tear things down

for thing in controlled_execution():
    do something with thing

```
**with ... as ...**
```Python
class controlled_execution:
    def __enter__(self):
        set things up
        return thing
    def __exit__(self, type, value, traceback):
        tear things down

with controlled_execution() as thing:
        do something

```
在python2.5及以后，file对象已经写好了enter和exit函数，我们可以这样测试：
```python
>>> f = open("x.txt")
>>> f  
<open file 'x.txt', mode 'r' at 0x00AE82F0>
>>> f.__enter__()
<open file 'x.txt', mode 'r' at 0x00AE82F0>
>>> f.read(1)
'X'
>>> f.__exit__(None, None, None)
>>> f.read(1)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file

```

# 4. Collections 模块

collections 是 Python 内建的一个集合模块，提供了许多有用的集合类。包括（Counter 类、defaultdict 类、namedtuple 类）。  











---

参考资料
1. [Python:你不知道的super](http://python.jobbole.com/86787/)
2. [实验楼-Python3 简明教程-类](https://www.shiyanlou.com/courses/596/labs/2046/document)
