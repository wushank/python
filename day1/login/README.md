作业：编写登陆接口

输入用户名密码
认证成功后显示欢迎信息
输错三次后锁定


解答具体如下：

帐号文件account.txt内容如下：

sam 123 

david 12 
kevin 123
lin 12 
tailen 123 
jack 12

 

锁文件account_lock.txt默认为空

 
只针对帐号文件里的用户进行判断并锁定，针对用户和密码各有三次错误重试机会。
详情见流程图
![image](https://github.com/wushank/python/day1/login.png)
