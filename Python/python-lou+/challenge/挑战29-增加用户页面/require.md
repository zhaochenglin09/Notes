# 增加用户页面
##介绍
在上一节实验代码基础上，增加一个新的蓝图（Blueprint），支持用户个人页面的显示。

首先下载上一节实验完成后的完整的代码：
```
$ cd /home/shiyanlou

# 下载代码文件并解压
$ wget http://labfile.oss.aliyuncs.com/courses/923/week7/code/lab1.zip
$ unzip lab1.zip

# 修改代码目录名称
$ mv /home/shiyanlou/lab1 /home/shiyanlou/simpledu

# 安装启动环境所依赖的软件包
$ sudo pip3 install flask flask-sqlalchemy mysqlclient
```

现在代码目录为 /home/shiyanlou/simpledu。

启动服务、创建数据库及添加测试数据：
```
$ cd /home/shiyanlou/simpledu
$ sudo service mysql start
$ mysql -uroot
> create database simpledu;
$ export FLASK_APP=manage.py
$ export FLASK_DEBUG=1
$ flask shell
>>> from simpledu.models import db, User, Course
>>> db.create_all()
>>> user = User(username='admin')
>>> course1 = Course(name='python course', author=user)
>>> course2 = Course(name='flask course', author=user)
>>> db.session.add(user)
>>> db.session.add(course1)
>>> db.session.add(course2)
>>> db.session.commit()
服务启动命令：

$ flask run

```
题目需求如下：

增加用户模块作为新的蓝图，需要支持用户主页的显示，即增加新的路由支持这个页面 localhost:5000/user/<username> 中显示用户 id，username 和这个用户发布的课程名称列表。

比如我们提交的测试数据中 admin 用户发布了两门课程 python course，flask course，那么最终显示的 localhost:5000/user/admin 页面预期会显示这些内容：



## 目标
增加新的 user 蓝图
蓝图中的路由可以支持用户主页的显示
提交结果的时候请保证 Flask 处于运行状态，既 http://localhost:5000 可以连接
后台会对 localhost:5000/user/admin 页面进行测试，查看是否包含 admin 用户的用户名，id 和课程名称列表（python course 和 flask course字符串），请确保页面中有这些内容
提示语
增加的文件列表（都在目录/home/shiyanlou/simpledu下)：simpledu/handlers/user.py，simpledu/templates/user.html，分别对应 user 蓝图和模板页面
修改的文件列表（都在目录/home/shiyanlou/simpledu下)：simpledu/handlers/__init__.py对外提供 user 蓝图的入口，simpledu/app.py，修改的内容为注册 user 蓝图
user.py 中需要增加 @user.route('/') 路由，这个路由函数中先通过 username 查询数据库中获得 User 对象，如果不存在则显示 404，获得 User 对象后再将 User 对象传入 user.html 页面进行渲染。
在 user.html 页面中需要从传入的 User 对象中打印其中的 id，username 及 publish_courses 中的所有课程的名称
知识点
Flask Web 框架
Flask Blueprint
Jinja2 模板
