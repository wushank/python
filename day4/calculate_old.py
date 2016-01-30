#!/usr/bin/python27
#_*_ coding=utf-8 _*_
'''
Created on 2016年1月17日
@author: 王凯
'''

import sys,os,re

############################指数函数######################################
def exponent(expression):
    if re.search('\d+\.?\d*[\*]{2}[\+\-]?\d+\.?\d*', expression):
        content = re.search('\d+\.?\d*[\*]{2}[\+\-]?\d+\.?\d*', expression).group()

        if len(content.split('**'))>1:
            n1, n2 = content.split('**')
            value = float(n1) ** float(n2)
        else:
            pass
 
        before, after = re.split('\d+\.?\d*[\*]{2}[\+\-]?\d+\.?\d*', expression, 1)
        result = "%s%s%s" % (before,value,after)

        return(exponent(result))
    else:
        return(expression)
    
############################加减函数######################################
def plus_subtract(expression):

    while True:
        if expression.__contains__('+-') or expression.__contains__("++") or expression.__contains__('-+') or expression.__contains__("--"):
            expression = expression.replace('+-','-')
            expression = expression.replace('++','+')
            expression = expression.replace('-+','-')
            expression = expression.replace('--','+')
        else:
            break
    if re.search('[\+\-]?\d+\.?\d*[\+\-]{1,2}\d+\.?\d*', expression):
        content = re.search('[\+\-]?\d+\.?\d*[\+\-]{1,2}\d+\.?\d*', expression).group()

        if len(content.split('+'))>1:
            n1, n2 = content.split('+')
            print(n1,n2)
            value = float(n1) + float(n2)
        else:
            n1, n2 = content.split('-')
            value = float(n1) - float(n2)
 
        before, after = re.split('[\+\-]?\d+\.?\d*[\+\-]{1,2}\d+\.?\d*', expression, 1)
        result = "%s%s%s" % (before,value,after)

        return(plus_subtract(result))
    else:
        return(expression)
    
############################乘除求余函数####################################
def multiply_divide(expression):
    if re.search('\d+\.?\d*[\*\/\%\/\/]+[\+\-]?\d+\.?\d*', expression):
        content = re.search('\d+\.?\d*[\*\/\%\/\/]+[\+\-]?\d+\.?\d*',expression).group()
 
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
 
        before, after = re.split('\d+\.?\d*[\*\/\%\/\/]+[\+\-]?\d+\.?\d*',expression, 1)
        result = "%s%s%s" % (before,value,after)

        return(multiply_divide(result))

    else:
        return(expression)
    
#################################计算函数#################################
def calculate(expression):
   index_result = exponent(expression)
   print('the index is %s' % index_result)
   mul_div_result = multiply_divide(index_result)
   print('the mul_div is %s' % mul_div_result)
   plus_sub_result = plus_subtract(mul_div_result)
   print('the plus_sub is %s' % plus_sub_result)
   return(plus_sub_result)

################################括号计算函数##############################
def bracket(expression):
   #result = re.search('\(([\+\-\*\/]?\d+[\+\-\*\/]+\d+){1}\)',calculate_input).group()
   if re.search('\([^\(\)]+\)',expression):
       result = re.search('\([^\(\)]+\)',expression).group()
       result_no_bracket = result.strip('\(\)')            
       print('the result_no_bracket is %s' % result_no_bracket)
       calculate_result = calculate(result_no_bracket)
  
       before, after = re.split('\([^\(\)]+\)',expression, 1)
       new_str = "%s%s%s" % (before,calculate_result,after) 
       print('the new_str is %s' % new_str)
       return bracket(new_str)
   else:
       return calculate(expression) 
##################################主程序开始##############################
if __name__ == '__main__':

    flag = True

    os.system('clear')                                                     ###清屏###
    a = '1-2*((60-30 +(-40-5)*(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
    a = re.sub('\s*','',a)

    print('\n================================================================')
    print('\033[33m 欢迎使用计算器 ：\033[0m')
    print('\033[32m 可以自定义浮点数精度，范围(1-6) ：\033[0m')
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
        elif re.search('[\(\)]',calculate_input):
            result = bracket(calculate_input)
            print('the expression result is %s' % result)
        else:
            result = calculate(calculate_input)
            print('the expression result is %s' % result)
