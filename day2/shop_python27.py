#!/usr/bin/python27
#_*_ coding:utf-8 _*_

import sys,os,getpass,time

######################raw_input输入字符类型转化函数#######################
def input_handle(s):
    if str.isdigit(s):                                                     ###对输入是否是数字进行判断###
        s = int(s)                                                         ###如果输出的是个数字，则转化为整数类型###
    return s                                                               ###返回输入字符###

#################################框架函数#################################
def framework(user='',init_money='',now_money='',recharge_money='',value=''):
    os.system('clear')                                                     ###清屏###
    init_money = int(init_money)                                           ###初始总金额数字化###
    now_money= int(now_money)                                              ###当前余额数字化###
    recharge_money = int(recharge_money)                                   ###充值金额数字化###
    print(''.center(82,'*'))
    print('*'+' '.center(80)+'*')
    print(''.ljust(1,'*')+'欢迎来到sky购物平台'.center(88,' ')+''.ljust(1,'*'))
    print('*'+' '.center(80)+'*')
    print(''.center(82,'*'))
    info = '会员 : {0} 金额 : {1} 当前余额 : {2} 充值金额 : {3} 购物车 : {4}'
    info = info.format(user,init_money,now_money,recharge_money,value)
    print(info.center(82,' '))
    print
#    print('''
#*********************************************************************************
#*                                                                               *
#*                                 欢迎来到sky购物平台                           *
#*                                                                               *
#*********************************************************************************
#会员：%s\t金额：%d\t当前余额：%d\t充值金额：%d\t购物车：%d
#''' % (user,init_money,now_money,recharge_money,value))

########################商品列表展示函数###################################
def goods_list_show(my_dict):

    local_dict = {}                                                        ###定义函数内部字典###
    ############对商品列表进行遍历并加上数字编号###########################
    i = 1
    print('商品列表 : ')
    print('=================================================================================')
    print('%-5s  %-20s  %-20s  %-20s  %-20s' % ('编号','商品名称','商品价格(元)','商品总数量(个)','商品剩余数量(个)'))
    for k in my_dict:
        v = my_dict[k]
        if type(v) is dict:
            print('%-5d  %-20s  %-20d  %-20d  %-20d' % (i,k,v['price'],v['sum'],v['num']))
            local_dict[i] = [k,v['price'],v['num'],v['sum']]               ###将商品列表赋值到local_dict###
        i += 1
    print('=================================================================================')

    return local_dict                                                      ###返回格式化后的字典###

########################显示购物车商品列表函数#############################
def cart_goods_show(show_dict):
    show_all_sum = 0                                                       ###初始化购物车商品总价###
    show_all_num = 0                                                       ###初始化购物车商品数量###
    ############对商品列表进行遍历并加上数字编号###########################
    print('%-5s  %-20s  %-20s  %-20s  %-20s  %-20s' % ('编号','商品名称','商品价格(元)','商品总数量(个)','购买数量(个)','购买金额（元）'))
    for k in show_dict:
        v = show_dict[k]
        if type(v) is list:
            print('%-5s  %-20s  %-20d  %-20d  %-20d  %-20d' % (k,v[0],v[1],v[2],v[3],v[4]))
            show_all_sum += v[4]                                           ###商品总价累计###
            show_all_num += 1                                              ###商品个数累计###
    print('请确认您购买商品，总金额：%d（元）'.center(84,'#') % show_all_sum)
    return (show_all_sum,show_all_num)                                     ###返回商品总价和商品个数###

########################修改购物车商品列表函数#############################
def cart_goods_modify(modify_dict,modify_goods_dict):

    a_flag = 1                                                             ###初始化第一层编号循环标记###
    while a_flag:
        index = raw_input('请输入商品编号 | 完成修改(q) : ')
        if len(index) != 0:                                                ###商品编号不为空进行字符转化###
            index = input_handle(index)
        if index == 'q':                                                   ###输入为q,即完成修改退出###
            break
        elif index in modify_dict:                                         ###输入为正确编号###
            b_flag = 1                                                     ###初始化第二层数量循环标记###
            name = modify_dict[index][0]                                   ###对name赋值商品名称###
            while b_flag:
                num = raw_input('请输入新的商品数量(最大值为%d) |  完成修改(q) : ' % modify_dict[index][2] )
                if len(num) != 0:                                          ###商品数量不为空进行字符转化###
                    num = input_handle(num)
                if num == 'q':                                             ###输入为q,即完成修改退出###
                    break
                elif num == 0:                                             ###输入为0,即删除字典中的这个条目###
                    modify_goods_dict[name]['num'] = modify_dict[index][2] ###商品列表中的商品数量变为初始值###
                    del modify_dict[index]                                 ###购物车删除这个商品###
                    b_flag = 0
                elif num > 0 and num <= modify_dict[index][2]:             ###输入为要求数字,则进行数量和金额修改###
                    modify_dict[index][3] = num
                    modify_dict[index][4] = modify_dict[index][1] * num
                    modify_goods_dict[name]['num'] = modify_dict[index][2] - num    ###更新商品列表中的商品数量###
                    b_flag = 0
                else:
                    pass
        else:
            pass
    return (modify_dict,modify_goods_dict)                                 ###返回修改后的购物车商品列表###


#########################购物车展示函数####################################
def shopping_cart_show(my_cart,my_goods_dict):

    print('欢迎来到您的购物车'.center(80,'#'))
    goods_all_sum = 0                                                      ###初始化购物车商品总金额###
    goods_all_num = 0                                                      ###初始化购物车商品总数量###

    if my_cart:                                                            ###购物车参数不为空###
        ###########调用购物车商品列表函数,并返回商品总金额和总数量#########
        (goods_all_sum,goods_all_num)  = cart_goods_show(my_cart)

        choice = raw_input('请进行如下操作 : 修改记录(c) | 继续购物(!c)')
        if choice == 'c':                                                  ###对购物车商品列表进行修改###
            (my_shop_cart,my_goods_dict) = cart_goods_modify(my_cart,my_goods_dict)  ###调用商品修改函数，并返回新的商品列表###
            (goods_all_sum,goods_all_num) = cart_goods_show(my_shop_cart)  ###购物车商品展示，并返回最新的商品总价###
        else:
            pass
    else:
        print('当前您的购物车为空'.center(80,' '))

    time.sleep(2)
    return (goods_all_sum,goods_all_num,my_goods_dict)                      ###返回购物车中商品总价、数量和用户商品列表###


#########################余额充值函数######################################
def balance_recharge(recharge_init_balance,recharge_now_balance,recharge_money):
    recharge_flag = 1                                                       ###充值循环参数初始化###
    while recharge_flag:
        recharge_num = raw_input('请输入充值金额 | 返回(b) | 退出(q):')
        if len(recharge_num) != 0:                                          ###如果输入非空，对输入进行判断并转化类型###
            recharge_num = input_handle(recharge_num)
        if recharge_num == 'q':                                             ###如果输入为q,则退出程序###
            sys.exit(0)
        elif recharge_num == 'b':                                           ###如果输入为b,则返回第一层循环，重新选择商品编号###
            break
        elif type(recharge_num) is int and recharge_num > 0 :               ###输入要求充值金额###
            recharge_init_balance += recharge_num                           ###初始金额增加###
            recharge_now_balance += recharge_num                            ###当前余额增加###
            recharge_money += recharge_num                                  ###充值金额增加###
            recharge_flag = 0                                               ###改变充值循环参数###
            print('充值成功，请查收'.center(80,' '))                        ###提示充值成功###
        else:
            pass
    return (recharge_init_balance,recharge_now_balance,recharge_money)      ###返回初始、当前、充值金额###


#########################用户结帐函数######################################
def user_billing(billing_list,my_cart,billing_balance):

    print('欢迎来到结算菜单'.center(80,'#'))
    if my_cart:                                                             ###购物车参数不为空###
        #############调用购物车商品列表函数################################
        cart_goods_show(my_cart)
        billing_flag = raw_input('请确认是否商品结算（y | n）：')
        if billing_flag == 'y':                                             ###商品结算确认###
            billing_file = open('info.txt','w')                             ###打开读写帐号文件###
            for user_info in billing_list:
                print(user_info)
                billing_file.writelines(user_info)                          ###回写用户列表信息###
            billing_file.close()                                            ###关闭帐号文件###
            sys.exit('结帐成功，你当前余额 ：%d'.center(80,' ') % billing_balance)
        else:
            print('退出结算菜单，继续购物'.center(80,' '))
            time.sleep(2)
    else:
        print('当前您的购物车为空，无需结算'.center(80,' '))
        time.sleep(2)



################################主程序开始##################################

################################商品列表####################################
###num为当前商品数量，sum为商品总数量###
goods_list = {
             'iphone6': {'price':6000,'num':10,'sum':10},
             'ipad': {'price':3000,'num':20,'sum':20},
             'mi4': {'price':2000,'num':43,'sum':43},
             'huawei6_plus': {'price':1999,'num':8,'sum':8},
}

i = 0
while i < 3:                                                                ###只要用户登录异常不超过3次就不断循环###
    username = raw_input('请输入用户名：')                                  ###输入用户名###
    password = raw_input('请输入密码：')                                    ###输入隐藏密码###
    user_file = open('info.txt','r')                                        ###打开帐号文件###
    user_list = user_file.readlines()                                       ###用户列表信息###
    user_file.close()                                                       ###关闭帐号文件###


    for user_line in user_list:                                             ###对帐号文件进行遍历###
        ######################分别获取帐号、密码信息和当前余额##############
        (user,passwd,init_balance) = user_line.strip('\n').split()

        init_balance = int(init_balance)                                    ###对总金额进行数字化###
        now_balance = init_balance                                          ###对当前余额进行数字化###
        my_goods_sum = 0                                                    ###初始化购买商品总金额###

        if username == user and password == passwd:                         ###如用户名和密码正常匹配###
            user_shopping_cart = {}                                         ###初始化用户购物车字典###
            user_shopping_cart_count = 0                                    ###初始化用户购物车内商品的数量###
            recharge_value = 0                                              ###初始化充值金额###
            line_num = user_list.index(user_line)                           ###赋值匹配用户的下标###
            first_flag = 1                                                  ###定义第一层循环变量参数###

            while first_flag:

                ########################调用框架函数输出用户信息############
                framework(username,init_balance,now_balance,recharge_value,user_shopping_cart_count)

                goods_output_dict = goods_list_show(goods_list)             ###调用商品列表展示函数输出商品信息###
                print(now_balance)
                goods_index = raw_input('请选择菜单 ：输入商品编号 | 购物车(c) | 余额充值(r) | 结帐(b) | 退出(q) : ')

                if len(goods_index) != 0:                                   ###如果输入非空，对输入进行判断并转化类型###
                    goods_index = input_handle(goods_index)

                if goods_index == 'q':                                      ###如果输入为q,则退出程序###
                    sys.exit(0)

                elif goods_index == 'c':                                    ###如果输入为c，则展示购物车###
                    ###调用购物车显示函数，并返回购物车商品总金额###########
                    (my_goods_sum,user_shopping_cart_count,goods_list) = shopping_cart_show(user_shopping_cart,goods_list)
                    now_balance = init_balance - my_goods_sum               ###计算出当前余额###
                    if now_balance < 0:
                        print('您的余额不足，请及时充值，谢谢')
                        time.sleep(2)

                elif goods_index == 'r':                                    ###如果输入为r，则进行余额充值###
                    (init_balance,now_balance,recharge_value) = balance_recharge(init_balance,now_balance,recharge_value)

                elif goods_index == 'b':                                    ###如果输入为b,则进入结账菜单###
                    ##############更新用户文件中用户的余额##################
                    user_list[line_num] = user + ' ' + passwd + ' ' + repr(now_balance) + '\n' 
                    print(user_list[line_num])
                    user_billing(user_list,user_shopping_cart,now_balance)  ###调用结算函数###

                elif goods_index in goods_output_dict:                      ###输入编号为正确的商品编号###

                    ###############################取出goods_index商品列表信息并进行赋值和展示############
                    (goods_name,goods_price,goods_num) = (goods_output_dict[goods_index][0], goods_output_dict[goods_index][1], goods_output_dict[goods_index][2])
                    print('【 编号：%-5d \t 名称：%-15s \t 价格：%-5d（元） \t 数量：%-5d（个）】' % (goods_index,goods_name,goods_price,goods_num))

                    second_flag = 1                                         ###定义第二层循环变量参数###
                    while second_flag:
                        buy_num = raw_input('请输入购买商品个数(最大值为%d) | 返回(b) | 退出(q): ' % goods_num)
                        if len(buy_num) != 0:                               ###如果输入非空，对输入进行判断并转化类型###
                            buy_num = input_handle(buy_num)
                        if buy_num == 'q':                                  ###如果输入为q,则退出程序###
                            sys.exit(0)
                        elif buy_num == 'b':                                ###如果输入为b,则返回第一层循环，重新选择商品编号###
                            break
                        elif buy_num > 0 and buy_num <= goods_num:          ###输入要求商品数量###
                            my_goods_sum = goods_price * buy_num            ###计算购买商品的总金额###
                            if my_goods_sum <= now_balance:
                                print('购买商品 %s 总价格为 : %d' % (goods_name,my_goods_sum))
                                add_flag = raw_input('请确认是否加入购物车（y | n）：')
                                if add_flag == 'y':                         ###购买商品确认加入购物车###

                                    ###判断购物车不存在该商品###############
                                    if goods_index not in user_shopping_cart:
                                        user_shopping_cart_count += 1       ###购物车里商品数量加1###
                                        ####将该商品加入用户购物车字典中####
                                        user_shopping_cart[goods_index] = [goods_name,goods_price,goods_num,buy_num,my_goods_sum]
                                    ####购物车已经存在该商品，则进行数量和金额累计计算############
                                    else:
                                        user_shopping_cart[goods_index][3] += buy_num
                                        user_shopping_cart[goods_index][4] += my_goods_sum

                                    now_balance -= my_goods_sum             ###计算出当前余额###

                                    goods_list[goods_name]['num'] -= buy_num   ###商品列表的商品数量更新###
                                    second_flag = 0                         ###设置第二层循环值为0，结束第二层循环####

                                else:
                                    break
                            else:
                                print('您的余额不足，请充值或重新选择，谢谢')
                                time.sleep(2)
                        else:
                            pass
                else:
                    pass
    else:
        if i != 2:                                                         ###i=2时，是最后一次机会，不用在提示还剩余0次机会了###
            print('用户或密码错误，请重新输入，还有 %d 次机会' % (2 - i))
    i += 1                                                                 ###当用户输入错误时，循环值增加1###
else:
    sys.exit('用户或密码输入错误超过三次，退出系统,欢迎下次光临')          ###用户输入三次错误后，异常退出###
