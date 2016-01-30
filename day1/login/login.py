#!/usr/bin/python27
#_*_ coding:utf-8 _*_

import sys,os,getpass


os.system('clear')
i = 0
while i < 3:                                                        #只要用户登录异常不超过3次就不断循环
    name = raw_input("请输入用户名：")

    lock_file = open('account_lock.txt','r+')                       #当用户输入用户名后，打开LOCK 文件 以检查是否此用户已经LOCK了
    lock_list = lock_file.readlines()

    for lock_line in lock_list:                                     #循环LOCK文件 
        lock_line = lock_line.strip('\n')                           #去掉换行符
        if name == lock_line:                                       #如果LOCK了就直接退出
            sys.exit('用户 %s 已经被锁定，退出' % name)  

    user_file = open('account.txt','r')                             #打开帐号文件 
    user_list = user_file.readlines()                               
    for user_line in user_list:                                     #对帐号文件进行遍历
        (user,password) = user_line.strip('\n').split()             #分别获取帐号和密码信息
        if name == user:                                            #如用户名正常匹配
            j = 0
            while j < 3:                                            #只要用户密码异常不超过3次就不断循环
                passwd = getpass.getpass('请输入密码：')            #输入隐藏密码
                if passwd == password:                              #密码正确，提示欢迎登录
                    print('欢迎登录管理平台，用户%s' % name)        
                    sys.exit(0)                                     #正常退出
                else:
                    if j != 2:                                      #j=2时，是最后一次机会，不用在提示还剩余0次机会了
                        print('用户 %s 密码错误，请重新输入，还有 %d 次机会' % (name,2 - j))
                j += 1                                              #密码输入错误后，循环值增加1
            else:
                lock_file.write(name + '\n')                        #密码输入三次错误后，将该用户追加到LOCK文件
                sys.exit('用户 %s 达到最大登录次数，将被锁定并退出' % name)
        else:
            pass                                                    #当用户没匹配时，跳过并继续循环
    else:
        if i != 2:                                                  #i=2时，是最后一次机会，不用在提示还剩余0次机会了
            print('用户 %s 不存在，请重新输入，还有 %d 次机会' % (name,2 - i))
    i += 1                                                          #当用户输入错误时，循环值增加1
else:
    sys.exit('用户 %s 不存在，退出' % name)                         #用户输入三次错误后，异常退出
           
lock_file.close()                                                   #关闭LOCK文件
user_file.close()                                                   #关闭帐号文件
