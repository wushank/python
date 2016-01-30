作业三：多级菜单
三级菜单
可依次选择进入各子菜单
所需新知识点：列表、字典
 

针对此菜单程序的设计，使用了yaml格式的文本，由python对其内容进行解析为多重字典，然后对字典进行遍历，判断并输出三层的菜单。


一、具体yaml文件pro格式说明：
注：三层结构：（其中以短杠“-”会被解析为数组，冒号“：”会被解析为字典）

       香港、澳门、台湾、钓鱼岛只有一层；

       北京、天津等直辖市只有二层，即直辖市===下属区县

       其他省份有三层，即省份===地级市===下属区县

二、流程图如下：
![image](https://github.com/wushank/python/blob/master/day1/menu/menu.png)

三、具体展示见下图：

1、初始状态，可以输入数字编号或中文名字：

![image](http://images2015.cnblogs.com/blog/857962/201512/857962-20151226161700890-608972755.png)

2、访问香港、澳门、台湾、钓鱼岛只有一层的菜单：

![image](http://images2015.cnblogs.com/blog/857962/201512/857962-20151226161848406-1580608373.png)

3、北京、天津等直辖市只有二层的菜单：

![image](http://images2015.cnblogs.com/blog/857962/201512/857962-20151226161856671-125938849.png)

4、其他省份三层的菜单：

![image](http://images2015.cnblogs.com/blog/857962/201512/857962-20151226161758781-744205670.png)

5、返回上一层功能:

![image](http://images2015.cnblogs.com/blog/857962/201512/857962-20151226161903734-1551690505.png)

6、退出功能，在任意一层输入'q'，即可退出程序。

四、针对python2.7和python3.4二个版本的不同之处说明如下：

1、在python3.4下，经测试字符串存储的类型已经都成为str，包括英文，汉字

    而在python2.7下，经测试字符串存储类型，英文为unicode；汉字为str

    （1）在python2.7下还需要设置默认编码，具体如下：

              reload(sys)
              sys.setdefaultencoding('utf-8')

    要不然会报如下错误：

UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 18: ordinal not in range(128)

     （2）在python2.7下还需要对汉字的str进行转码，具体如下：

              s = s.decode('utf-8')    

 

2、针对print的使用，略有不同，具体如下：

          python2.7 ： 

                 print '%d . %s' % (k,v) + '\t',              ###末尾加','，取消默认换行###

          python3.4 ：

                 print('%d . %s' % (k,v) + '\t',end='')       ###加上end参数，取消默认换行###

3、windows上进行测试，python2.7有一部分会出现乱码，python3.4一切正常，需要对二个地方需要注意：

         (1) .  fd = open(sys.argv[1],'rb') 打开文件一定要用rb，以二进制方式 。方便迁移

         (2) .  清屏命令    linux下用os.system('clear')    windows下用os.system('cls')
