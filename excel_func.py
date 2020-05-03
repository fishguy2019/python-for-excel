# -*-coding:utf-8-*-

import re
import xlrd
import openpyxl
import numpy as np
import pandas as pd
import requests


# pandas读取csv文件封装函数
# 如果是xls或xlsx文件，去除文件头的方式是否也一样
# 传递参数，识别文件行开头字符，传递多个可选字符串
def remove_data_file_header(file_path, skip_lines_num, linestartstr):
    with open(file_path, 'r', encoding='gb18030') as fp:
        line = fp.readline()     #读取一行
        #print(line)
        assert isinstance(line, str)
        if line.startswith('Date') or line.startswith('日期') or line.startswith(','):
            need_fixed = False
        else:
            need_fixed = True
        #print(need_fixed)
        if need_fixed:
            with open(file_path, 'r', encoding='gb2312') as fp:
                lines = fp.readlines()     #读取多行
                lines = lines[skip_lines_num:]         #去掉多少行
            with open(file_path, 'w+', encoding='gb2312') as fp:
                fp.writelines(lines)

def load_data_from_file(file_path, skip_lines_num):
    remove_data_file_header(file_path, skip_lines_num)
    data = pd.read_csv(file_path, encoding='gb18030')
    return data

