#!/usr/bin/python27
#_*_ coding=utf-8 _*_

'''
Created on 2016年1月17日
@author: 王凯
'''


'''
该计算器思路：
    1、递归寻找表达式中只含有 数字和运算符的表达式，并计算结果
    2、由于整数计算会忽略小数，所有的数字都认为是浮点型操作，以此来保留小数
使用技术：
    1、正则表达式
    2、递归

执行流程如下：
******************** 请计算表达式： 1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) ********************
before： ['1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
-40.0/5=-8.0
after： ['1-2*((60-30+-8.0*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
========== 上一次计算结束 ==========
before： ['1-2*((60-30+-8.0*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
9-2*5/3+7/3*99/4*2998+10*568/14=173545.880953
after： ['1-2*((60-30+-8.0*173545.880953)-(-4*3)/(16-3*2))']
========== 上一次计算结束 ==========
before： ['1-2*((60-30+-8.0*173545.880953)-(-4*3)/(16-3*2))']
60-30+-8.0*173545.880953=-1388337.04762
after： ['1-2*(-1388337.04762-(-4*3)/(16-3*2))']
========== 上一次计算结束 ==========
before： ['1-2*(-1388337.04762-(-4*3)/(16-3*2))']
-4*3=-12.0
after： ['1-2*(-1388337.04762--12.0/(16-3*2))']
========== 上一次计算结束 ==========
before： ['1-2*(-1388337.04762--12.0/(16-3*2))']
16-3*2=10.0
after： ['1-2*(-1388337.04762--12.0/10.0)']
========== 上一次计算结束 ==========
before： ['1-2*(-1388337.04762--12.0/10.0)']
-1388337.04762--12.0/10.0=-1388335.84762
after： ['1-2*-1388335.84762']
========== 上一次计算结束 ==========
我的计算结果： 2776672.69524
'''


import re,os,sys

def compute_exponent(arg):
    """ 操作指数
    :param expression:表达式
    :return:计算结果
    """

    val = arg[0]
    pattern = re.compile(r'\d+\.?\d*[\*]{2}[\+\-]?\d+\.?\d*')
    mch = pattern.search(val)
    if not mch:
        return
    content = pattern.search(val).group()

    if len(content.split('**'))>1:
        n1, n2 = content.split('**')
        value = float(n1) ** float(n2)
    else:
        pass

    before, after = pattern.split(val, 1)
    new_str = "%s%s%s" % (before,value,after)
    arg[0] = new_str
    compute_exponent(arg)

def compute_mul_div(arg):
    """ 操作乘除
    :param expression:表达式
    :return:计算结果
    """

    val = arg[0]
    pattern = re.compile(r'\d+\.?\d*[\*\/\%\/\/]+[\+\-]?\d+\.*\d*')
    mch = pattern.search(val)
    if not mch:
        return
    content = pattern.search(val).group()

    if len(content.split('*'))>1:
        n1, n2 = content.split('*')
        value = float(n1) * float(n2)
    elif len(content.split('//'))>1:
        n1, n2 = content.split('//')
        value = float(n1) // float(n2)
    elif len(content.split('%'))>1:
        n1, n2 = content.split('%')
        value = float(n1) % float(n2)
    elif len(content.split('/'))>1:
        n1, n2 = content.split('/')
        value = float(n1) / float(n2)
    else:
        pass

    before, after = pattern.split(val, 1)
    new_str = "%s%s%s" % (before,value,after)
    arg[0] = new_str
    compute_mul_div(arg)


def compute_add_sub(arg):
    """ 操作加减
    :param expression:表达式
    :return:计算结果
    """
    while True:
        if arg[0].__contains__('+-') or arg[0].__contains__("++") or arg[0].__contains__('-+') or arg[0].__contains__("--"):
            arg[0] = arg[0].replace('+-','-')
            arg[0] = arg[0].replace('++','+')
            arg[0] = arg[0].replace('-+','-')
            arg[0] = arg[0].replace('--','+')
        else:
            break


    if arg[0].startswith('-'):

        arg[1] += 1
        arg[0] = arg[0].replace('-','&')
        arg[0] = arg[0].replace('+','-')
        arg[0] = arg[0].replace('&','+')
        arg[0] = arg[0][1:]
    val = arg[0]

    pattern = re.compile(r'\d+\.?\d*[\+\-]{1}\d+\.?\d*')
    mch = pattern.search(val)
    if not mch:
        return
    content = pattern.search(val).group()
    if len(content.split('+'))>1:
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)

    before, after = pattern.split(val, 1)
    new_str = "%s%s%s" % (before,value,after)
    arg[0] = new_str
    compute_add_sub(arg)


def compute(expression):
    """ 操作加减乘除
    :param expression:表达式
    :return:计算结果
    """
    inp = [expression,0]

    # 处理表达式中的指数
    compute_exponent(inp)

    # 处理表达式中的乘除求余等
    compute_mul_div(inp)

    # 处理表达式的加减
    compute_add_sub(inp)
    if divmod(inp[1],2)[1] == 1:
        result = float(inp[0])
        result = result * -1
    else:
        result = float(inp[0])
    return result


def exec_bracket(expression):
    """ 递归处理括号，并计算
    :param expression: 表达式
    :return:最终计算结果
    """
    pattern = re.compile(r'\(([\+\-\*\/\%\/\/\*\*]*\d+\.*\d*){2,}\)')
    # 如果表达式中已经没有括号，则直接调用负责计算的函数，将表达式结果返回，如：2*1-82+444
    #if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression):
    if not pattern.search(expression):
        final = compute(expression)
        return final
    # 获取 第一个 只含有 数字/小数 和 操作符 的括号
    # 如：
    #    ['1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    #    找出：(-40.0/5)
    content = pattern.search(expression).group()


    # 分割表达式，即：
    # 将['1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    # 分割更三部分：['1-2*((60-30+(    (-40.0/5)      *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    before, nothing, after = pattern.split(expression, 1)

    print('before:',expression)
    content = content[1:len(content)-1]

    # 计算，提取的表示 (-40.0/5)，并活的结果，即：-40.0/5=-8.0
    ret = compute(content)

    print('%s=%s' %( content, ret))

    # 将执行结果拼接，['1-2*((60-30+(      -8.0     *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    expression = "%s%s%s" %(before, ret, after)
    print('after:',expression)
    print("="*10,'previous result is',"="*10)

    # 循环继续下次括号处理操作，本次携带者的是已被处理后的表达式，即：
    # ['1-2*((60-30+   -8.0  *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']

    # 如此周而复始的操作，直到表达式中不再含有括号
    return exec_bracket(expression)



# 使用 __name__ 的目的：
#   只有执行 python index.py 时，以下代码才执行
#   如果其他人导入该模块，以下代码不执行
if __name__ == "__main__":
    flag = True

    os.system('clear')                                                     ###清屏###

    print('\n================================================================')
    print('\033[33m 欢迎使用计算器 ：\033[0m')
    print('\n================================================================')



    while flag:
        calculate_input = raw_input('\033[32m请输入计算的表达式 | (退出:q)\033[0m')
        calculate_input = re.sub('\s*','',calculate_input)
        if len(calculate_input) == 0:
            continue
        elif calculate_input == 'q':
            sys.exit('退出程序')
        elif re.search('[^0-9\.\-\+\*\/\%\/\/\*\*\(\)]',calculate_input):
            print('\033[31m 输入错误，请重新输入!!!\033[0m')
        else:
            result = exec_bracket(calculate_input)
            print('the expression result is %s' % result)

