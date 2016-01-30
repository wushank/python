#!/usr/bin/python27
#_*_ coding:utf-8 _*_
import sys,os,re,yaml,time
reload(sys)
sys.setdefaultencoding('utf-8')  

######################对raw_input输入字符类型判断并转化#####################
def input_handle(s):
   if str.isdigit(s):                   ###对输入是否是数字进行判断
       s = int(s)                       ###如果输出的是个数字，则转化为整数类型
   else:
       s = s.decode('utf-8')            ###如果是字符串或汉字，则转化为unicode类型(主要是针对汉字转化，汉字默认是str)
   return s
   
   # try:
   #     eval(s)                         ###eval将字符串str当成有效的表达式来求值并返回计算结果
   # except NameError:                   ###名称错误
   #     return s
   # except SyntaxError:                 ###语法错误
   #     return s
   # else:
   #     return eval(s)
    

####################框架函数######################
def framework(province='',city='',county=''):
    os.system('clear')                             ###清屏###
    print('''
******************************************************************
*                                                                *
*                     欢迎访问全国省市查询系统                   *
*                                                                *
******************************************************************


+-----------------------------------------------------------------
|           省份:  %s 
|
|           市(区): %s 
|
|           县(区): %s
+-----------------------------------------------------------------
''' % (province,city,county))
    
######################输出展示函数#################
def show(province_name='',city_name='',county_name=''):
    output= '''
******************************************************************
*                                                                *
                  美丽的%s %s %s
*                           欢迎您                               *
                  这里的山美，水美，妹子更美                     
*                                                                *
******************************************************************  
'''
    print output % (province_name,city_name,county_name)
    sys.exit('欢迎下次使用，再见')

###################菜单第一层省份或直辖市输出函数#################
def province_show(province_list):
  
    ############申明全局变量####################
    global P_NAME
    global C_NAME
    global X_NAME
    global FLAG_M

    province_dict = {}            
    ############对省份或直辖市列表参数进行遍历并加上数字编号############### 
    for k,v in enumerate(province_list,1):
            province_dict[k] = v
            print '%d . %s' % (k,v) + '\t',              ###末尾加','，取消默认换行###
            if k % 4 == 0:                               ###按4列换行###
                print
    print('\n================================================================')
    print('q : Exit')

    ###############键盘读入编号或省份，可以输入汉字#################
    province_index = raw_input('请输入编号或省份 : ')

    ###############如果输入非空，对输入进行判断并转化类型###########
    if len(province_index) != 0:
        province_index = input_handle(province_index)

    if province_index == 'q':                            ###如果输入为q,则退出程序###
        sys.exit(0)     
    elif province_index in province_dict.keys():         ###如果输入为数字编号，则从字典中获取具体省份或直辖市名称###
        P_NAME = province_dict[province_index]           ###对全局变量赋值省份名称###
    elif province_index in province_dict.values():       ###如果输入为具体省份，则从字典中获取具体省份或直辖市名称###
        P_NAME = province_index                          ###对全局变量赋值省份名称###
    else:
        P_NAME = ''                                      ###输入其他字符，赋值全局变量为空### 

    while P_NAME:                                        ###全局变量不为空进行循环###
        framework(P_NAME,C_NAME,X_NAME)                  ###调用框架###
        if type(yaml_dict[P_NAME]) is list:
            city_show(P_NAME)                            ###调用城市函数，并传入省份值###
            if FLAG_M == 'b':                            ###城市函数输入b，返回上一层，重新选择省份###
                break
        else:
            show(P_NAME)                                 ###调用输出展示函数### 
            time.sleep(5)
            P_NAME = ''
            break
    else:
        print('输入错误，请重新输入!')                   ###P_NAME为空，即输入错误，重新输入###
        time.sleep(2)
    
##############菜单第二层城市输出函数#######################
def city_show(province_name):

    ############申明全局变量###############
    global P_NAME
    global C_NAME
    global X_NAME
    global FLAG_M
    
    city_name = ''                                       ###定义城市变量默认为空###
    city_list = yaml_dict[province_name]                 ###定义赋值城市列表###
    city_dict = {}                                       ###定义城市编号和名称字典###
    city_county_dict = {}                                ###定义地级市和下属区县字典###

    ############对城市列表参数进行遍历并加上数字编号############### 
    for k,v in enumerate(city_list,1):
        if type(v) is unicode:                           ###直辖市只有二层菜单，第二层为直接的各区或县，值类型为具体字符unicode###
            city_dict[k] = v                             ###对直辖市下的区或县进行新字典赋值，方便查询和展示###
            print '%d . %s' % (k,v) + '\t',              ###末尾加','，取消默认换行###
        elif type(v) is dict:                            ###其他省份有三层菜单，第二层为各地级市，值类型字典###
            for kk,vv in v.items():                      ###对地级市的字典进行遍历###
                city_dict[k] = kk                        ###对其他省份下的地级市进行新字典赋值，方便查询和展示### 
                city_county_dict[kk] = vv                ###对二层地级市和三层县市重新赋值新字典###             
                print '%d . %s' % (k,kk) + '\t',         ###末尾加','，取消默认换行###
        else:
            pass
                
        if k % 4 == 0:                                   ###按4列换行###
            print
    print('\n================================================================')
    print('q : Exit   b : Back')

    ###############键盘读入编号或区市，可以输入汉字#################
    city_index = raw_input('请输入编号或区市 : ')
    
    ###############如果输入非空，对输入进行判断并转化类型###########
    if len(city_index) != 0:
        city_index = input_handle(city_index)

    if city_index == 'q':                                ###如果输入为q,则退出程序###
        sys.exit(0)
    elif city_index == 'b':                              ###如果输入为b，则返回上一层，重新选择省份或直辖市###
        (P_NAME,C_NAME,FLAG_M) = ('','','b')             ###全局变量P_NAME,C_NAME设置为空，FLAG_M设置为b，则返回上一层###
        return                                           ###直接返回，不进行函数以下的操作###
    elif city_index in city_dict.keys():                 ###如果输入为数字编号，则从字典中获取具体城市名称###
        city_name = city_dict[city_index]                ###赋值地级市的名称，并对全局变量进行赋值###
        (P_NAME,C_NAME,FLAG_M) = (province_name,city_name,'')
    elif city_index in city_dict.values():               ###如果输入为城市名称，则从字典中获取具体省份名称###
        city_name = city_index                           ###赋值地级市的名称，并对全局变量进行赋值###
        (P_NAME,C_NAME,FLAG_M) = (province_name,city_name,'')
    else:
        pass                                             ###如果输入其他字符，则不做任何操作###
    
    if city_name:                                        ###如果地级市名字不为空，即键盘输入为要求字符###
        if city_name in city_county_dict.keys():         ###判断是省份的地级市名字### 
            while C_NAME:                                ###环境变量C_NAME不为空###
                framework(P_NAME,C_NAME,X_NAME)          ###调用框架函数，并将省份名字和地级市名字传入###

                ###调用三层区县显示函数，并传入具体变量###
                county_show(P_NAME,C_NAME,city_county_dict[city_name])    
                if FLAG_N == 'b':                        ###三层区县函数输入b，返回上一层，重新选择地级市###
                    break
            else:
                print('输入错误，请重新输入!')           ###C_NAME为空，即输入错误，重新输入###
                time.sleep(2)
        else:                                            ###判断是直辖市的区或县名字###
           show(P_NAME,C_NAME)                           ###调用输出展示函数### 
           time.sleep(5)
    else:                                                ###输入非要求字符，提示重新输入###
        print('输入错误，请重新输入!')
        time.sleep(2)
     
##############菜单第三层区县输出函数#######################
def county_show(province_name,city_name,county_list):

    ############申明全局变量####################
    global P_NAME
    global C_NAME
    global X_NAME
    global FLAG_N

    county_name = ''                                     ###定义三级区县变量默认为空###
    county_dict = {}                                     ##定义赋值区县字典###
 
    ############对区县列表参数进行遍历并加上数字编号############### 
    for k,v in enumerate(county_list,1):                 
        if type(v) is unicode:                           ###第三层为直接的各区或县，值类型为具体字符unicode###
            county_dict[k] = v                           ###对区或县进行新字典赋值，方便查询和展示###
            print '%d . %s' % (k,v) + '\t',              ###末尾加','，取消默认换行###

        if k % 4 == 0:                                   ###按4列换行###
            print
    print('\n================================================================')
    print('q : Exit   b : Back')

    ###############键盘读入编号或区县，可以输入汉字#################
    county_index = raw_input('请输入编号或区县 : ')

    ###############如果输入非空，对输入进行判断并转化类型###########
    if len(county_index) != 0:                           
        county_index = input_handle(county_index)

    if county_index == 'q':                              ###如果输入为q,则退出程序###
        sys.exit(0)
    elif county_index == 'b':                            ###如果输入为b，则返回上一层，重新选择第二层地级市###
        (P_NAME,C_NAME,X_NAME,FLAG_N) = (province_name,'','','b')   ###全局变量C_NAME设置为空，FLAG_M设置为b，则返回上一层###
        return                                           ###直接返回，不进行函数以下的操作### 
    elif county_index in county_dict.keys():             ###如果输入为数字编号，则从字典中获取具体区县名称###
        county_name = county_dict[county_index]          ###赋值区县的名称，并对全局变量进行赋值###
        (P_NAME,C_NAME,X_NAME,FLAG_N) = (province_name,city_name,county_name,'')
    elif county_index in county_dict.values():           ###如果输入为区县名称，则从字典中获取具体区县名称###
        county_name = county_index                       ###赋值区县的名称，并对全局变量进行赋值###
        (P_NAME,C_NAME,X_NAME,FLAG_N) = (province_name,city_name,county_name,'')
    else:                                                ###如果输入其他字符，则不做任何操作### 
        (P_NAME,C_NAME,X_NAME,FLAG_N) = (province_name,city_name,'','')

    if county_name:                                      ###如果区县名字不为空，即键盘输入为要求字符###
        show(P_NAME,C_NAME,X_NAME)                       ###调用输出展示函数### 
        time.sleep(5)
    else:
        print('输入错误，请重新输入!')                   ###输入非要求字符，提示重新输入###
        time.sleep(2)
    


##########################################主程序###############################

###############读取yaml格式文件#######################
fd = open(sys.argv[1],'rb')
yaml_dict = yaml.load(fd)

###############定义全局变量###########################
P_NAME = ''                                             ###省份或直辖市全局变量###
C_NAME = ''                                             ###各省地级市或直辖市区县的全局变量###
X_NAME = ''                                             ###各省地级市下的区或县 全局变量###
FLAG_M = ''                                             ###退出菜单第二层，返回上一层循环的变量###
FLAG_N = ''                                             ###退出菜单第三层，返回上一层循环的变量###

###############获取省份或直辖市的列表#################
prov_list = yaml_dict.keys()

###############主循环开始#############################
while True:
    framework(P_NAME,C_NAME,X_NAME)                     ###调用框架函数，显示初始状态###
    province_show(prov_list)                            ###调用第一层省份或直辖市输出函数###
