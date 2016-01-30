python之haproxy配置文件操作（第三天）

作业：

对haproxy配置文件进行操作

要求：

     对haproxy配置文件中backend下的server实现增删改查的功能

 

一、这个程序有二个版本

1、 python2.7版本见haproxy_python27.py

2、 python3.4版本见haproxy_python34.py

 

二、具体实现了如下功能：
     1、输入1，进入backend菜单，查询server信息
     2、输入2，进入backend菜单，添加server条目
     3、输入3，进入backend菜单，选择server条目，进入修改环节
     4、输入4，进入backend菜单，选择server条目，进入删除环节
     5、输入5，退出程序

三、haproxy配置文件如下见haproxy.cfg

 

四、流程图如下：


五、效果图：

1、  初始菜单直接显示backend列表，并列出选择菜单：

  

2、  输入1，选择查询菜单，并输入backend的名称或编号，均可，并展示对应名称下的server信息：


3、  输入b可以返回上层菜单，输入2进入添加server条目：


4、  输入server对应的name，address，weight，maxconn，并对有效性进行判断：


       添加成功后查看结果：

 

注：

name以数字、字母、下划线开头（其中包含数字的原因是可以输入ip地址）

address可以是单独的ip地址，也可以是ip加端口的形式，例：192.168.100.3或192.168.100.3:8080

weight和maxconn必须输入数字，大小暂时没有限制

 

5、 输入b可以返回上层菜单，输入3进入修改server条目，并对www.oldboy.org下的sky条目进行修改：


          同样对输入的server有效性进行判断，最后确认回写配置文件，查看修改结果：


6、  输入b可以返回上层菜单，输入4进入删除server条目，并对指定条目进行修改：

 

7、输入b可以返回上层菜单，输入5，即可退出程序。

 

六、针对python2.7和python3.4的代码区别：

       1、print的使用。

       2、python2.7下使用raw_input，python3.4下使用input。
