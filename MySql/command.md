1. 用户查询：

- root登录数据库
- 查询用户表

> SELECT User, Host, Password FROM mysql.user;

- 显示所有的用户（不重复）

> SELECT DISTINCT User FROM mysql.user;
